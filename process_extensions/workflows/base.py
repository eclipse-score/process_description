"""Shared validation and human finalization for the demonstration workflow."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CHECKLIST_IDS = (
    "REQ_01_01", "REQ_02_01", "REQ_02_02", "REQ_02_03", "REQ_02_04",
    "REQ_02_05", "REQ_03_01", "REQ_04_01", "REQ_05_01", "REQ_06_01",
    "REQ_07_01", "REQ_07_02", "REQ_08_01", "REQ_08_02", "REQ_09_01", "REQ_10_01",
)
VERDICTS = {"yes", "no", "n/a"}
TEMPLATE = Path(__file__).parent / "req_safety_inspection/templates/inspection_report.rst"


class WorkflowError(ValueError):
    """Invalid input, assessment, review, or approval."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise WorkflowError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(text: str) -> Any:
    try:
        return json.loads(text, object_pairs_hook=_unique_object)
    except json.JSONDecodeError as error:
        raise WorkflowError(f"Invalid JSON: {error}") from error


def _keys(value: Any, expected: set[str], name: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise WorkflowError(f"{name} must contain exactly: {sorted(expected)}")


def _text(value: Any, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise WorkflowError(f"{name} must be non-empty text")


def validate_assessment(data: Any, requirements: list[dict[str, str]]) -> dict:
    _keys(data, {"requirements"}, "Assessment")
    entries = data["requirements"]
    if not isinstance(entries, list) or len(entries) != len(requirements):
        raise WorkflowError("Assessment requirement count does not match input")
    expected = {requirement["id"]: requirement for requirement in requirements}
    if not expected or len(expected) != len(requirements):
        raise WorkflowError("Input requirement IDs must be unique and non-empty")
    seen = set()
    for entry in entries:
        _keys(entry, {"req_id", "req_title", "checklist", "findings"}, "Requirement")
        _text(entry["req_id"], "Requirement ID")
        identifier = entry["req_id"]
        if identifier not in expected or identifier in seen:
            raise WorkflowError(f"Unexpected or duplicate requirement ID: {identifier}")
        seen.add(identifier)
        if entry["req_title"] != expected[identifier]["title"]:
            raise WorkflowError(f"Requirement title changed: {identifier}")
        _keys(entry["checklist"], set(CHECKLIST_IDS), "Checklist")
        for check_id, check in entry["checklist"].items():
            _keys(check, {"verdict", "rationale"}, check_id)
            if not isinstance(check["verdict"], str) or check["verdict"] not in VERDICTS:
                raise WorkflowError(f"Invalid verdict: {identifier}/{check_id}")
            _text(check["rationale"], "Rationale")
        if not isinstance(entry["findings"], list):
            raise WorkflowError("Findings must be a list")
        for finding in entry["findings"]:
            _keys(finding, {"check_id", "severity", "description", "suggestion"}, "Finding")
            check_id = finding["check_id"]
            if not isinstance(check_id, str) or check_id not in CHECKLIST_IDS:
                raise WorkflowError("Finding references an unknown checklist ID")
            if entry["checklist"][check_id]["verdict"] != "no":
                raise WorkflowError("Finding must reference a 'no' verdict")
            if finding["severity"] not in ("major", "minor", "observation"):
                raise WorkflowError("Invalid finding severity")
            _text(finding["description"], "Finding description")
            _text(finding["suggestion"], "Finding suggestion")
    return data


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _rst_text(value: str) -> str:
    text = " ".join(value.split())
    for character in ("\\", "*", "`", "_", "|"):
        text = text.replace(character, "\\" + character)
    return text


def render_report(draft: dict, approved: bool = False) -> str:
    sections = []
    for entry in draft["assessment"]["requirements"]:
        identifier = entry["req_id"]
        sections.extend([
            _rst_text(identifier), "~" * (len(_rst_text(identifier)) + 1), "",
            ".. list-table:: Requirement assessment", "   :header-rows: 1", "",
            "   * - Check", "     - AI verdict", "     - Full AI rationale",
            "     - Reviewer decision", "     - Reviewer remarks",
        ])
        for check_id in CHECKLIST_IDS:
            check = entry["checklist"][check_id]
            review = draft["review"][identifier][check_id]
            cells = (check_id, check["verdict"], check["rationale"],
                     review["decision"], review["remarks"])
            sections.append("   * - " + _rst_text(cells[0]))
            sections.extend("     - " + _rst_text(cell) for cell in cells[1:])
        sections.append("")
        for finding in entry["findings"]:
            sections.append("- " + _rst_text(
                f"{finding['check_id']} ({finding['severity']}): "
                f"{finding['description']} Suggestion: {finding['suggestion']}"
            ))
        sections.append("")
    template = TEMPLATE.read_text(encoding="utf-8")
    return (template.replace("{{STATUS}}", "HUMAN-APPROVED DEMONSTRATION" if approved else "DRAFT")
            .replace("{{FEATURE_NAME}}", _rst_text(draft["context"]["feature_name"]))
            .replace("{{REQUIREMENT_SECTIONS}}", "\n".join(sections)))


def prepare_draft(directory: Path, requirements: list[dict[str, str]],
                  assessment: dict, context: dict, provenance: dict) -> Path:
    validate_assessment(assessment, requirements)
    if directory.exists() and any(path.name not in {"request.json", "prompt.md", "response.json"}
                                  for path in directory.iterdir()):
        raise WorkflowError("Run directory already contains a draft; choose a new run name")
    directory.mkdir(parents=True, exist_ok=True)
    manifest = {
        "requirements": requirements, "context": context, "provenance": provenance,
        "initial_assessment": assessment,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    _write_json(directory / "manifest.json", manifest)
    draft = {
        "assessment": assessment, "context": context,
        "review": {entry["req_id"]: {
            check_id: {"decision": "", "remarks": ""} for check_id in CHECKLIST_IDS
        } for entry in assessment["requirements"]},
    }
    _write_json(directory / "review.json", draft)
    (directory / "draft.rst").write_text(render_report(draft), encoding="utf-8")
    return directory / "review.json"


def finalize(directory: Path) -> Path:
    if not sys.stdin.isatty():
        raise WorkflowError("Human finalization requires an interactive terminal")
    if any((directory / name).exists() for name in ("report.rst", "audit.json")):
        raise WorkflowError("This run has already been finalized")
    manifest_path = directory / "manifest.json"
    manifest_snapshot = _digest(manifest_path)
    manifest = read_json(manifest_path.read_text(encoding="utf-8"))
    review_path = directory / "review.json"
    draft = read_json(review_path.read_text(encoding="utf-8"))
    _keys(draft, {"assessment", "context", "review"}, "Review document")
    if draft["context"] != manifest["context"]:
        raise WorkflowError("Review context differs from the run manifest")
    validate_assessment(draft["assessment"], manifest["requirements"])
    identifiers = {entry["id"] for entry in manifest["requirements"]}
    _keys(draft["review"], identifiers, "Reviewer requirements")
    for identifier, checks in draft["review"].items():
        _keys(checks, set(CHECKLIST_IDS), "Reviewer checklist")
        for check_id, check in checks.items():
            _keys(check, {"decision", "remarks"}, "Reviewer entry")
            if not isinstance(check["decision"], str) or check["decision"] not in VERDICTS:
                raise WorkflowError(f"Missing or invalid reviewer decision: {identifier}/{check_id}")
            _text(check["remarks"], f"Reviewer remarks: {identifier}/{check_id}")
    snapshot = _digest(review_path)
    print("Review review.json and fill every decision and remark before approving.")
    try:
        decision = input("Type 'approve <reviewer-name>' or 'reject <reason>': ").strip()
    except EOFError as error:
        raise WorkflowError("No human approval received") from error
    action, separator, reviewer = decision.partition(" ")
    if action != "approve" or not separator or not reviewer.strip():
        raise WorkflowError("Rejected or no explicit named approval; draft retained")
    if _digest(review_path) != snapshot or _digest(manifest_path) != manifest_snapshot:
        raise WorkflowError("Review or manifest changed during approval; review again")
    audit = {
        "provenance": manifest["provenance"], "run_timestamp": manifest["run_timestamp"],
        "reviewer": reviewer.strip(), "decision": "approved",
        "review_timestamp": datetime.now(timezone.utc).isoformat(),
        "assessment_corrections_applied": draft["assessment"] != manifest["initial_assessment"],
        "review_sha256": snapshot, "manifest_sha256": manifest_snapshot,
        "qualification_claim": "none; demonstration approval is not tool qualification",
    }
    report = render_report(draft, approved=True)
    report += "\nAudit Record\n------------\n\n.. code-block:: json\n\n"
    report += "\n".join("   " + line for line in json.dumps(audit, indent=2).splitlines()) + "\n"
    (directory / "report.rst").write_text(report, encoding="utf-8")
    _write_json(directory / "audit.json", audit)
    return directory / "report.rst"
