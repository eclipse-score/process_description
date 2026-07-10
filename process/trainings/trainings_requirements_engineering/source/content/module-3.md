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
id: module-3
title: "Requirement Attributes and Quality"
breadcrumb: "Module 3: Requirement Attributes and Quality"
day: 1
module_number: 3
duration: "~45 min"
standard: Requirements
quiz_pass_mark: 70
prev:
  url: module-2.html
  label: "Module 2: Requirement Levels and Types"
next:
  url: module-4.html
  label: "Module 4: Workflows and Work Products"
---

# Requirement Attributes and Quality

A requirement without well-defined attributes is not a requirement — it is a
wish. S-CORE mandates a specific attribute set for every requirement and
automates part of its population. This module covers all attributes, versioning
rules, and the formulation principles that make requirements verifiable.

## 3.1 Manual Attributes

Every S-CORE requirement must have the following attributes set by the author
before a pull request can be merged:

| Attribute | Values / Format | Purpose |
|-----------|----------------|---------|
| **Unique ID** | `<type_prefix>__<keyword>_<shortname>` | Stable identifier used for all traceability links |
| **Status** | `valid` \| `invalid` | Only `valid` requirements are accepted in main branch |
| **Title** | Free text, expressive | Human-readable label |
| **Description** | Free text | The actual requirement statement |
| **Version** | Integer (1, 2, 3, …) | Bumped on every *significant* change |
| **Rationale / Linkage** | Free text \| derived_from link | Stakeholder reqs need a rationale; derived reqs link to parent |
| **Safety** | `QM` \| `ASIL_B` | Safety integrity level of this requirement |
| **Security** | Boolean / free text | Whether the requirement has security relevance |
| **Type** | `Functional` \| `Interface` \| `Process` \| `Non-Functional` | Determines verification method and linkage rules |

:::important No "Draft" Status in Main Branch
S-CORE intentionally has no `draft` status value. A requirement is either
`valid` (merged) or it lives in a pull request / feature branch. This forces
engineers to complete a requirement before integrating it rather than
accumulating technical debt in the form of unfinished requirements.
:::

## 3.2 The Safety Attribute in Detail

The `safety` attribute is the cornerstone of ISO 26262 compliance. S-CORE
currently supports two values:

| Value | Meaning |
|-------|---------|
| `QM` | Quality Management — no ASIL claim; standard software quality processes apply |
| `ASIL_B` | Automotive Safety Integrity Level B — requires ASIL-B process measures, verification rigour, and traceability |

:::important ASIL Decomposition Is Not Used
S-CORE does not currently apply ASIL decomposition, so ASIL_A, ASIL_C, and
ASIL_D are not required. Only QM and ASIL_B are defined. All safety-relevant
requirements must be classified ASIL_B — a safety-relevant requirement that is
incorrectly marked QM is a safety defect.
:::

The tooling enforces linkage rules: an ASIL_B requirement may only be linked to
other ASIL_B requirements or to QM requirements with a documented rationale.

## 3.3 Auto-Generated Attributes

The Docs-as-Code build populates three attributes automatically, eliminating
manual maintenance overhead and ensuring the attributes are always current:

| Attribute | How it is populated | Tool |
|-----------|---------------------|------|
| **Derives** | Automatically inserted into the parent requirement when a child requirement references it via `derived_from` | Docs-as-Code |
| **Implemented by** | Source files are scanned for a defined tag containing the requirement ID; matching code locations are linked | Docs-as-Code |
| **Verified by** | Test files are scanned for a defined marker containing the requirement ID; matching test cases are linked | Docs-as-Code |

:::example How Implemented by Works
A developer adds the following tag in C++ source code:

```cpp
// [feat__json_config__parse_body]
void ConfigParser::parseBody(const std::string& json) { ... }
```

During the docs build, the tool finds this tag, resolves `feat__json_config__parse_body`
to the corresponding feature requirement, and automatically links the source
file and line to the `implemented_by` attribute.
:::

This automatic population means that the traceability matrix is always
regenerated from the actual code and test artefacts — it cannot be manually
falsified or forgotten.

## 3.4 Requirement Versioning

### Significant vs. Non-Significant Changes

Not every edit to a requirement warrants a version increment. S-CORE defines
precisely which changes are significant:

| Attribute | Significant change | Non-significant change |
|-----------|-------------------|----------------------|
| **Description** | Functional content change or rewrite affecting meaning | Typo corrections, layout, notes |
| **Safety** | Any change | — |
| **Security** | Any change | — |
| **Type** | Any change | — |

:::important Version Mismatch Is a Build Error
Child requirements reference their parent requirement with an explicit version number
(e.g., `derived_from: stkh__platform__config_files[version==2]`). If the parent
requirement's version is later bumped, all child derivation links become stale and
the docs build emits a warning that **blocks merging** until the child requirements
are updated. This ensures that a change in a parent requirement always triggers a
review of all its children.
:::

### Versioning Sets of Requirements

Individual requirement versioning covers single-requirement changes. For
**baselines** — frozen sets of requirements used as the basis for a release or
for a safety case — S-CORE uses standard version control tagging: a git tag
applied to the repository records the exact state of all requirement files.

## 3.5 Requirement Quality and Formulation

A well-written requirement has four properties:

| Property | Test question |
|----------|--------------|
| **Atomic** | Does the requirement describe exactly one thing? |
| **Verifiable** | Can we write a test or review criterion that definitively confirms conformance? |
| **Unambiguous** | Is there exactly one valid interpretation? |
| **Traceable** | Does the requirement link upward to a parent (or have a rationale) and downward to implementation and test? |

:::important Notes Are Not Requirements
A note in a requirement (marked as such in the Docs-as-Code tool) is **not part of
the requirement** itself. Notes provide additional explanation or context but
must not contain normative content. Reviewers must check that normative
statements are in the description, not buried in notes.
:::

## 3.6 Requirement Reviews

Requirements that cannot be checked automatically require a manual inspection.
The S-CORE process supports two kinds of review:

1. **Peer review (PR review)** — every requirement passes through a pull request
   where Committers (`rl__committer`) and Project Leads (`rl__project_lead`) review it before it is merged to `main`.
2. **Formal inspection** — triggered explicitly when a contributor wants a
   thorough review of a set of requirements. Uses a structured inspection
   checklist (`gd_chklst__req_inspection`) that may be integrated into requirements/version management tooling.

:::collapsible What does the inspection checklist cover?
The inspection checklist verifies:

- Completeness: all mandatory attributes are populated
- Consistency: no contradictions between requirements at the same level
- Feasibility: the requirement can realistically be implemented and tested
- Traceability: every requirement is derived from a parent or has a documented rationale
- Safety/security classification: safety attribute is correct relative to safety analysis
- Formulation quality: atomic, verifiable, unambiguous
:::

:::quiz module-3-check

- q: "A developer edits a requirement's description to fix a typo and improve layout, with no change to its functional meaning. Should the version attribute be incremented?"
  options:
    - text: "Yes — any edit to a requirement must increment the version"
    - text: "No — only significant changes (functional content, safety, security, type) trigger a version increment"
      correct: true
    - text: "Yes — the version must be incremented so child links are re-validated"
    - text: "No — versions are only managed by git tags, not per-requirement"
  feedback: >-
    Correct: B. S-CORE explicitly distinguishes significant changes (content changes,
    safety/security/type attribute changes) from non-significant ones (typos, layout,
    notes). Only significant changes require a version bump so that child requirement
    links are re-validated.

- q: "Which attribute is automatically populated by the Docs-as-Code build when test files contain a defined marker with the requirement ID?"
  options:
    - text: "Derives"
    - text: "Implemented by"
    - text: "Verified by"
      correct: true
    - text: "Status"
  feedback: >-
    Correct: C. The build scans test files for a defined marker containing the
    requirement ID and automatically links matching test cases to the 'verified_by'
    attribute. This makes the traceability matrix always current without manual
    maintenance.

- q: "A requirement is marked safety=QM but a safety analysis has determined it is ASIL_B relevant. What is the consequence?"
  options:
    - text: "Nothing — QM and ASIL_B requirements can be freely mixed"
    - text: "The build will flag a linkage violation and the requirement is a safety defect"
      correct: true
    - text: "The requirement is automatically upgraded to ASIL_B at build time"
    - text: "A note is added to the requirement by the tool"
  feedback: >-
    Correct: B. An incorrectly classified safety attribute is a safety defect. The
    S-CORE tooling enforces linkage rules so that ASIL_B requirements may only be
    linked to other ASIL_B requirements (or QM with documented rationale). A wrong
    safety attribute would allow a safety-relevant element to be inadequately
    verified and could invalidate the safety case.
:::
