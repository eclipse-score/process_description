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

Release Note v2.1.0
===================

.. document:: Process description Release Note v2.1.0
   :id: doc__process_description_release_note_v210
   :status: valid
   :safety: ASIL_B
   :version: 1
   :security: YES
   :realizes: wp__module_sw_release_note
   :tags:

| **Module Name:** Process description
| **Release Tag:** v2.1.0
| **Origin Release Tag:** v2.0.1...v2.0.3
| **Release Date:** 2026-09-02

Overview
^^^^^^^^

The module process_description provides a process model establishing organization rules
for developing open source software in the automotive industry, which can be used in
safety and security context.

The process model provides processes, which conform to state-of the art standards

ASPICE 4.0
ISO 26262
ISO 21434
ISO PAS 8926

Disclaimer
----------

This release note does not "release for production", as it does not come with a safety
argumentation and a performed safety assessment.
The work products compiled in the safety package are created with care according to a
process satisfying standards, but the project, being a non-profit and open source
organization, can not take over any liability for its content.

Changes to the Module
^^^^^^^^^^^^^^^^^^^^^

New Features
------------

Update of change management to consider new FEP proposal.

Add framework for trainings and an example training.

Maturity Level 3 is achieved for:
Documentation Management
Quality Management
Safety Analysis

The process model contains

- General concepts e.g. for Building Blocks and their traceability
- Process meta model for proper modeling
- Process areas covering the required standards
- Roles, Work Products, Workflows defining the process areas
- Standard overview and coverage information
- Folder templates for simplifying deployment for users
- Glossary
- Release Notes

Improvements
------------

- chore(docs): align score_docs_as_code repository files by @AlexanderLanin in https://github.com/eclipse-score/process_description/pull/762
- refactor decision record template, move to folder templates by @masc2023 in https://github.com/eclipse-score/process_description/pull/734
- Remove Covered attribute from req process by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/739
- Fix: Add versions where missing by @MaximilianSoerenPollak in https://github.com/eclipse-score/process_description/pull/740
- Bug: Link to static code analysis by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/741
- upgrade doc-as-code to version 4.6.1 by @masc2023 in https://github.com/eclipse-score/process_description/pull/743
- Correct Requirement check: suspicious by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/746
- DR Template: add new attributes by @masc2023 in https://github.com/eclipse-score/process_description/pull/745
- update of change management to consider new FEP proposal by @masc2023 in https://github.com/eclipse-score/process_description/pull/748
- Add framework for trainings and an example training by @masc2023 in https://github.com/eclipse-score/process_description/pull/742
- Update dependency score_docs_as_code to v5 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/750
- Change responsibles for Feature docs approval by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/752
- improve implementation by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/751
- link is optional for log_arc_int by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/753
- Update dependency score_docs_as_code to v6 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/755
- build: bump Bazel version to 8.7.0 by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/756
- switch link direction between feat and log_arc_int by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/754
- fix build error for training files by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/758
- update most needextend directives to affect only the current file by @AlexanderLanin in https://github.com/eclipse-score/process_description/pull/759
- remove operations from examples by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/760
- remove superflued optional linking of logic_arc_int_op by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/761
- Update dependency score_docs_as_code to v7 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/763
- Update Documentation Mgt to ML3 by @PandaeDo in https://github.com/eclipse-score/process_description/pull/765
- Update Quality Mgt ML2->3 by @PandaeDo in https://github.com/eclipse-score/process_description/pull/767
- Rename _platform_templates to platform_management_templates by @anmittag in https://github.com/eclipse-score/process_description/pull/768
- fix urls after structure changes in other repos by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/769
- fix: Fix needextend for future needextend changes by @MaximilianSoerenPollak in https://github.com/eclipse-score/process_description/pull/770
- Update dependency score_docs_as_code to v7.0.1 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/764
- fix: migrate needs role template to Jinja by @AlexanderLanin in https://github.com/eclipse-score/process_description/pull/771
- Update dependency score_docs_as_code to v7.1.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/772
- fix: Add git_override for docs-as-code by @MaximilianSoerenPollak in https://github.com/eclipse-score/process_description/pull/774
- Updated RequirementsInspection Template by @anmittag in https://github.com/eclipse-score/process_description/pull/775
- Allow multiple test derivation techniques by @attifunel in https://github.com/eclipse-score/process_description/pull/714
- fix naming of bazel module by @masc2023 in https://github.com/eclipse-score/process_description/pull/776

Bug Fixes
---------

not applicable

Other changes by Label
----------------------

not applicable

Compatibility
^^^^^^^^^^^^^

Doc-as-code, module_template

For a detailed list checkout here: https://github.com/eclipse-score/process_description/blob/main/MODULE.bazel

Performed Verification
^^^^^^^^^^^^^^^^^^^^^^

Initial Safety Audit by external assessor teams for every process area.

Known Issues
------------

- Issue 1: Standard requirements and work products are not yet fully mapped to the process model, https://eclipse-score.github.io/process_description//main/standards/index.html
- Issue 2: Safety package containing external Audit report not available, due to open improvement proposals/recommendation from external assessor team, #652
- Issue 3: Maturity level 2 no yet completed for security processes, but deploying is still ongoing also auditing per external auditor to achieve higher maturity levels, #652, https://github.com/eclipse-score/score/issues/2911

Known Vulnerabilities
---------------------

None

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

As Building Blocks Meta Model is adapted and Templates are removed, consider to use the compatible doc-as-code version and the module templates from the module_template repository.
Updated with the latest doc-as-code version.

Contact Information
For any questions or support, please contact the SW Process Development Community (https://github.com/orgs/eclipse-score/discussions/108) or raise an issue/discussion.
