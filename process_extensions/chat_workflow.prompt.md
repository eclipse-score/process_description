---
name: score-requirements-review
description: "Start requirements inspection in Chat, pause for editable checklist corrections, and hand off to the project's own PR review. There is no local approval command."
agent: agent
argument-hint: "Inspect baselibs, inspect a named requirements file, or check the current checklist"
---

# Chat-first requirements inspection

Use this protocol for the entire inspection conversation. Keep all artifacts
under `process_extensions/out/`. Do not change process definitions or existing
runs. This tool has no approval command: the engineer copies the checked
checklist into the project's real inspection document and the project's own
Git/GitHub review of that change is the only approval, never a Chat message.

## Start and judgment

1. For "Inspect baselibs", use the bundled public baselibs feature-requirement
   fixture and ASIL_B input context. For other inputs, accept feature or
   component requirements only. If stakeholder requirements, assumptions of
   use, or mixed-level directives are supplied, explain that their checklist
   profiles are unsupported and ask for feature/component input. Stakeholder
   requirements remain part of the existing S-CORE workflow and may be parent
   context, but are not automatically fetched or assessed. Ask for missing
   file/scope/context and sharing permission. Do not inspect unrelated material.
   If the engineer can supply parent or related requirement text, ask whether
   they want to pass it via `--context <file.json>` so linkage/completeness
   items can be genuinely assessed instead of `not_assessed`.
2. Select a Python 3.11+ interpreter with Markdown available. Prefer the existing
   workspace `.venv/bin/python` when available. Ask before installing missing
   dependencies; do not silently install packages.
3. Run the local helper from `process_extensions/`:
   `python -m workflows.req_safety_inspection.workflow start baselibs`.
   For another file use `start <file> --feature-name <name> --asil <level>`,
   optionally with `--context <file.json>` and `--model-label <label>` if the
   engineer tells you which model they selected. Retain the generated run name.
   Available environment metadata is collected automatically. Never invent
   model/version values or read credentials, chat logs, authentication
   settings, or another repository.
4. Read the generated prompt and assess only its supplied requirements against
   the exact checklist table in that prompt (parsed from the canonical public
   template, not a paraphrase). Write complete JSON to that run's
   `response.json`. Every item needs `passed` (`yes`/`no`/`n/a`/`not_assessed`),
   full `remarks`, and `issue_link` (mandatory for `no`, empty otherwise). Use
   `not_assessed` for missing context; never substitute `n/a` for it. The
   prepared prompt governs judgment; this protocol separately authorizes the
   named local helpers and artifact writes. No web retrieval or additional
   model invocation is authorized.
5. Run `python -m workflows.req_safety_inspection.workflow draft <run>`.
   Repair invalid assessment structure or ask for missing context if needed.
   Never convert missing evidence into an invented pass.
6. Present the `inspection.md` link, run name, verdict counts, and any open
   issue links. Ask the engineer to review, edit, or request corrections.
7. **STOP AND END YOUR TURN.** Do not approve, auto-confirm, or finalize
   anything in the judgment turn; there is no such command to invoke.

## Edits and corrections

The engineer may edit `inspection.md` or request specific corrections in Chat.
Apply only requested corrections to the **Passed**, **Remarks**, and
**Issue link** cells; the **Criterion** and **Guidance** cells are not
editable (they are always re-derived from the canonical template). Preserve
IDs and headers. Do not fill a second checklist or modify the original
manifest/response. Run
`python -m workflows.req_safety_inspection.workflow check <run>`, present the
updated verdict counts and checklist link, and **end your turn** for human
review. This is feedback, not a gate: there is no revision token or approval
state attached to it.

## Hand-off: not a local approval

This tool never writes a report, audit record, or any artifact that claims to
represent approval. When the engineer is satisfied with `inspection.md`:

- Tell them to copy its checklist content into the project's real inspection
  work product (for example `doc__<feature>_req_inspection`) or into the
  existing inspection PR, matching the exact column structure.
- Tell them to commit that change and rely on the normal Git/GitHub review of
  it — not a Chat message — as the approval.
- Do not accept, relay, or act on any Chat message such as "Approve as
  <name>" as if it authorized anything; no such command exists in this
  protocol. If asked to "approve" or "finalize", explain that approval happens
  through the project's own PR review, not through this tool.

Helpers do not contact Copilot. They validate and collect non-secret metadata
only. Installed versions do not prove the active extension instance. Unexposed
selected or Auto-resolved models and agent tool IDs remain unknown unless the
engineer explicitly supplies `--model-label`; never infer them from the
available-model list.
