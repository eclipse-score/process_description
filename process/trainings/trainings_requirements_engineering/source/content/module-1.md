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
id: module-1
title: "Why Requirements Engineering?"
breadcrumb: "Module 1: Why Requirements Engineering?"
day: 1
module_number: 1
duration: "~30 min"
standard: Requirements
quiz_pass_mark: 70
prev:
  url: index.html
  label: Course Overview
next:
  url: module-2.html
  label: "Module 2: Requirement Levels and Types"
---

# Why Requirements Engineering?

Requirements engineering is not bureaucracy — it is the foundation that connects
a customer's need to the last line of tested code. In safety- and security-critical
automotive software this chain must be complete, correct, and auditable.
This module explains why, who is involved, and what standards demand.

## 1.1 The Role of Requirements in Safety-Critical Software

Modern automotive software controls safety-critical actuators — brakes, steering,
power management — and runs in open-source collaborative environments where dozens of
contributors work across organisational boundaries. Without a structured requirements
process two problems become inevitable:

1. **No agreed specification** — contributors implement different interpretations
   of the same need.
2. **No audit trail** — safety and security auditors cannot verify that every
   standard requirement is addressed.

:::important Why RE is Mandated by Standards
ISO 26262 (Part 8, SWE.1), ASPICE PAM 4.0, ISO/SAE 21434, and ISO PAS 8926 all
explicitly require a documented, traceable requirements hierarchy as a precondition
for safety and security releases. Without it, certification is impossible.
:::

The S-CORE Requirements Engineering process provides a single, standardised answer
to both problems: a hierarchy of requirement levels with defined attributes,
mandatory reviews, and automatic traceability links to code and tests.

## 1.2 Stakeholders and Their Information Needs

The requirements hierarchy must satisfy the needs of every stakeholder who will
either write, review, implement, test, or audit requirements. The S-CORE process
identifies the following key stakeholders:

| Stakeholder | Role in S-CORE | What they need from requirements |
|-------------|---------------|----------------------------------|
| **Project Lead** | Defines platform specification and timeline, tracks progress | Clear stakeholder requirements as a project description |
| **SW Architect** | Derives features from stakeholder reqs, allocates to architecture | Feature requirements and AoUs to drive architecture decisions |
| **Tester** | Verifies specification is satisfied | Verifiable, testable requirements with traceability to test cases |
| **Safety Manager** | Initiates safety requirements, performs DFA and FMEA support | Requirements with safety attributes and independence information |
| **Security Manager** | Initiates security requirements, performs TARA support | Requirements with security attributes |
| **SW Developer** | Implements requirements, creates traceability to code | Component requirements with clear acceptance criteria |
| **Feature User** | Integrates platform components into their vehicle project | AoUs — boundary conditions they must fulfil when using the SW |
| **Platform Integration Developer** | Implements requirements for integration | Component and feature requirements |

:::tip Open Source Working Mode
In S-CORE **any Contributor may write a requirement**, but every requirement must be
approved by a Committer or Project Lead before it is merged. Safety and Security
Managers provide support when their domain is involved.
:::

## 1.3 Standard Connections

The S-CORE requirements process implements requirements from multiple standards
simultaneously. Understanding these connections helps prioritise engineering effort.

| Standard | Relevant Clause | What it requires |
|----------|----------------|-----------------|
| **ISO 26262** | Part 8, SWE.1 | SW requirements specification with safety classification, traceability, and review |
| **ASPICE PAM 4.0** | SWE.1 | Elicitation, documentation, agreement, and traceability of SW requirements |
| **ISO/SAE 21434** | §10.5.1 | Cybersecurity requirements derived from TARA, traceable through development |
| **ISO PAS 8926** | §4.5.2.1 | Safety and cybersecurity requirements for automated driving |

:::definition Assumptions of Use (AoU)
A special requirement type that defines the **boundary conditions the user of a
software element must fulfil** to ensure safe and secure operation. AoUs are
exportable to integrators so they can include them in their own requirements
management systems.
:::

## 1.4 Roles and Approval Chains

The S-CORE process defines clear responsibility for each level of the hierarchy:

- **Stakeholder requirements and SW-Platform AoU:** Written by Contributor, approved by Project Lead, supported by Safety Manager.
- **Feature requirements and Feature AoU:** Written by Contributor, approved by Project Lead, supported by Safety Manager and Security Manager.
- **Component requirements and Component AoU:** Written by Contributor, approved by Committer, supported by Safety Manager and Security Manager.
- **Tool/Process requirements:** Written by Contributor, approved by Committer.

This separation ensures that the level of scrutiny matches the safety and security
implications of the requirement.

:::collapsible Why does the approval chain differ between Feature and Component level?
Feature requirements describe platform-level integration behaviour and are visible
to all users of the platform — they require Project Lead approval because they
represent agreements between the platform team and its stakeholders.

Component requirements are implementation-specific and concern only the component
team — Committer approval is sufficient, as Committers are the technical
gatekeepers for their component.
:::

:::quiz module-1-check

- q: "Who is responsible for approving Feature Requirements in S-CORE?"
  options:
    - text: "Contributor"
    - text: "Project Lead"
      correct: true
    - text: "Safety Manager"
    - text: "Feature User"
  feedback: >-
    Correct: B. Feature requirements are written by any Contributor but must be approved
    by the Project Lead. Safety and Security Managers provide support but do not approve.

- q: "Which standard requires SW requirements with a safety classification attribute, traceability, and formal review?"
  options:
    - text: "ISO/SAE 21434"
    - text: "ISO PAS 8926"
    - text: "ISO 26262 Part 8 / ASPICE SWE.1"
      correct: true
    - text: "IEC 61508"
  feedback: >-
    Correct: C. ISO 26262 Part 8 (in conjunction with ASPICE SWE.1) drives the SW requirements
    specification obligations in S-CORE. ISO/SAE 21434 and ISO PAS 8926 add cybersecurity
    and ADS-specific requirements on top.

- q: "An integrator using an S-CORE platform component needs to know the boundary conditions they must satisfy for safe use. Which requirement type addresses this?"
  options:
    - text: "Stakeholder Requirements"
    - text: "Feature Requirements"
    - text: "Process Requirements"
    - text: "Assumptions of Use (AoU)"
      correct: true
  feedback: >-
    Correct: D. Assumptions of Use (AoUs) define the boundary conditions that the user of a
    software element must fulfil. They are exportable so integrators can incorporate them
    into their own requirements management systems.
:::
