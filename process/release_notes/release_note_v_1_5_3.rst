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

Release Note v1.5.3
===================

.. document:: Process description Release Note v1.5.3
   :id: doc__process_description_release_note_v152
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__module_sw_release_note
   :tags:

| **Module Name:** Process description
| **Release Tag:** v1.5.3
| **Origin Release Tag:** v1.4.4
| **Release Date:** 2026-04-13


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

Process model gives compliance with ISO 26262, ISO 21434, ISOPAS 8926 and ASPICE 4.0
(https://eclipse-score.github.io/process_description/main/index.html).

- Initial Security Analysis Process
- Project Lead Role replaces Technical Project Lead Role (removed)

The process model contains

- General concepts e.g. for Building Blocks and their traceability
- Process meta model for proper modeling
- Process areas covering the required standards
- Roles, Work Products, Workflows defining the process areas
- Standard overview and coverage information
- Folder templates for simplifying deployment for users

Improvements
------------

- Platform sec analysis first draft - part 1 without templates by @NarasipurRohini in #596
- Improved sentence clarity, readability, and flow across sections by @Chidananda-Swamy in #600
- Update needs_role_need_template to use {title} so :need: links render titles without IDs by @Chidananda-Swamy in #601
- update gps level 2 and level 3 by @masc2023 in #602
- Improve Release Notes Templates According to Usage by @aschemmel-tech in #604
- Improve req inspect templates by @aschemmel-tech in #605
- Refine the security analysis guidelines for better readability by @Chidananda-Swamy in #606
- Add process requirements for AoU linking by @aschemmel-tech in #599
- correct process requirements to current meta model by @RolandJentschETAS in #610
- Update acc. to release mgt. plan by @PandaeDo in #611
- Clarify security mitigation requirements by @Chidananda-Swamy in #613
- chore(ci): pin cicd-workflows reusable workflows to commit SHA by @AlexanderLanin in #607
- add example for meta model deployment by @masc2023 in #614
- preparation for independend modules by @RolandJentschETAS in #615

Bug Fixes
---------

None

Other changes by Label
----------------------

- Add version back to Docs-as-code by @MaximilianSoerenPollak in #616
- Safety management process for changes by @aschemmel-tech in #620
- Fix API access by @a-zw in #622
- AoU creation based on Safety Analysis by @aschemmel-tech in #623
- Add functional testing to interface tests by @pahmann in #626
- Remove issue templates by @masc2023 in #619
- add tool requirements from feat/comp to tool man process by @RolandJentschETAS in #630
- Update to latest docs_as_code 4.0.0 by @a-zw in #653
- Enhance one tailored verification clause by @pahmann in #655

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
- Issue 2: Safety package containing external Audit report not available, due to open improvement proposals/recommendation from external assessor team, #77
- Issue 3: Maturity level 1 achieved, but deploying is still ongoing also auditing per external auditor to achieve higher maturity levels, #77, https://eclipse-score.github.io/process_description/main/index.html

Known Vulnerabilities
---------------------

None

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

not applicable for this release

Contact Information
For any questions or support, please contact the SW Process Development Community (https://github.com/orgs/eclipse-score/discussions/108) or raise an issue/discussion.
