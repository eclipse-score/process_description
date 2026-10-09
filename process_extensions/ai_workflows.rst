.. _ai_workflows:

AI-Assisted Workflow Extensions
################################

These draft proposals describe optional AI-supported requirements inspection.
They are based on the proposed concept and public S-CORE process definitions.
They do not establish standards compliance,
tool qualification, or coverage of a particular safety level.

The Bazel documentation bundle publishes these draft nodes alongside the
existing process. Role assignments are proposed responsibilities, not recorded
approvals. The executable demonstration is described in :doc:`execution`.

The workflow augments ``wf__monitor_verify_requirements`` without replacing the
existing manual inspection. Proposed tool evaluation and monitoring are described
in :doc:`ai_tool_management`.


.. workflow:: AI-Assisted Safety Requirements Inspection
   :id: wf__ai_req_safety_inspect
   :status: draft
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__committer
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__requirements_feat[version==1], wp__requirements_comp[version==1]
   :output: wp__requirements_inspect[version==1]
   :contains: gd_chklst__req_inspection[version==1]

   An engineer selects feature or component requirements, context, and the
   applicable public S-CORE inspection checklist. Before sharing input with an
   AI service, the engineer verifies that sharing is permitted. Roles match
   :need:`wf__monitor_verify_requirements`, which this workflow augments: the
   committer remains responsible and approving, with the safety manager
   supporting as moderator, consistent with :need:`doc_concept__wp_inspections`.
   This also applies to re-inspection triggered by change or release review;
   no separate reusable sub-workflow is defined for that case.

   The AI fills the checklist content directly in the exact column structure of
   :need:`gd_chklst__req_inspection` (Review ID, Acceptance Criteria, Guidance,
   Passed, Remarks, Issue link), parsed from that template rather than
   paraphrased, without changing requirements or inventing checklist IDs. Each
   entry has a ``yes`` / ``no`` / ``n/a`` / ``not_assessed`` verdict (missing
   context is never silently treated as ``n/a``) and full remarks; an issue
   link is mandatory for every ``no``. The result is presented as one editable
   table; the original judgment remains preserved separately.

   **Scope:** The existing ``wf__monitor_verify_requirements`` includes
   ``wp__requirements_stkh``, ``wp__requirements_feat``, and
   ``wp__requirements_comp``. This AI variant assesses feature and component
   requirements only. Stakeholder requirements may be relevant parent context,
   but their distinct checklist profile is not implemented and their text is
   not retrieved automatically unless the engineer explicitly supplies it as
   context, in which case linkage/completeness items may be assessed instead
   of marked ``not_assessed``.

   **Proposed review guardrail:** After presenting a validated draft, the agent
   ends its turn. The reviewer independently checks the assessment, evidence
   gaps, parent traceability, and consistency, and may edit the checklist or
   request corrections; the agent validates and presents every changed
   revision, then stops again. There is no local chat-confirmation command:
   the engineer copies the checked checklist into the project's real
   inspection document (for example ``doc__<feature>_req_inspection``), commits
   it, and the normal Git/GitHub review of that change is the only approval
   this workflow recognizes. Editing, ``Ready``, positive feedback, and tool
   permissions are not that approval.

   **Proposed constraints:**

   - Validation rejects entries outside the feature/component checklist profile,
     unknown checklist IDs, or checklist text diverging from
     :need:`gd_chklst__req_inspection`.
   - The reviewer checks the AI assessment independently against the requirements
     and applicable checklist as part of the normal PR review; there is no
     separate local confirmation step to substitute for that review.
   - Drafts are distinguished from accepted evidence: nothing is written to the
     project's inspection document until the engineer does so themselves.
   - Human approval alone does not establish tool qualification. Tool evaluation
     under the existing tool-management workflows (see :doc:`ai_tool_management`)
     must be assessed for the intended use before adoption.
   - Model, prompt, configuration, or usage changes trigger impact evaluation.
