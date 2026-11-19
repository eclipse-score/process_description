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


Platform Security Package Checklist
===================================

.. document:: [Your Platform Name] Security Package Checklist
   :id: doc__platform_name_security_package_fdr
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports[version==1]
   :tags: template

.. attention::
    The above directive must be updated according to your Platform.

    - Modify ``Your Platform Name`` to be your Platform Name
    - Modify ``id`` to be your Platform Name in lower snake case preceded by ``doc__`` and followed by ``_security_package_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety``, ``security`` and ``tags`` according to your needs


**Purpose**

The purpose of this review checklist is to report status of the formal review for the platform security package.

**Conduct**

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an independent reviewer. The external security auditor is responsible for the review, the security manager supports it. The external review is currently tailored out for the platform; for ML 2 the review is performed as internal inspection:

- reviewer: <committer with security manager skills explicitly named here, not the author of the package>

**Checklist**

.. list-table:: Security Package Checklist
        :header-rows: 1

        * - Id
          - Security package activity
          - Compliant to ISO/SAE 21434?
          - Comment

        * - 1
          - Is a security package provided which matches the security plan (i.e. all planned work products referenced)?
          - [YES | NO ]
          - <Rationale for result>

        * - 2
          - Is the argument how security is achieved, provided in the security package, plausible and sufficient?
          - NO
          - The argument is intentionally not provided by the project (see wp__platform_security_package).

        * - 3
          - Are the referenced work products available (e.g. security analyses, platform security manual, SBOM)?
          - [YES | NO ]
          - <Rationale for result>

        * - 4
          - Are the referenced work products in released state? The process security audit report is tailored out, see the platform security plan.
          - [YES | NO ]
          - <Rationale for result>

        * - 5
          - If security related deviations from the process or security concept are documented, are these argued understandably?
          - [YES | NO ]
          - <Rationale for result>

        * - 6
          - Is the SBOM of the platform generated automatically and does it cover all open source components?
          - [YES | NO ]
          - <Rationale for result>
