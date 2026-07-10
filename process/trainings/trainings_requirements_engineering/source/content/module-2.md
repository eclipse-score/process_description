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
id: module-2
title: "Requirement Levels and Types"
breadcrumb: "Module 2: Requirement Levels and Types"
day: 1
module_number: 2
duration: "~45 min"
standard: Requirements
quiz_pass_mark: 70
prev:
  url: module-1.html
  label: "Module 1: Why Requirements Engineering?"
next:
  url: module-3.html
  label: "Module 3: Requirement Attributes and Quality"
---

# Requirement Levels and Types

S-CORE defines a five-level requirement hierarchy. Each level has a precise
meaning, a defined audience, a characteristic abstraction, and specific
compliance obligations under ISO 26262, ASPICE, and ISO/SAE 21434.
This module maps the hierarchy and explains when to use each level.

## 2.1 The S-CORE Requirement Hierarchy

The following diagram summarises the levels and their derivation relationships:

```
Stakeholder Requirements (SW-Platform level)
    │
    ▼
Feature Requirements  ←→  Feature AoU
    │
    ▼
Component Requirements  ←→  Component AoU
    │
    ├── Code (Implemented by)
    └── Tests (Verified by)
```

Additionally, **Process/Tool Requirements** sit alongside the hierarchy and
describe the tooling and process activities that support it.

A child requirement is always *derived from* its parent. The derivation link
includes the parent's version number so that stale links are automatically
detected during the docs build.

## 2.2 Stakeholder Requirements (`wp__requirements_stkh`)

**Stakeholder Requirements** are defined at the SW-Platform level. They describe
**what the platform needs to contain** from the perspective of the customer
(stakeholder), expressed as technical requirements at the highest level of
abstraction.

:::important Assumed Technical Safety Requirements
In SEooC (Safety Element out of Context) development — which is the S-CORE model
— Stakeholder Requirements represent the **assumed Technical Safety Requirements**.
The integrator must verify that these assumptions match their vehicle-level
safety goals before using the platform.
:::

:::example Stakeholder Requirement Example
```
The platform shall support configuration of applications via files
(e.g. yaml, json).
```
This describes a platform-level capability without specifying how it is
implemented or which component provides it.
:::

**Compliance obligations:** ISO 26262 §8 / SWE.1, ISO/SAE 21434 §10.5.1

## 2.3 Feature Requirements (`wp__requirements_feat`)

**Feature Requirements** are derived from Stakeholder Requirements and describe
the behaviour of a feature **at platform integration level**, independent of
which components implement it.

A "feature" represents a coherent set of requirements that together deliver a
platform-level capability. Feature requirements are the primary input for
architects, testers, and integrators.

:::example Feature Requirement Example
```
The feature shall use JSON formatted string according to RFC-8259 for
configuration.
```
This specifies the format at feature level without naming an implementation component.
:::

Feature requirements also serve as the basis for integration testing on
platform level.

**Compliance obligations:** ISO 26262 §8 / SWE.1, ISO/SAE 21434 §10.5.1

## 2.4 Component Requirements (`wp__requirements_comp`)

**Component Requirements** are derived from Feature Requirements and describe
component-specific behaviour. They are implementation-facing: they tell a
developer exactly what a component must do within the context of its feature.

:::example Component Requirement Example
```
The component shall provide API calls to read and interpret every field of a
JSON body in C++.
```
This is unambiguously allocated to a single component and is directly testable
at unit level.
:::

Component Requirements are the lowest level in the hierarchy and have the most
direct link to code and test artefacts via the auto-generated `implemented_by`
and `verified_by` attributes.

**Compliance obligations:** ISO 26262 §8 / SWE.1, ISO PAS 8926 §4.5.2.1,
ISO 26262 (analysis appendix), ISO/SAE 21434 §10.5.1 + §10.5.2

## 2.5 Assumptions of Use (AoU)

AoUs can exist at **every level** — SW-Platform, Feature, and Component. They
define the boundary conditions that the *user* of the software element must
fulfil to ensure correct, safe, and secure operation.

| AoU Level | Work Product ID | Audience | Compliance |
|-----------|----------------|----------|------------|
| SW-Platform AoU | `wp__requirements_sw_platform_aou` | Vehicle integrators using the platform | ISO 26262, ISO/SAE 21434 §10.5.1–2 |
| Feature AoU | `wp__requirements_feat_aou` | Teams integrating the feature into a product | ISO 26262, ISO/SAE 21434 §10.5.1–2 |
| Component AoU | `wp__requirements_comp_aou` | Developers using the component API | ISO 26262, ISO PAS 8926, ISO/SAE 21434 §10.5.1–2 |

:::example AoU Example
```
The user shall provide a string as input which is not corrupted due to HW or
QM SW errors.
```
This AoU tells the caller of the JSON configuration component what quality of
input they must guarantee.
:::

:::important AoU and the Safety Manual
Feature and Component AoUs feed directly into the **Platform Safety Manual** and
**Module Safety Manual** respectively. These manuals are the exportable artefacts
that document all conditions an integrator must satisfy when deploying S-CORE
components in a safety-relevant context.
:::

## 2.6 Process and Tool Requirements (`wp__requirements_proc_tool`)

**Process/Tool Requirements** describe the activities and tooling constraints
that support the development process. They are derived from the process
description and specify what must be done manually versus what must be
automated (tool-supported).

:::example Process/Tool Requirement Example
```
It shall be checked that safety requirements (Safety != QM) can only be linked
against safety requirements.
```
This is a process requirement that drives tool implementation in the
Docs-as-Code build.
:::

Process Requirements are verified by **reviewing the process description** rather
than by functional testing.

## 2.7 Requirement Types

Every requirement — regardless of level — carries a **type** attribute that
determines how it is verified and how it participates in traceability:

| Type | Definition | Verification method |
|------|-----------|---------------------|
| **Functional** | Describes a behaviour that can be demonstrated by test | Unit test, integration test |
| **Interface** | Defines an API or protocol; does not itself describe a behaviour | Review / analysis |
| **Process** | Describes a process activity or constraint; sub-type of Non-Functional | Review of process description |
| **Non-Functional** | All other quality constraints (performance, capacity, …) | Review / analysis |

:::important Type Affects Linkage Rules
The `type` attribute controls which architecture and safety linkage rules apply.
For example, safety requirements of type Functional must eventually be linked to
a test that exercises the functional behaviour. A Process requirement linked to a
Functional safety requirement would be flagged as a linkage violation.
:::

:::collapsible Interface requirements — when are they needed?
Use the **Interface** type when a requirement defines a contract between two
parties (e.g., an API signature, a protocol format, a data format) rather than a
behaviour. Interface requirements are important for safety analysis because they
define the boundaries across which faults can propagate — they often appear as
inputs to DFA (Dependent Failure Analysis) and TARA.
:::

:::quiz module-2-check

- q: "A requirement states: 'The feature shall use JSON formatted strings according to RFC-8259 for configuration.' At which requirement level does this belong?"
  options:
    - text: "Stakeholder Requirements"
    - text: "Feature Requirements"
      correct: true
    - text: "Component Requirements"
    - text: "Process Requirements"
  feedback: >-
    Correct: B. The requirement describes behaviour at feature (platform integration)
    level — it specifies the format the feature uses without naming a specific component.
    Stakeholder requirements would be even more abstract; component requirements would
    name the implementing component and its API.

- q: "An integrator is building a vehicle product using an S-CORE platform component. They receive a document listing the conditions their application must satisfy to use the component safely. What type of requirement is this?"
  options:
    - text: "Stakeholder Requirements"
    - text: "Process Requirements"
    - text: "Assumptions of Use (AoU)"
      correct: true
    - text: "Functional Requirements"
  feedback: >-
    Correct: C. Assumptions of Use (AoUs) define boundary conditions for the user
    of a software element. They are exportable to integrators precisely so they can
    be incorporated into the integrator's own requirements management system.

- q: "Which requirement type is verified by reviewing the process description rather than by functional test execution?"
  options:
    - text: "Functional"
    - text: "Interface"
    - text: "Process"
      correct: true
    - text: "Non-Functional"
  feedback: >-
    Correct: C. Process requirements describe activities in the development process
    and are verified by reviewing the process description (or checking that tooling
    enforces them). They cannot be verified by running a functional test.
:::
