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


Platform Security Analysis Checklist
====================================

.. document:: [Your Platform Name] Security Analysis Checklist
   :id: doc__platform_name_security_analysis_fdr
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports_security[version==1]
   :tags: template

.. attention::
    The above directive must be updated according to your Platform.

    - Modify ``Your Platform Name`` to be your Platform Name
    - Modify ``id`` to be your Platform Name in lower snake case preceded by ``doc__`` and followed by ``_security_analysis_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety``, ``security`` and ``tags`` according to your needs


**Purpose**
The purpose of this Security Analysis formal review report template is to collect the topics to be checked during verification of the Platform Security Analysis.

**Conduct**
As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by the external auditor, supported by the Security Manager:

- reviewer: **<external auditor explicitly named here>**
- scope: **<describe the scope of the review here, e.g. "the security analysis of the platform and its results">**

The same checklist guides the verification of the security analysis by the security engineer (:need:`wf__vy_sec_analyses`).

**Checklist**

Please note that it is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additional to add in the remarks why it is passed or not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column. See also :ref:`review_concept` for further information about reviews in general and inspection in particular.


.. list-table:: Security Analysis Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Security analysis activity
        - Compliant to ISO/SAE 21434?
        - Reference
        - Comment

      * - Sec 1
        - Is the security analysis performed according to the defined process and templates, and based on the assumptions on the intended use and the operational environment of the platform security manual?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__prj_management_6451>`
        - <Rationale for result>

      * - Sec 2
        - Are the assets with their cybersecurity properties and the threat scenarios identified?
        - [YES | NO ]
        - 
        - <Rationale for result>

      * - Sec 3
        - Are the attack paths identified and their attack feasibility rated?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__assessment_15621>`, :need:`[[title]] <std_req__isosae21434__assessment_15622>`, :need:`[[title]] <std_req__isosae21434__assessment_15721>`
        - <Rationale for result>

      * - Sec 4
        - Is a risk value determined for each threat scenario, with the assumed worst-case impact?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__assessment_15821>`, :need:`[[title]] <std_req__isosae21434__assessment_15822>`
        - <Rationale for result>

      * - Sec 5
        - Is a risk treatment decision taken for each threat scenario, with a mitigation for a reduced risk and an assumption of use in the security manual for a shared or retained risk?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__assessment_15921>`
        - <Rationale for result>

      * - Sec 6
        - Are all assumptions of use that are used as mitigation, including the assumed worst-case impact, created and covered in the security manual?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__prj_management_6451>`
        - <Rationale for result>

      * - Sec 7
        - Is the analysis updated when the platform, its assumed environment or the known threats change?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__prj_management_6426>`, :need:`[[title]] <std_req__isosae21434__prj_management_6428>`
        - <Rationale for result>
