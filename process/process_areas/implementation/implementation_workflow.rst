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

.. _workflow_implementation:

Implementation Workflows
########################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

.. workflow:: Create/Maintain Software Development Plan
   :id: wf__sw_development_plan
   :status: valid
   :version: 1
   :tags: implementation
   :responsible: rl__committer[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__platform_mgmt[version==1]
   :output: wp__sw_development_plan[version==1]
   :contains: gd_temp__software_development_plan[version==1]
   :has: doc_concept__imp_concept[version==1], doc_getstrt__imp_getstrt[version==1]

   The Software Development Plan shall describe
     - Design and programming language selection
     - Guidelines for design and coding
     - Development tools

.. workflow:: Create/Maintain Implementation
   :id: wf__sw_detailed_design
   :status: valid
   :version: 1
   :tags: implementation
   :responsible: rl__contributor[version==1]
   :approved_by: rl__committer[version==1]
   :input: wp__requirements_comp[version==1], wp__component_arch[version==1], wp__sw_development_plan[version==1]
   :output: wp__sw_implementation[version==1]
   :contains: gd_temp__detailed_design[version==1]
   :has: doc_concept__imp_concept[version==1], doc_getstrt__imp_getstrt[version==1]

   The implementation is created, consisting of
     - Detailed Design
     - Unit
     - Interface

.. workflow:: Verify Implementation
   :id: wf__sw_verify_implementation
   :status: valid
   :version: 1
   :tags: implementation
   :responsible: rl__committer[version==1]
   :approved_by: rl__committer[version==1]
   :input: wp__sw_implementation[version==1], wp__sw_development_plan[version==1]
   :output: wp__issue_track_system[version==1], wp__sw_implementation_inspection[version==1], wp__verification_module_ver_report[version==1]
   :contains: gd_chklst__impl_inspection_checklist[version==1]
   :has: doc_concept__imp_concept[version==1], doc_getstrt__imp_getstrt[version==1]

   The Implementation Verification of the Detailed Design and Code consists of the following topics
     - Detailed Design and Code Inspection
     - Static and Dynamic Code Analysis performed by a tool. Acceptance criteria are defined in the Verification Plan :need:`gd_temp__verification_plan`.


RAS(IC) for Implementation:
***************************

.. needtable:: RASIC Overview for Implementation
   :tags: implementation
   :filter: "implementation" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
