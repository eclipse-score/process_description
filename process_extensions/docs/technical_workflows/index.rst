..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

..
   AI Disclosure: This draft was largely AI-generated and reviewed by the
   author before contribution; it remains subject to independent human review.
   The AI-generated portions are made available under CC0-1.0.
   SPDX-License-Identifier: Apache-2.0 AND CC0-1.0
   Assisted-by: GitHub Copilot (active model/version unavailable)

.. _technical_workflows:

Technical Workflows
===================

A process workflow defines what must be done and who is responsible.
A technical workflow explains how to do it with tools such as GitHub and an
AI-assisted editor. It does not add process requirements.

For example, :need:`wf__platform_cr_mt_platform_mgmt_plan` uses PR Authoring to
prepare a change and PR Review to check and approve it.

.. toctree::
   :maxdepth: 1

   pr_review
   pr_authoring
   examples/platform_management_plan

Rules for AI Assistance
-----------------------

The existing :need:`gd_guidl__ai_usage` applies:

* The author understands and takes responsibility for every submitted change.
* AI suggestions do not replace human review or reduce its scope.
* Only humans approve. AI agents and bots must not merge PRs or push directly
  to protected branches.
* Disclose AI assistance in commits, PR text, and comments as the guideline
  requires.

Share only information permitted for the selected AI service. Use existing
templates, checklists, and reviewed instructions; do not ask AI to invent
missing decisions or evidence.

AI use is optional. If it is unavailable or its review is incomplete, say so in
the PR and carry out the full human review. Keep decisions and review comments
in the existing PR, not only in a chat. No additional report is required here.

Existing Responsibilities Still Apply
-------------------------------------

Use the approving roles defined by the process workflow as well as the required
human committer approval. Having permission to merge does not by itself fulfill
the process's approval responsibility.

Ordinary PR review is not the formal inspection described by
:need:`doc_concept__wp_inspections`. Where that inspection is required, follow
its existing rules.

Tool evaluation remains part of :need:`wf__tool_evaluate_tool`. The
:doc:`concept <../concept/ai_supported_development>` and
:doc:`tool-management guidance <../process_guidance/tool_management>` explain
the AI-specific considerations.
