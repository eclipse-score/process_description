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

.. _process_management_workflows:

Process Management Workflows
############################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

.. workflow:: Create/Maintain Process Management Strategy
   :id: wf__cr_mt_process_mgt_strategy
   :status: valid
   :version: 1
   :responsible: rl__contributor[version==1]
   :approved_by: rl__process_community[version==1]
   :supported_by: rl__safety_external_auditor[version==1], rl__security_external_auditor[version==1], rl__project_lead[version==1]
   :input: wp__policies[version==1], wp__issue_track_system[version==1]
   :output: wp__process_strategy[version==1], wp__policies[version==1]
   :contains: gd_guidl__process_management[version==1], gd_temp__process_workflow[version==1]
   :has: doc_concept__process_management[version==1], doc_getstrt__process_management[version==1]

   The process management strategy is created and maintained. Policies are
   reviewed and updated, if required.

.. workflow:: Define/Approve Process Description
   :id: wf__def_app_process_description
   :status: valid
   :version: 1
   :responsible: rl__contributor[version==1]
   :approved_by: rl__process_community[version==1]
   :supported_by: rl__safety_external_auditor[version==1], rl__security_external_auditor[version==1], rl__project_lead[version==1]
   :input: wp__process_strategy[version==1], wp__issue_track_system[version==1]
   :output: wp__process_description[version==1], wp__tailoring_work_products[version==1]
   :contains: gd_guidl__process_management[version==1], gd_temp__process_workflow[version==1]
   :has: doc_concept__process_management[version==1], doc_getstrt__process_management[version==1]

   The process description is defined and approved.

.. workflow:: Monitor/Improve Process Implementation
   :id: wf__mon_imp_process_description
   :status: valid
   :version: 1
   :responsible: rl__contributor[version==1]
   :approved_by: rl__process_community[version==1]
   :supported_by: rl__safety_external_auditor[version==1], rl__security_external_auditor[version==1], rl__project_lead[version==1]
   :input: wp__process_description[version==1]
   :output: wp__process_impr_report[version==1], wp__issue_track_system[version==1]
   :contains: gd_guidl__process_management[version==1], gd_temp__process_workflow[version==1]
   :has: doc_concept__process_management[version==1], doc_getstrt__process_management[version==1]

   The process strategy and description implementation is monitored and improvements are
   triggered, if required.


.. needextend:: docname is not None and "process_areas/process_management" in docname
   :+tags: process_management

RAS(IC) for Process Management:
*******************************

.. needtable:: RASIC Overview for Process Management
   :tags: process_management
   :filter: "process_management" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
