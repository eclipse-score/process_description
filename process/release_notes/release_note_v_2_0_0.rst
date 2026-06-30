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

Release Note v2.0.0
===================

.. document:: Process description Release Note v2.0.0
   :id: doc__process_description_release_note_v200
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__module_sw_release_note
   :tags:

| **Module Name:** Process description
| **Release Tag:** v2.0.0
| **Origin Release Tag:** v1.5.4
| **Release Date:** 2026-06-28

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

Building blocks meta model is reworked.
(https://eclipse-score.github.io/process_description/main/index.html).
Contains now Features, Components as own elements, adapt linkage names, e.g.
Requirements are now "derived_from" parent requirements, correct some linkages between
elements

Module Templates removed from Folder Templates and
(https://eclipse-score.github.io/process_description/main/folder_templates/index.html)

moved now to module_templates folder
(https://eclipse-score.github.io/module_template/main/)

Implementation is now defined.

Now versioning of sphinx-needs elements is introduced. Thus this version is the first
baseline of the process_description.

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

- Fix trace to external AoU for Components by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/654
- Update Safety Analysis  by @PandaeDo in https://github.com/eclipse-score/process_description/pull/659
- fix meta model example picture by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/665
- Update Safety Analysis templates and process descriptions by @PandaeDo in https://github.com/eclipse-score/process_description/pull/663
- PR for platform analysis template #455 #454 by @NarasipurRohini in https://github.com/eclipse-score/process_description/pull/662
- Add release trigger to docs workflow by @Saumya-R in https://github.com/eclipse-score/process_description/pull/667
- add minimal required elements in meta model as example by @masc2023 in https://github.com/eclipse-score/process_description/pull/666
- Update safety analysis process requirements by @PandaeDo in https://github.com/eclipse-score/process_description/pull/673
- Update process req of documentation management by @PandaeDo in https://github.com/eclipse-score/process_description/pull/674
- Update Safety Analysis FDR by @PandaeDo in https://github.com/eclipse-score/process_description/pull/677
- Correct branch name by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/678
- Metamodel link renames by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/621
- Enhance test log details with execution log links by @pahmann in https://github.com/eclipse-score/process_description/pull/682
- rename relations for SysML compatibility by @RSingh1511 in https://github.com/eclipse-score/process_description/pull/618
- Document iso26262 audit 7 status by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/685
- upgrade doc-as-code to v4.1.0 by @masc2023 in https://github.com/eclipse-score/process_description/pull/687
- remove module folder template by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/683
- Update Safety Analysis Template by @ANegm-ETAS in https://github.com/eclipse-score/process_description/pull/669
- rework implementation by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/689
- Add attribute requirement to config mgm by @pahmann in https://github.com/eclipse-score/process_description/pull/690
- adopt pictures to new implementation concept by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/691
- increase docs as code version by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/692
- increase bazel version to 8.6 by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/693
- upgrade doc-as-code version 4.3.0 by @masc2023 in https://github.com/eclipse-score/process_description/pull/694
- Update status to valid for merged Requirements and Documents by @PandaeDo in https://github.com/eclipse-score/process_description/pull/697
- Correct automation tag for process reqs in requirements process by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/699
- Update linking check from req to architecture by @aschemmel-tech https://github.com/eclipse-score/process_description/pull/700
- Clarify tool verification report version attribute by @aschemmel-tech https://github.com/eclipse-score/process_description/pull/701
- Apply tool version and Bzlmod locking, update docs-as-code by @AlexanderLanin https://github.com/eclipse-score/process_description/pull/705
- add versioning of requirements by @AlexanderLanin in https://github.com/eclipse-score/process_description/pull/708
- upgrade docs-as-code version 4.5.0 by @AlexanderLanin in https://github.com/eclipse-score/process_description/pull/710
- add aspice 4 ml3 architecture by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/702
- Fix links to requirement templates by @PandaeDo in https://github.com/eclipse-score/process_description/pull/713
- Selection of codeowner @RolandJentsch by @masc2023 in https://github.com/eclipse-score/process_description/pull/712
- Attifunel process req test description added by @attifunel in https://github.com/eclipse-score/process_description/pull/679
- Update process requirements by @PandaeDo in https://github.com/eclipse-score/process_description/pull/716
- Fix FMEA fault model table layout by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/718
- Rename ISO 26262 audit status charts and adjust colors by @pahmann in https://github.com/eclipse-score/process_description/pull/720
- Set verification process to ML2 by @pahmann in https://github.com/eclipse-score/process_description/pull/722
- Verification: Update test specification details by @pahmann in https://github.com/eclipse-score/process_description/pull/719
- fix implementation review findings by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/717
- Update dependency score_docs_as_code to v4.6.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/725
- fix one link and update some requirements automation status by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/727
- add initial version of the release notes for version 2.0.0 by @masc2023 in https://github.com/eclipse-score/process_description/pull/688

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
- Issue 3: Maturity level 2 no yet completed in total, but deploying is still ongoing also auditing per external auditor to achieve higher maturity levels, #652, https://github.com/eclipse-score/score/issues/2911

Known Vulnerabilities
---------------------

None

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

As Building Blocks Meta Model is adapted and Templates are removed, consider to use the compatible doc-as-code version and the module templates from the module_template repository.

Versionning is introduced. Updated with the latest doc-as-code version.

Contact Information
For any questions or support, please contact the SW Process Development Community (https://github.com/orgs/eclipse-score/discussions/108) or raise an issue/discussion.
