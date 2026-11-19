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
   :realizes: wp__fdr_reports[version==1]
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

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an independent reviewer. The external security auditor is responsible for the review, the security manager supports it. The external review is currently tailored out for the platform; for ML 2 the review is performed as internal inspection:

- reviewer: <committer with security manager skills explicitly named here, not the author of the plan>

**Checklist**

.. list-table:: Security Plan Checklist
        :header-rows: 1

        * - Id
          - Security plan activity
          - Compliant to ISO/SAE 21434?
          - Comment

        * - 1
          - Is the rationale for the security work products tailoring included and reviewed (incl. the tailoring of the process audit and of the formal review)? (RQ-06-14)
          - [YES | NO ]
          - <Rationale for result>

        * - 2
          - Is impact analysis planned in case of re-use of SW or a feature modification request?
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
          - Does the security plan define for each activity the objective, dependencies, responsible persons, resources, start and end, and the work products to be produced? (RQ-06-03, RQ-06-04)
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
          - Are the competence and awareness of the persons with security roles defined, incl. committers and approvers? (RQ-05-07)
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
          - Is the cybersecurity relevance of each item or component determined, and is the choice between new development and reuse documented? (RQ-06-02)
          - [YES | NO ]
          - <Rationale for result>

        * - 14
          - Are configuration management and documentation management defined for the security plan and its work products? (RQ-06-11, RQ-06-12)
          - [YES | NO ]
          - <Rationale for result>

        * - 15
          - Is the decision whether to perform a cybersecurity assessment documented with a risk-based rationale, and is this rationale reviewed independently? (RQ-06-24, RQ-06-25)
          - [YES | NO ]
          - <Rationale for result>

        * - 16
          - If an assessment is performed, is an independent person appointed to plan and perform it, with access to the information and tools needed? (RQ-06-27, RQ-06-28)
          - [YES | NO ]
          - <Rationale for result>

        * - 17
          - If an assessment is performed, does its scope include the plan, the work products, the risk treatment and the rationales, and does its report recommend acceptance, conditional acceptance or rejection? (RQ-06-30, RQ-06-31, RQ-06-32)
          - [YES | NO ]
          - <Rationale for result>
