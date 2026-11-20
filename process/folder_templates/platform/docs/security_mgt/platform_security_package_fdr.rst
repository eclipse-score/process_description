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

The purpose of this review checklist is to report status of the formal review for the platform security package.

**Conduct**

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an "external" security manager from the pool of platform security managers, who did not create or approve the package. The security engineer supports the review. The reviewer is named below:

- reviewer: <security manager explicitly named here, not the author or approver of the package>

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
          - Is a cybersecurity case provided, or is its absence justified by a tailoring rationale that has been reviewed? (:need:`[[title]] <std_req__isosae21434__prj_management_6471>`, :need:`[[title]] <std_req__isosae21434__prj_management_6432>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 3
          - Are the referenced work products available (e.g. security analyses, platform security manual, SBOM, cybersecurity requirements for post-development :need:`[[title]] <std_wp__isosae21434__development_1052>`, and the cybersecurity assessment report)? (:need:`[[title]] <std_req__isosae21434__prj_management_6491>`)
          - [YES | NO ]
          - <Rationale for result>

        * - 4
          - Are the referenced work products in released state, and is the cybersecurity case confirmed by the cybersecurity assessment? (:need:`[[title]] <std_req__isosae21434__prj_management_6492>`)
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

        * - 7
          - Does the cybersecurity assessment report recommend acceptance, conditional acceptance or rejection, and are the conditions stated for a conditional acceptance? (:need:`[[title]] <std_req__isosae21434__prj_management_6488>`, :need:`[[title]] <std_req__isosae21434__prj_management_6489>`)
          - [YES | NO ]
          - <Rationale for result>
