# AI-supported process execution

All extension content is in this directory. Start with the
[concept](docs/concept/ai_supported_development.md). The public reference
list is in the concept.

- [Technical workflows](docs/technical_workflows/index.rst) defines an additive
  execution-guidance layer, not new process workflow nodes:
  - [PR Review](docs/technical_workflows/pr_review.rst) combines parallel AI and
    independent human review, retaining human sign-off and approval.
  - [PR Authoring](docs/technical_workflows/pr_authoring.rst) describes bounded AI
    editing with author verification.
  - [Change Management Plan pilot](docs/technical_workflows/examples/platform_management_plan.rst)
    compares the published S-CORE plan with the current process and proposes
    corrections using both technical workflows. The upstream plan is not yet
    changed or approved.
- [Requirements inspection](docs/process_guidance/requirements_inspection.rst)
  describes draft inspection workflows,
  with the same roles as the existing `wf__monitor_verify_requirements`.
- [Tool management](docs/process_guidance/tool_management.rst) uses the public S-CORE
  qualification-required/not-required decision and Tool Verification Report
  directly, with no parallel tool-management workflows.
- The `workflows/` package implements preparation, automatic metadata,
  checklist validation, and re-check after edits. It never invokes Copilot,
  transmits input to an AI service, or approves anything locally.
- The `tests/` directory contains offline tests and the public baselibs example.

Technical workflow guidance needs no helper installation or new automation.
Existing process definitions, roles, and acceptance criteria remain unchanged.
For the separate executable requirements-inspection demonstration, use the
[execution guide](docs/demonstrator/execution.rst) and quick start below.

## Layout

- `docs/concept/`: AI-supported development concept.
- `docs/technical_workflows/`: reusable technical workflows and concrete examples.
- `docs/process_guidance/`: draft inspection and tool-management guidance.
- `docs/demonstrator/`: executable demonstration instructions.
- `docs/_assets/`: published diagrams.
- `workflows/`, `tests/`, `example/`: unchanged executable package and fixtures.

The documentation entry point is [docs/index.rst](docs/index.rst).

## Requirements inspection quick start

Attach [chat_workflow.prompt.md](chat_workflow.prompt.md) in Chat and ask:

```text
Inspect baselibs. Prepare the editable checklist and stop.
```

This pilot assesses feature and component requirements. Stakeholder requirements
remain part of the existing S-CORE requirements workflow and can be relevant as
parent context, but direct stakeholder assessment is not implemented because
the checklist profile differs. Assumptions of use are also unsupported. The
helper rejects those input types rather than applying the feature/component
checklist; parent text is only used when explicitly supplied via `--context`.

Edit the linked `inspection.md` or request corrections, then re-run
`python -m workflows.req_safety_inspection.workflow check <run>` for immediate
feedback. There is no local approval command: copy the checked checklist into
the project's real inspection document and rely on the normal Git/GitHub review
of that change as the only approval. No manual preparation, JSON import,
version entry, or terminal finalization is needed — and nothing here can
fabricate or stand in for that review.

Helpers need Python 3.11+ and Markdown. Use an existing suitable interpreter;
setup can use `pip install -e .` in this directory. Developer checks:

```bash
python -m unittest discover -s tests/req_inspection -v
python -m workflows.req_safety_inspection.workflow --help
```

Tests use constructed responses and do not transmit input. The reusable prompt
is explicitly attached or run from its editor button, not globally discovered.
It directs the agent to stop after every presented checklist. Helpers collect
available metadata but cannot authenticate Chat authors or enforce turn
boundaries. Unknown request-level model data stays unknown unless explicitly
supplied with `--model-label`.

From the repository root, build the publication pages with `bazel run //:docs`.
The root BUILD file discovers publication sources only under `docs/` and mounts
them at the existing `process_extensions` publication location. Keep runtime
prompts, templates, tests, fixtures, and ignored `out/` artifacts outside `docs/`
so they cannot become Sphinx document inputs. Existing process directories stay
in place; helper imports, commands, and output locations are unchanged.

## Publication boundary

This adapts the original concept and pilot structure rather than copying the
external repository wholesale. It uses public S-CORE requirements, checklist
criteria, and tool-management language, with original explanatory wording.
Non-public standards content, classification schemes, private compliance
records, credentials, personal reviewer data, and unsupported qualification
claims are excluded. The ISO 26262 reference is only a public catalogue link.
Normal contribution and redistribution review still applies.

All process nodes remain draft proposals. Neither offline tests nor the
project's own PR review establishes tool qualification by itself; reviewer
competence, tool acceptance, and the public S-CORE qualification decision
remain separate, governed by the existing tool-management process. See the
concept and execution guide for the limits of the local guardrail.
