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

.. _arch_workflow:

Architecture Workflows
######################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

.. workflow:: Create/Maintain Platform architecture
   :id: wf__cr_mt_platarch
   :status: valid
   :version: 1
   :tags: architecture_design
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__requirements_stkh[version==1], wp__issue_track_system[version==1]
   :output: wp__platform_arch[version==1]
   :contains: gd_guidl__arch_design[version==1]
   :has: doc_concept__arch_process[version==1], doc_getstrt__arch_process[version==1]

   The platform architecture is created and maintained.

.. workflow:: Create/Maintain Feature architecture
   :id: wf__cr_mt_featarch
   :status: valid
   :version: 1
   :tags: architecture_design
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__requirements_feat[version==1], wp__issue_track_system[version==1]
   :output: wp__feature_arch[version==1]
   :contains: gd_guidl__arch_design[version==1], gd_temp__arch_feature[version==1]
   :has: doc_concept__arch_process[version==1], doc_getstrt__arch_process[version==1]

   The feature architectures are created and maintained.

.. workflow:: Create/Maintain Components architecture
   :id: wf__cr_mt_comparch
   :status: valid
   :version: 1
   :tags: architecture_design
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__feature_arch[version==1], wp__requirements_comp[version==1], wp__issue_track_system[version==1]
   :output: wp__component_arch[version==1]
   :contains: gd_guidl__arch_design[version==1], gd_temp__arch_comp[version==1]
   :has: doc_concept__arch_process[version==1], doc_getstrt__arch_process[version==1]

   The component architectures are created and maintained.

.. workflow:: Monitor/Verify Architecture
   :id: wf__mr_vy_arch
   :status: valid
   :version: 1
   :tags: architecture_design
   :responsible: rl__committer[version==1]
   :approved_by: rl__committer[version==1]
   :supported_by: rl__safety_manager[version==1], rl__security_manager[version==1]
   :input: wp__feature_arch[version==1], wp__component_arch[version==1]
   :output: wp__issue_track_system[version==1], wp__sw_arch_verification[version==1]
   :contains: gd_guidl__arch_design[version==1], gd_chklst__arch_inspection_checklist[version==1]
   :has: doc_concept__arch_process[version==1], doc_getstrt__arch_process[version==1]

   The architecture designs are monitored and verified.

   The inspection shall be implemented as integral part of the review in GitHub.

RAS(IC) for Architecture Design:
********************************

.. needtable:: RASIC Overview for Architecture Design
   :tags: architecture_design
   :filter: "architecture_design" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
