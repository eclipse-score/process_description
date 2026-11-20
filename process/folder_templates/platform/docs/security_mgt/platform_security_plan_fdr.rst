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


Platform Security Plan Formal Review Report
===========================================

.. document:: [Your Platform Name] Security Plan Checklist
   :id: doc__platform_name_security_plan_fdr
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports_security[version==1]
   :tags: template

.. attention::
    The above directive must be updated according to your Platform.

    - Modify ``Your Platform Name`` to be your Platform Name
    - Modify ``id`` to be your Platform Name in lower snake case preceded by ``doc__`` and followed by ``_security_plan_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs


**Purpose**

The purpose of this security plan formal review checklist is to report status of the review for the platform security plan.

**Conduct**

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an "external" security manager from the pool of platform security managers, who did not create or approve the plan. The security engineer supports the review. The reviewer is named below:

- reviewer: <security manager explicitly named here, not the author or approver of the plan>

**Checklist**

.. list-table:: Security Plan Checklist
        :header-rows: 1

        * - Id
          - Security plan activity
          - Compliant to ISO/SAE 21434?
          - Comment

        * - 1
          - Is the rationale for the security work products tailoring included and reviewed (incl. the tailoring of the process audit and of the formal review)? (:need:`[[title]] <std_req__isosae21434__prj_management_6432>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 2
          - Is a reuse analysis planned and carried out in case of re-use of SW, a change in the operational environment, or a relevant change of cybersecurity information? (:need:`[[title]] <std_req__isosae21434__prj_management_6441>` to :need:`[[title]] <std_req__isosae21434__prj_management_6443>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 3
          - Does the security plan define all needed activities for security management (incl. formal security reviews)?
          - [YES | NO ]
          - <Rationale for result>

        * - 4
          - Does the security plan define all needed activities for security analysis on platform, feature and component level?
          - [YES | NO ]
          - <Rationale for result>

        * - 5
          - Does the security plan define all needed activities for security development and verification (e.g. fuzz testing, static analysis)?
          - [YES | NO ]
          - <Rationale for result>

        * - 6
          - Does the security plan define all needed activities for supporting processes (incl. vulnerability management, tool management and SBOM)?
          - [YES | NO ]
          - <Rationale for result>

        * - 7
          - Does the security plan define for each activity the objective, dependencies, responsible persons, resources, start and end, and the work products to be produced? (:need:`[[title]] <std_req__isosae21434__prj_management_6422>`, :need:`[[title]] <std_req__isosae21434__prj_management_6423>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 8
          - Are open source components and third-party dependencies covered (SBOM, monitoring for known vulnerabilities)?
          - [YES | NO ]
          - <Rationale for result>

        * - 9
          - Is a security manager and a project manager appointed for the project?
          - [YES | NO ]
          - <Rationale for result>

        * - 10
          - Are the competence and awareness of the persons with security roles defined, incl. committers and approvers? (:need:`[[title]] <std_req__isosae21434__org_management_5422>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 11
          - Is the security plan linked to the project plan and to the module security plans?
          - [YES | NO ]
          - <Rationale for result>

        * - 12
          - Is the security plan updated iteratively to show the progress?
          - [YES | NO ]
          - <Rationale for result>

        * - 13
          - Is the cybersecurity relevance of each item or component determined, and is the choice between new development and reuse documented? (:need:`[[title]] <std_req__isosae21434__prj_management_6421>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 14
          - Are configuration management and documentation management defined for the security plan and its work products? (:need:`[[title]] <std_req__isosae21434__prj_management_64210>`, :need:`[[title]] <std_req__isosae21434__prj_management_64211>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 15
          - Is the decision whether to perform a cybersecurity assessment documented with a risk-based rationale, and is this rationale reviewed independently? (:need:`[[title]] <std_req__isosae21434__prj_management_6481>`, :need:`[[title]] <std_req__isosae21434__prj_management_6482>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 16
          - If an assessment is performed, is an independent person appointed to plan and perform it, with access to the information and tools needed? (:need:`[[title]] <std_req__isosae21434__prj_management_6484>`, :need:`[[title]] <std_req__isosae21434__prj_management_6485>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 17
          - If an assessment is performed, does its scope include the plan, the work products, the risk treatment and the rationales, and does its report recommend acceptance, conditional acceptance or rejection? (:need:`[[title]] <std_req__isosae21434__prj_management_6487>`, :need:`[[title]] <std_req__isosae21434__prj_management_6488>`, :need:`[[title]] <std_req__isosae21434__prj_management_6489>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 18
          - For each off-the-shelf component, are the fulfilment of the allocated cybersecurity requirements, the suitability for the intended use, and the sufficiency of its documentation analysed? (:need:`[[title]] <std_req__isosae21434__prj_management_6461>`, :need:`[[title]] <std_req__isosae21434__prj_management_6462>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 19
          - Are the sources of cybersecurity information and the triggers for the cybersecurity monitoring defined? (:need:`[[title]] <std_req__isosae21434__continual_8321>`, :need:`[[title]] <std_req__isosae21434__continual_8322>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 20
          - Is the cybersecurity interface with the integrator defined, incl. the activities the integrator performs (validation, production, end of support) and the tailoring of supplier selection? (:need:`[[title]] <std_req__isosae21434__distributed_7431>`)
          - [YES | NO ]
          - <Rationale for result>
