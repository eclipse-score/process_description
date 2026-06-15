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

.. _workflow_platform_management:

Platform Management Workflows
#############################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

.. workflow:: Create/Maintain Platform Management Plan
   :id: wf__platform_cr_mt_platform_mgmt_plan
   :status: valid
   :version: 1
   :tags: platform_management
   :responsible: rl__project_lead[version==1]
   :approved_by: rl__process_community[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1], rl__quality_manager[version==1]
   :input: wp__policies[version==1], wp__issue_track_system[version==1]
   :output: wp__platform_mgmt[version==1],
            wp__project_mgt[version==1],
            wp__document_mgt_plan[version==1],
            wp__config_mgt_plan[version==1],
            wp__prm_plan[version==1],
            wp__tlm_plan[version==1],
            wp__chm_plan[version==1]
   :contains: gd_temp__platform_mgmt_plan[version==1],
              gd_guidl__platform_mgmt_plan[version==1],
              gd_guidl__documentation[version==1],
              gd_chklst__documentation_review[version==1],
              gd_temp__documentation[version==1]
   :has: doc_concept__platform_process[version==1], doc_getstrt__platform_process[version==1]

   The Platform Management Plan shall include the plans as defined by the
   :ref:`Platform Management Plan Template <platform_templates>`.

   The project management plan should contain the scope of work, project life cycle, work packages,
   planning and monitoring approaches, project schedule, escalation and communication path.

.. workflow:: Monitor/Improve Platform Management Plan
   :id: wf__platform_mr_im_platform_mgmt_plan
   :status: valid
   :version: 1
   :tags: platform_management
   :responsible: rl__project_lead[version==1]
   :approved_by: rl__process_community[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1], rl__quality_manager[version==1]
   :input: wp__platform_mgmt[version==1],
           wp__project_mgt[version==1],
           wp__document_mgt_plan[version==1],
           wp__config_mgt_plan[version==1]
   :output: wp__issue_track_system[version==1]
   :contains: gd_temp__platform_mgmt_plan[version==1],
              gd_guidl__platform_mgmt_plan[version==1],
              gd_guidl__documentation[version==1],
              gd_chklst__documentation_review[version==1]
   :has: doc_concept__platform_process[version==1], doc_getstrt__platform_process[version==1]

   The :need:`Project Lead <rl__project_lead>` is responsible for the monitoring and reporting
   of the work products and activities against the platform management plan.

   The :need:`Project Lead <rl__project_lead>` is responsible to adjust the plan,
   if deviations are detected.


RAS(IC) for Platform Management:
********************************

.. needtable:: RASIC Overview for Platform Management
   :tags: platform_management
   :filter: "platform_management" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
