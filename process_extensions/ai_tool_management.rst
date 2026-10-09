.. _ai_tool_management:

AI Tool Management
##################

This draft extension proposes evaluation and monitoring of offline AI
development-support tools. It uses original explanatory wording based on the
proposed concept and public S-CORE process definitions.

These nodes are published as drafts through the Bazel documentation bundle.
Role assignments are proposals, not recorded approvals. Nothing here
demonstrates completed qualification or coverage of a particular safety level.

The public `S-CORE Tool Management Plan
<https://eclipse-score.github.io/score/main/platform_management_plan/tool_management.html>`_
defines the evaluation decision: qualification is required when tool impact
is YES and tool error detection is NO; otherwise qualification is not required.
The presence of a human reviewer must not automatically establish error detection.
Tool acceptance is separate from an individual inspection report's approval.

This proposal separates two kinds of tool-confidence subjects. The local
deterministic helpers (requirements parser, JSON schema validator, Markdown
renderer) perform a fixed, independently testable conversion and are evaluated
like any other development tool. The LLM performing the draft assessment is
treated as categorically not qualifiable: its output never earns qualification
credit and remains subject to the full human review guardrail regardless of
model evaluation results.

This proposal does **not** define a separate AI tool-management workflow. The
AI development-support tool goes through the existing
:need:`wf__tool_evaluate_tool`, :need:`wf__tool_qualify_tool`, and
:need:`wf__tool_approve_tool_verification_report` with their existing roles
and approvals unchanged. The guidance below only supplements the existing
``wp__tool_verification_report`` content for this specific kind of tool; it
is additive guidance, not a parallel process or a second set of roles for the
same work product.

The proposed requirements inspection activity is described in
:doc:`ai_workflows`.


Evaluation Guidance
-------------------

.. gd_temp:: AI Development Tool Evaluation Record Template
   :id: gd_temp__ai_tool_evaluation_record
   :status: draft
   :version: 1
   :tags: tool_management

   Proposed guidance for recording a tool's intended use in the existing
   ``wp__tool_verification_report``, used during :need:`wf__tool_evaluate_tool`
   and :need:`wf__tool_qualify_tool`. It supplements the public S-CORE Tool
   Verification Report Template; it is not a completed evidence record.

   The project documents the tool, model selection and available version information, affected work
   products, permitted input data, intended scope, known limitations, and
   reviewer responsibilities. It records tool impact and error detection,
   the resulting qualification-required/not-required decision, chosen controls,
   evaluation cases and results, unresolved issues, and authorization for use.
   Helpers detect editor and installed-extension metadata, interpreter/parser
   versions, and workflow hashes. Installation metadata is not proof of the
   active Chat extension or model. Unexposed request metadata stays unknown.

   Review competence, report ownership, model-change handling, and audit
   retention are defined by the project. This proposal is not a completed
   evidence record and contains no private evaluation results or reviewer data.

   Evaluation should explicitly cover, in addition to the existing tool
   evaluation criteria:

   1. Impact and error detection under the public S-CORE plan, with the
      detection/prevention claim justified rather than assumed from the mere
      presence of a reviewer.
   2. Error modes specific to this kind of tool: an invented pass, a false
      ``n/a``/``not_assessed``, an omitted checklist item, a rationale that
      contradicts its verdict, and prompt injection through requirement text.
   3. The schema validation and hand-off boundary itself (rejection of
      malformed structure, mandatory issue links, parent-context enforcement)
      as a control, not as a substitute for independent human review.
   4. Model, prompt, configuration, or usage changes, each triggering a new
      impact assessment of which evaluation cases must be repeated; results
      are compared against the previously approved baseline.
   5. Whether accepted inspection records show an identifiable model/tool
      version, an independent reviewer distinct from the requirements author,
      and per-item review evidence consistent with the authorized scope.

   A failed or incomplete evaluation must not be treated as approval, and
   project-approved acceptance criteria apply before adoption, exactly as for
   any other tool reaching :need:`wf__tool_approve_tool_verification_report`.
