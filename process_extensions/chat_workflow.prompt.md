---
name: score-requirements-review
description: "Start requirements inspection in Chat, pause for editable review, and finalize only after separate named user confirmation."
agent: agent
argument-hint: "Inspect baselibs, inspect a named requirements file, revise, approve, or reject"
---

# Chat-first requirements inspection

Use this protocol for the entire inspection conversation. Keep all artifacts
under `process_extensions/out/`. Do not change process definitions or existing
runs. User confirmation is declared approval, not authenticated safety sign-off.

## Start and judgment

1. For "Inspect baselibs", use the bundled public baselibs feature-requirement
   fixture and ASIL_B input context. For other inputs, accept feature or
   component requirements only. If stakeholder requirements, assumptions of
   use, or mixed-level directives are supplied, explain that their checklist
   profiles are unsupported and ask for feature/component input. Stakeholder
   requirements remain part of the existing S-CORE workflow and may be parent
   context, but are not automatically fetched or assessed. Ask for missing
   file/scope/context and sharing permission. Do not inspect unrelated material.
2. Select a Python 3.11+ interpreter with Markdown available. Prefer the existing
   workspace `.venv/bin/python` when available. Ask before installing missing
   dependencies; do not silently install packages.
3. Run the local helper from `process_extensions/`:
   `python -m workflows.req_safety_inspection.workflow start baselibs`.
   For another file use `start <file> --feature-name <name> --asil <level>`.
   Retain the generated run name. Available environment metadata is collected
   automatically. Never invent model/version values or read credentials, chat
   logs, authentication settings, or another repository.
4. Read the generated prompt and assess only its supplied requirements,
   checklist, and schema. Write complete JSON to that run's `response.json`.
   The prepared prompt governs judgment; this protocol separately authorizes
   the named local helpers and artifact writes. No web retrieval or additional
   model invocation is authorized.
5. Run `python -m workflows.req_safety_inspection.workflow draft <run>`.
   Repair invalid assessment structure or ask for missing context if needed.
   Never convert missing evidence into an invented pass.
6. Present the review.md link, run name, revision number/token, finding count,
   and material metadata limitations. Ask the user to review, edit, or request
   corrections. They can reply `Ready` after edits or `Approve as <name>` for
   the unchanged presented revision.
7. **STOP AND END YOUR TURN.** Do not approve, auto-confirm, or finalize in the
   judgment turn. A start request is not approval.

## Edits and revisions

The user may edit `review.md` or request specific corrections in Chat. Apply
only requested corrections to its tables; preserve IDs and headers. Do not
fill a second checklist or modify the original manifest/response.
Run `python -m workflows.req_safety_inspection.workflow stage <run>`, present
the updated revision and review link, and **end your turn** for human review.
`Ready`, positive feedback, file editing, and tool permissions are not approval.

## Separate confirmation or rejection

- Accept only a later explicit user message `Approve as <name>` or
  `Approve this revision as <name>` for the revision already presented.
  Ask before proceeding if the run or identity is ambiguous.
- Run `python -m workflows.req_safety_inspection.workflow confirm <run>
  --revision <previously-presented-token> --message <verbatim-user-message>`.
  Quote arguments for the local terminal. Do not fabricate a confirmation,
  default an approver, or approve on the user's behalf. Do not stage a changed
  artifact and confirm it in the same turn using an earlier approval.
- If the artifact changed, stage and present the new revision, then **stop for
  a new user confirmation**.
- On success link `report.rst` and `audit.json`. Do not claim qualification,
  authenticated identity, or automatic acceptance into a safety case.
- For user rejection, run `python -m workflows.req_safety_inspection.workflow
  reject <run> --reason <user-reason>` and stop without final output.

Helpers do not contact Copilot. They validate, collect non-secret metadata,
snapshot revisions, and render local reports. Installed versions do not prove
the active extension instance. Unexposed selected or Auto-resolved models and
agent tool IDs remain unknown; never infer them from the available-model list.
