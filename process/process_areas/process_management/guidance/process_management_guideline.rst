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


Guideline
#########

.. gd_guidl:: Process Management Guideline
   :id: gd_guidl__process_management
   :status: valid
   :tags: process_management
   :complies: std_req__iso26262__management_5421, std_req__iso26262__management_5422, std_req__aspice_40__gp-311, std_req__aspice_40__iic-10-00, std_req__aspice_40__iic-15-54

This document describes the general guidances for Process Management based on the concept which is defined :need:`[[title]]<doc_concept__process_management>`.

General Hints
=============

The detailed implementation of all process areas defined in the process description for
the project shall be described in the
:ref:`Workflow Platform Management <workflow_platform_management>`.

Templates
---------

The process and strategy description shall use the following templates:
:ref:`process_management_templates`.

Requirements
------------

For the process descriptions the following mandatory requirements exist:

.. needtable:: Overview of mandatory process description requirements
   :tags: process_management
   :filter: "mandatory" in tags and "attribute" in tags and "process_management" in tags and is_external == False
   :style: table
   :columns: title
   :colwidths: 30


.. _workflow_process_management_requirements:


Activities for Process Management
=================================

This section describes in detail which steps need to be performed for the process
Management.

.. list-table:: Activities for Process Management
   :header-rows: 1
   :widths: 10,60,30,30

   * - Step
     - Description
     - Responsible
     - Approver
   * - :ref:`1. <pm_create_maintain_strategy>`
     - Create/Maintain Process Management Strategy
     - :need:`[[title]] <rl__contributor>`
     - :need:`[[title]] <rl__process_community>`
   * - :ref:`2. <pm_define_approve_process_description>`
     - Define/Approve Process Description
     - :need:`[[title]] <rl__contributor>`
     - :need:`[[title]] <rl__process_community>`
   * - :ref:`3. <pm_monitor_improve_process>`
     - Monitor/Control Process Implementation
     - :need:`[[title]] <rl__contributor>`
     - :need:`[[title]] <rl__process_community>`


.. _pm_create_maintain_strategy:

Create/Maintain Process Strategy
--------------------------------

:need:`[[title]] <rl__contributor>` (as author, submitter) creates and maintains the
process management strategy. They create Pull request (PR) for contributions.

The potential contribution is discussed during the public Process Community Meetings
or standard pull request reviews and if decided to implement,
:need:`[[title]] <rl__process_community>` approves the Pull Request to include
the contribution in the process strategy.


.. _pm_define_approve_process_description:

Define/Approve Process Description
----------------------------------

:need:`[[title]] <rl__contributor>` (as author, submitter) creates and maintains the
process description. They create Pull request (PR) for contributions.

The potential contribution is discussed during the public Process Community Meetings
or standard pull request reviews and if decided to implement,
:need:`[[title]] <rl__process_community>` approves the Pull Request to include
the contribution in the process description.

.. _pm_monitor_improve_process:

Monitor/Improve Process
-----------------------

If potential improvements are detected, the :need:`[[title]] <rl__contributor>` triggers
an ISSUE for improvement by using the
`Issue Template Improvement <https://github.com/eclipse-score/process_description/blob/main/.github/ISSUE_TEMPLATE/2-improvement.yml>`_.

The potential improvement is discussed during the public Process Community Meetings
and if decided to implement, a pull request to follow :ref:`pm_create_maintain_strategy`
or :ref:`pm_define_approve_process_description` must be created.


Tailoring
=========
.. gd_guidl:: IIC Requirements Tailored
   :id: gd_guidl__iic_req_tailored
   :status: valid
   :complies: std_req__aspice_40__iic-01-53, std_req__aspice_40__iic-01-54,
              std_req__aspice_40__iic-02-01,
              std_req__aspice_40__iic-03-06, std_req__aspice_40__iic-03-51, std_req__aspice_40__iic-03-53,
              std_req__aspice_40__iic-04-02, std_req__aspice_40__iic-04-51,
              std_req__aspice_40__iic-06-51,
              std_req__aspice_40__iic-07-04, std_req__aspice_40__iic-07-05, std_req__aspice_40__iic-07-06, std_req__aspice_40__iic-07-08, std_req__aspice_40__iic-07-51, std_req__aspice_40__iic-07-61, std_req__aspice_40__iic-07-62, std_req__aspice_40__iic-07-63, std_req__aspice_40__iic-07-64,
              std_req__aspice_40__iic-08-54, std_req__aspice_40__iic-08-61, std_req__aspice_40__iic-08-63, std_req__aspice_40__iic-08-64, std_req__aspice_40__iic-08-65, std_req__aspice_40__iic-08-66,
              std_req__aspice_40__iic-11-50,
              std_req__aspice_40__iic-13-06, std_req__aspice_40__iic-13-09, std_req__aspice_40__iic-13-13, std_req__aspice_40__iic-13-14, std_req__aspice_40__iic-13-18, std_req__aspice_40__iic-13-25, std_req__aspice_40__iic-13-50, std_req__aspice_40__iic-13-55,
              std_req__aspice_40__iic-15-57, std_req__aspice_40__iic-15-58,
              std_req__aspice_40__iic-16-00, std_req__aspice_40__iic-16-06, std_req__aspice_40__iic-16-50, std_req__aspice_40__iic-16-52,
              std_req__aspice_40__iic-17-05, std_req__aspice_40__iic-17-55,
              std_req__aspice_40__iic-18-00, std_req__aspice_40__iic-18-58, std_req__aspice_40__iic-18-59, std_req__aspice_40__iic-18-70, std_req__aspice_40__iic-18-80, std_req__aspice_40__iic-18-81,
              std_req__aspice_40__iic-19-01, std_req__aspice_40__iic-19-50

   This part of the guideline links to all the information item characteristics (IIC) which are not fulfilled by the
   current process description. Make sure these are tailored out in the safety/security/quality plans
   for your project (documented in the PMP). Reasoning given below must be confirmed there.

   The reasoning is:

   - For Machine Learning related IICs, as the project does not develop ML components so far.
   - For IICs related to hardware development, as the project does not develop hardware components so far.
   - For IICs concerning commitment, agreements, organizational processes, as these are not in the scope of the current project.
   - For IICs concerning GPs (2 and 3), at the are not addressed yet in the current project phase or higher, which are out of scope for the current project phase.
   - For IICs concerning specific techniques or methods not used in the current project.
