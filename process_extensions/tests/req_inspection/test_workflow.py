import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from workflows.base import CHECKLIST_IDS, WorkflowError, finalize, prepare_draft, read_json, validate_assessment
from workflows.req_safety_inspection.workflow import draft_chat, import_response, main, make_request, parse_requirements_rst, run_directory, start_chat
from workflows.environment import collect_environment
from workflows.review import confirm_review, parse_review, prepare_chat_review, reject_review, render_review, stage_review


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name) / "run"
        self.requirements = [{"id": "feat_req__example", "title": "Example", "text": "Shall work."}]
        self.assessment = {"requirements": [{
            "req_id": "feat_req__example", "req_title": "Example",
            "checklist": {identifier: {"verdict": "yes", "rationale": "Full rationale " * 30}
                          for identifier in CHECKLIST_IDS}, "findings": [],
        }]}

    def prepare(self, reviewed=True):
        path = prepare_draft(self.directory, self.requirements, self.assessment,
                             {"feature_name": "Example"}, {"interface": "offline-test"})
        draft = read_json(path.read_text())
        if reviewed:
            for check in draft["review"]["feat_req__example"].values():
                check.update(decision="yes", remarks="Independently checked.")
            path.write_text(json.dumps(draft))
        return path

    def test_valid_assessment(self):
        validate_assessment(self.assessment, self.requirements)

    def test_wrong_identity(self):
        self.assessment["requirements"][0]["req_id"] = "invented"
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_extra_checklist_item(self):
        self.assessment["requirements"][0]["checklist"]["invented"] = {}
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_duplicate_json_key(self):
        with self.assertRaises(WorkflowError):
            read_json('{"requirements": [], "requirements": []}')

    def test_noninteractive_approval_rejected(self):
        self.prepare()
        with patch("sys.stdin.isatty", return_value=False), self.assertRaises(WorkflowError):
            finalize(self.directory)
        self.assertFalse((self.directory / "report.rst").exists())

    def test_missing_review_rejected(self):
        self.prepare(reviewed=False)
        with patch("sys.stdin.isatty", return_value=True), self.assertRaises(WorkflowError):
            finalize(self.directory)

    def test_explicit_rejection(self):
        self.prepare()
        with patch("sys.stdin.isatty", return_value=True), patch("builtins.input", return_value="reject incorrect"), self.assertRaises(WorkflowError):
            finalize(self.directory)
        self.assertFalse((self.directory / "audit.json").exists())

    def test_missing_named_approval(self):
        self.prepare()
        with patch("sys.stdin.isatty", return_value=True), patch("builtins.input", return_value="approve"), self.assertRaises(WorkflowError):
            finalize(self.directory)

    def test_approved_report_preserves_full_rationale(self):
        self.prepare()
        with patch("sys.stdin.isatty", return_value=True), patch("builtins.input", return_value="approve Test Reviewer"):
            report = finalize(self.directory)
        self.assertIn("Full rationale " * 29, report.read_text())
        audit = read_json((self.directory / "audit.json").read_text())
        self.assertEqual(audit["reviewer"], "Test Reviewer")
        self.assertFalse(audit["assessment_corrections_applied"])

    def test_edited_assessment_recorded(self):
        path = self.prepare()
        draft = read_json(path.read_text())
        draft["assessment"]["requirements"][0]["checklist"]["REQ_01_01"]["rationale"] = "Corrected by reviewer."
        path.write_text(json.dumps(draft))
        with patch("sys.stdin.isatty", return_value=True), patch("builtins.input", return_value="approve Reviewer"):
            finalize(self.directory)
        self.assertTrue(read_json((self.directory / "audit.json").read_text())["assessment_corrections_applied"])

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

    def test_chat_response_uses_same_validation(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        with patch("workflows.req_safety_inspection.workflow.EXTENSION_ROOT", Path(self.temporary.name)):
            make_request(fixture, "Example", "ASIL_B", "chat")
            response = run_directory("chat") / "response.json"
            response.write_text(json.dumps(self.assessment))
            review = import_response("chat", response, "selected-model", "extension-test-version")
        self.assertTrue(review.exists())
        self.assertFalse((review.parent / "audit.json").exists())
        provenance = read_json((review.parent / "manifest.json").read_text())["provenance"]
        self.assertEqual(provenance["interface"], "copilot-chat")
        self.assertEqual(provenance["tool_version_source"], "reviewer supplied")
        self.assertIsNone(provenance["resolved_model_version"])

    def test_eof_does_not_finalize(self):
        self.prepare()
        with patch("sys.stdin.isatty", return_value=True), patch("builtins.input", side_effect=EOFError), self.assertRaises(WorkflowError):
            finalize(self.directory)
        self.assertFalse((self.directory / "report.rst").exists())

    def test_review_change_during_approval_rejected(self):
        path = self.prepare()

        def change_review(prompt):
            path.write_text(path.read_text() + "\n")
            return "approve Reviewer"

        with patch("sys.stdin.isatty", return_value=True), patch("builtins.input", side_effect=change_review), self.assertRaises(WorkflowError):
            finalize(self.directory)
        self.assertFalse((self.directory / "audit.json").exists())

    def test_generation_command_not_available(self):
        with patch("sys.argv", ["workflow", "generate"]), patch("sys.stderr"), self.assertRaises(SystemExit) as error:
            main()
        self.assertEqual(error.exception.code, 2)

    def test_invalid_verdict_rejected(self):
        self.assessment["requirements"][0]["checklist"]["REQ_01_01"]["verdict"] = "maybe"
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_missing_requirement_rejected(self):
        self.assessment["requirements"] = []
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)

    def test_finding_on_passed_item_rejected(self):
        self.assessment["requirements"][0]["findings"] = [{
            "check_id": "REQ_01_01", "severity": "major", "description": "Issue", "suggestion": "Fix",
        }]
        with self.assertRaises(WorkflowError):
            validate_assessment(self.assessment, self.requirements)


class ChatReviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name) / "run"
        self.requirements = [{"id": "feat_req__example", "title": "Example", "text": "Shall work."}]
        self.assessment = {"requirements": [{
            "req_id": "feat_req__example", "req_title": "Example",
            "checklist": {identifier: {"verdict": "yes", "rationale": "Evidence | value < 3.\nNext line."}
                          for identifier in CHECKLIST_IDS}, "findings": [],
        }]}
        self.state = prepare_chat_review(self.directory, self.requirements, self.assessment,
                                         {"feature_name": "Example"}, {"interface": "copilot-chat"})

    def test_markdown_round_trip(self):
        self.assertEqual(parse_review(render_review(self.assessment), self.requirements), self.assessment)

    def test_findings_round_trip(self):
        entry = self.assessment["requirements"][0]
        entry["checklist"]["REQ_01_01"]["verdict"] = "no"
        entry["findings"] = [{"check_id": "REQ_01_01", "severity": "minor",
                              "description": "Issue | details", "suggestion": "Correct the wording."}]
        self.assertEqual(parse_review(render_review(self.assessment), self.requirements), self.assessment)

    def test_extra_table_cell_not_silently_truncated(self):
        text = render_review(self.assessment).replace("| REQ_01_01 | yes |", "| REQ_01_01 | yes | extra |")
        with self.assertRaises(WorkflowError):
            parse_review(text, self.requirements)

    def test_stops_after_draft(self):
        self.assertEqual(self.state["status"], "awaiting_confirmation")
        self.assertFalse((self.directory / "report.rst").exists())
        self.assertFalse((self.directory / "audit.json").exists())

    def test_named_chat_confirmation(self):
        report = confirm_review(self.directory, self.state["revision_token"], "Approve as Test Reviewer")
        self.assertTrue(report.exists())
        audit = read_json((self.directory / "audit.json").read_text())
        self.assertEqual(audit["approver"], "Test Reviewer")
        self.assertEqual(audit["reviewed_assessment"], self.assessment)

    def test_no_implicit_approval(self):
        for message in ("", "Looks fine", "Approve", "Approve as "):
            with self.assertRaises(WorkflowError):
                confirm_review(self.directory, self.state["revision_token"], message)
        self.assertFalse((self.directory / "report.rst").exists())

    def test_edit_invalidates_confirmation(self):
        review = self.directory / "review.md"
        review.write_text(review.read_text().replace("Evidence", "Corrected evidence"))
        with self.assertRaises(WorkflowError):
            confirm_review(self.directory, self.state["revision_token"], "Approve as Reviewer")
        updated = stage_review(self.directory)
        self.assertEqual(updated["revision"], 2)
        with self.assertRaises(WorkflowError):
            confirm_review(self.directory, self.state["revision_token"], "Approve as Reviewer")
        confirm_review(self.directory, updated["revision_token"], "Approve as Reviewer")
        audit = read_json((self.directory / "audit.json").read_text())
        self.assertTrue(audit["assessment_corrections_applied"])
        self.assertEqual(audit["original_assessment"], self.assessment)

    def test_rejection_closes_run(self):
        reject_review(self.directory, "Missing evidence")
        with self.assertRaises(WorkflowError):
            confirm_review(self.directory, self.state["revision_token"], "Approve as Reviewer")
        self.assertFalse((self.directory / "audit.json").exists())

    def test_no_duplicate_finalization(self):
        confirm_review(self.directory, self.state["revision_token"], "Approve as Reviewer")
        with self.assertRaises(WorkflowError):
            confirm_review(self.directory, self.state["revision_token"], "Approve as Reviewer")

    def test_invalid_review_not_staged(self):
        review = self.directory / "review.md"
        review.write_text(review.read_text().replace("REQ_01_01", "invented"))
        with self.assertRaises(WorkflowError):
            stage_review(self.directory)

    def test_changed_manifest_rejected(self):
        manifest = self.directory / "manifest.json"
        manifest.write_text(manifest.read_text() + "\n")
        with self.assertRaises(WorkflowError):
            stage_review(self.directory)

    def test_start_to_chat_confirmation(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        environment = collect_environment()
        with patch("workflows.req_safety_inspection.workflow.EXTENSION_ROOT", Path(self.temporary.name)), patch("workflows.req_safety_inspection.workflow.collect_environment", return_value=environment):
            run = start_chat(fixture, "Example", "ASIL_B", "example")
            Path(run["response"]).write_text(json.dumps(self.assessment))
            state = draft_chat(run["run"])
            self.assertEqual(state["status"], "awaiting_confirmation")
            report = confirm_review(run_directory(run["run"]), state["revision_token"], "Approve as User")
        self.assertTrue(report.exists())
        audit = read_json((report.parent / "audit.json").read_text())
        self.assertIn("environment", audit["provenance"])
        self.assertEqual(audit["approver"], "User")

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
        home = Path(self.temporary.name)
        inventory = home / ".vscode-server/extensions/extensions.json"
        inventory.parent.mkdir(parents=True)
        inventory.write_text(json.dumps([{"identifier": {"id": "GitHub.copilot-chat"}, "version": "0.68.0"}]))
        with patch("workflows.environment.Path.home", return_value=home), patch("workflows.environment.shutil.which", return_value=None), patch.dict("os.environ", {"TERM_PROGRAM": "vscode", "TERM_PROGRAM_VERSION": "1.100.0"}):
            metadata = collect_environment()
        self.assertEqual(metadata["editor"]["version"], "1.100.0")
        self.assertEqual(metadata["copilot_chat"]["installed_versions"][0]["version"], "0.68.0")
        self.assertIsNone(metadata["copilot_chat"]["active_version"])

    def test_start_keeps_previous_runs(self):
        fixture = Path(self.temporary.name) / "input.rst"
        fixture.write_text(".. feat_req:: Example\n   :id: feat_req__example\n\n   Shall work.\n")
        with patch("workflows.req_safety_inspection.workflow.EXTENSION_ROOT", Path(self.temporary.name)):
            first = start_chat(fixture, "Example", "ASIL_B", "example")
            second = start_chat(fixture, "Example", "ASIL_B", "example")
        self.assertNotEqual(first["run"], second["run"])
        self.assertTrue(Path(first["prompt"]).exists())


if __name__ == "__main__":
    unittest.main()
