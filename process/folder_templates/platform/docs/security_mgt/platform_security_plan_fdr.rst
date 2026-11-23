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
As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by the external auditor, supported by the Security Manager:

- reviewer: <external auditor explicitly named here>

**Checklist**

.. list-table:: Security Plan Checklist
        :header-rows: 1

        * - Id
          - Security plan activity
          - Compliant to ISO/SAE 21434?
          - Reference
          - Comment

        * - 1
          - Is the rationale for the security work products tailoring included?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6432>`
          - <Rationale for result>

        * - 2
          - Is a reuse analysis planned in case of re-use of SW, a change in the operational environment, or a relevant change of cybersecurity information?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6441>`
            :need:`[[title]] <std_req__isosae21434__prj_management_6442>`
            :need:`[[title]] <std_req__isosae21434__prj_management_6443>`
          - <Rationale for result>

        * - 3
          - Does the security plan define all needed activities for security management (including formal security reviews and security audit, or the rationale why they are tailored out)?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 4
          - Does the security plan define all needed activities for security analysis on platform, feature and component level?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 5
          - Does the security plan define all needed activities for security development and verification (e.g. fuzz testing, static analysis)?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 6
          - Does the security plan define all needed activities for supporting processes (including vulnerability management, tool management and SBOM)?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 7
          - Does the security plan define for each activity the objective, dependencies, responsible persons, resources, start and end, and the work products to be produced?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6422>`
            :need:`[[title]] <std_req__isosae21434__prj_management_6423>`
          - <Rationale for result>

        * - 8
          - Are all open source components and third-party dependencies covered (SBOM, monitoring for known vulnerabilities)?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 9
          - If off-the-shelf or open source components are used, is it planned to analyse whether they fulfil the allocated cybersecurity requirements, whether they are suitable for the intended use, and whether their documentation is sufficient?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6461>`
            :need:`[[title]] <std_req__isosae21434__prj_management_6462>`
          - <Rationale for result>

        * - 10
          - Is a security manager and a project manager appointed for the platform?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 11
          - Are the competence and awareness of the persons with security roles defined?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__org_management_5422>`
          - <Rationale for result>

        * - 12
          - Is the security plan linked to the project plan and to the module security plans?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 13
          - Is the security plan updated iteratively to show the progress?
          - [YES | NO ]
          -
          - <Rationale for result>

        * - 14
          - Is the cybersecurity relevance of each item or component determined, and is the choice between new development and reuse documented?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6421>`
          - <Rationale for result>

        * - 15
          - Are configuration management and documentation management defined for the security plan and its work products?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_64210>`
            :need:`[[title]] <std_req__isosae21434__prj_management_64211>`
          - <Rationale for result>

        * - 16
          - Are the sources of cybersecurity information and the triggers for the cybersecurity monitoring defined?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__continual_8321>`
            :need:`[[title]] <std_req__isosae21434__continual_8322>`
          - <Rationale for result>
