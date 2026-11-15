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
   AI Disclosure: This draft was largely AI-generated and awaits human review.
   The AI-generated portions are made available under CC0-1.0.
   SPDX-License-Identifier: Apache-2.0 AND CC0-1.0
   Assisted-by: GitHub Copilot (active model/version unavailable)

.. _technical_workflow_pr_authoring:

Technical Workflow: Pull Request Authoring
==========================================

Prepare a change for human review, with optional help from an AI editor.
The :doc:`shared rules <index>` apply.

Before You Start
----------------

Have the issue or change request, the documents to change, and the applicable
templates and guidance ready. Know what change is wanted and which facts or
decisions support it. Ask the responsible person about missing decisions.

Steps
-----

#. **Prepare the PR.** Create a branch. Open a draft PR if useful and link the
   issue or change request. Describe what you intend to change.
#. **Edit.** Make the changes yourself or ask AI to propose edits to the named
   files. Give it the relevant source material and existing templates. Ask it
   to flag missing information rather than guess.
#. **Check the changes yourself.** Read the complete diff. Check the facts,
   links, and consistency with related documents. Correct or reject unsuitable
   AI suggestions. You remain responsible for the submitted content.
#. **Run the checks.** Use the checks required by the repository. For
   documentation in this repository, run ``bazel run //:docs`` and inspect the
   generated pages. Fix failures before requesting approval.
#. **Request review.** Commit the changes, explain them in the PR, and include
   the required AI disclosure. Request human review and, if used, AI review
   through :doc:`pr_review`.

The result is a PR ready for review, not an approved change. If reviewers
request corrections, repeat the relevant editing and checking steps, then
request another review.
