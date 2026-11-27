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

Release Note v2.3.0
===================

.. document:: Process description Release Note v2.3.0
  :id: doc__process_description_release_note_v230
  :status: valid
  :safety: ASIL_B
  :version: 1
  :security: YES
  :realizes: wp__module_sw_release_note
  :tags:

| **Module Name:** Process description
| **Release Tag:** v2.3.0
| **Origin Release Tag:** v2.2.2...v2.3.0
| **Release Date:** 2026-12-14

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
T.B.D.

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
The public report of the initial safety audit is available for review here:

:download:`Download the ECLIPSE-1902-152_2025-R087-Safety-Audit-Summary-SCORE-V4R0.pdf <./_assets/ECLIPSE-1902-152_2025-R087-Safety-Audit-Summary-SCORE-V4R0.pdf>`

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
