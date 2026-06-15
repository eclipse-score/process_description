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

.. _workflow_safety_management:

Safety Management Workflows
###########################

.. workflow:: Create/Maintain Safety Plan
   :id: wf__cr_mt_safety_plan
   :status: valid
   :version: 1
   :responsible: rl__safety_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__platform_mgmt[version==1],
           wp__issue_track_system[version==1],
           wp__sw_component_class[version==1],
           wp__tailoring_work_products[version==1]
   :output: wp__module_safety_plan[version==1], wp__platform_safety_plan[version==1], wp__safety_tailoring[version==1]
   :contains: gd_guidl__saf_plan_definitions[version==1], gd_temp__feature_safety_wp[version==1], gd_temp__module_safety_plan[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | The Safety Manager is responsible for the planning and coordination of the safety activities for the platform.
   | The Safety Manager creates and maintains the safety plan.
   | For this a template exists to guide the creator of the safety plan.

.. workflow:: Create Component Classification
   :id: wf__cr_comp_class
   :status: valid
   :version: 1
   :responsible: rl__committer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :input: wp__platform_mgmt[version==1], wp__issue_track_system[version==1]
   :output: wp__sw_component_class[version==1]
   :contains: gd_guidl__component_classification[version==1], gd_temp__component_classification[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | The Safety Manager shall approve the OSS component classification performed by an expert on this component.

.. workflow:: Create/Maintain Safety Package
   :id: wf__cr_mt_safety_package
   :status: valid
   :version: 1
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :input: wp__module_safety_plan[version==1],
           wp__platform_safety_plan[version==1],
           wp__issue_track_system[version==1],
           wp__safety_tailoring[version==1]
   :output: wp__module_safety_package[version==1], wp__platform_safety_package[version==1]
   :contains: gd_guidl__saf_package[version==1], gd_temp__feature_safety_wp[version==1], gd_temp__module_safety_plan[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | The Safety Manager in the project is NOT responsible to provide the argument for the achievement of functional safety.
   | But the Safety Manager creates and maintains the safety package in the sense of a collection of safety related work products.
   | The generation and the maintenance of this draft safety package shall be automated as much as possible.
   | It does not contain the final argumentation of the safety of the product.
   | As the safety package is only a collection of work products, the safety plan (template) can be used for documentation.

.. workflow:: Perform Safety Audit
   :id: wf__p_fs_audit
   :status: valid
   :version: 1
   :responsible: rl__safety_external_auditor[version==1]
   :approved_by: rl__safety_manager[version==1]
   :input: wp__module_safety_plan[version==1],
           wp__platform_safety_plan[version==1],
           wp__module_safety_package[version==1],
           wp__platform_safety_package[version==1]
   :output: wp__audit_report[version==1]
   :contains: gd_guidl__saf_plan_definitions[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | The external auditor is responsible to perform a safety audit.
   | The Safety Manager and the process community shall support the external auditor during this.
   | The Project Manager and and the Safety Manager shall approve the audit report.

.. workflow:: Perform Formal Reviews
   :id: wf__p_formal_rv
   :status: valid
   :version: 1
   :responsible: rl__safety_manager[version==1]
   :approved_by: rl__safety_manager[version==1]
   :input: wp__module_safety_plan[version==1],
           wp__platform_safety_plan[version==1],
           wp__module_safety_package[version==1],
           wp__platform_safety_package[version==1]
   :output: wp__fdr_reports[version==1]
   :contains: gd_guidl__saf_plan_definitions[version==1], gd_chklst__safety_plan[version==1], gd_chklst__safety_package[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | An "external" safety manager is responsible the formal reviews on safety plan, safety package and safety analysis.
   | In this context "external" means that the person is not the Safety Manager of the platform/module (i.e. created or approved the respective work product).
   | The Safety Manager (of the platform/module) shall support the "external" safety manager during the reviews.
   | The Safety Manager (of the platform/module) shall approve the formal reviews.
   | Checklists exist to guide the creator of the relevant safety documents.

.. workflow:: Create/Maintain Safety Manual
   :id: wf__cr_mt_safety_manual
   :status: valid
   :version: 1
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :input: wp__requirements_feat_aou[version==1],
           wp__requirements_feat[version==1],
           wp__feature_arch[version==1],
           wp__feature_fmea[version==1],
           wp__feature_dfa[version==1],
           wp__requirements_comp_aou[version==1],
           wp__requirements_comp[version==1],
           wp__component_arch[version==1],
           wp__sw_component_fmea[version==1],
           wp__sw_component_dfa[version==1]
   :output: wp__platform_safety_manual[version==1], wp__module_safety_manual[version==1]
   :contains: gd_guidl__saf_man[version==1], gd_temp__safety_manual[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | The Safety Engineer collects the necessary input for the safety manuals on platform and module level and documents it.
   | The safety manager makes sure all items are in valid state for a release of the safety manual.
   | Also for the safety manual a template exists as a guidance.

.. workflow:: Monitor/Verify Safety
   :id: wf__mr_vy_safety
   :status: valid
   :version: 1
   :responsible: rl__safety_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__module_safety_plan[version==1],
           wp__platform_safety_plan[version==1],
           wp__module_safety_package[version==1],
           wp__platform_safety_package[version==1],
           wp__audit_report[version==1],
           wp__fdr_reports[version==1]
   :output: wp__issue_track_system[version==1], wp__module_sw_release_note[version==1], wp__platform_sw_release_note[version==1]
   :contains: gd_guidl__saf_plan_definitions[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | The Safety Manager is responsible for the monitoring of the safety activities against the safety plan.
   | The Safety Manager is responsible to verify, that the preconditions for the release, which are  part of the release notes, are fulfilled.
   | The Safety Manager is responsible to verify the correctness, completeness and consistency of the release notes.

.. workflow:: Impact Analysis of Change Request
   :id: wf__impact_analysis_change_request
   :status: valid
   :version: 1
   :responsible: rl__safety_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :input: wp__platform_mgmt[version==1],
           wp__issue_track_system[version==1],
           wp__sw_component_class[version==1],
           wp__safety_tailoring[version==1]
   :output: wp__issue_track_system[version==1]
   :contains: gd_temp__change_component_request[version==1], gd_temp__change_decision_record[version==1], gd_temp__change_impact_analysis[version==1]
   :has: doc_concept__safety_management_process[version==1], doc_getstrt__safety_management_process[version==1]

   | In accordance with ISO 26262-2:2018 section 5.2.2.3 d/e (Impact Analysis), the project implements a dedicated workflow for analyzing change requests.
   | The Safety Manager is responsible for ensuring that each change request is analyzed for its impact on safety, as required by ISO 26262-2:2018.
   | Impact analysis is performed at the element level (e.g., module or component) rather than the item (system) level, reflecting the modular architecture of the platform. This tailoring is documented in the safety plan and justified by the project structure and scope.
   | The analysis includes:
   |   - Reviewing the change request and its context
   |   - Assessing the impact on affected elements, safety requirements, and work products
   |   - Documenting the rationale for decisions regarding acceptance, implementation, or rejection of the change
   | The outcome is a change impact analysis report and a documented decision, which are reviewed and approved as part of the Safety Management process.


.. needextend:: docname is not None and "process_areas/safety_management" in docname
   :+tags: safety_management

RAS(IC) for Safety Management:
******************************

.. needtable:: RASIC Overview for Safety Management
   :tags: safety_management
   :filter: "safety_management" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
