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
id: module-4
title: "Workflows and Work Products"
breadcrumb: "Module 4: Workflows and Work Products"
day: 1
module_number: 4
duration: "~45 min"
standard: Requirements
quiz_pass_mark: 70
prev:
  url: module-3.html
  label: "Module 3: Requirement Attributes and Quality"
next:
  url: quiz-1.html
  label: "Checkpoint Quiz"
orphan: true
---

# Workflows and Work Products

S-CORE defines six specific workflows for requirements engineering and eight
formal work products. This module walks through each workflow, its inputs and
outputs, its responsible parties, and how the work products satisfy the
applicable standards. The module closes with the end-to-end traceability
picture.

## 4.1 Overview of the Six Workflows

| Workflow ID | Workflow name | Responsible | Approved by |
|-------------|---------------|-------------|-------------|
| `wf__req_stkh_req` | Create/Maintain Stakeholder Requirements and SW-Platform AoU | Contributor `rl__contributor` | Project Lead `rl__project_lead` |
| `wf__req_feat_req` | Create/Maintain Feature Requirements | Contributor `rl__contributor` | Project Lead `rl__project_lead` |
| `wf__req_feat_aou` | Create/Maintain Feature AoUs | Contributor `rl__contributor` | Project Lead `rl__project_lead` |
| `wf__req_comp_req` | Create/Maintain Component Requirements | Contributor `rl__contributor` | Committer `rl__committer` |
| `wf__req_comp_aou` | Create/Maintain Component AoUs | Contributor `rl__contributor` | Committer `rl__committer` |
| `wf__req_tool` | Create/Maintain Tool/Process Requirements | Contributor `rl__contributor` | Committer `rl__committer` |
| `wf__monitor_verify_requirements` | Monitor/Verify Requirements | Committer `rl__committer` | Committer `rl__committer` |

All six creation workflows can be initiated as part of a **Change Request** —
the Change Management process is the single entry point for all content changes
in S-CORE.

The **Monitor/Verify Requirements** workflow (`wf__monitor_verify_requirements`)
is responsible for inspecting the full requirements set. Unlike the creation
workflows it is owned by the Committer, who checks all requirement levels and
safety manuals against the inspection checklist (`gd_chklst__req_inspection`).
Its output is either an updated issue tracker entry or a completed Requirements
Inspection work product.

Safety Managers (`rl__safety_manager`) are *supported_by* in the three stakeholder/feature workflows;
both Safety and Security Managers (`rl__security_manager`) are *supported_by* in the two AoU workflows
at feature and component level.

## 4.2 Workflow: Stakeholder Requirements and SW-Platform AoU

**Purpose:** Establish the top-level specification of what the platform must
contain. This workflow produces the assumed Technical Safety Requirements for
the SEooC.

**Inputs:** `wp__policies`, `wp__issue_track_system`

**Outputs:** `wp__requirements_stkh`, `wp__requirements_sw_platform_aou`

:::example Triggering this workflow
A project lead opens a change request: *"The platform shall support OTA software
updates for individual components."* A contributor writes the stakeholder
requirement and the SW-Platform AoU (the conditions the OEM integrator must
satisfy to use OTA safely). The project lead reviews and approves the PR.
:::

**Key guidance templates available:** `gd_temp__req_stkh_req`,
`gd_temp__req_formulation`

## 4.3 Workflow: Feature Requirements

**Purpose:** Break down stakeholder requirements into feature-level
specifications that describe integration behaviour independent of implementation.

**Inputs:** `wp__requirements_stkh`, `wp__issue_track_system`

**Output:** `wp__requirements_feat`

Feature requirements are the primary driver of SW Architecture work. The SW
Architect reads them to derive the feature architecture that allocates
behaviour to components.

## 4.4 Workflows: AoU Requirements

Feature AoUs and Component AoUs are managed by their own workflows because
they involve additional inputs from architecture work products and feed directly
into the Safety Manual artefacts:

- **Feature AoU** (`wf__req_feat_aou`):
  - Extra input: `wp__feature_arch`
  - Additional output: `wp__platform_safety_manual`

- **Component AoU** (`wf__req_comp_aou`):
  - Extra input: `wp__component_arch`
  - Additional output: `wp__module_safety_manual`

:::important AoU and Architecture Are Coupled
AoUs cannot be written without the architecture work product because AoUs
emerge from the safety concept: once the architecture defines the isolation
boundaries and safety mechanisms, the AoUs state what conditions must hold
*outside* those boundaries for the safety concept to be valid.
:::

## 4.5 Work Products and Their Compliance Tags

Each work product carries compliance tags that map it to the specific standard
clauses it satisfies. Understanding these tags is important for auditors and
safety managers.

| Work Product | ID | Compliance tags |
|-------------|-----|-----------------|
| Stakeholder Requirements | `wp__requirements_stkh` | ISO 26262 §8/6.5.1, ISO/SAE 21434 §10.5.1 |
| Feature Requirements | `wp__requirements_feat` | ISO 26262 §8/6.5.1, ISO/SAE 21434 §10.5.1 |
| Component Requirements | `wp__requirements_comp` | ISO 26262 §8/6.5.1, ISO PAS 8926 §4.5.2.1, ISO 26262 analysis annex, ISO/SAE 21434 §10.5.1 |
| SW-Platform AoU | `wp__requirements_sw_platform_aou` | ISO 26262 §8/6.5.1, ISO/SAE 21434 §10.5.1–2 |
| Feature AoU | `wp__requirements_feat_aou` | ISO 26262 §8/6.5.1, ISO/SAE 21434 §10.5.1–2 |
| Component AoU | `wp__requirements_comp_aou` | ISO 26262 §8/6.5.1, ISO PAS 8926 §4.5.2.1, ISO/SAE 21434 §10.5.1–2 |
| Process/Tool Requirements | `wp__requirements_proc_tool` | (internal process lifecycle) |
| Requirements Inspection | `wp__requirements_inspect` | ISO 26262 §8/6.5.3 |

The **Requirements Inspection** work product is based on a structured checklist
and may be integrated into requirements or version management tooling. It
addresses the ISO 26262 requirement for formal review of SW requirements.

## 4.6 End-to-End Traceability

The S-CORE traceability model connects every requirement from its origin at
stakeholder level down to the implementation artefacts and verification
evidence:

```
Stakeholder Requirements
      │ derived_from
      ▼
Feature Requirements ──────────────────────► Feature AoU
      │ derived_from
      ▼
Component Requirements ────────────────────► Component AoU
      │ implemented_by (auto)   │ verified_by (auto)
      ▼                         ▼
   Source code              Test cases
```

:::important Traceability Is Automatically Maintained
The `implemented_by` and `verified_by` links are populated automatically by the
Docs-as-Code build. This means **the traceability matrix is always regenerated
from the real artefacts** — it cannot drift from the code. Auditors can trust
that a requirement shown as "verified by test X" genuinely corresponds to a test
that references that requirement ID.
:::

## 4.7 Using the Tooling

The S-CORE Docs-as-Code tool provides:

1. **Requirement templates** — pre-formatted stubs for each requirement type that enforce the mandatory attribute set.
2. **Build-time validation** — attribute completeness, version link consistency, linkage rule enforcement, and safety attribute propagation checks.
3. **Coverage reports** — automatically generated views showing which requirements lack `implemented_by` or `verified_by` links (coverage gaps).
4. **PR-based review workflow** — all requirement changes go through a pull request; the Committer or Project Lead review is recorded in git history.

:::tip Getting Started
The Requirements Engineering concept (`doc_concept__req_process`) and Getting
Started guide (`doc_getstrt__req_process`) describe the exact steps for creating
a new requirement, deriving child requirements, and triggering a formal inspection.
The workflow diagram in the getting started guide maps every step to the
corresponding workflow ID listed in Section 4.1.
:::

:::collapsible Linking requirements to code and tests — practical steps
1. **Find the requirement ID** in the generated HTML portal or in the RST source.
2. **Add the implementation tag** in the source file as a structured comment:
   `// [<requirement_id>]` (exact syntax depends on the Docs-as-Code version).
3. **Add the verification marker** in the test file using the framework-specific
   marker (e.g., a pytest mark or a comment annotation).
4. **Run the docs build** (`bazel run //:docs`). The build will now populate
   `implemented_by` and `verified_by` in the HTML output.
5. **Verify coverage** in the generated requirements traceability report.
:::

:::quiz module-4-check

- q: "A contributor wants to create new Component Requirements. Which approval chain applies?"
  options:
    - text: "Written by Safety Manager, approved by Project Lead"
    - text: "Written by Contributor, approved by Committer"
      correct: true
    - text: "Written by Committer, approved by Project Lead"
    - text: "Written by Contributor, approved by Safety Manager"
  feedback: >-
    Correct: B. Component Requirements are created by any Contributor and approved
    by a Committer. Project Lead approval is required for Stakeholder and Feature
    level requirements; Committer approval is sufficient for Component level because
    this is an implementation-specific concern.

- q: "Feature AoU requirements have an additional input compared to Feature Requirements. What is it?"
  options:
    - text: "wp__requirements_stkh (Stakeholder Requirements)"
    - text: "wp__requirements_comp (Component Requirements)"
    - text: "wp__feature_arch (Feature Architecture)"
      correct: true
    - text: "wp__issue_track_system (Issue Tracker)"
  feedback: >-
    Correct: C. AoUs at feature level emerge from the safety concept defined in
    the Feature Architecture. Without the architecture there is no basis for
    determining what boundary conditions must hold outside the software element.

- q: "An auditor asks: 'How do you guarantee that the traceability matrix between requirements and test cases is up to date?' What is the correct S-CORE answer?"
  options:
    - text: "The traceability matrix is maintained manually by the Safety Manager and reviewed quarterly"
    - text: "Traceability is managed in an external ALM tool which is synced monthly"
    - text: "The Docs-as-Code build automatically regenerates the verified_by links from test file markers on every build, so the matrix cannot drift from the actual test artefacts"
      correct: true
    - text: "Developers are required to update the traceability spreadsheet when they add tests"
  feedback: >-
    Correct: C. The 'verified_by' attribute is auto-populated by scanning test files
    for the requirement ID marker on every build. This means the traceability matrix
    is always regenerated from the real artefacts — it is impossible for it to show
    a test link that does not exist in the codebase.
:::
