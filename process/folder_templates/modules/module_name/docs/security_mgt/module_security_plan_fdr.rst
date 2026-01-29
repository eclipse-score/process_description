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

Module Security Plan Formal Review Report
=========================================

.. note:: Document header

.. document:: [Your Module Name] Security Plan Formal Review
   :id: doc__module_name_security_plan_fdr
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports
   :tags: template

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in upper snake case preceded by ``doc_`` and succeeded by ``_security_plan_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

**1. Purpose**

The purpose of this review checklist is to provide a guidence for reviewing the security plans for each module.
Each module security plan shall one checklist filled.

**2. Checklist**

See also :ref:`review_concept` for further information about reviews in general and inspection in particular.

.. list-table:: Security Plan Checklist
        :header-rows: 1

        * - Id
          - Security plan activity
          - Compliant to ISO SAE 21434?
          - Comment

        * - 1
          - Is the rationale for the security work products tailoring included?
          - [YES | NO ]
          - <Rationale for result>

        * - 2
          - Is impact analysis planned in case of re-use of SW (needed for every release following the first formal release)?
          - [YES | NO ]
          - <Rationale for result>

        * - 3
          - Does the security plan define all needed activities for security management (incl. Review and Security Audit)?
          - [YES | NO ]
          - <Rationale for result>

        * - 4
          - Does the security plan define all needed activities for SW development, integration and verification?
          - [YES | NO ]
          - <Rationale for result>

        * - 5
          - Does the security plan define all needed activities for security analysis?
          - [YES | NO ]
          - <Rationale for result>

        * - 6
          - Does the security plan define all needed activities for supporting processes (incl. tool mgt)?
          - [YES | NO ]
          - <Rationale for result>

        * - 7
          - Does the security plan document a responsible for all activities?
          - [YES | NO ]
          - <Rationale for result>

        * - 8
          - If Off-the-shelf (e.g. existing OSS) software components is used, is it planned to be analysed?
          - [YES | NO ]
          - <Rationale for result>

        * - 9
          - Is a security manager and a project lead appointed for the project?
          - [YES | NO ]
          - <Rationale for result>

        * - 10
          - Is security plan sufficiently linked to the project plan?
          - [YES | NO ]
          - <Rationale for result>

        * - 11
          - Is security plan updated iteratively to show the progress?
          - [YES | NO ]
          - <Rationale for result>

        * - 12
          - If Out-of-context software components is used, are the assumptions documented?
          - [YES | NO ]
          - <Rationale for result>

        * - 13
          - Does the security plan define all needed activities for SBOM generation?
          - [YES | NO ]
          - <Rationale for result>

        * - 14
          - Does the security plan define regular vulnerability scans for the generated SBOM?
          - [YES | NO ]
          - <Rationale for result>

.. note::
    Off-the-shelf means existing software which may used w/o modification, e.g. existing OSS
