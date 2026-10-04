.. _ai_workflows:

AI-Assisted Workflow Extensions
################################

These draft proposals describe optional AI-supported requirements inspection.
They are adapted from the external pilot using the publication-oriented concept
and public S-CORE process definitions. They do not establish standards compliance,
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
   :responsible: rl__safety_manager
   :approved_by: rl__committer
   :supported_by: rl__contributor
   :input: wp__requirements_feat, wp__requirements_comp
   :output: wp__requirements_inspect
   :contains: gd_chklst__req_inspection

   An engineer selects feature or component requirements, context, and the
   applicable public S-CORE inspection checklist. Before sharing input with an
   AI service, the engineer verifies that sharing is permitted.

   The AI prepares draft assessments without changing requirements or inventing
   checklist IDs. Each entry contains a ``yes`` / ``no`` / ``n/a`` verdict and
   rationale. Findings contain a severity and suggested improvement. The result
   is presented as one editable Markdown review; the original judgment remains
   preserved separately.

   **Scope:** The existing ``wf__monitor_verify_requirements`` includes
   ``wp__requirements_stkh``, ``wp__requirements_feat``, and
   ``wp__requirements_comp``. This AI variant assesses feature and component
   requirements only. Stakeholder requirements may be relevant parent context,
   but their distinct checklist profile is not implemented and their text is
   not retrieved automatically. Assumptions of use are also out of scope.

   **Proposed review guardrail:** After presenting a validated draft, the agent
   ends its turn. The reviewer independently checks the assessment, evidence
   gaps, parent traceability, and consistency, and may edit the review or request
   corrections. The agent validates and presents every changed revision, then
   stops again. Only a later named Chat confirmation referring to the presented
   revision authorizes finalization. Editing, ``Ready``, positive feedback, and
   tool permissions are not approval.

   The final record retains original and reviewed results, declared approver,
   relayed confirmation message, revision/hash, timestamps, changes, and
   available tool metadata. Unexposed active-extension or model information
   remains unknown. Local controls do not authenticate the Chat author or prove
   a separate turn; prompt instructions are not security controls.

   **Proposed constraints:**

   - The project reviews and approves the demonstration report structure before
     adoption; it is not an approved S-CORE template.
   - Validation rejects entries outside the feature/component checklist profile.
   - The reviewer checks the AI assessment independently against the requirements
     and applicable checklist.
   - Drafts are distinguished from accepted evidence.
   - Human approval alone does not establish tool qualification. Tool evaluation
     and review controls must be assessed for the intended use before adoption.
   - Model, prompt, configuration, or usage changes trigger impact evaluation.


.. workflow:: AI-Assisted Requirements Inspection (reusable sub-workflow)
  :id: wf__ai_req_inspect_sub
  :status: draft
  :version: 1
  :responsible: rl__safety_manager
  :approved_by: rl__committer
  :input: wp__requirements_feat, wp__requirements_comp
  :output: wp__requirements_inspect
  :contains: gd_chklst__req_inspection

  Reusable proposal for activities that trigger feature or component
  requirements re-inspection, such as change review or release review. The
  calling activity supplies requirements, feature context, intended safety
  level, and inspection scope. Stakeholder requirements and assumptions of use
  are outside this checklist profile.

  The same draft, independent human review, revision presentation, and separate
  named Chat confirmation as ``wf__ai_req_safety_inspect`` apply. Calling this
  activity must not bypass the review pause or confirm a revision that was not
  presented to the user.
