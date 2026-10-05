# AI-supported development process execution in a safety context

> **Context:** This document accompanies the discussion in
> [eclipse-score/process_description #805](https://github.com/eclipse-score/process_description/issues/805)
> — *"Pilot for AI supported development process execution in safe context"*.
> It describes a proposed concept and a pilot implementation.

---

## 1. The problem

The [S-CORE process description](https://eclipse-score.github.io/process_description/main/)
defines structured workflows, templates, and checklists to produce verifiable
safety evidence. Requirements inspection applies a level-appropriate checklist
to stakeholder, feature, and component requirements before they are accepted as
safety evidence. The checklist profile is not identical at every level.

Filling that checklist is **manual, time-consuming, and repetitive** — the
same quality questions apply to every requirement. Meanwhile, Large Language
Models (LLMs) are now capable of performing exactly this kind of structured
text assessment. The question is now
**under what conditions their output can legitimately enter a safety case**.

**The goal is development support**: AI assists an engineer during development.

So AI is only considered here as a **development support tool** —
it shall never generate safety evidence autonomously.

The safety premise is therefore:

> *If every AI-generated output is treated as a draft that a qualified engineer
> must explicitly review and approve before it becomes part of the safety case,
> then errors introduced by the AI can be detected and corrected before they
> cause any harm.*

This is not a novel concept. [ISO 26262 Part 8, Clause 11](https://www.iso.org/standard/68388.html)
establishes the principle of **tool confidence**: when a development tool
affects a safety-relevant work product, the confidence in that tool (and the
controls around it) must be demonstrated.

---

## 2. Concept: AI as a qualified development support tool

Based on ISO 26262 Part 8 tool confidence principles, the approach in this
pilot rests on three pillars:

### 2.1 The human review guardrail

The chat-first demonstration follows this sequence:

```
1. Engineer starts the inspection in Copilot Chat
      │
      ▼
2. Agent prepares permitted input and a structured draft assessment
      │
      ▼
3. Validated editable review file is presented
   Agent stops; engineer may edit or request corrections
      │
      ▼
4. A later explicit named Chat confirmation applies to that revision
   Rejection produces no approved report
    │
    ▼
5. Agent writes final report and audit record for the confirmed revision
```

This means the AI output is never in the safety case — only the
**human-reviewed and approved** version is.

### 2.2 Fixed output schema (no invented structure)

The AI fills a fixed demonstration schema:

- Verdict per checklist item: `yes` / `no` / `n/a`
- One-sentence rationale per item
- List of flagged findings with severity and suggested improvement

The AI cannot add new sections, invent checklist IDs, or change the document
structure. Schema validation rejects any response that does not conform. The
demonstration report template is not a pre-approved S-CORE work-product template.

### 2.3 Model provenance and evaluation trigger

Available tool and model information is recorded with its source. Unavailable
active model details remain unknown. A change to model, prompt, configuration,
or intended use triggers evaluation of its impact on existing tool evidence.

Every AI assessment is a draft. A competent human independently reviews all
checklist entries, corrects errors, and explicitly approves the reviewed
artifact. This control can support error detection; it does not prove that all
errors are detected, that the reviewer is competent, or that the tool is qualified.

Tool qualification may also be required, based on the S-CORE tool evaluation
described in the [Tool Management process](https://eclipse-score.github.io/process_description/main/process_areas/tool_management/index.html),
if independent human review is not sufficient to establish error detection.

---

## 3. The executable concept

### 3.1 What the pilot implements

An automated workflow that pre-fills the feature/component S-CORE requirements
inspection checklist for each supported requirement in scope. The
[S-CORE process description](https://eclipse-score.github.io/process_description/main/requirements_engineering/index.html)
defines inspection for stakeholder, feature, and component requirement levels;
each level has applicable, potentially different inspection guidance.

The AI inspects each requirement against the quality criteria defined in the
S-CORE checklist — the same criteria a human reviewer would apply — and
provides a structured first-pass assessment with a verdict and rationale for
each criterion.

The pilot demonstrates an optional Copilot Chat Agent workflow for feature and
component requirements only. Stakeholder requirements remain part of the
existing S-CORE process and may be relevant as parent context, but are not
directly assessed by this demonstrator. Their dedicated checklist profile is
not implemented. Assumptions of use are also out of scope.

The Chat Agent workflow is:

```text
Engineer starts the inspection directly in Chat
  -> agent prepares input and automatically collects tool metadata
    -> Copilot Chat Agent produces a JSON assessment
    -> deterministic validation rejects wrong IDs or structure
    -> editable review file is written and the agent stops
    -> engineer edits or requests corrections; new revisions are presented
    -> engineer confirms a previously presented revision in a later Chat message
    -> agent writes report and audit with approver and detected tool information
```

### 3.2 Fixed structure

Assessments contain one entry per input requirement, the exact public S-CORE
checklist IDs, `yes` / `no` / `n/a` verdicts, full rationales, and structured
findings. Unknown IDs, duplicate JSON keys, additional fields, invalid verdicts,
or missing requirements are rejected. The report template is a proposed
demonstration template, not a pre-approved S-CORE work-product template.

There is one editable set of verdicts, rationales, and findings in
[`example/review.md`](https://github.com/eclipse-score/process_description/blob/main/process_extensions/example/review.md),
not a duplicate checklist. The original judgment remains preserved separately.
Missing context must be resolved or dispositioned by the reviewer; `n/a` must
not silently mean that evidence has been verified.

### 3.3 Human finalization

After judgment the agent presents the editable review and ends its turn.
The engineer edits the tables in the [`example/review.md`](https://github.com/eclipse-score/process_description/blob/main/process_extensions/example/review.md)
or requests corrections in Chat.
Changed artifacts are validated and shown as new revisions. A later explicit message
`Approve as <name>` confirms the presented revision, or the engineer rejects it.
Only then does the agent run local finalization; no engineer terminal step is needed.
File edits after presentation invalidate confirmation and require a new revision.

The report records original/reviewed judgments, declared approver, relayed
confirmation, timestamps, changes, revision snapshots/hashes, and detected
provenance. Rejected runs produce no approved report. Existing runs are preserved
and final artifacts cannot be overwritten.

### Copilot provenance

Helpers automatically collect tool versions, workflow version and
code hashes, available editor metadata, and installed Copilot Chat versions.
Every value has a source; no manual model/version arguments are required for
the chat-first path. Finalization records its executing environment as well.

## 4. Requirements inspection demonstration

The included example used is a snapshot of four publicly available S-CORE baselibs
feature requirements. For example, the Utils Library requirement lists Base64,
scoped operations, string views, safe arithmetic, atomic operations, and
termination handling. This input demonstrates parsing and review flow; it is
not a set of independently validated expected verdicts.

The prompt summarizes the public S-CORE inspection checklist. It requests
structured draft assessments. Reviewers must
consider parent requirements, traceability, timing, interfaces, safety/security
attributes, verifiability, completeness, and justified exceptions.

Start in Chat using the reusable workflow prompt. The agent prepares input,
validates its JSON judgment, presents the review file, and stops. A later
named confirmation authorizes finalization of the presented artifact. Check
permission to share input before starting. Local helpers collect metadata,
validate, track revisions, and render reports; they never invoke Copilot or
transmit data. Existing manually imported runs remain unchanged.

The execution guide gives the Chat requests. Offline tests use constructed
responses, without invoking Copilot. No live Copilot result or timing measurement
is claimed by those tests. The historical pilot's assessments are not reported
as results from this implementation.

## 5. Additive S-CORE integration

All extension content is under `process_extensions/`. Existing process
directories and workflows remain in place. An additive Bazel bundle mount
publishes the concept, execution guide, and draft workflow definitions alongside
the existing process using `bazel run //:docs`.

The existing `wf__monitor_verify_requirements` accepts stakeholder, feature, and
component requirements, including `wp__requirements_stkh`. The optional
`wf__ai_req_safety_inspect` proposal augments it for feature/component
assessments only; it references `wp__requirements_feat`,
`wp__requirements_comp`, and `wp__requirements_inspect`. Stakeholder requirements
remain upstream context in the existing workflow, not direct input to this AI
profile. The S-CORE stakeholder checklist differs and is not implemented here.
Published nodes remain draft proposals, not approved process changes. Runtime
templates, inputs, tests, and generated outputs are not published as process
definitions.

## 6. Limitations

- The RST reader accepts simple feature/component requirement directives only.
  It rejects stakeholder/AOU and mixed-level files rather than applying the
  wrong checklist, and does not implement general Sphinx-Needs parsing.
- Parent IDs may be supplied, but parent text (including stakeholder
  requirements), implementation evidence, test traces, and related requirements
  are not automatically retrieved.
- Copilot outputs are non-deterministic and require strict validation and human
  review. No ASIL coverage or completed qualification is claimed.
- Installed versions are not active-session metadata; selected or Auto-resolved
  model information remains unavailable without a supported editor integration.
- The guardrail does not establish reviewer identity or prevent a privileged
  agent from bypassing the local scripts.
- Published RST nodes express intended responsibilities; executable review
  controls do not replace project governance.

## 7. Public references

| Reference | URL |
|---|---|
| S-CORE project | https://eclipse-score.github.io/score/main/ |
| S-CORE process description | https://eclipse-score.github.io/process_description/main/ |
| Requirements Engineering | https://eclipse-score.github.io/process_description/main/process_areas/requirements_engineering/index.html |
| Feature inspection checklist | https://eclipse-score.github.io/process_description/main/folder_templates/platform/features/feature_name/requirements/req_inspection.html |
| Public baselibs requirements | https://eclipse-score.github.io/score/main/features/baselibs/requirements/index.html |
| Tool Management process | https://eclipse-score.github.io/process_description/main/process_areas/tool_management/index.html |
| Tool Management Plan | https://eclipse-score.github.io/score/main/platform_management_plan/tool_management.html |
| GitHub issue #805 | https://github.com/eclipse-score/process_description/issues/805 |
| ISO 26262 public catalogue entry | https://www.iso.org/standard/68388.html |
| Copilot in VS Code documentation | https://code.visualstudio.com/docs/copilot/overview |
