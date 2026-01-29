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

In this section a concept for the Security Management will be discussed. Inputs for this concepts
are mainly the requirements of ISO SAE 21434 Clause 5, 6 and 8.

Inputs
******

#. Stakeholders for the Security Management work products?
#. Who needs which information?
#. Which security plans do we have?
#. Which other work products of security management are important?
#. What tooling do we need?


Stakeholders for the Security Management
****************************************

#. :need:`Project Lead <rl__project_lead>`

   * is overall approver for security management activities.
   * For more details refer the role definition in :need:`Project Lead <rl__project_lead>`.

#. :need:`Security Manager <rl__security_manager>`

   * is the main responsible for the security management work products (as in :doc:`security_management_workproducts`).
     See also role definition in :doc:`security_management_roles`.

#. :need:`Security Engineer <rl__security_engineer>`

   * is the main responsible for the security management work products (as in :doc:`security_management_workproducts`).
     See also role definition in :doc:`security_management_roles`.

#. :need:`Committer <rl__committer>`

   * creates and maintains SBOM
   * reports weaknesses and vulnerabilities

#. :need:`Committer <rl__contributor>`

   * reports weaknesses and vulnerabilities

#. :need:`External Security Auditor <rl__security_external_auditor>`

   * understand activities planning, processes definition and execution (needs review, if we consider that)

#. "Distributor" (external role)

   * Use the platform in a safe and secure way.
   * Integrate the platform in their product (distribution) and security package
   * Plan this integration (also in time)
   * Qualify the SW platform as part of his product
   * Ensures that all Assumptions of use are analyzed for the project. It is recommended that these assumptions of use shall be treated as “requirements” by the the distributors and/or project system integrators.

#. :need:`Safety Manager <rl__safety_manager>`

   * Supports activities

#. :need:`Infrastructure/Tooling community <rl__infrastructure_tooling_community>`, :need:`Process community <rl__process_community>`, :need:`Process community <rl__security_team>`

   * Supports the creation and maintenance of the SBOM

Security Plans
**************

This SW platform project defines two levels of planning: platform and module. There will be one security plan on platform level and several security plans on module level (one for each module).
This is how we organize our development teams and repositories. Each of these security plan "creates" one component OoC.
The :need:`wp__platform_security_plan` exists only once and is part of the :need:`wp__platform_mgmt` of the development project.

Security Management Work Products
*********************************

Apart from the security plans the main work products of security management are (see also the link to workflows below):

* :need:`Security Manual <wp__platform_security_manual>` - the security manual defines the requirements for safe and secure usage or integration of the SW platform (or its individual modules)
* :need:`Reviews <wp__fdr_reports_security>` - on security plan, security package and security analyses, according to ISO SAE 21434 requirements
* :need:`Security Package <wp__platform_security_package>` - the security package does not contain the security argumentation. By this the development project ensures it does not take over liability for the SW platform (or its individual modules). But it enables the distributors to integrate the SW platform (or its individual modules) in their security package.

Security Management Tooling
***************************

For the security planning and security manual a “Docs-as-Code” approach is used and within that approach Id will be used for referencing.

For the activities planning (who, when) we use :need:`wp__issue_track_system` to create and manage issues, and monitor progress through a project management dashboard.

For the reporting (e.g. displaying the status of the work products) additional tooling is created (see :doc:`guidance/security_management_process_reqs`).
