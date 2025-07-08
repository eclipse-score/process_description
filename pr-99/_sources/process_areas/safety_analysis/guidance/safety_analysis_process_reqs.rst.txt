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

.. _process_requirements_safety_analysis:

Safety Analysis Process Requirements
====================================

.. gd_req:: Safety Analysis Structure
   :id: gd_req__saf__structure
   :status: valid
   :tags: done_automation, safety_analysis
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__support_6432

   Safety Analysis shall be hierarchically grouped into different levels.

   Following levels are defined:

      * Feature architecture
      * Component architecture

.. _process_requirements_safety_analysis_attributes:

Process Safety Analysis Attributes
----------------------------------

.. gd_req:: Safety Analysis attribute: UID
   :id: gd_req__saf__attr_uid
   :status: valid
   :tags: done_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6432

   Each Safety Analysis shall have a unique ID. It shall be in a format which is also human readable and consists of

      * type of Safety Analysis
      * keyword describing the level of analysis
      * keyword describing the content of the Safety Analysis

   The naming convention shall be defined in the project and shall be used consistently.

.. gd_req:: Safety Analysis attribute: title
   :id: gd_req__saf__attr_title
   :status: valid
   :tags: manual, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__support_6424

   The title of the Safety Analysis shall provide a short summary of the description

.. gd_req:: Safety Analysis attribute: mitigation
   :id: gd_req__saf__attr_mitigation
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_844, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747

   Each violation shall have an associated mitigation. The mitigation may be a requirement or a brief description of the mitigation.
   Use "None" if a mitigation has not yet been implemented, and update it once completed.

.. gd_req:: Safety Analysis attribute: mitigation issue
   :id: gd_req__saf__attr_mitigation_issue
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_844, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747

   For every mitigation that is needed a issue shall be created. If a mitigation is already implemented without
   an issue, please remark it so this can be reconstructed.

.. gd_req:: Safety Analysis attribute: sufficient
   :id: gd_req__saf__attr_sufficient
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749, std_req__isopas8926__44431, std_req__isopas8926__44432

   Each mitigation shall have a statement if it's sufficient.

.. gd_req:: Safety Analysis attribute: argument
   :id: gd_req__saf__attr_argument
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749, std_req__isopas8926__44433

   The argument shall describe why the mitigation is sufficient or not. If it is not sufficient, the argument shall describe how the mitigation
   can be improved to achieve sufficiency.

.. gd_req:: Safety Analysis attribute: status
   :id: gd_req__saf__attr_status
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749, std_req__isopas8926__44431, std_req__isopas8926__44432

   Each safety analysis shall have the status invalid until the analysis is finished. The status shall be set to valid if the analysis is finished and all issues are closed.

.. _process_requirements_safety_analysis_linkage:

Safety Analysis Linkage
'''''''''''''''''''''''

.. gd_req:: Safety Analysis Linkage check
   :id: gd_req__saf__linkage_check
   :status: valid
   :tags: prio_1_automation, attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_842, std_req__iso26262__software_7410, std_req__iso26262__software_7411

   Safety Analysis shall be linked to at least one dynamic diagram of the architecture on the corresponding level via the attribute verifies.

.. gd_req:: Safety Analysis Linkage
   :id: gd_req__saf__linkage
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_842, std_req__iso26262__software_7410, std_req__iso26262__software_7411

   Each Safety Analysis shall be automatically linked to the corresponding dynamic diagram via the "verified by" linkage.

.. gd_req:: Safety Analysis attribute: check Requirements linkage
   :id: gd_req__saf__attr_requirements_check
   :status: valid
   :tags: prio_1_automation, attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_842, std_req__iso26262__software_7410, std_req__iso26262__software_7411

   Safety Analysis shall be linked to a requirement on the corresponding level via the attribute "mitigated by".

.. gd_req:: Safety Analysis attribute: Requirements linkage
   :id: gd_req__saf__attr_requirements
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_842, std_req__iso26262__software_7410, std_req__iso26262__software_7411

   Each Safety Analysis shall be automatically linked to the corresponding Safety Requirement via the mitigates linkage.

.. gd_req:: Safety Analysis attribute: link to Aou
   :id: gd_req__saf__attr_aou
   :status: valid
   :tags: prio_1_automation, attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_845

   It shall be possible to link Aou.

.. gd_req:: Safety Analysis attribute: versioning
   :id: gd_req__saf__attr_hash
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6434

   It shall be possible to provide a versioning for Safety Analysis. It shall be possible to detect any differences in mandatory attributes compared to the versioning: :need:`gd_req__saf__attr_mandatory`


.. _process_requirements_safety_analysis_checks:

Process Requirements Checks
'''''''''''''''''''''''''''

.. gd_req:: Safety Analysis mandatory attributes provided
   :id: gd_req__saf__attr_mandatory
   :status: valid
   :tags: prio_1_automation, attribute, check
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   It shall be checked if all mandatory attributes for each Safety Analysis are provided by the user. For all Safety Analysis following attributes shall be mandatory:

   .. needtable:: Overview mandatory Safety Analysis attributes
      :filter: "mandatory" in tags and "attribute" in tags and "safety_analysis" in tags and type == "gd_req"
      :style: table
      :columns: title
      :colwidths: 30


.. gd_req:: Safety Analysis linkage safety
   :id: gd_req__saf__linkage_safety
   :status: valid
   :tags: prio_2_automation, attribute, check
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   It shall be checked that Safety Analysis (Safety != QM) can only be linked against elements with the same ASIL.

DFA Process Requirements
========================

.. gd_req:: DFA attribute: violation ID
   :id: gd_req__saf__attr_vid
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6432

   Each DFA shall have a violation ID. The violation ID is used to identify the related fault <:need:`gd_guidl__dfa_failure_initiators`>.

.. gd_req:: DFA attribute: violation cause
   :id: gd_req__saf__attr_vcause
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_742

   Every DFA shall have a short description of the violation cause.

FMEA Process Requirements
=========================

.. gd_req:: FMEA attribute: failure mode
   :id: gd_req__saf__attr_fmode
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848

   Each FMEA shall have a failure mode. The failure mode is used to identify the related fault <:need:`gd_guidl__fault_models`>.

.. gd_req:: FMEA attribute: failure effect
   :id: gd_req__saf__attr_veffect
   :status: valid
   :tags: prio_1_automation, attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_849

   Every FMEA shall have a short description of the failure effect.


.. needextend:: docname is not None and "process_areas/safety_analysis" in docname
   :+tags: safety_analysis
