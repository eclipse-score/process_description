..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

.. _glossary:

Glossary
########

Overview
========

The glossary is intended to provide a common vocabulary for all project participants
and to ensure clarity and consistency in the use of terminology across the project.

It includes definitions for terms related to the building blocks concept,
development phases, roles, work products, and other relevant concepts.

Terms
=====

.. list-table:: Process Description Glossary
   :header-rows: 1
   :widths: 20,80, 80

   * - **Term**
     - **Definition**
     - **Comment/Link**

   * - **Assumptions of Use (AoU)**
     - Constraints and conditions under which a component, feature, or platform element can be safely and correctly used. AoUs must be documented and considered by users of the element.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Building Blocks**
     - Fundamental structural elements of the platform including Features, Components, Units, and Dependable Elements that form the basis of the system architecture.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Change Request (CR)**
     - A formal request to modify, add, or remove features or components in the platform. Change requests drive the development lifecycle and must be tracked and approved.
     - :ref:`Process change management<change_management>`

   * - **Committer**
     - A developer role who reviews and accepts contributions (pull requests) to the main codebase. Committers maintain code quality and enforce project processes.
     - :ref:`Roles<roles>`

   * - **Component**
     - A major building block of the platform consisting of one or more Units. Components are defined by Component Requirements and Component Architecture, and are tested through Component Integration Tests.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Component Architecture**
     - The design specification that defines how a component is structured, including its internal organization, interfaces, and relationships with other components.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Component Integration Tests**
     - Verification tests that verifies component requirements and architecture, as well as the integration of multiple Units into a single Component.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Component Safety/Security Analysis**
     - Systematic analysis performed on component architecture to verify compliance with safety and security requirements, documenting any violations or potential faults.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Concept Phase**
     - Initial development phase where feasibility and decision criteria are established for a new feature or component request. Only Change Management is mandatory in this phase.
     - :ref:`Lifecycle concept<general_concepts_lifecycle>`

   * - **Contributor**
     - An individual who contributes to the project by submitting code, documentation, processes, or other work products. Contributors work within defined workflows and processes.
     - :ref:`Roles<roles>`

   * - **Delivery Container**
     - A packaging mechanism for delivering Dependable Elements (e.g., executable code or libraries) to users or integrators of the platform.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Dependable Element**
     - The highest abstraction level in the building blocks model. A Dependable Element consists of one or more Components and can be developed as a Safety Element out of Context (SEooC). It is delivered in a Delivery Container.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Dependable Element View**
     - Documentation that maps components to Dependable Elements, showing how components are grouped for delivery.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Detailed Design**
     - The comprehensive design specification for a Unit, including implementation details and algorithms. Verified through Unit Tests.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Development Phase**
     - The phase where accepted features or components are planned, implemented, and verified according to defined project processes. May include iterative implementation cycles.
     - :ref:`Lifecycle concept<general_concepts_lifecycle>`

   * - **Feature**
     - A collection of related components that provide a specific capability to the platform. Features are defined by Feature Requirements and Feature Architecture.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Feature Architecture**
     - The design specification that defines how a feature is structured, including its components, interfaces, and logical architecture interfaces.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Feature Integration Tests**
     - Verification tests that verifies feature requirements and architecture, ensuring proper integration of multiple components within the feature.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Feature Requirements**
     - Specifications defining what a feature must accomplish, derived from higher-level stakeholder requirements and allocated to components.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Feature Safety/Security Analysis**
     - Systematic analysis performed on feature architecture to verify compliance with safety and security requirements at the feature level, documenting any violations or potential faults.
     - ::ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Impact Analysis**
     - The process of evaluating the effects and consequences of proposed changes on work products.
     - :ref:`Process change management<change_management>`

   * - **Inspection**
     - A formal review of work products supported by a checklist with documented conduct and outcome. Inspections verify quality and compliance of requirements, architecture, and implementation.
     - ::ref:`Review concept<review_concept>`

   * - **Logical Architecture Interfaces**
     - Abstract interfaces defined at the feature level that specify how components communicate and interact within a feature.
     - ::ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Maintenance Phase**
     - Development phase following the first major release, where released features and components are maintained. Triggered by problem reports requiring fixes.
     - :ref:`Lifecycle concept<general_concepts_lifecycle>`

   * - **Module**
     - An synonym term for Dependable Element
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Module Team**
     - Cross-functional team responsible for all artifacts within a Module, including development, quality, safety, and security activities.
     - :ref:`Roles<roles>`

   * - **Platform**
     - The complete software platform consisting of features, components, and supporting infrastructure.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Platform Integration Tests**
     - Verification tests performed on reference hardware platforms to test stakeholder requirements and overall platform functionality.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Platform Safety/Security Analysis**
     - Systematic analysis of the complete platform architecture to verify compliance with stakeholder-level safety and security requirements, documenting any violations or potential faults.
     - ::ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Problem Report**
     - A report documenting issues found in released features or components, including bugs, quality issues, or safety/security anomalies. Initiates the Maintenance Phase.
     - :ref:`Workflows<workflows>`

   * - **Project Lead**
     - Executive role responsible for strategic decisions, approving feature requests, performing project management, and high-level coordination between software modules.
     - :ref:`Roles<roles>`

   * - **Quality Manager**
     - Role responsible for quality assurance, process compliance, work product reviews, quality audits, and continuous process improvement.
     - :ref:`Process quality management<quality_management>`

   * - **Role**
     - A defined position within the project with specific responsibilities, authorities, and required competencies. Examples include Project Lead, Developer, Tester, Safety Manager.
     - :ref:`Roles<roles>`

   * - **Safety Element out of Context (SEooC)**
     - A software element developed and analyzed independently but intended to be integrated into specific applications, as defined by functional safety standards.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Safety Manager**
     - Role responsible for ensuring functional safety compliance (e.g., ISO 26262), conducting safety analyses, approving safety work products, and providing safety guidance.
     - :ref:`Process safety management<process_safety_management>`

   * - **Security Manager**
     - Role responsible for security management, vulnerability handling, cybersecurity compliance (e.g., ISO SAE 21434), and security analysis approvals.
     - :ref:`Process security management<security_management>`

   * - **Source Code**
     - The actual implementation of a Unit, typically written in a programming language and version-controlled in the repository.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Stakeholder Requirements**
     - High-level requirements specified at the platform level that define what the platform must accomplish for its intended users.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **SW Platform Assumptions of Use**
     - Constraints and conditions defined at the platform level that must be considered by users integrating the platform into their applications.
     - :ref:`Building blocks concept<general_concepts_building_blocks>`

   * - **Traceability**
     - The documented relationship between work products at different levels (requirements, architecture, design, code, tests) enabling impact analysis and coverage determination.
     - :ref:`Traceability concept<general_concepts_traceability>`

   * - **Unit**
     - The lowest level in the building blocks model, representing source code that implements a specific function or feature. Units are verified through Unit Tests.
     - :ref:`Implementation process<implementation>`

   * - **Unit Tests**
     - Verification tests that verifies the detailed design and implementation of individual Units.
     - :ref:`Verification process<process_verification>`

   * - **Verification**
     - The process of confirming that work products (requirements, architecture, design, code) correctly implement and satisfy higher-level specifications through testing and analysis.
     - :ref:`Verification process<process_verification>`

   * - **Work Product**
     - Any tangible output produced during development, including requirements, architecture documents, design specifications, source code, test cases, and analysis reports.
     - :ref:`Work products<work_products>`

   * - **Workflow**
     - A defined sequence of activities with inputs, outputs, responsible roles, and supporting guidance. Workflows form the central building blocks of the process description.
     - :ref:`Workflows<workflows>`
