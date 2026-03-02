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


Platform Safety Analysis Checklist
==================================

.. document:: [Your Platform Name] Safety Analysis Checklist
   :id: doc__platform_name_safety_analysis_fdr
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__fdr_reports
   :tags: template

.. attention::
    The above directive must be updated according to your Platform.

    - Modify ``Your Platform Name`` to be your Platform Name
    - Modify ``id`` to be your Platform Name in lower snake case preceded by ``doc__`` and followed by ``_safety _analysis_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety``, ``security`` and ``tags`` according to your needs


**Purpose**
The purpose of this Safety Analysis (DFA and FMEA) checklist template is to collect the topics to be checked during verification of the Safety Analysis.

**Conduct**
As described in :need:`wf__p_formal_rv`, the formal document review is performed by an "external" safety manager:

- reviewer: <committer with safety manager skills explicitly named here>

**Checklist**

Please note that it is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additional to add in the remarks why it is passed or not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column. See also :ref:`review_concept` for further information about reviews in general and inspection in particular.

.. list-table:: Safety Analysis Checklist
      :header-rows: 1
      :widths: 10,10,30,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - 1
        - Is it plausible that each potential identified dependent failure that has been identified, will lead to a dependent failure which cause a violation of FFI?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_742>`
        - <Rationale for result>

      * - 2
        - Are the failure initiators :need:`[[title]] <gd_guidl__dfa_failure_initiators>` / fault models :need:`[[title]] <gd_guidl__fault_models>` applied?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_744>`
        - <Rationale for result>

      * - 3
        - Are measures defined to resolute the identified potential dependent failures?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_746>`, :need:`[[title]] <std_req__iso26262__analysis_747>`
        - <Rationale for result>

      * - 4
        - Is the result of the safety analysis indicate if the safety requirements are complied?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_842>`
        - <Rationale for result>

      * - 5
        - Are for all not complied safety requirements mitigations defined to resolute the non-compliance? The mitigations shall have a direct influence on the violation by prevention, detection or mitigation to reduce the risk to an acceptable level.
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_843>`
        - <Rationale for result>

      * - 6
        - Are the mitigations effective and implemented?
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_844>`
        - <Rationale for result>

      * - 7
        - Are the templates for DFA and/or FMEA used? See :ref:`dfa_templates` / :ref:`FMEA_templates` and also :ref:`process_requirements_safety_analysis`
        - [YES | NO ]
        - :need:`[[title]] <std_req__iso26262__analysis_748>`, :need:`[[title]] <std_req__iso26262__analysis_849>`, :need:`[[title]] <std_req__iso26262__analysis_8410>`
        - <Rationale for result>
