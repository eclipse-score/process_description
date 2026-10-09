import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workflows.base import (
    CHECKLIST, CHECKLIST_IDS, PARENT_TEXT_REQUIRED_IDS, WorkflowError,
    load_checklist, read_json, validate_assessment,
)
from workflows.req_safety_inspection.workflow import (
    draft_chat, load_parent_context, main,
    parse_requirements_rst, run_directory, start_chat,
)
from workflows.environment import collect_environment
from workflows.review import check_inspection, parse_checklist, prepare_inspection, render_checklist


def _checklist_entry(**overrides):
    entry = {"passed": "yes", "remarks": "Full remarks " * 10, "issue_link": ""}
    entry.update(overrides)
    return entry


class ChecklistSchemaTests(unittest.TestCase):
    def setUp(self):
        self.requirements = [{"id": "feat_req__example", "title": "Example", "text": "Shall work.",
                              "parent_context_available": True}]
        self.assessment = {"requirements": [{
            "req_id": "feat_req__example", "req_title": "Example",
            "checklist": {identifier: _checklist_entry() for identifier in CHECKLIST_IDS},
        }]}

    def test_valid_assessment(self):
        validate_assessment(self.assessment, self.requirements)

    def test_canonical_checklist_has_sixteen_items(self):
        self.assertEqual(len(CHECKLIST_IDS), 16)
        self.assertEqual(load_checklist(), CHECKLIST)

    def test_wrong_identity_rejected(self):
        self.assessment["requirements"][0]["req_id"] = "invented"
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_extra_checklist_item_rejected(self):
        self.assessment["requirements"][0]["checklist"]["invented"] = _checklist_entry()
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_duplicate_json_key_rejected(self):
        with self.assertRaises(WorkflowError):
            read_json('{"requirements": [], "requirements": []}')

    def test_invalid_verdict_rejected(self):
        self.assessment["requirements"][0]["checklist"]["REQ_01_01"]["passed"] = "maybe"
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_missing_requirement_rejected(self):
        self.assessment["requirements"] = []
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_issue_link_mandatory_for_no(self):
        self.assessment["requirements"][0]["checklist"]["REQ_01_01"]["passed"] = "no"
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_issue_link_forbidden_unless_no(self):
        self.assessment["requirements"][0]["checklist"]["REQ_01_01"]["issue_link"] = "https://example/issue/1"
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_issue_link_accepted_for_no(self):
        self.assessment["requirements"][0]["checklist"]["REQ_01_01"].update(
            passed="no", issue_link="https://example/issue/1")
        validate_assessment(self.assessment, self.requirements)

    def test_all_not_assessed_is_structurally_valid_but_distinct_from_pass(self):
        for check in self.assessment["requirements"][0]["checklist"].values():
            check["passed"] = "not_assessed"
        validate_assessment(self.assessment, self.requirements)
        counts = {check["passed"] for check in self.assessment["requirements"][0]["checklist"].values()}
        self.assertEqual(counts, {"not_assessed"})

    def test_parent_dependent_items_blocked_without_context(self):
        requirements = [{"id": "feat_req__example", "title": "Example", "text": "Shall work.",
                         "parent_context_available": False}]
        for identifier in PARENT_TEXT_REQUIRED_IDS:
            with self.subTest(identifier):
                with self.assertRaises(WorkflowError):
                    validate_assessment(self.assessment, requirements)

    def test_parent_dependent_items_allowed_as_not_assessed_without_context(self):
        requirements = [{"id": "feat_req__example", "title": "Example", "text": "Shall work.",
                         "parent_context_available": False}]
        for identifier in PARENT_TEXT_REQUIRED_IDS:
            self.assessment["requirements"][0]["checklist"][identifier]["passed"] = "not_assessed"
        validate_assessment(self.assessment, requirements)


class RequirementsParserTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)

    def test_public_baselibs_parser(self):
        fixture = Path(__file__).parent / "fixtures/score_baselibs_requirements.rst"
        requirements = parse_requirements_rst(fixture)
        self.assertEqual(len(requirements), 4)
        self.assertIn("stkh_req__functional_req__base_libraries", requirements[0]["parent"])
        self.assertIn("program termination handling", requirements[0]["text"])

    def test_duplicate_input_ids_rejected(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: duplicate\n\n   Body.\n\n" * 2)
        with self.assertRaises(WorkflowError):
            parse_requirements_rst(fixture)

    def test_stakeholder_requirements_require_their_own_checklist(self):
        fixture = Path(self.temporary.name) / "stakeholder.rst"
        fixture.write_text(".. stkh_req:: Stakeholder need\n   :id: stkh_req__example\n\n   Shall work.\n")
        with self.assertRaisesRegex(WorkflowError, "corresponding S-CORE checklist"):
            parse_requirements_rst(fixture)

    def test_mixed_feature_and_stakeholder_file_is_not_misassessed(self):
        fixture = Path(self.temporary.name) / "mixed.rst"
        fixture.write_text(
            ".. stkh_req:: Stakeholder need\n   :id: stkh_req__example\n\n   Shall work.\n\n"
            ".. feat_req:: Feature child\n   :id: feat_req__example\n\n   Shall work.\n"
        )
        with self.assertRaisesRegex(WorkflowError, "Direct stkh_req assessment"):
            parse_requirements_rst(fixture)

    def test_path_traversal_rejected(self):
        with self.assertRaises(WorkflowError):
            run_directory("../../escape")

    def test_context_file_marks_parent_context_available(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        context = Path(self.temporary.name) / "context.json"
        context.write_text(json.dumps({"feat_req__example": "Parent requirement text."}))
        parse_requirements_rst(fixture)
        supplied = load_parent_context(context)
        self.assertEqual(supplied["feat_req__example"], "Parent requirement text.")

    def test_missing_context_file_is_optional(self):
        self.assertEqual(load_parent_context(None), {})


class InspectionChecklistTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name) / "run"
        self.requirements = [{"id": "feat_req__example", "title": "Example", "text": "Shall work.",
                              "parent_context_available": True}]
        self.assessment = {"requirements": [{
            "req_id": "feat_req__example", "req_title": "Example",
            "checklist": {identifier: _checklist_entry(remarks="Evidence | value < 3.\nNext line.")
                          for identifier in CHECKLIST_IDS},
        }]}

    def test_markdown_round_trip(self):
        rendered = render_checklist(self.assessment)
        self.assertEqual(parse_checklist(rendered, self.requirements), self.assessment)

    def test_criterion_and_guidance_are_not_trusted_from_file(self):
        rendered = render_checklist(self.assessment)
        tampered = rendered.replace(CHECKLIST["REQ_01_01"]["criterion"], "Tampered criterion")
        # Criterion/guidance columns are ignored on parse; only passed/remarks/issue_link
        # round-trip, so tampering with them does not change the parsed assessment.
        self.assertEqual(parse_checklist(tampered, self.requirements), self.assessment)

    def test_issue_link_round_trip(self):
        entry = self.assessment["requirements"][0]
        entry["checklist"]["REQ_01_01"].update(passed="no", issue_link="https://example/issue/7")
        rendered = render_checklist(self.assessment)
        self.assertEqual(parse_checklist(rendered, self.requirements), self.assessment)

    def test_extra_table_cell_not_silently_truncated(self):
        text = render_checklist(self.assessment).replace("| REQ_01_01 |", "| REQ_01_01 | extra |", 1)
        with self.assertRaises(WorkflowError):
            parse_checklist(text, self.requirements)

    def test_prepare_writes_inspection_file_and_no_approval_artifacts(self):
        result = prepare_inspection(self.directory, self.requirements, self.assessment,
                                    {"feature_name": "Example"}, {"interface": "offline-test"})
        self.assertTrue((self.directory / "inspection.md").exists())
        self.assertFalse((self.directory / "report.rst").exists())
        self.assertFalse((self.directory / "audit.json").exists())
        self.assertFalse((self.directory / "review_state.json").exists())
        self.assertEqual(result["verdict_counts"]["yes"], len(CHECKLIST_IDS))

    def test_check_reflects_edits_without_any_approval_state(self):
        prepare_inspection(self.directory, self.requirements, self.assessment,
                          {"feature_name": "Example"}, {"interface": "offline-test"})
        checklist_path = self.directory / "inspection.md"
        assessment = parse_checklist(checklist_path.read_text(), self.requirements)
        assessment["requirements"][0]["checklist"]["REQ_01_01"].update(
            passed="no", issue_link="https://example/issue/9")
        checklist_path.write_text(render_checklist(assessment))
        result = check_inspection(self.directory)
        self.assertEqual(result["verdict_counts"]["no"], 1)
        self.assertEqual(len(result["open_issues"]), 1)
        self.assertTrue(result["changed_since_draft"])
        self.assertIn("Git/GitHub review", result["next_step"])

    def test_invalid_edit_not_silently_accepted(self):
        prepare_inspection(self.directory, self.requirements, self.assessment,
                          {"feature_name": "Example"}, {"interface": "offline-test"})
        checklist_path = self.directory / "inspection.md"
        checklist_path.write_text(checklist_path.read_text().replace("REQ_01_01", "invented"))
        with self.assertRaises(WorkflowError):
            check_inspection(self.directory)

    def test_overwrite_protection(self):
        prepare_inspection(self.directory, self.requirements, self.assessment,
                          {"feature_name": "Example"}, {"interface": "offline-test"})
        (self.directory / "unexpected.txt").write_text("not part of the protocol")
        with self.assertRaises(WorkflowError):
            prepare_inspection(self.directory, self.requirements, self.assessment,
                              {"feature_name": "Example"}, {"interface": "offline-test"})


class ChatFlowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)

    def test_start_to_draft_without_local_approval(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        assessment = {"requirements": [{
            "req_id": "feat_req__example", "req_title": "Example",
            "checklist": {identifier: _checklist_entry() for identifier in CHECKLIST_IDS},
        }]}
        # REQ_03_01/REQ_10_01 require parent context; mark them not_assessed since none is supplied.
        for identifier in PARENT_TEXT_REQUIRED_IDS:
            assessment["requirements"][0]["checklist"][identifier]["passed"] = "not_assessed"
        with patch("workflows.req_safety_inspection.workflow.EXTENSION_ROOT", Path(self.temporary.name)):
            run = start_chat(fixture, "Example", "ASIL_B", "example")
            self.assertIsNone(run["declared_model"]["label"])
            Path(run["response"]).write_text(json.dumps(assessment))
            result = draft_chat(run["run"])
        self.assertTrue(Path(result["checklist_file"]).exists())
        directory = run_directory(run["run"])
        self.assertFalse((directory / "report.rst").exists())
        self.assertFalse((directory / "audit.json").exists())

    def test_declared_model_label_is_recorded_only_when_supplied(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        with patch("workflows.req_safety_inspection.workflow.EXTENSION_ROOT", Path(self.temporary.name)):
            run = start_chat(fixture, "Example", "ASIL_B", "example", model_label="gpt-5 (declared by reviewer)")
        self.assertEqual(run["declared_model"]["label"], "gpt-5 (declared by reviewer)")
        self.assertEqual(run["declared_model"]["source"], "reviewer supplied")

    def test_start_keeps_previous_runs(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        with patch("workflows.req_safety_inspection.workflow.EXTENSION_ROOT", Path(self.temporary.name)):
            first = start_chat(fixture, "Example", "ASIL_B", "example")
            second = start_chat(fixture, "Example", "ASIL_B", "example")
        self.assertNotEqual(first["run"], second["run"])
        self.assertTrue(Path(first["prompt"]).exists())

    def test_generation_command_not_available(self):
        with patch("sys.argv", ["workflow", "generate"]), patch("sys.stderr"), self.assertRaises(SystemExit) as error:
            main()
        self.assertEqual(error.exception.code, 2)

    def test_legacy_approval_commands_removed(self):
        for removed in ("confirm", "reject", "stage", "finalize", "import-response", "request"):
            with patch("sys.argv", ["workflow", removed]), patch("sys.stderr"), self.assertRaises(SystemExit) as error:
                main()
            self.assertEqual(error.exception.code, 2)


class EnvironmentMetadataTests(unittest.TestCase):
    def test_metadata_does_not_invent_active_model(self):
        metadata = collect_environment()
        self.assertIsNone(metadata["model"]["selected_label"])
        self.assertIsNone(metadata["model"]["resolved_version"])
        self.assertIsNone(metadata["copilot_chat"]["active_version"])
        self.assertTrue(metadata["python"]["version"])

    def test_metadata_does_not_copy_arbitrary_environment(self):
        with patch.dict("os.environ", {"PRIVATE_TOKEN_FOR_TEST": "do-not-copy-this-value"}):
            metadata = collect_environment()
        self.assertNotIn("do-not-copy-this-value", json.dumps(metadata))

    def test_metadata_uses_installed_inventory(self):
        with tempfile.TemporaryDirectory() as home_name:
            home = Path(home_name)
            inventory = home / ".vscode-server/extensions/extensions.json"
            inventory.parent.mkdir(parents=True)
            inventory.write_text(json.dumps([{"identifier": {"id": "GitHub.copilot-chat"}, "version": "0.68.0"}]))
            with patch("workflows.environment.Path.home", return_value=home), \
                 patch("workflows.environment.shutil.which", return_value=None), \
                 patch.dict("os.environ", {"TERM_PROGRAM": "vscode", "TERM_PROGRAM_VERSION": "1.100.0"}):
                metadata = collect_environment()
        self.assertEqual(metadata["editor"]["version"], "1.100.0")
        self.assertEqual(metadata["copilot_chat"]["installed_versions"][0]["version"], "0.68.0")
        self.assertIsNone(metadata["copilot_chat"]["active_version"])


if __name__ == "__main__":
    unittest.main()
