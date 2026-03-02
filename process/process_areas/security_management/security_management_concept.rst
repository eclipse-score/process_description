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

.. _process_security_management:

Concept Description
###################

.. doc_concept:: Concept Description
   :id: doc_concept__security_management_process
   :status: valid
   :tags: security_management

In this section a concept for the security management will be discussed. Inputs for this concepts
are mainly the requirements of ISO SAE 21434 Clause 5, 6 and 8.

Key concept
***********
The Security Management Plan establishes a comprehensive strategy for managing all identified security activities throughout the entire project life cycle.
It ensures that these activities are executed in a systematic, effective, and repeatable manner, providing clear guidance on responsibilities, processes, and control measures.
This approach supports risk mitigation, regulatory compliance, and continuous improvement, enabling the project team to maintain secrity standards consistently from initiation to completion.

Inputs
******

#. Stakeholders for the security management work products?
#. Which security plans do we have?
#. Which other work products of security management are important?
#. What tooling do we need?


Stakeholders for the Security Management
****************************************

#. :need:`Security Manager <rl__security_manager>`

   * is the main responsible for the security management work products (as in :doc:`security_management_workproducts`).
     See also role definition in :doc:`security_management_roles`.

#. :need:`Security Engineer <rl__security_engineer>`

   * is the main responsible for the security engineering work products (as in :doc:`../security_analysis/security_analysis_workproducts`).
     See also role definition in :need:`Security Engineer <rl__security_engineer>`.

#. :need:`Project Lead <rl__project_lead>`

   * is overall approver for security management activities.
   * For more details refer the role definition in :need:`Project Lead <rl__project_lead>`.

#. :need:`Committer <rl__committer>`

   * creates and maintains SBOM
   * reports weaknesses and vulnerabilities

#. :need:`Committer <rl__contributor>`

   * reports weaknesses and vulnerabilities

#. :need:`External Security Auditor <rl__security_external_auditor>`

   * understand activities planning, processes definition and execution (needs review, if we consider that)

#. :need:`Safety Manager <rl__safety_manager>`

   * Supports activities

#. :need:`Infrastructure/Tooling community <rl__infrastructure_tooling_community>`, :need:`Process community <rl__process_community>`, :need:`Process community <rl__security_team>`

   * Supports the creation and maintenance of the SBOM

Security Plans
**************

This SW platform project defines two levels of planning: platform and module. There will be one Security Plan on platform level and several Security Plans on module level (one for each module).
This is how we organize our development teams and repositories. Each of these Security Plan "creates" one component OoC.
The :need:`wp__platform_security_plan` exists only once and is part of the :need:`wp__platform_mgmt` of the development project.

Security Management Work Products
*********************************

Apart from the security plans the main work products of security management are (see also the link to workflows below):

* :need:`Security Manual <wp__platform_security_manual>` - the Security Manual defines the requirements for safe and secure usage or integration of the SW platform (or its individual modules)
* :need:`Reviews <wp__fdr_reports_security>` - on Security Plan, Security Package and Security Analyses, according to ISO SAE 21434 requirements
* :need:`Security Package <wp__platform_security_package>` - the Security Package does not contain the security argumentation. By this the development project ensures it does not take over liability for the SW platform (or its individual modules). But it enables the distributors to integrate the SW platform (or its individual modules) in their Security Package.

Security Management Tooling
***************************

For the security planning and security manual a “docs-as-code” approach is used and within that approach Id will be used for referencing.

For the activities planning (who, when) we use :need:`wp__issue_track_system` to create and manage issues, and monitor progress through a project management dashboard.

Also, refer :need:`wf__mr_sec_analyses` for the monitoring of security analyses.

For the reporting (e.g. displaying the status of the work products) additional tooling is created (see :doc:`guidance/security_management_process_reqs`).
