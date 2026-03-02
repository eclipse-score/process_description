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

Security Package Formal Review Report
=====================================

.. note:: Document header

.. document:: [Your Module Name] Security Package Formal Review
   :id: doc__module_name_security_package_fdr
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports
   :tags: template

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in upper snake case preceded by ``doc_`` and succeeded by ``safety_package_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs


**1. Purpose**

The purpose of this review checklist is to report status of the formal review for the Security Package.

**2. Checklist**

See also :ref:`review_concept` for further information about reviews in general and inspection in particular.

.. list-table:: Security Package Checklist
        :header-rows: 1

        * - Id
          - Security Package activity
          - Compliant to ISO SAE 21434?
          - Comment

        * - 1
          - Is a Security Package provided which matches the Security Plan (i.e. all planned work products referenced)?
          - [YES | NO ]
          - <Rationale for result>

        * - 2
          - Is the argument how security is achieved, provided in the Security Package, plausible and sufficient?
          - NO
          - The argument is intentionally not provided by the Project.

        * - 3
          - Are the referenced work products available?
          - [YES | NO ]
          - <Rationale for result>

        * - 4
          - Are the referenced work products in released state, including the Process Security Audit?
          - NO
          - Security Audit is currently not planned, tailored out.

        * - 5
          - If security related deviations from the process or security concept are documented, are these argued understandably?
          - [YES | NO ]
          - <Rationale for result>

        * - 6
          - Are the requirements for post-development available?
          - [YES | NO ]
          - <Rationale for result>
