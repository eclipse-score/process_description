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
   :realizes: wp__fdr_reports_security[version==1]
   :tags: template

.. attention::
    The above directive must be updated according to your Platform.

    - Modify ``Your Platform Name`` to be your Platform Name
    - Modify ``id`` to be your Platform Name in lower snake case preceded by ``doc__`` and followed by ``_security_package_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety``, ``security`` and ``tags`` according to your needs


**Purpose**

The purpose of this security package formal review checklist is to report status of the review for the platform security package.

**Conduct**
As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by the external auditor, supported by the Security Manager:

- reviewer: <external auditor explicitly named here>

**Checklist**

.. list-table:: Security Package Checklist
        :header-rows: 1

        * - Id
          - Security package activity
          - Compliant to ISO/SAE 21434?
          - Reference
          - Comment

        * - 1
          - Is a security package provided which matches the security plan (i.e. all planned work products referenced)?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6471>`
          - <Rationale for result>

        * - 2
          - Is the argument how cybersecurity is achieved (cybersecurity case), provided in the security package, plausible and sufficient?
          - NO
          - :need:`[[title]] <std_req__isosae21434__prj_management_6471>`
          - The argument is intentionally not provided by the project.

        * - 3
          - Are the referenced work products available (e.g. security analyses, platform security manual, SBOM)?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6491>`
          - <Rationale for result>

        * - 4
          - Are the referenced work products in released state?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6492>`
          - <Rationale for result>

        * - 5
          - If security related deviations from the process are documented, are these argued understandably?
          - [YES | NO ]
          - :need:`[[title]] <std_req__isosae21434__prj_management_6471>`
          - <Rationale for result>
