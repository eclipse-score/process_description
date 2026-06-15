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

.. _requirements_workflows:

Requirements Engineering Workflows
##################################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.


.. workflow:: Create/Maintain Stakeholder requirements and SW-Platform AoU
   :id: wf__req_stkh_req
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__contributor[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1]
   :input: wp__policies[version==1], wp__issue_track_system[version==1]
   :output: wp__requirements_stkh[version==1], wp__requirements_sw_platform_aou[version==1]
   :contains: gd_temp__req_stkh_req[version==1], gd_temp__req_formulation[version==1]
   :has: doc_concept__req_process[version==1], doc_getstrt__req_process[version==1]

   Stakeholder requirements and SW-Platform Assumptions of Use (AoU) can be created during a change request.
   Any contributor can create a stakeholder requirement (or AoU) and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: wf__req_feat_req
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__contributor[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__requirements_stkh[version==1], wp__issue_track_system[version==1]
   :output: wp__requirements_feat[version==1]
   :contains: gd_temp__req_feat_req[version==1], gd_temp__req_formulation[version==1]
   :has: doc_concept__req_process[version==1], doc_getstrt__req_process[version==1]

   Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a project lead. If needed safety and security managers can provide support.

.. workflow:: Create/Maintain Feature AoUs
   :id: wf__req_feat_aou
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__contributor[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__requirements_feat[version==1], wp__feature_arch[version==1], wp__issue_track_system[version==1]
   :output: wp__requirements_feat_aou[version==1], wp__platform_safety_manual[version==1]
   :contains: gd_temp__req_aou_req[version==1], gd_temp__req_formulation[version==1]
   :has: doc_concept__req_process[version==1], doc_getstrt__req_process[version==1]

   Based on the safety concept on feature level, feature AoUs can be derived. See also :ref:`aou_workflow`

.. workflow:: Create/Maintain Component requirements
   :id: wf__req_comp_req
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__requirements_feat[version==1], wp__issue_track_system[version==1]
   :output: wp__requirements_comp[version==1]
   :contains: gd_temp__req_comp_req[version==1], gd_temp__req_formulation[version==1]
   :has: doc_concept__req_process[version==1], doc_getstrt__req_process[version==1]

.. workflow:: Create/Maintain Component AoUs
   :id: wf__req_comp_aou
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__requirements_comp[version==1], wp__component_arch[version==1], wp__issue_track_system[version==1]
   :output: wp__requirements_comp_aou[version==1], wp__module_safety_manual[version==1]
   :contains: gd_temp__req_aou_req[version==1], gd_temp__req_formulation[version==1]
   :has: doc_concept__req_process[version==1], doc_getstrt__req_process[version==1]

   Based on the safety concept on component level, component AoUs can be derived. See also :ref:`aou_workflow`

.. workflow:: Create/Maintain Tool Requirements
   :id: wf__req_tool
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__process_description[version==1]
   :output: wp__requirements_proc_tool[version==1]
   :contains: gd_temp__req_tool_req[version==1], gd_temp__req_formulation[version==1]
   :has: doc_concept__req_process[version==1], doc_getstrt__req_process[version==1]

   Based on the process descriptions (which comply to standards) and/or stakeholder/feature/component requirements tool requirements are derived.

.. workflow:: Monitor/Verify Requirements
   :id: wf__monitor_verify_requirements
   :status: valid
   :version: 1
   :tags: requirements_engineering
   :responsible: rl__committer[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1]
   :input: wp__requirements_stkh[version==1],
           wp__requirements_feat[version==1],
           wp__requirements_comp[version==1],
           wp__requirements_feat_aou[version==1],
           wp__requirements_comp_aou[version==1],
           wp__platform_safety_manual[version==1],
           wp__module_safety_manual[version==1]
   :output: wp__issue_track_system[version==1], wp__requirements_inspect[version==1]
   :contains: gd_chklst__req_inspection[version==1]

   The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in version management tool.


RAS(IC) for Requirements Engineering:
*************************************

.. needtable:: RASIC Overview for Requirements Engineering
   :tags: requirements_engineering
   :filter: "requirements_engineering" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
