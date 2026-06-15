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
   :version: 1
   :tags: process_management
   :complies: std_req__iso26262__management_5421[version==1],
              std_req__iso26262__management_5422[version==1],
              std_req__iso26262__management_5426[version==1],
              std_req__aspice_40__gp-311[version==1],
              std_req__aspice_40__iic-10-00[version==1],
              std_req__aspice_40__iic-15-54[version==1],
              std_req__aspice_40__gp-211[version==1],
              std_req__aspice_40__gp-212[version==1],
              std_req__aspice_40__gp-213[version==1],
              std_req__aspice_40__gp-214[version==1],
              std_req__aspice_40__gp-215[version==1],
              std_req__aspice_40__gp-216[version==1],
              std_req__aspice_40__gp-224[version==1],
              std_req__aspice_40__gp-312[version==1],
              std_req__aspice_40__gp-313[version==1],
              std_req__aspice_40__gp-314[version==1],
              std_req__aspice_40__gp-321[version==1],
              std_req__aspice_40__gp-322[version==1],
              std_req__aspice_40__gp-323[version==1],
              std_req__aspice_40__gp-324[version==1]

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
`Issue Template Improvement <https://github.com/eclipse-score/.github/blob/main/.github/ISSUE_TEMPLATE/4_Task.yml>`_.

The potential improvement is discussed during the public Process Community Meetings
and if decided to implement, a pull request to follow :ref:`pm_create_maintain_strategy`
or :ref:`pm_define_approve_process_description` must be created.


Tailoring
=========
.. gd_guidl:: IIC Requirements Tailored
   :id: gd_guidl__iic_req_tailored
   :status: valid
   :version: 1
   :complies: std_req__aspice_40__iic-01-53[version==1],
              std_req__aspice_40__iic-01-54[version==1],
              std_req__aspice_40__iic-02-01[version==1],
              std_req__aspice_40__iic-03-06[version==1],
              std_req__aspice_40__iic-03-51[version==1],
              std_req__aspice_40__iic-03-53[version==1],
              std_req__aspice_40__iic-04-02[version==1],
              std_req__aspice_40__iic-04-51[version==1],
              std_req__aspice_40__iic-06-51[version==1],
              std_req__aspice_40__iic-07-04[version==1],
              std_req__aspice_40__iic-07-05[version==1],
              std_req__aspice_40__iic-07-06[version==1],
              std_req__aspice_40__iic-07-08[version==1],
              std_req__aspice_40__iic-07-51[version==1],
              std_req__aspice_40__iic-07-61[version==1],
              std_req__aspice_40__iic-07-62[version==1],
              std_req__aspice_40__iic-07-63[version==1],
              std_req__aspice_40__iic-07-64[version==1],
              std_req__aspice_40__iic-08-54[version==1],
              std_req__aspice_40__iic-08-61[version==1],
              std_req__aspice_40__iic-08-63[version==1],
              std_req__aspice_40__iic-08-64[version==1],
              std_req__aspice_40__iic-08-65[version==1],
              std_req__aspice_40__iic-08-66[version==1],
              std_req__aspice_40__iic-11-50[version==1],
              std_req__aspice_40__iic-13-06[version==1],
              std_req__aspice_40__iic-13-09[version==1],
              std_req__aspice_40__iic-13-13[version==1],
              std_req__aspice_40__iic-13-14[version==1],
              std_req__aspice_40__iic-13-18[version==1],
              std_req__aspice_40__iic-13-25[version==1],
              std_req__aspice_40__iic-13-50[version==1],
              std_req__aspice_40__iic-13-55[version==1],
              std_req__aspice_40__iic-15-57[version==1],
              std_req__aspice_40__iic-15-58[version==1],
              std_req__aspice_40__iic-16-00[version==1],
              std_req__aspice_40__iic-16-06[version==1],
              std_req__aspice_40__iic-16-50[version==1],
              std_req__aspice_40__iic-16-52[version==1],
              std_req__aspice_40__iic-17-05[version==1],
              std_req__aspice_40__iic-17-55[version==1],
              std_req__aspice_40__iic-18-00[version==1],
              std_req__aspice_40__iic-18-58[version==1],
              std_req__aspice_40__iic-18-59[version==1],
              std_req__aspice_40__iic-18-70[version==1],
              std_req__aspice_40__iic-18-80[version==1],
              std_req__aspice_40__iic-18-81[version==1],
              std_req__aspice_40__iic-19-01[version==1],
              std_req__aspice_40__iic-19-50[version==1]

   This part of the guideline links to all the information item characteristics (IIC) which are not fulfilled by the
   current process description. Make sure these are tailored out in the safety/security/quality plans
   for your project (documented in the PMP). Reasoning given below must be confirmed there.

   The reasoning is:

   - For Machine Learning related IICs, as the project does not develop ML components so far.
   - For IICs related to hardware development, as the project does not develop hardware components so far.
   - For IICs concerning commitment, agreements, organizational processes, as these are not in the scope of the current project.
   - For IICs concerning GPs (2 and 3), at the are not addressed yet in the current project phase or higher, which are out of scope for the current project phase.
   - For IICs concerning specific techniques or methods not used in the current project.
