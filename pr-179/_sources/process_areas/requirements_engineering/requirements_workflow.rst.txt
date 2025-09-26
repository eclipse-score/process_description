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


Workflow Requirements Engineering
#################################

.. workflow:: Create/Maintain Stakeholder requirements
   :id: wf__req_stkh_req
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager
   :input: wp__policies, wp__issue_track_system
   :output: wp__requirements_stkh
   :contains: gd_temp__req_stkh_req, gd_temp__req_formulation
   :has: doc_concept__req_process, doc_getstrt__req_process

   Stakeholder requirements can be created during a change request. Any contributor can create a stakeholder requirement and propose it for approval.

.. workflow:: Create/Maintain Feature requirements
   :id: wf__req_feat_req
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__contributor
   :approved_by: rl__technical_lead
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__requirements_stkh, wp__issue_track_system
   :output: wp__requirements_feat, wp__requirements_feat_aou, wp__platform_safety_manual
   :contains: gd_temp__req_feat_req, gd_temp__req_formulation
   :has: doc_concept__req_process, doc_getstrt__req_process

   Depending on the stakeholder requirements feature requirements can be derived. This can be done by any contributor and will be approved by a contributor. If needed safety and security managers can provide support.


.. workflow:: Create/Maintain Component requirements
   :id: wf__req_comp_req
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__contributor
   :approved_by: rl__committer
   :supported_by: rl__safety_manager, rl__security_manager
   :input: wp__requirements_feat, wp__issue_track_system
   :output: wp__requirements_comp, wp__requirements_comp_aou, wp__platform_safety_manual
   :contains: gd_temp__req_comp_req, gd_temp__req_formulation
   :has: doc_concept__req_process, doc_getstrt__req_process

   On the lowest level the component requirements are created and maintained. This can be done by any contributor and will be approved by a committer. If needed safety and security managers can provide support.

.. workflow:: Monitor/Verify Requirements
   :id: wf__monitor_verify_requirements
   :status: valid
   :tags: requirements_engineering
   :responsible: rl__committer
   :approved_by: rl__committer
   :supported_by: rl__safety_manager
   :input: wp__requirements_stkh, wp__requirements_feat, wp__requirements_comp, wp__requirements_feat_aou, wp__requirements_comp_aou, wp__platform_safety_manual, wp__module_safety_manual
   :output: wp__issue_track_system, wp__requirements_inspect
   :contains: gd_chklst__req_inspection

   The requirements are monitored and verified. The inspection shall be implemented as integral part of the review in GitHub.
