---
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
# AI Disclosure: This file was largely AI-generated. The AI-generated
# portions are made available under CC0-1.0 and not subject to the
# project's license. The human contributor has reviewed and verified
# that the code is correct.
# SPDX-License-Identifier: CC0-1.0
# Assisted-by: Claude Sonnet 4.6
# *******************************************************************************
id: quiz-1
page_type: quiz
title: "Requirements Engineering Checkpoint Quiz"
breadcrumb: "Requirements Engineering Checkpoint Quiz"
description: >-
  10 questions covering all four modules — Module 1 through Module 4.
  Read each question carefully. Some questions are scenario-based.
  Instant scoring with explanations on submission.
stats:
  - "📋 10 Questions"
  - "⏱ ~20 min"
  - "🎯 Pass mark: 70% (7/10)"
  - "📖 Covers Modules 1–4"
pass_mark: 70
certificate_title: "Requirements Engineering Certified"
certificate_desc: "You have successfully passed the S-CORE Requirements Engineering Training."
certificate_name: "S-CORE Requirements Engineering Training — Eclipse Foundation"
prev:
  url: module-4.html
  label: "Module 4: Workflows and Work Products"
next: null
questions:

  - q: "Why is structured requirements engineering mandated in S-CORE rather than left to individual project discretion?"
    options:
      - text: "It is required because requirements management tools are already available in the platform."
      - text: "ISO 26262, ASPICE SWE.1, ISO/SAE 21434, and ISO PAS 8926 all require a documented, traceable requirements hierarchy as a precondition for certification; without it a safety and security release is not possible."
        correct: true
      - text: "It is only needed for ASIL_D projects; QM-only projects can skip structured RE."
      - text: "Requirements engineering is optional — projects can substitute it with comprehensive test coverage."
    feedback: >-
      Correct: B. All applicable standards in S-CORE (ISO 26262, ASPICE, ISO/SAE 21434,
      ISO PAS 8926) require a documented, traceable requirements hierarchy. There is no
      standards-compliant path to certification without it, regardless of test coverage.

  - q: "In S-CORE, any Contributor may write a requirement. Which of the following statements about the approval process is correct?"
    options:
      - text: "Contributors may directly merge requirements without review if the safety attribute is QM."
      - text: "All requirements are approved exclusively by Safety Managers."
      - text: "Stakeholder and Feature requirements must be approved by the Project Lead; Component requirements must be approved by a Committer."
        correct: true
      - text: "Requirements are approved by the Feature User because they are the primary consumer."
    feedback: >-
      Correct: C. The approval authority depends on the requirement level. Project Lead
      approval is required for Stakeholder and Feature level (visible to all platform users);
      Committer approval is sufficient for Component level (implementation-specific). Safety
      and Security Managers provide support but do not hold the approval role.

  - q: "A requirement states: 'The platform shall support JSON-based configuration.' At which level does this belong, and why?"
    options:
      - text: "Component Requirements — because it describes a concrete implementation detail."
      - text: "Stakeholder Requirements — because it describes a platform-level capability at high abstraction, without specifying how any component implements it."
        correct: true
      - text: "Feature Requirements — because JSON is a specific technical format."
      - text: "Process Requirements — because it describes a process constraint."
    feedback: >-
      Correct: B. Stakeholder Requirements describe what the platform must contain from
      the customer's perspective at the highest abstraction level. This requirement names
      a platform capability without specifying which component implements it or how —
      that decomposition happens at Feature and Component levels.

  - q: "An S-CORE component is released for integration into a vehicle OEM project. The OEM needs to know the boundary conditions their application must satisfy for the component to behave correctly under safety constraints. Which S-CORE work product delivers this information?"
    options:
      - text: "wp__requirements_comp (Component Requirements)"
      - text: "wp__requirements_feat (Feature Requirements)"
      - text: "wp__requirements_comp_aou (Component Assumptions of Use)"
        correct: true
      - text: "wp__requirements_proc_tool (Process/Tool Requirements)"
    feedback: >-
      Correct: C. Component Assumptions of Use (AoU) define the boundary conditions the
      user of a component must fulfil. They are exported in the Module Safety Manual so
      integrators can include them in their own requirements management systems, satisfying
      ISO 26262 and ISO/SAE 21434 requirements for SEooC integration.

  - q: "Which values are currently defined for the 'safety' attribute in S-CORE requirements?"
    options:
      - text: "QM and ASIL_B only, because ASIL decomposition is not used in S-CORE."
        correct: true
      - text: "ASIL_A, ASIL_B, ASIL_C, and ASIL_D to cover the full ISO 26262 range."
      - text: "QM, ASIL_A, and ASIL_B for the subset of ISO 26262 levels used in automotive OSS."
      - text: "Safety classification is not an attribute in S-CORE requirements."
    feedback: >-
      Correct: A. S-CORE currently defines only QM and ASIL_B as valid safety attribute
      values. ASIL decomposition is not applied, so ASIL_A, _C, and _D are not needed.
      A safety-relevant requirement incorrectly marked QM is a safety defect.

  - q: "A developer edits a Component Requirement by changing its description to fix a typo and rewrites one sentence for clarity — the functional meaning is identical. Must the version attribute be incremented?"
    options:
      - text: "Yes — any edit to description requires a version bump."
      - text: "No — only functional content changes, or changes to the safety, security, or type attribute, are significant and require a version increment."
        correct: true
      - text: "Yes — otherwise child requirement links become invalid."
      - text: "No — version increments are only required for ASIL_B requirements."
    feedback: >-
      Correct: B. S-CORE distinguishes significant changes (functional content changes;
      any change to safety, security, or type attributes) from non-significant changes
      (typos, layout, notes). Only significant changes require a version bump and
      trigger re-validation of child requirement links.

  - q: "Which of the three auto-generated attributes is populated by scanning source code files for a defined tag containing the requirement ID?"
    options:
      - text: "Derives"
      - text: "Implemented by"
        correct: true
      - text: "Verified by"
      - text: "Status"
    feedback: >-
      Correct: B. 'Implemented by' is populated by scanning source code files for a
      defined tag containing the requirement ID. 'Verified by' comes from test files.
      'Derives' is automatically inserted into parent requirements when a child uses
      'derived_from'. 'Status' is a manual attribute.

  - q: "A contributor wants to create Feature AoU requirements. Compared to a plain Feature Requirements workflow, which additional input is required?"
    options:
      - text: "wp__requirements_stkh (Stakeholder Requirements)"
      - text: "wp__requirements_proc_tool (Process/Tool Requirements)"
      - text: "wp__feature_arch (Feature Architecture)"
        correct: true
      - text: "wp__requirements_inspect (Requirements Inspection)"
    feedback: >-
      Correct: C. AoUs at Feature level emerge from the safety concept defined in the
      Feature Architecture. The architecture defines isolation boundaries and safety
      mechanisms; AoUs express the conditions that must hold outside those boundaries.
      Without the Feature Architecture there is no basis for writing Feature AoUs.

  - q: "A safety auditor asks how S-CORE ensures that a requirement shown as 'verified by Test_X' in the documentation genuinely corresponds to a test that references that requirement. What is the correct answer?"
    options:
      - text: "The Safety Manager manually cross-checks the traceability matrix against the test repository each sprint."
      - text: "The Docs-as-Code build scans all test files for requirement ID markers on every build and regenerates the 'verified_by' links automatically, so the documentation can never show a test link that does not exist in the codebase."
        correct: true
      - text: "An external ALM tool is synchronised monthly to keep the traceability matrix current."
      - text: "Developers are required to update the traceability spreadsheet whenever a new test is added."
    feedback: >-
      Correct: B. The 'verified_by' attribute is auto-populated on every docs build by
      scanning actual test files. The traceability matrix is therefore always regenerated
      from real artefacts — it cannot be manually falsified, forgotten, or allowed to
      drift. This is a key argument in the S-CORE safety case for requirements coverage.

  - q: "A new feature is being specified. The correct end-to-end flow in S-CORE is:"
    options:
      - text: "Write Component Requirements first to anchor implementation, then derive Feature and Stakeholder Requirements bottom-up."
      - text: "Write Stakeholder Requirements first, then derive Feature Requirements, then derive Component Requirements top-down, linking each level to its parent with a versioned derived_from reference."
        correct: true
      - text: "Write Feature Requirements first, then both Stakeholder Requirements and Component Requirements independently."
      - text: "Only Stakeholder Requirements and Component Requirements are needed; Feature Requirements are optional in S-CORE."
    feedback: >-
      Correct: B. S-CORE follows the standards' top-down derivation model. Stakeholder
      Requirements describe what the platform must contain; Feature Requirements break this
      down to integration level; Component Requirements specify individual component
      behaviour. Each level links to its parent using a versioned 'derived_from'
      reference. Process Requirements are a separate, parallel concern derived from the
      process description, not a step that precedes stakeholder requirements.
orphan: true
---
