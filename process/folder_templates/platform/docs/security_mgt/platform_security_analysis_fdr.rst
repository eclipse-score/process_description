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
The purpose of this Security Analysis Checklist template is to collect the topics to be checked during verification of the Security Analysis.

**Conduct**

As described in :need:`wf__p_formal_security_rv`, the formal document review is performed by an "external" security manager from the pool of platform security managers, who did not create or approve the security analysis. The security engineer supports the review. The reviewer and the scope are named below:

- reviewer: <security manager explicitly named here, not the author or approver of the analysis>
- scope: <the security analysis of the platform, feature or component and its results>

**Checklist**

Mark each item "YES" or "NO" and state the reason in the comment. A "NO" needs an issue.

.. list-table:: Security Analysis Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Security analysis activity
        - Compliant to ISO/SAE 21434?
        - Reference (clause 9 and 15 of the standard)
        - Comment

      * - Sec 1
        - Is the item definition complete: the information on the item and its operational environment is identified?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9321>`, :need:`[[title]] <std_req__isosae21434__concept_9322>`
        - <Rationale for result>

      * - Sec 2
        - Is the analysis based on the item definition and performed with the defined method and templates?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9421>`
        - <Rationale for result>

      * - Sec 3
        - Are the damage scenarios, the threat scenarios, their impact per impact category and their risk values (1 to 5) identified for the assets?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9421>`, :need:`[[title]] <std_req__isosae21434__assessment_15521>`, :need:`[[title]] <std_req__isosae21434__assessment_15822>`
        - <Rationale for result>

      * - Sec 4
        - Is a risk treatment decision taken for each threat scenario, and are the risks retained because of assumptions documented as such?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9422>`, :need:`[[title]] <std_req__isosae21434__concept_9424>`
        - <Rationale for result>

      * - Sec 5
        - Are the cybersecurity goals and claims consistent with the risk treatment decisions?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9423>`, :need:`[[title]] <std_req__isosae21434__concept_9424>`
        - <Rationale for result>

      * - Sec 6
        - Are the cybersecurity controls, requirements and their allocation to the item defined and consistent with the goals?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9521>`, :need:`[[title]] <std_req__isosae21434__concept_9522>`, :need:`[[title]] <std_req__isosae21434__concept_9523>`
        - <Rationale for result>

      * - Sec 7
        - Is the verification of the analysis result performed: correctness, completeness and consistency of the analysis, the treatment and the claims?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__concept_9425>`, :need:`[[title]] <std_req__isosae21434__concept_9524>`
        - <Rationale for result>

      * - Sec 8
        - Are the assumptions of use of the analysis the same as the assumptions in the security manual?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__prj_management_6451>`
        - <Rationale for result>

      * - Sec 9
        - Is the analysis updated when the item, its environment or the known threats change?
        - [YES | NO ]
        - :need:`[[title]] <std_req__isosae21434__prj_management_6426>`, :need:`[[title]] <std_req__isosae21434__prj_management_6428>`
        - <Rationale for result>

Note: the references link to the requirements modelled on the standards page. The check against the standard text is part of the security manager's review of the analysis checklist.
