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

.. _quality_workflows:

Quality Management Workflows
############################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.


.. workflow:: Create/Maintain Quality Management Plan
   :id: wf__cr_mt_qlm_plan
   :status: valid
   :version: 1
   :responsible: rl__quality_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by:
   :input: wp__policies[version==1], wp__issue_track_system[version==1], wp__platform_mgmt[version==1]
   :output: wp__qms_plan[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1], gd_temp__qlm_plan[version==1]
   :has: doc_concept__quality_process[version==1], doc_getstrt__quality_process[version==1]

   | The Quality Management Plan is created and maintained by the :need:`rl__quality_manager`.

.. workflow:: Execute Platform Process Audit
   :id: wf__exe_pltprocess_audit
   :status: valid
   :version: 1
   :responsible: rl__quality_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__qms_plan[version==1], wp__process_description[version==1]
   :output: wp__process_impr_report[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1], gd_chklst__review_checklist[version==1]
   :has: doc_concept__quality_process[version==1], doc_getstrt__quality_process[version==1]

   | The project/platform processes are audited.

.. workflow:: Execute Feature Contribution Conformance Checks
   :id: wf__exe_featprocess_conformance_checks
   :status: valid
   :version: 1
   :responsible: rl__quality_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__qms_plan[version==1], wp__feat_request[version==1], wp__process_description[version==1]
   :output: wp__qms_report[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1], gd_chklst__review_checklist[version==1]
   :has: doc_concept__quality_process[version==1], doc_getstrt__quality_process[version==1]

   | The conformance of the feature contribution is checked. The conformance check consists of
   | * No open issues that are related to quality that are relevant for the feature contribution
   | * All required work products are provided and fulfill the quality criteria as defined in :need:`wp__qms_plan`
   | * Work product reviews are performed and passed for all required work products as defined in :need:`wp__qms_plan`
   | * Quality management plan is up to date and reflects the current state of the :need:`wp__platform_mgmt`

.. workflow:: Execute Work Product Reviews
   :id: wf__exe_wp_review
   :status: valid
   :version: 1
   :responsible: rl__quality_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__committer[version==1]
   :input: wp__qms_plan[version==1], wp__process_description[version==1]
   :output: wp__verification_platform_ver_report[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1], gd_chklst__review_checklist[version==1], gd_guidl__wp_review[version==1]
   :has: doc_concept__quality_process[version==1], doc_getstrt__quality_process[version==1]

   | The quality of the work products is assured.

.. workflow:: Consult and Execute Quality Trainings
   :id: wf__consult_exe_qly_training
   :status: valid
   :version: 1
   :responsible: rl__quality_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__qms_plan[version==1], wp__policies[version==1], wp__process_description[version==1]
   :output: wp__training_path[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1]
   :has: doc_concept__quality_process[version==1], doc_getstrt__quality_process[version==1]

   | The :need:`rl__quality_manager` consults all project/platform stakeholder as defined in :need:`doc_concept__quality_process` for quality topics and executes regularly quality trainings.

.. workflow:: Monitor/Improve Quality Activities
   :id: wf__mr_imp_qlm_plan_processes
   :status: valid
   :version: 1
   :responsible: rl__quality_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__qms_plan[version==1],
           wp__platform_sw_release_note[version==1],
           wp__module_sw_release_note[version==1],
           wp__process_impr_report[version==1],
           wp__qms_report[version==1],
           wp__verification_platform_ver_report[version==1],
           wp__verification_module_ver_report[version==1],
           wp__training_path[version==1]
   :output: wp__issue_track_system[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1], gd_chklst__review_checklist[version==1], gd_req__quality_report[version==1]
   :has: doc_concept__quality_process[version==1], doc_getstrt__quality_process[version==1]

   | The :need:`rl__quality_manager` is responsible for the monitoring of the activities against the quality management plan.
   | The :need:`rl__quality_manager` is responsible to adjust the quality management plan, if deviations are detected.


.. needextend:: docname is not None and "process_areas/quality_management" in docname
   :+tags: quality_management

RAS(IC) for Safety Analysis
***************************

.. needtable:: RASIC Overview for Quality Management
   :tags: quality_management
   :filter: "quality_management" in tags and type == "workflow"
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
