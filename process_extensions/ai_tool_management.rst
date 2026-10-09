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
like any other development tool under ``wf__ai_tool_qualify`` below. The LLM
performing the draft assessment is treated as categorically not qualifiable
by this evaluation: its output never earns qualification credit and remains
subject to the full human review and approval guardrail regardless of model
evaluation results.

The proposed requirements inspection activity is described in
:doc:`ai_workflows`.


Evaluation Guidance
-------------------

.. gd_temp:: AI Development Tool Evaluation Record Template
   :id: gd_temp__ai_tool_evaluation_record
   :status: draft
   :version: 1

   Proposed guidance for recording a tool's intended use in the existing
   ``wp__tool_verification_report``. It supplements the public S-CORE Tool
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


Workflows
---------

.. workflow:: Evaluate AI Development Tool Before Use
   :id: wf__ai_tool_qualify
   :status: draft
   :version: 1
   :responsible: rl__safety_manager
   :approved_by: rl__project_lead
   :supported_by: rl__contributor
   :input: wp__tlm_plan
   :output: wp__tool_verification_report
   :contains: gd_temp__ai_tool_evaluation_record

   Proposed initial evaluation before adoption:

   1. Agree the intended use, permitted input data, report structure, and
      reviewer responsibilities within the existing tool-management process.
   2. Identify possible incorrect or missing assessments and how the review
      and validation controls should detect them.
   3. Evaluate impact and error detection under the public S-CORE plan and record
      whether qualification is required. Justify the detection/prevention claim.
   4. If qualification is required, apply the existing software-tool validation
      process. Define representative cases with independently reviewed expected results
      and project-approved acceptance criteria before evaluating the tool.
   5. Evaluate draft generation, structure validation, and the approval boundary,
      including rejection, missing named Chat confirmation, changed revisions,
      and the risk of an agent fabricating a relayed confirmation message.
   6. Record results, limitations, and unresolved issues in the evaluation record.
   7. Obtain the required project approval before use. If the evidence is
      insufficient, do not authorize adoption.

   This activity supports the existing tool-management process; it does not
   replace that process or decide qualification from human review alone.


.. workflow:: Re-evaluate AI Tool on Model Change
   :id: wf__ai_tool_requalify
   :status: draft
   :version: 1
   :responsible: rl__safety_manager
   :approved_by: rl__project_lead
   :input: wp__tool_verification_report
   :output: wp__tool_verification_report
   :contains: gd_temp__ai_tool_evaluation_record

   Record the proposed model selection and available version information, then re-run the agreed evaluation cases
   before using a changed model. Compare results with the approved baseline,
   investigate regressions, and update the evidence record and limitations.
   Changes to prompts, report structure, or usage scope also require an impact
   assessment to determine which evaluation cases must be repeated.

   The project applies its approved acceptance criteria and records an explicit
   approval decision before adoption. A failed evaluation must not be treated
   as approval. No universal numerical pass threshold is specified here.


.. workflow:: Monitor AI Tool Usage and Review Controls
   :id: wf__ai_tool_monitor
   :status: draft
   :version: 1
   :responsible: rl__safety_manager
   :approved_by: rl__project_lead
   :input: wp__requirements_inspect, wp__tool_verification_report
   :output: wp__tool_verification_report
   :contains: gd_temp__ai_tool_evaluation_record

   Periodically review whether accepted records contain the expected model,
   timestamp, reviewer, approval decision, and correction metadata. Check that
   reviewers meet project-defined competency expectations and detected tool
   configurations match the authorized scope. Unknown active-model and extension
   versions remain limitations; do not infer them from installed inventories.

   Investigate missing approvals, unexpected model changes, and recurring
   corrections or missed findings. Record issues and determine whether usage
   must be restricted or suspended pending renewed evaluation and approval.
   Audit metadata is evidence for review, not proof that the controls are
   implemented correctly or that every error has been detected.
