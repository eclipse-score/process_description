"""Canonical checklist loading and schema validation for the demonstration workflow."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
CANONICAL_CHECKLIST_TEMPLATE = (
    REPO_ROOT / "process/folder_templates/platform/features/feature_name/requirements/req_inspection.rst"
)
VERDICTS = {"yes", "no", "n/a", "not_assessed"}
# Items whose public guidance requires parent requirement text; enforced to
# "not_assessed" when no parent context was supplied, instead of a guess.
PARENT_TEXT_REQUIRED_IDS = ("REQ_03_01", "REQ_10_01")

_ROW = re.compile(
    r"^    \* - (?P<id>REQ_\d{2}_\d{2})\s*\n"
    r"      - (?P<criterion>.+?)\s*\n"
    r"      - (?P<guidance>.+?)\s*\n"
    r"      -\s*\n"
    r"      -\s*\n"
    r"      -\s*$",
    re.MULTILINE,
)


class WorkflowError(ValueError):
    """Invalid input, assessment, review, or configuration."""


def load_checklist() -> dict[str, dict[str, str]]:
    """Parse Review ID, Acceptance Criteria, and Guidance directly from the
    canonical public S-CORE feature requirements inspection checklist template.

    This is the single source of truth for checklist content: no paraphrased
    or hand-copied text is kept elsewhere, so the prompt and schema cannot
    silently drift from the template this project already publishes.
    """
    try:
        text = CANONICAL_CHECKLIST_TEMPLATE.read_text(encoding="utf-8")
    except OSError as error:
        raise WorkflowError(
            f"Cannot read the canonical checklist template at {CANONICAL_CHECKLIST_TEMPLATE}"
        ) from error
    checklist = {}
    for match in _ROW.finditer(text):
        identifier = match["id"]
        if identifier in checklist:
            raise WorkflowError(f"Canonical checklist template has a duplicate ID: {identifier}")
        checklist[identifier] = {"criterion": match["criterion"], "guidance": match["guidance"]}
    if not checklist:
        raise WorkflowError("Canonical checklist template has no parseable Review ID rows")
    return checklist


CHECKLIST = load_checklist()
CHECKLIST_IDS = tuple(CHECKLIST)


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
    """Validate an assessment against the exact public checklist and supplied input.

    Each checklist entry carries a ``passed`` verdict (restricted to
    ``yes``/``no``/``n/a``/``not_assessed``), free-text ``remarks``, and an
    ``issue_link`` that is mandatory for every ``no`` and forbidden otherwise.
    ``not_assessed`` means the AI lacked sufficient context to judge the item;
    it is never equivalent to a pass or to a genuine ``n/a``. Items whose
    public guidance requires parent requirement text (REQ_03_01, REQ_10_01)
    must be ``not_assessed`` unless parent context was actually supplied.
    """
    _keys(data, {"requirements"}, "Assessment")
    entries = data["requirements"]
    if not isinstance(entries, list) or len(entries) != len(requirements):
        raise WorkflowError("Assessment requirement count does not match input")
    expected = {requirement["id"]: requirement for requirement in requirements}
    if not expected or len(expected) != len(requirements):
        raise WorkflowError("Input requirement IDs must be unique and non-empty")
    seen = set()
    for entry in entries:
        _keys(entry, {"req_id", "req_title", "checklist"}, "Requirement")
        _text(entry["req_id"], "Requirement ID")
        identifier = entry["req_id"]
        if identifier not in expected or identifier in seen:
            raise WorkflowError(f"Unexpected or duplicate requirement ID: {identifier}")
        seen.add(identifier)
        if entry["req_title"] != expected[identifier]["title"]:
            raise WorkflowError(f"Requirement title changed: {identifier}")
        _keys(entry["checklist"], set(CHECKLIST_IDS), "Checklist")
        has_parent_context = bool(expected[identifier].get("parent_context_available"))
        for check_id, check in entry["checklist"].items():
            _keys(check, {"passed", "remarks", "issue_link"}, check_id)
            if not isinstance(check["passed"], str) or check["passed"] not in VERDICTS:
                raise WorkflowError(f"Invalid verdict: {identifier}/{check_id}")
            _text(check["remarks"], f"Remarks: {identifier}/{check_id}")
            if not isinstance(check["issue_link"], str):
                raise WorkflowError(f"Issue link must be text: {identifier}/{check_id}")
            if check["passed"] == "no" and not check["issue_link"].strip():
                raise WorkflowError(f"Issue link is mandatory for a 'no' verdict: {identifier}/{check_id}")
            if check["passed"] != "no" and check["issue_link"].strip():
                raise WorkflowError(f"Issue link is only allowed for a 'no' verdict: {identifier}/{check_id}")
            if (check_id in PARENT_TEXT_REQUIRED_IDS and not has_parent_context
                    and check["passed"] != "not_assessed"):
                raise WorkflowError(
                    f"{check_id} requires supplied parent context; got '{check['passed']}' "
                    f"without context for {identifier}. Supply --context or use 'not_assessed'."
                )
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
