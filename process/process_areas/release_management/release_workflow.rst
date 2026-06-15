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

.. _release_workflows:

Release Management Workflows
############################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

.. workflow:: Create/Maintain Module Release Note
   :id: wf__rel_mod_rel_note
   :status: valid
   :version: 1
   :responsible: rl__committer[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__module_safety_package[version==1], wp__module_sw_release_plan[version==1], wp__verification_module_ver_report[version==1]
   :output: wp__module_sw_release_note[version==1]
   :contains: gd_temp__rel_mod_rel_note[version==1], gd_guidl__rel_management[version==1]
   :has: doc_concept__rel_process[version==1], doc_getstrt__release_process[version==1]

   The module release note is created for each release by the committer acting as the module lead.
   It may be updated later in case of bugs are found after the release is published.

.. workflow:: Create/Maintain Platform Release Note
   :id: wf__rel_platform_rel_note
   :status: valid
   :version: 1
   :responsible: rl__project_lead[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__platform_safety_package[version==1], wp__platform_sw_release_plan[version==1], wp__verification_platform_ver_report[version==1]
   :output: wp__platform_sw_release_note[version==1]
   :contains: gd_temp__rel_plat_rel_note[version==1], gd_guidl__rel_management[version==1]
   :has: doc_concept__rel_process[version==1], doc_getstrt__release_process[version==1]

   The platform release note is prepared and approved by the project lead circle.
   It may be updated later in case of bugs found after the release is published.

.. workflow:: Plan Module Release
   :id: wf__rel_mod_rel_plan
   :status: valid
   :version: 1
   :responsible: rl__committer[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__issue_track_system[version==1], wp__platform_mgmt[version==1]
   :output: wp__module_sw_release_plan[version==1]
   :contains: gd_temp__rel_issue[version==1], gd_guidl__rel_management[version==1]
   :has: doc_concept__rel_process[version==1], doc_getstrt__release_process[version==1]

   The module release plan is created as part of the modules planning and documented as part of the module's project planning.

.. workflow:: Plan Platform Release
   :id: wf__rel_plat_rel_plan
   :status: valid
   :version: 1
   :responsible: rl__project_lead[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__issue_track_system[version==1], wp__platform_mgmt[version==1]
   :output: wp__platform_sw_release_plan[version==1]
   :contains: gd_temp__rel_issue[version==1], gd_guidl__rel_management[version==1]
   :has: doc_concept__rel_process[version==1], doc_getstrt__release_process[version==1]

   The platform release plan is created as part of the project planning and documented in the platform management plan.


.. workflow:: Create/Maintain Platform Handbook
   :id: wf__rel_platform_handbook
   :status: valid
   :version: 1
   :responsible: rl__project_lead[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__platform_safety_package[version==1], wp__platform_sw_release_plan[version==1], wp__verification_platform_ver_report[version==1]
   :output: wp__platform_handbook[version==1]
   :contains: gd_guidl__rel_handbook[version==1]
   :has: doc_concept__rel_process[version==1], doc_getstrt__release_process[version==1]

   The platform handbook is prepared and approved by the project lead circle.
   It may be updated later in case of bugs found after the release is published.


.. workflow:: Verify/Approve Module Release
   :id: wf__vy_ap_modrelease
   :status: valid
   :version: 1
   :responsible: rl__release_team[version==1]
   :approved_by: rl__project_lead[version==1], rl__quality_manager[version==1]
   :input: wp__module_sw_release_plan[version==1]
   :output: wp__module_sw_release_note[version==1]
   :contains: gd_temp__rel_mod_rel_note[version==1], gd_guidl__rel_management[version==1]
   :has: doc_concept__rel_process[version==1], doc_getstrt__release_process[version==1]

   | The module release is verified and approved.


.. workflow:: Verify/Approve Platform Release
   :id: wf__vy_ap_pltrelease
   :status: valid
   :version: 1
   :responsible: rl__release_team[version==1]
   :approved_by: rl__project_lead[version==1], rl__quality_manager[version==1]
   :input: wp__qms_plan[version==1], wp__platform_sw_release_plan[version==1]
   :output: wp__platform_sw_release_note[version==1]
   :contains: gd_guidl__qlm_plan_definitions[version==1],
              gd_chklst__review_checklist[version==1],
              gd_temp__rel_plat_rel_note[version==1],
              gd_guidl__rel_management[version==1]
   :has: doc_concept__quality_process[version==1],
         doc_getstrt__quality_process[version==1],
         doc_concept__rel_process[version==1],
         doc_getstrt__release_process[version==1]

   | The project/platform release is verified and approved.


RAS(IC) for Release Management:
*******************************

.. needtable:: RASIC Overview for Release Management
   :tags: release_management
   :filter: "release_management" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
