"""Editable Markdown review and revision-bound chat confirmation."""

from __future__ import annotations

import html
import csv
import json
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

import markdown

from workflows.base import CHECKLIST_IDS, TEMPLATE, WorkflowError, _digest, _rst_text, _write_json, read_json, validate_assessment
from workflows.environment import collect_environment


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _cell(value: str) -> str:
    text = html.escape(value, quote=False).replace("|", "&#124;")
    for character in ("\\", "*", "_", "`"):
        text = text.replace(character, "\\" + character)
    return text.replace("\n", "<br>")


def render_review(assessment: dict) -> str:
    lines = [
        "# Requirements review", "",
        "Edit the verdicts, rationales, and findings in these tables. Keep the",
        "requirement/checklist IDs and table headers unchanged. Missing context",
        "is not a pass. Return to Chat when ready; editing is not approval.", "",
    ]
    for entry in assessment["requirements"]:
        lines.extend([
            f"## `{entry['req_id']}`", "", _cell(entry["req_title"]), "",
            "### Checklist", "", "| Check | Verdict | Rationale |",
            "| --- | --- | --- |",
        ])
        for check_id in CHECKLIST_IDS:
            check = entry["checklist"][check_id]
            lines.append(f"| {check_id} | {check['verdict']} | {_cell(check['rationale'])} |")
        lines.extend([
            "", "### Findings", "", "| Check | Severity | Description | Suggestion |",
            "| --- | --- | --- | --- |",
        ])
        for finding in entry["findings"]:
            lines.append("| " + " | ".join(_cell(finding[key]) for key in
                         ("check_id", "severity", "description", "suggestion")) + " |")
        lines.append("")
    return "\n".join(lines) + "\n"


class _ReviewTables(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.sections = []
        self.heading = None
        self.table = None
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            self.heading = []
        elif tag == "table":
            if not self.sections or self.table is not None:
                raise WorkflowError("Review tables must belong to a requirement heading")
            self.table = []
        elif tag == "tr" and self.table is not None:
            self.row = []
        elif tag in ("th", "td") and self.row is not None:
            self.cell = []
        elif tag == "br" and self.cell is not None:
            self.cell.append("\n")

    def handle_data(self, data):
        if self.heading is not None:
            self.heading.append(data)
        elif self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag == "h2" and self.heading is not None:
            self.sections.append({"id": "".join(self.heading).strip(), "tables": []})
            self.heading = None
        elif tag in ("th", "td") and self.cell is not None:
            self.row.append("".join(self.cell).strip())
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            self.sections[-1]["tables"].append(self.table)
            self.table = None


def parse_review(text: str, requirements: list[dict[str, str]]) -> dict:
    width = None
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            width = None
            continue
        cells = next(csv.reader([line.strip()], delimiter="|", escapechar="\\", quoting=csv.QUOTE_NONE))
        if cells[0] != "" or cells[-1] != "":
            raise WorkflowError("Review table rows must start and end with a pipe")
        count = len(cells) - 2
        if width is None:
            width = count
        if count != width:
            raise WorkflowError("Review table cell count changed; escape literal pipes")
    parser = _ReviewTables()
    parser.feed(markdown.markdown(text, extensions=["tables"]))
    parser.close()
    expected = {entry["id"]: entry for entry in requirements}
    assessment = {"requirements": []}
    for section in parser.sections:
        identifier = section["id"]
        if identifier not in expected or len(section["tables"]) != 2:
            raise WorkflowError("Each known requirement must have exactly two review tables")
        checklist_rows, finding_rows = section["tables"]
        if not checklist_rows or checklist_rows[0] != ["Check", "Verdict", "Rationale"]:
            raise WorkflowError("Checklist table header changed")
        if not finding_rows or finding_rows[0] != ["Check", "Severity", "Description", "Suggestion"]:
            raise WorkflowError("Findings table header changed")
        checklist = {}
        for row in checklist_rows[1:]:
            if len(row) != 3 or row[0] in checklist:
                raise WorkflowError("Checklist rows must be unique and have three cells")
            checklist[row[0]] = {"verdict": row[1], "rationale": row[2]}
        findings = []
        for row in finding_rows[1:]:
            if not any(row):
                continue
            if len(row) != 4:
                raise WorkflowError("Finding rows must have four cells")
            findings.append(dict(zip(("check_id", "severity", "description", "suggestion"), row)))
        assessment["requirements"].append({
            "req_id": identifier, "req_title": expected[identifier]["title"],
            "checklist": checklist, "findings": findings,
        })
    return validate_assessment(assessment, requirements)


def _load(directory: Path) -> tuple[dict, dict]:
    manifest = read_json((directory / "manifest.json").read_text(encoding="utf-8"))
    state = read_json((directory / "review_state.json").read_text(encoding="utf-8"))
    if _digest(directory / "manifest.json") != state["manifest_sha256"]:
        raise WorkflowError("Run manifest changed; original judgment must remain intact")
    if state["status"] in ("approved", "rejected"):
        raise WorkflowError("Run is closed; start a new run")
    return manifest, state


def prepare_chat_review(directory: Path, requirements: list[dict[str, str]],
                        assessment: dict, context: dict, provenance: dict) -> dict:
    validate_assessment(assessment, requirements)
    allowed = {"request.json", "prompt.md", "response.json"}
    if directory.exists() and any(path.name not in allowed for path in directory.iterdir()):
        raise WorkflowError("Run already contains review artifacts; do not overwrite")
    directory.mkdir(parents=True, exist_ok=True)
    _write_json(directory / "manifest.json", {
        "format_version": 2, "requirements": requirements, "context": context,
        "provenance": provenance, "initial_assessment": assessment, "run_timestamp": _now(),
    })
    (directory / "review.md").write_text(render_review(assessment), encoding="utf-8")
    _write_json(directory / "review_state.json", {
        "status": "awaiting_review", "revision": 0, "review_sha256": None,
        "manifest_sha256": _digest(directory / "manifest.json"),
    })
    return stage_review(directory)


def stage_review(directory: Path) -> dict:
    manifest, state = _load(directory)
    review_path = directory / "review.md"
    text = review_path.read_text(encoding="utf-8")
    assessment = parse_review(text, manifest["requirements"])
    digest = _digest(review_path)
    if digest != state["review_sha256"]:
        state["revision"] += 1
        revisions = directory / "revisions"
        revisions.mkdir(exist_ok=True)
        snapshot = revisions / f"review-{state['revision']:04d}.md"
        if snapshot.exists():
            raise WorkflowError("Revision snapshot already exists; history must not be overwritten")
        snapshot.write_text(text, encoding="utf-8")
    state.update(status="awaiting_confirmation", review_sha256=digest,
                 revision_token=f"r{state['revision']}-{digest}", staged_at=_now())
    _write_json(directory / "review_state.json", state)
    return {**state, "review_file": str(review_path),
            "requirement_count": len(assessment["requirements"]),
            "finding_count": sum(len(entry["findings"]) for entry in assessment["requirements"])}


def _report(manifest: dict, reviewed: dict) -> str:
    original = {entry["req_id"]: entry for entry in manifest["initial_assessment"]["requirements"]}
    sections = []
    for entry in reviewed["requirements"]:
        identifier = entry["req_id"]
        sections.extend([
            _rst_text(identifier), "~" * (len(_rst_text(identifier)) + 1), "",
            ".. list-table:: Original and reviewed assessment", "   :header-rows: 1", "",
            "   * - Check", "     - Original AI verdict", "     - Original AI rationale",
            "     - Reviewed verdict", "     - Reviewed rationale",
        ])
        for check_id in CHECKLIST_IDS:
            before = original[identifier]["checklist"][check_id]
            after = entry["checklist"][check_id]
            cells = (check_id, before["verdict"], before["rationale"], after["verdict"], after["rationale"])
            sections.append("   * - " + _rst_text(cells[0]))
            sections.extend("     - " + _rst_text(cell) for cell in cells[1:])
        sections.append("")
        for finding in entry["findings"]:
            sections.append("- " + _rst_text(
                f"{finding['check_id']} ({finding['severity']}): {finding['description']} "
                f"Suggestion: {finding['suggestion']}"
            ))
        sections.append("")
    return (TEMPLATE.read_text(encoding="utf-8")
            .replace("{{STATUS}}", "HUMAN-CONFIRMED DEMONSTRATION")
            .replace("{{FEATURE_NAME}}", _rst_text(manifest["context"]["feature_name"]))
            .replace("{{REQUIREMENT_SECTIONS}}", "\n".join(sections)))


def confirm_review(directory: Path, revision: str, message: str) -> Path:
    manifest, state = _load(directory)
    match = re.fullmatch(r"Approve(?: this revision)? as ([^\r\n]+)", message.strip(), re.IGNORECASE)
    if not match or not match[1].strip():
        raise WorkflowError("An explicit user message 'Approve as <name>' is required")
    if state["status"] != "awaiting_confirmation" or revision != state["revision_token"]:
        raise WorkflowError("Confirmation does not match the revision presented in Chat")
    review_path = directory / "review.md"
    digest = _digest(review_path)
    if digest != state["review_sha256"]:
        raise WorkflowError("Review changed after presentation; stage and confirm the new revision")
    snapshot = directory / "revisions" / f"review-{state['revision']:04d}.md"
    if _digest(snapshot) != digest:
        raise WorkflowError("Presented revision snapshot changed")
    reviewed = parse_review(review_path.read_text(encoding="utf-8"), manifest["requirements"])
    if any((directory / name).exists() for name in ("report.rst", "audit.json")):
        raise WorkflowError("Final artifacts already exist; do not overwrite")
    timestamp = _now()
    final_environment = collect_environment()
    original_environment = manifest["provenance"].get("environment", {})
    original_fingerprint = original_environment.get("workflow", {}).get("sha256")
    if original_fingerprint and original_fingerprint != final_environment["workflow"]["sha256"]:
        raise WorkflowError("Workflow implementation changed since judgment; start a new run")
    audit = {
        "provenance": manifest["provenance"], "run_timestamp": manifest["run_timestamp"],
        "finalization_environment": final_environment,
        "tools_used": ["Copilot Chat Agent judgment", "Python input and schema validation",
                       "Markdown review parser", "Python revision tracking and report renderer"],
        "approver": match[1].strip(), "decision": "approved", "confirmation_timestamp": timestamp,
        "confirmation_source": "user Chat message relayed by agent; not authenticated",
        "confirmation_message": message, "revision": state["revision"], "revision_token": revision,
        "review_sha256": digest, "manifest_sha256": state["manifest_sha256"],
        "assessment_corrections_applied": reviewed != manifest["initial_assessment"],
        "original_assessment": manifest["initial_assessment"], "reviewed_assessment": reviewed,
        "qualification_claim": "none; Chat confirmation is not tool qualification",
    }
    report = _report(manifest, reviewed)
    report += "\nAudit Record\n------------\n\n.. code-block:: json\n\n"
    report += "\n".join("   " + line for line in json.dumps(audit, indent=2).splitlines()) + "\n"
    if _digest(review_path) != digest or _digest(directory / "manifest.json") != state["manifest_sha256"]:
        raise WorkflowError("Artifacts changed during finalization; confirmation invalidated")
    (directory / "report.rst").write_text(report, encoding="utf-8")
    _write_json(directory / "audit.json", audit)
    state.update(status="approved", approver=match[1].strip(), confirmed_at=timestamp)
    _write_json(directory / "review_state.json", state)
    return directory / "report.rst"


def reject_review(directory: Path, reason: str) -> None:
    _, state = _load(directory)
    if not reason.strip():
        raise WorkflowError("A rejection reason is required")
    state.update(status="rejected", rejection_reason=reason, rejected_at=_now())
    _write_json(directory / "review_state.json", state)
