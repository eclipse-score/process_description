# Copilot Chat Agent process execution demonstrator

All extension content is in this directory. Start with the
[concept](ai_sup_dev_proc_exe_in_safe_context_concept.md) and
[execution guide](execution.rst). The public reference list is in the concept.

- [ai_workflows.rst](ai_workflows.rst) describes draft inspection workflows.
- [ai_tool_management.rst](ai_tool_management.rst) uses the public S-CORE
  qualification-required/not-required decision and Tool Verification Report.
- The `workflows/` package implements preparation, automatic metadata,
  Markdown review, revision tracking, and named Chat confirmation. It never
  invokes Copilot or transmits input to an AI service.
- The `tests/` directory contains offline tests and the public baselibs example.

## Quick start

Attach [chat_workflow.prompt.md](chat_workflow.prompt.md) in Chat and ask:

```text
Inspect baselibs. Prepare the editable review and stop for my confirmation.
```

This pilot assesses feature and component requirements. Stakeholder requirements
remain part of the existing S-CORE requirements workflow and can be relevant as
parent context, but direct stakeholder assessment is not implemented because
the checklist profile differs. Assumptions of use are also unsupported. The
helper rejects those input types rather than applying the feature/component
checklist; parent text is not retrieved automatically.

Edit the linked `review.md` or request corrections. After direct edits, say
`Ready` to have the agent present the current revision. Confirm it in a later
message with `Approve as <your name>`, or reject with a reason. No manual
preparation, JSON import, version entry, or terminal finalization is needed.

Helpers need Python 3.11+ and Markdown. Use an existing suitable interpreter;
setup can use `pip install -e .` in this directory. Developer checks:

```bash
python -m unittest discover -s tests/req_inspection -v
python -m workflows.req_safety_inspection.workflow --help
```

Tests use constructed responses and do not transmit input. The reusable prompt
is explicitly attached or run from its editor button, not globally discovered.
It directs the agent to stop after every presented revision. Helpers collect
available metadata but cannot authenticate Chat authors or enforce turn
boundaries. Unknown request-level model data stays unknown. Existing manually
imported runs remain untouched; use a fresh run for the chat-first format.

From the repository root, build the publication pages with `bazel run //:docs`.
The root BUILD file mounts only the five publication pages; prompts, templates,
tests, fixtures, and ignored `out/` artifacts are not Sphinx document inputs.
Existing process directories stay in place.

## Publication boundary

This adapts the original concept and pilot structure rather than copying the
external repository wholesale. It uses public S-CORE requirements, checklist
criteria, and tool-management language, with original explanatory wording.
Non-public standards content, classification schemes, private compliance
records, credentials, personal reviewer data, and unsupported qualification
claims are excluded. The ISO 26262 reference is only a public catalogue link.
Normal contribution and redistribution review still applies.

All process nodes remain draft proposals. The report template is not already
approved. Neither offline tests nor human approval establishes inspection quality,
tool qualification, reviewer identity, or acceptance into the project safety case.
Instructions and hashes are not access controls or signed attestations; see the
concept and execution guide for the limits of the local guardrail.
