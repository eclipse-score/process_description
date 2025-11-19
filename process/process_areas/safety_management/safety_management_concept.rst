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

Concept
-------

.. doc_concept:: Safety Management Concept
   :id: doc_concept__safety_management_process
   :status: valid

In this section a concept for the safety management will be discussed.
Inputs for this concepts are mainly the requirements of ISO26262 "Part 2: Management of functional safety".

Key concept
^^^^^^^^^^^
The Safety Management Plan should define the strategy to manage the identified safety activities
in an effective and repeatable way for the project life cycle.

Inputs
^^^^^^

#. Stakeholders for the safety management work products?
#. Who needs which information?
#. Which safety plans do we have?
#. Which other work products of safety management are important?
#. What tooling do we need?

Stakeholders
^^^^^^^^^^^^

#. :need:`Project Lead <rl__project_lead>`

   * planning of development for module and for platform projects
   * status reporting of safety activities

#. :need:`Safety Manager <rl__safety_manager>`

   * main responsible for the safety management work products
   * role definition in :doc:`roles`

#. :need:`External Auditor <rl__external_auditor>`

   * understand activities planning, processes definition and execution

#. "Distributor" (external role)

   * use the platform in a safe way
   * integrate the platform in his product (distribution) and safety case
   * plan this integration (also in time)
   * qualify the SW platform as part of his product

Safety Plans
^^^^^^^^^^^^

This SW platform project defines two levels of planning: platform and module. There will be one safety plan on platform level and several safety plans on module level (one for each module).
This is how we organize our development teams and repositories. Each of these safety plan "creates" one SEooC.
The Platform Safety Plan exists only once and is part of the Platform Management Plan of S-CORE.

Safety Management Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Apart from the safety plans the main work products of safety management are:

* :need:`Safety Manual <wp__platform_safety_manual>` - the safety manual defines the requirements for safe usage or integration of the SW platform (or its individual modules)
* :need:`Confirmation Reviews <wp__fdr_reports>` - on safety plan, safety package and safety analyses, according to ISO 26262 requirements
* :need:`Safety Package <wp__platform_safety_package>` - the safety package does not contain the safety argumentation. By this the S-CORE project ensures it does not take over liability for the SW platform (or its individual modules). But it enables the distributors to integrate the SW platform (or its individual modules) in their safety package.

Safety Management Tooling
^^^^^^^^^^^^^^^^^^^^^^^^^

For the safety planning and safety manual, `sphinx-needs <https://www.sphinx-needs.com/>`_ will be used for referencing.

For the activities planning (who, when) we use `GitHub issues <https://github.com/features/issues>`_ and monitor these in GitHub projects.

For the reporting (e.g. displaying the status of the work products) additional tooling is created.

Guidance
^^^^^^^^

The safety management guideline can be found in the guidance section.
