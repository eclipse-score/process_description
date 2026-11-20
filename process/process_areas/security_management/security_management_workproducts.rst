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

Security Management Work Products
#################################
.. workproduct:: Platform Security Plan
   :id: wp__platform_security_plan
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__prj_management_651[version==1],
              std_wp__isosae21434__continual_8331[version==1],
              std_wp__isosae21434__continual_8332[version==1]

   Plan to manage and guide the execution of the security activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Security Manager appointment)  and resources.

   This Platform Security Plan also takes into account the eclipse organization's rules relevant for security development.

   The Platform Security Plan defines the sources of cybersecurity information and the triggers for the monitoring
   (part of the vulnerability management of the platform), and it documents the decision whether a cybersecurity
   assessment is performed, with its rationale.

   Changes to an item or component are analysed with the change impact analysis of the change management (template :need:`gd_temp__change_impact_analysis`). The reuse analysis of the standard is part of that analysis.

   For the template see here: :need:`doc__platform_security_plan`

   This is on following level:

   * Project/Platform (contains definitions how security planning is performed generally in the project)

.. workproduct:: Module Security Plan
   :id: wp__module_security_plan
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__prj_management_651[version==1]

   Plan to manage and guide the execution of the security activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Security Manager appointment) and resources.

   Changes to an item or component are analysed with the change impact analysis of the change management (template :need:`gd_temp__change_impact_analysis`). The reuse analysis of the standard is part of that analysis.

   For the template see here: `Module Security Plan Template <https://eclipse-score.github.io/module_template/main/module/security_mgt/module_security_plan.html>`__

   This is on following level:

   * Module (contains activities planning based on a Change Request)

.. workproduct:: Platform Security Package
   :id: wp__platform_security_package
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__prj_management_652[version==1]

   Compiled security relevant work products. For platform OoC.

   Note that the Platform Security Package does not contain an argument that the platform is safe and secure.

.. workproduct:: Module Security Package
   :id: wp__module_security_package
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__prj_management_652[version==1]

   Compiled security relevant work products. For Module OoC.

   Note that the Module Security Package does not contain an argument that the module is safe and secure.

.. workproduct:: Formal Document Review Reports
   :id: wp__fdr_reports_security
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__concept_9434[version==1], std_wp__isosae21434__concept_9532[version==1]

   Review that a work product provides sufficient and convincing evidence of their contribution to the achievement of security considering the corresponding objectives and requirements of ISO SAE 21434.

   Will contain formal review report for Security Plan, Security Package and Security Analyses, and the verification of the cybersecurity goals and of the cybersecurity concept of the platform.

   For the different review checklist see here:
     - Review checklist for Security Plans: :need:`doc__platform_name_security_plan_fdr` and `Module Security Plan Formal Review Checklist <https://eclipse-score.github.io/module_template/main/module/security_mgt/module_security_plan_fdr.html>`__
     - Review checklist for Security Packages: :need:`doc__platform_name_security_package_fdr` and `Module Security Package Formal Review Checklist <https://eclipse-score.github.io/module_template/main/module/security_mgt/module_security_package_fdr.html>`__
     - Review checklist for Security Analyses: :need:`doc__platform_name_security_analysis_fdr`

.. workproduct:: Process Security Audit Report
   :id: wp__audit_report_security
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__org_management_555[version==1]

   Examination of an implemented process with regard to the process objectives and that those match the ISO SAE 21434.
   (Performed before the assessment for maturity level 3, see :need:`wf__p_fs_audit_security`)

.. workproduct:: Cybersecurity Assessment Report
   :id: wp__security_assessment_report
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__prj_management_653[version==1]

   Result of the cybersecurity assessment of the platform (see :need:`gd_guidl__security_assessment`):
   the judgement of the cybersecurity of the platform and the recommendation for acceptance, conditional
   acceptance or rejection, with the conditions for a conditional acceptance.

.. workproduct:: Platform Security Manual
   :id: wp__platform_security_manual
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__development_1052[version==1],
              std_wp__isosae21434__distributed_751[version==1],
              std_wp__isosae21434__concept_9432[version==1],
              std_wp__isosae21434__concept_9433[version==1],
              std_wp__isosae21434__concept_9531[version==1]

   The Security Manual describes:

   * the assumed platform requirements (security related, including for post-development);
   * the security concept of the OoC (i.e. which attack paths are taken care of);
   * the cybersecurity goals of the platform, derived from the threat scenarios whose risk is reduced;
   * the assumptions of use (of the features);
   * a link to the user manual;
   * the reactions of the implemented functions under threatened operating conditions;
   * a description of known vulnerabilities with corresponding workaround measures; and
   * the platform part of the cybersecurity interface agreement with the integrator (see :need:`gd_guidl__security_interface`).

   This is on platform level. Only one manual for the entire platform.

   For template see here: :need:`doc__platform_security_manual`

.. workproduct:: Module Security Manual
   :id: wp__module_security_manual
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__development_1052[version==1],
              std_wp__isosae21434__distributed_751[version==1]

   The Security Manual describes:

   * the assumed platform requirements (security related, including for post-development);
   * the security concept of the OoC (i.e. which attack paths are taken care of);
   * the assumptions of use (of the module's components);
   * a link to the module user manual (:need:`wp__module_user_manual`);
   * the reactions of the implemented functions under threatened operating conditions;
   * a description of known vulnerabilities with corresponding workaround measures; and
   * the module part of the cybersecurity interface agreement with the integrator (see :need:`gd_guidl__security_interface`).

   This is on module level. One manual per each module.

   For template see here: `Module Security Manual Template <https://eclipse-score.github.io/module_template/main/module/manuals/security_manual.html>`__

.. workproduct:: Platform Software Bill of Material (SBOM)
   :id: wp__sw_platform_sbom
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2

   Platform Software Bill of Material
   - comprehensive inventory of software components to ensure security, integrity, and compliance.

.. workproduct:: Module Software Bill of Material (SBOM)
   :id: wp__sw_module_sbom
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2

   Module Software Bill of Material
   - comprehensive inventory of software components to ensure security, integrity, and compliance.

.. workproduct:: Release for Post-Development Report (Security)
   :id: wp__release_post_development_security
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__prj_management_654[version==1]

   Evidence that the conditions for the release for post-development are fulfilled: the security case is convincing, the case is confirmed by the cybersecurity assessment (:need:`wp__security_assessment_report`), and the cybersecurity requirements for post-development are accepted.

.. workproduct:: Cybersecurity Incident Response Plan
   :id: wp__security_incident_response_plan
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__isosae21434__maintenance_13331[version==1]

   One incident response plan per cybersecurity incident, recorded in the security problem issue of the
   incident in the :need:`wp__issue_track_system`. Its content is described in :need:`gd_guidl__security_plan_definitions`.

.. workproduct:: Off-the-Shelf and Open-Source Component Assessment (Security)
   :id: wp__sw_component_oss_assessment
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2

   Assessment of each off-the-shelf or open-source component the platform uses, with three results: whether the allocated cybersecurity requirements can be fulfilled by the component, whether the component is suitable for the intended use, and whether its documentation is sufficient for the cybersecurity activities. Where the documentation is insufficient, the activities to close the gap are named (requirements :need:`std_req__isosae21434__prj_management_6461` and :need:`std_req__isosae21434__prj_management_6462` of the standard).

.. needextend:: "c.this_doc()"
   :+tags: security_management
