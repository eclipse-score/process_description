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

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an independent security manager:

- reviewer: <committer with security manager skills explicitly named here, not the author of the plan>

**Checklist**

.. list-table:: Security Plan Checklist
        :header-rows: 1

        * - Id
          - Security plan activity
          - Compliant to ISO/SAE 21434?
          - Comment

        * - 1
          - Is the rationale for the security work products tailoring included (incl. the tailoring of the process audit)?
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
          - Does the security plan document a responsible for all activities?
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
          - Is the competence requirement for committers and approvers defined and consistent with the process?
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
