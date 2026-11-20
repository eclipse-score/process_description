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

.. _workflow_security_management:

Security Management Workflows
#############################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

.. workflow:: Create/Maintain Security Plan
   :id: wf__cr_mt_security_plan
   :status: valid
   :version: 1
   :responsible: rl__security_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__safety_manager[version==1]
   :input: wp__platform_mgmt[version==1], wp__issue_track_system[version==1], wp__tailoring_work_products[version==1]
   :output: wp__module_security_plan[version==1], wp__platform_security_plan[version==1]
   :contains: gd_guidl__security_plan_definitions[version==1], gd_temp__module_security_plan[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Security Manager is responsible for the planning and coordination of the security activities for the platform/module.
   | For each item or component the Security Manager determines whether it is cybersecurity relevant, and whether it is a new development or a reuse, using the method of the standard's relevance annex.
   | The Security Manager creates and maintains the Security Plan.
   | For this a template exists to guide the creator of the Security Plan.

.. workflow:: Create/Maintain Security Package
   :id: wf__cr_mt_security_package
   :status: valid
   :version: 1
   :responsible: rl__security_engineer[version==1]
   :approved_by: rl__security_manager[version==1]
   :supported_by: rl__committer[version==1]
   :input: wp__module_security_plan[version==1], wp__platform_security_plan[version==1], wp__issue_track_system[version==1]
   :output: wp__module_security_package[version==1], wp__platform_security_package[version==1]
   :contains: gd_guidl__security_package[version==1], gd_temp__module_security_plan[version==1], gd_guidl__security_plan_definitions[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Security Manager is NOT responsible to provide the argument for the achievement of security.
   | But the Security Manager creates and maintains the Security Package in the sense of a collection of security related work products.
   | The generation and the maintenance of this draft Security Package shall be automated as much as possible.
   | It does not contain the final argumentation of the security of the product.
   | As the Security Package is only a collection of work products, the Security Plan (template) can be used for documentation.

.. workflow:: Perform Security Audit
   :id: wf__p_fs_audit_security
   :status: valid
   :version: 1
   :responsible: rl__security_external_auditor[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__security_manager[version==1], rl__security_engineer[version==1]
   :input: wp__module_security_plan[version==1],
           wp__platform_security_plan[version==1],
           wp__module_security_package[version==1],
           wp__platform_security_package[version==1]
   :output: wp__audit_report_security[version==1]
   :contains: gd_guidl__security_plan_definitions[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The external auditor is responsible to perform a security audit.
   | The Security Manager and the process community shall support the external auditor during this.
   | The Project Manager and and the Security Manager shall approve the audit report.
   |
   | The security audit is performed before the assessment for maturity level 3. For maturity level 2 the conformity of the security activities is judged by the formal security reviews and by the cybersecurity assessment (:need:`wf__p_security_assessment`), whose scope includes the security plan and all work products identified in it.

.. workflow:: Perform Formal Security Reviews
   :id: wf__p_formal_security_rv
   :status: valid
   :version: 1
   :responsible: rl__security_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__security_engineer[version==1]
   :input: wp__module_security_plan[version==1],
           wp__platform_security_plan[version==1],
           wp__module_security_package[version==1],
           wp__platform_security_package[version==1],
           wp__platform_security_analysis[version==1],
           wp__feature_security_analysis[version==1],
           wp__sw_component_security_analysis[version==1]
   :output: wp__fdr_reports_security[version==1]
   :contains: gd_guidl__security_plan_definitions[version==1],
              gd_chklst__platform_security_plan[version==1],
              gd_chklst__security_plan[version==1],
              gd_chklst__security_package[version==1],
              gd_chklst__security_analysis[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | An "external" Security Manager is responsible to perform the formal reviews on Security Plan, Security Package and Security Analyses.
   | In this context "external" means that the person is not the Security Manager of the platform/module, i.e. did not create or approve the reviewed work product. The reviewer is taken from the pool of platform security managers and is named in the review report.
   | The Security Engineer supports the reviews.
   | The Project Lead approves the formal reviews.
   | Checklists exist to guide the reviewer and the creator of the relevant security documents.
   | The formal review of the Security Plan includes the review of the tailoring rationales and the independent review of the rationale for the cybersecurity assessment decision.

.. workflow:: Perform Cybersecurity Assessment
   :id: wf__p_security_assessment
   :status: valid
   :version: 1
   :responsible: rl__security_external_auditor[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__security_manager[version==1], rl__security_engineer[version==1]
   :input: wp__platform_security_plan[version==1],
           wp__platform_security_package[version==1],
           wp__platform_security_analysis[version==1],
           wp__platform_security_manual[version==1],
           wp__fdr_reports_security[version==1]
   :output: wp__security_assessment_report[version==1]
   :contains: gd_guidl__security_assessment[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The External Security Auditor plans and performs the cybersecurity assessment of the platform before its release for post-development, if the Security Plan decides that an assessment is performed.
   | The assessor is independent of the assessed activities. The Security Manager provides access to the information and tools and ensures the cooperation of the persons who performed the activities.
   | The assessment judges the cybersecurity of the platform. Its scope and its report are described in :need:`gd_guidl__security_assessment`.
   | The Project Lead approves the assessment report.

.. workflow:: Create/Maintain Security Manual
   :id: wf__cr_mt_security_manual
   :status: valid
   :version: 1
   :responsible: rl__security_engineer[version==1]
   :approved_by: rl__security_manager[version==1]
   :supported_by: rl__committer[version==1]
   :input: wp__requirements_feat_aou[version==1],
           wp__requirements_feat[version==1],
           wp__feature_arch[version==1],
           wp__feature_security_analysis[version==1],
           wp__requirements_comp_aou[version==1],
           wp__requirements_comp[version==1],
           wp__component_arch[version==1],
           wp__sw_component_security_analysis[version==1],
           wp__platform_security_analysis[version==1]
   :output: wp__platform_security_manual[version==1], wp__module_security_manual[version==1]
   :contains: gd_guidl__security_manual[version==1],
              gd_temp__platform_security_manual[version==1],
              gd_temp__module_security_manual[version==1],
              gd_guidl__security_plan_definitions[version==1],
              gd_guidl__security_interface[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Security Engineer collects the necessary input for the Security Manuals on
   | platform and module level and documents it.
   | He makes sure all items are in valid state for a release of the Security Manual.
   | Also for the Security Manual a template exists as a guidance.
   | The Security Manual contains the platform part of the cybersecurity interface agreement with the integrator (see :need:`gd_guidl__security_interface`).

.. workflow:: Create/Maintain SBOM
   :id: wf__cr_mt_security_sbom
   :status: valid
   :version: 1
   :responsible: rl__committer[version==1]
   :approved_by: rl__security_manager[version==1], rl__security_engineer[version==1], rl__project_lead[version==1]
   :supported_by: rl__infrastructure_tooling_community[version==1],
                  rl__process_community[version==1],
                  rl__security_team[version==1],
                  rl__contributor[version==1]
   :input: wp__issue_track_system[version==1],
           wp__module_security_plan[version==1],
           wp__platform_security_plan[version==1],
           wp__module_security_package[version==1],
           wp__platform_security_package[version==1]
   :output: wp__sw_platform_sbom[version==1], wp__sw_module_sbom[version==1]
   :contains: gd_guidl__security_plan_definitions[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Committer is responsible to create and the maintain the SBOM for the platform/module.
   | The Committer makes sure all components and dependencies are identified and made available.

.. workflow:: Assess Off-the-Shelf and Open-Source Components
   :id: wf__assess_oss_ots_components
   :status: valid
   :version: 1
   :responsible: rl__security_engineer[version==1]
   :approved_by: rl__security_manager[version==1]
   :supported_by: rl__committer[version==1]
   :input: wp__sw_platform_sbom[version==1], wp__issue_track_system[version==1]
   :output: wp__sw_component_oss_assessment[version==1]
   :contains: gd_guidl__security_plan_definitions[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Security Engineer analyses each off-the-shelf or open-source component the platform uses against three results: whether the cybersecurity requirements allocated to it can be fulfilled, whether it is suitable for the intended use, and whether its documentation is sufficient for the cybersecurity activities.
   | Where the documentation is insufficient, the activities that close the gap are identified and planned.
   | The Security Manager approves the assessment.

.. workflow:: Monitor/Verify Security
   :id: wf__mr_vy_security
   :status: valid
   :version: 1
   :responsible: rl__security_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__security_team[version==1]
   :input: wp__issue_track_system[version==1],
           wp__module_security_plan[version==1],
           wp__platform_security_plan[version==1],
           wp__module_security_package[version==1],
           wp__platform_security_package[version==1],
           wp__audit_report_security[version==1],
           wp__fdr_reports_security[version==1],
           wp__security_assessment_report[version==1],
           wp__sw_platform_sbom[version==1],
           wp__sw_module_sbom[version==1]
   :output: wp__issue_track_system[version==1], wp__module_sw_release_note[version==1], wp__release_post_development_security[version==1], wp__platform_sw_release_note[version==1], wp__security_incident_response_plan[version==1]
   :contains: gd_guidl__security_plan_definitions[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Security Manager is responsible for the monitoring of the security activities against the Security Plan.
   | The Security Manager is responsible to verify, that the preconditions for the "release for post-development", which are  part of the release notes, are fulfilled.
   | The Security Manager is responsible to verify the correctness, completeness and consistency of the release notes.
   | The Security Manager is responsible for the monitoring of security information from the sources and with the triggers defined in the Security Plan.
   | The Security Manager is responsible to identify weaknesses and vulnerabilities based on received information, and to analyse and manage the vulnerabilities until closure.
   | For each cybersecurity incident the Security Manager creates the incident response plan in the security problem issue and tracks it until closure (see :need:`gd_guidl__security_plan_definitions`).
   | Beside reporting vulnerabilities in the :need:`wp__issue_track_system`, they may also be reported through the `Eclipse Foundation security policy <https://www.eclipse.org/security/policy/>`_.

.. workflow:: Consult and Execute Security Trainings
   :id: wf__consult_exe_sec_training
   :status: valid
   :version: 1
   :responsible: rl__security_manager[version==1]
   :approved_by: rl__project_lead[version==1]
   :supported_by: rl__security_engineer[version==1], rl__safety_manager[version==1], rl__quality_manager[version==1]
   :input: wp__module_security_plan[version==1],
           wp__platform_security_plan[version==1],
           wp__policies[version==1],
           wp__process_description[version==1]
   :output: wp__training_path[version==1]
   :contains: gd_temp__module_security_plan[version==1]
   :has: doc_concept__security_management_process[version==1], doc_getstrt__security_management_process[version==1]

   | The Security Manager :need:`rl__security_manager` consults all project/platform stakeholder as defined in :need:`doc_concept__security_management_process` for security topics and executes regularly security trainings.


.. needextend:: "c.this_doc()"
   :+tags: security_management

RAS(IC) for Security Management:
********************************

.. needtable:: RASIC Overview for Security Management
   :tags: security_management
   :filter: "security_management" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
