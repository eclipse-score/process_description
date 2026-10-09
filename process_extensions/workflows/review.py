"""Editable requirements inspection checklist, in the exact public template shape.

There is no local approval step here. The engineer copies the confirmed table
into the project's real inspection work product (for example
``doc__<feature>_req_inspection.rst``) and commits it; approval is the normal
Git/GitHub review of that change, not a Chat message relayed by this tool.
"""

from __future__ import annotations

import csv
import html
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

import markdown

from workflows.base import CHECKLIST, CHECKLIST_IDS, WorkflowError, _write_json, read_json, validate_assessment


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _cell(value: str) -> str:
    text = html.escape(value, quote=False).replace("|", "&#124;")
    for character in ("\\", "*", "_", "`"):
        text = text.replace(character, "\\" + character)
    return text.replace("\n", "<br>")


def render_checklist(assessment: dict) -> str:
    lines = [
        "# Requirements inspection checklist", "",
        "Draft prepared by a Chat Agent; not reviewed or approved. The",
        "**Criterion** and **Guidance** columns are the canonical public S-CORE",
        "checklist text and are not editable here (edits to them are ignored on",
        "re-check). Edit **Passed**, **Remarks**, and **Issue link** only.",
        "`not_assessed` means missing context, never a pass. An issue link is",
        "mandatory for every `no` and not allowed otherwise. When ready, copy",
        "this table into the project's real requirements inspection document",
        "and open it for the normal Git/GitHub review; that review is the only",
        "approval this tool recognizes.", "",
    ]
    for entry in assessment["requirements"]:
        lines.extend([
            f"## `{entry['req_id']}`", "", _cell(entry["req_title"]), "",
            "| Check | Criterion | Guidance | Passed | Remarks | Issue link |",
            "| --- | --- | --- | --- | --- | --- |",
        ])
        for check_id in CHECKLIST_IDS:
            check = entry["checklist"][check_id]
            lines.append(
                f"| {check_id} | {_cell(CHECKLIST[check_id]['criterion'])} | "
                f"{_cell(CHECKLIST[check_id]['guidance'])} | {check['passed']} | "
                f"{_cell(check['remarks'])} | {_cell(check['issue_link'])} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


class _ChecklistTables(HTMLParser):
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
                raise WorkflowError("Checklist tables must belong to a requirement heading")
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


def parse_checklist(text: str, requirements: list[dict[str, str]]) -> dict:
    width = None
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            width = None
            continue
        cells = next(csv.reader([line.strip()], delimiter="|", escapechar="\\", quoting=csv.QUOTE_NONE))
        if cells[0] != "" or cells[-1] != "":
            raise WorkflowError("Checklist table rows must start and end with a pipe")
        count = len(cells) - 2
        if width is None:
            width = count
        if count != width:
            raise WorkflowError("Checklist table cell count changed; escape literal pipes")
    parser = _ChecklistTables()
    parser.feed(markdown.markdown(text, extensions=["tables"]))
    parser.close()
    expected = {entry["id"]: entry for entry in requirements}
    assessment = {"requirements": []}
    header = ["Check", "Criterion", "Guidance", "Passed", "Remarks", "Issue link"]
    for section in parser.sections:
        identifier = section["id"]
        if identifier not in expected or len(section["tables"]) != 1:
            raise WorkflowError("Each known requirement must have exactly one checklist table")
        rows = section["tables"][0]
        if not rows or rows[0] != header:
            raise WorkflowError("Checklist table header changed")
        checklist = {}
        for row in rows[1:]:
            if len(row) != 6 or row[0] in checklist:
                raise WorkflowError("Checklist rows must be unique and have six cells")
            check_id = row[0]
            if check_id not in CHECKLIST_IDS:
                raise WorkflowError(f"Unknown checklist ID: {check_id}")
            # Criterion/guidance (row[1], row[2]) are not trusted from the file;
            # they are always taken from the canonical template.
            checklist[check_id] = {"passed": row[3], "remarks": row[4], "issue_link": row[5]}
        if set(checklist) != set(CHECKLIST_IDS):
            raise WorkflowError(f"Checklist for {identifier} is missing rows")
        assessment["requirements"].append({
            "req_id": identifier, "req_title": expected[identifier]["title"],
            "checklist": checklist,
        })
    return validate_assessment(assessment, requirements)


def prepare_inspection(directory: Path, requirements: list[dict[str, str]],
                       assessment: dict, context: dict, provenance: dict) -> dict:
    validate_assessment(assessment, requirements)
    allowed = {"request.json", "prompt.md", "response.json"}
    if directory.exists() and any(path.name not in allowed for path in directory.iterdir()):
        raise WorkflowError("Run already contains inspection artifacts; do not overwrite")
    directory.mkdir(parents=True, exist_ok=True)
    _write_json(directory / "manifest.json", {
        "format_version": 3, "requirements": requirements, "context": context,
        "provenance": provenance, "initial_assessment": assessment, "run_timestamp": _now(),
    })
    (directory / "inspection.md").write_text(render_checklist(assessment), encoding="utf-8")
    return check_inspection(directory)


def check_inspection(directory: Path) -> dict:
    """Re-validate the current ``inspection.md`` and summarize it for presentation.

    This has no approval semantics: it is immediate feedback while editing,
    not a gate. Nothing here can be fabricated into an approval.
    """
    manifest = read_json((directory / "manifest.json").read_text(encoding="utf-8"))
    checklist_path = directory / "inspection.md"
    assessment = parse_checklist(checklist_path.read_text(encoding="utf-8"), manifest["requirements"])
    counts = {"yes": 0, "no": 0, "n/a": 0, "not_assessed": 0}
    issue_links = []
    for entry in assessment["requirements"]:
        for check_id, check in entry["checklist"].items():
            counts[check["passed"]] += 1
            if check["passed"] == "no":
                issue_links.append({"req_id": entry["req_id"], "check_id": check_id,
                                     "issue_link": check["issue_link"]})
    return {
        "checklist_file": str(checklist_path), "requirement_count": len(assessment["requirements"]),
        "verdict_counts": counts, "open_issues": issue_links,
        "changed_since_draft": assessment != manifest["initial_assessment"],
        "next_step": "Copy this table into the project's real inspection document, "
                     "commit it, and open it for Git/GitHub review. This tool does not "
                     "approve or finalize the inspection.",
    }
