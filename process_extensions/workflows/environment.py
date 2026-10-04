"""Collect version metadata without credentials, chat logs, or network access."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import platform
import shutil
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def collect_environment() -> dict:
    editor = {"version": None, "source": "not exposed to helper"}
    terminal_version = os.environ.get("TERM_PROGRAM_VERSION")
    if os.environ.get("TERM_PROGRAM") == "vscode" and terminal_version:
        editor = {"version": terminal_version, "source": "VS Code terminal environment"}
    candidates = []
    code = shutil.which("code") or shutil.which("code-insiders")
    if code:
        for parent in Path(code).resolve().parents:
            package = _json(parent / "package.json")
            product = _json(parent / "product.json")
            if isinstance(package, dict) and isinstance(product, dict) and package.get("version"):
                if editor["version"] is None:
                    editor = {"version": package["version"],
                              "source": "editor installation associated with code on PATH"}
                for folder in ("copilot", "github.copilot-chat"):
                    extension = _json(parent / "extensions" / folder / "package.json")
                    if isinstance(extension, dict):
                        identifier = f"{extension.get('publisher', '')}.{extension.get('name', '')}".lower()
                        if identifier == "github.copilot-chat" and extension.get("version"):
                            candidates.append({"version": extension["version"],
                                               "source": "bundled editor extension manifest"})
    for folder in (".vscode", ".vscode-server", ".vscode-server-insiders"):
        inventory = _json(Path.home() / folder / "extensions" / "extensions.json")
        if not isinstance(inventory, list):
            continue
        for entry in inventory:
            if not isinstance(entry, dict):
                continue
            identifier = entry.get("identifier", {})
            if isinstance(identifier, dict) and identifier.get("id", "").lower() == "github.copilot-chat":
                if entry.get("version"):
                    candidates.append({"version": entry["version"], "source": "installed extension inventory"})
    candidates = [dict(items) for items in sorted({tuple(sorted(entry.items())) for entry in candidates})]
    try:
        with (ROOT / "pyproject.toml").open("rb") as file:
            version = tomllib.load(file)["project"]["version"]
    except (OSError, KeyError, ValueError):
        version = None
    fingerprints = {}
    for path in sorted((ROOT / "workflows").rglob("*.py")):
        fingerprints[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    fingerprint = hashlib.sha256(json.dumps(fingerprints, sort_keys=True).encode()).hexdigest()
    return {
        "editor": editor,
        "copilot_chat": {
            "installed_versions": candidates, "active_version": None,
            "source": "local editor manifests and installed extension inventories",
            "limitation": "Installed versions do not prove which extension instance handled the Chat request",
        },
        "model": {
            "selected_label": None, "resolved_version": None,
            "source": "active built-in Chat request metadata is not exposed to the local helper",
            "limitation": "Do not infer the selected or resolved model from installed models or Auto",
        },
        "python": {"version": platform.python_version(), "source": "executing interpreter"},
        "markdown_parser": {"version": importlib.metadata.version("Markdown"), "source": "executing environment"},
        "workflow": {"version": version, "source": "local project metadata",
                     "sha256": fingerprint, "files": fingerprints},
        "agent_tool_ids": {"value": None, "source": "not exposed by the Chat session"},
    }
