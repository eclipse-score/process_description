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

Roles
#####


.. role:: Security Manager
   :id: rl__security_manager
   :status: draft
   :tags: security_management
   :contains: rl__committer

   The Security Manager is responsible for making sure that ISO SAE 21434 is complied
   to in the project. The Security Manager shall lead and monitor the security relevant
   activities of the project.

   Required skills

   * Degree: Master's degree in electrical engineering/computer science/mathematics, or similar degree, or comparable work experience
   * Solid understanding of security management
   * Knowledge in project management
   * Deep understanding of quality criteria and the correlating methods and procedures to achieve and verify them
   * Technical know-how of embedded systems
   * Preferred training: (Automotive) Cybersecurity Specialist (CySec) or similar

   Knowledge of standards

   * ISO SAE 21434

   Experience

   * 3 years of experience in the management of security topics
   * Experience in managing projects
   * Experience in managing security weaknesses, vulnerabilities

   Responsibility

   * Creates and maintains following security artifacts at platform level: Platform Security Plan, Platform Security Package, Platform Security Manual, Platform SBOM
   * Approves following security artifacts at module: Module Security Plan, Module Security Package, Module Security Manual, Module SBOM
   * Verifies, that the preconditions for the "release for production", which are  part of the release notes, are fulfilled, and the correctness, completeness and consistency of the release notes
   * Supports reporting of security related project status
   * Reports security weaknesses, vulnerabilities
   * Coaches the project team w.r.t all questions related to security
   * Plans and approves the security audit (to be discussed, currently not in scope)
   * Plans and approves the formal security reviews
   * Approval of security analyses
   * Checks that every person in his team has sufficient security skills for their role

   Authority

   * Escalation of planning topics to the project manager defined in the Security Plan
   * Initiate the publication of a security weakness, vulnerability
   * Recommend the Release of a SW platform or a module
   * Refusing the approval of work products as defined in the workflows
   * Refusing the approval of his team's role nomination (i.e. requesting that the role will be withdrawn)

.. role:: Security External Auditor
   :id: rl__security_external_auditor
   :status: valid

   Required skills, Knowledge of security standards (ISO 21434), Experience

   * External Auditor comes from organization specialized in secrity audits and assessment, thus sufficient skill should be guaranteed by the sending organization.
   * For performing the formal document reviews also a Security Manager from another Eclipse Safety project can play the role of an external auditor, in this case the same skills apply as for the Security Manager.

   Responsibility

   * Performing and reporting of secrity audit

   Authority

   * Decision on the passing or failing of an audit
