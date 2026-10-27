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

Release Note v2.2.2
===================

.. document:: Process description Release Note v2.2.2
   :id: doc__process_description_release_note_v222
   :status: valid
   :safety: ASIL_B
   :version: 1
   :security: YES
   :realizes: wp__module_sw_release_note
   :tags:

| **Module Name:** Process description
| **Release Tag:** v2.2.2
| **Origin Release Tag:** v2.1.0...v2.2.2
| **Release Date:** 2026-11-02

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

Closed external audit findings (audit meeting #7, #652) for three process areas:

- Problem Resolution: clarified critical-review topics, notification handling and the two
  closure conditions for safety-affected problems (#557, by @PandaeDo in
  https://github.com/eclipse-score/process_description/pull/832)
- Change Management: clarified Change Management Plan scope, request attributes and
  impact-analysis prompts, aligned with ISO 26262-8:2018 8.4.1-8.4.4 (#567, by @PandaeDo in
  https://github.com/eclipse-score/process_description/pull/834)
- Release/Quality Management: referenced the conformance check and work-product reviews as
  mandatory input to module/platform release approval (#562, #564, by @PandaeDo in
  https://github.com/eclipse-score/process_description/pull/835)

Maturity Level 3 is achieved for:
Documentation Management
Quality Management
Safety Analysis
Requirements Engineering

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

- fix: MODULE.bazel.lock by @AlexanderLanin in https://github.com/eclipse-score/process_description/pull/782
- Update implementation process requirement and needextend by @PandaeDo in https://github.com/eclipse-score/process_description/pull/783
- Update dependency score_docs_as_code to v8.1.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/786
- Add workpackages in tool requirements by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/787
- Update dependency score_docs_as_code to v8.1.1 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/788
- Update dependency score_docs_as_code to v8.1.2 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/790
- Update dependency score_docs_as_code to v8.2.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/791
- fix: missing 'satisfies' link by @a-zw in https://github.com/eclipse-score/process_description/pull/792
- Fix broken link to feature architecture inspection checklist by @NicolasFussberger in https://github.com/eclipse-score/process_description/pull/795
- Improvement: Add security process checks by @PandaeDo in https://github.com/eclipse-score/process_description/pull/796
- Update dependency score_docs_as_code to v8.3.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/797
- Modify valid_from/until attribute requirements by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/799
- split feature integration test place by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/793
- Modify valid_from/until attribute description by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/800
- Lists al QM related wp in the Quality Plan by @PandaeDo in https://github.com/eclipse-score/process_description/pull/803
- Update structural coverage reference from unit to component by @pahmann in https://github.com/eclipse-score/process_description/pull/798
- Monitoring requirement link completeness by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/806
- Extend versioned links concept for reqs and arch by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/807
- chore(docs): update score_docs_as_code gitignore configuration by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/808
- update version to tool_version by @masc2023 in https://github.com/eclipse-score/process_description/pull/814
- Add Documentation Management Plan Template by @PandaeDo in https://github.com/eclipse-score/process_description/pull/818
- change architecture element definition by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/815
- Improve guidance on interface documentation by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/819
- Update verification requirements to include Architectural elements by @pahmann in https://github.com/eclipse-score/process_description/pull/820
- add line breaks in arc template by @RolandJentschETAS in https://github.com/eclipse-score/process_description/pull/822
- Fix several spellings by @PandaeDo in https://github.com/eclipse-score/process_description/pull/824
- Change style for notes by @PandaeDo in https://github.com/eclipse-score/process_description/pull/823
- Add module user manual to release mgt process by @PandaeDo in https://github.com/eclipse-score/process_description/pull/821
- Update links for template consistency by @PandaeDo in https://github.com/eclipse-score/process_description/pull/825
- chore(devcontainer): sync standard SCORE tool launcher by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/826
- Change impact tooling corrections by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/827
- Update dependency score_docs_as_code to v8.4.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/829
- Fix title and list rendering in Security Management Getting Started section by @CryptoNutcase in https://github.com/eclipse-score/process_description/pull/831
- update problem resolution to close  audit findings by @masc2023 in https://github.com/eclipse-score/process_description/pull/832
- fix qlm audit findings by @masc2023 in https://github.com/eclipse-score/process_description/pull/835
- fix audit findings chm by @masc2023 in https://github.com/eclipse-score/process_description/pull/834
- Add release notes for S-CORE release v10.0 by @masc2023 in https://github.com/eclipse-score/process_description/pull/833
- Change to valid_inspected state by @aschemmel-tech in https://github.com/eclipse-score/process_description/pull/836
- Update dependency score_docs_as_code to v8.5.0 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/837
- Add ai supported concept by @masc2023 in https://github.com/eclipse-score/process_description/pull/809
- Update dependency score_docs_as_code to v8.5.1 by @eclipse-score-bot in https://github.com/eclipse-score/process_description/pull/839
- Solves id naming convention by @PandaeDo in https://github.com/eclipse-score/process_description/pull/841
- Improve verification report based on module template by @pahmann in https://github.com/eclipse-score/process_description/pull/794
- Fix safety fdr linkage by @panddo in https://github.com/eclipse-score/process_description/pull/842
- Fix safety fdr linkage by @panddo in https://github.com/eclipse-score/process_description/pull/843
- Add platform aou template by @panddo in https://github.com/eclipse-score/process_description/pull/844
- Add complies links to work products by @panddo in https://github.com/eclipse-score/process_description/pull/845
- Align process req to metamodel by @panddo in https://github.com/eclipse-score/process_description/pull/846
- Fix verification report version by @panddo in https://github.com/eclipse-score/process_description/pull/847
- Add release notes for S-CORE release v0.10 by @masc2023 in https://github.com/eclipse-score/process_description/pull/833


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
- Issue 2: Safety package containing external Audit report not available, due to open improvement proposals/recommendation from external assessor team, #652. Findings for Problem Resolution, Change Management and Release/Quality Management are closed as of this release; findings for other process areas remain open.
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
