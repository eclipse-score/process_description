..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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


.. _workflow_safety_analysis:

Safety Analysis Workflows
#########################

For a detailed explanation of workflows and their role within the process model, please refer to the :ref:`processes_introduction`.

Safety Analysis is used as a umbrella term for the methods FMEA (Failure Modes and Effects Analysis) and DFA (Dependent Failure Analysis).

.. workflow:: Analyze Platform Feature Architecture
   :id: wf__analyse_platform_featarch
   :status: valid
   :version: 1
   :tags: safety_analysis
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :supported_by: rl__contributor[version==1], rl__committer[version==1], rl__security_manager[version==1]
   :input: wp__requirements_feat[version==1], wp__feature_arch[version==1], wp__issue_track_system[version==1]
   :output: wp__platform_dfa[version==1]
   :contains: gd_guidl__dfa_failure_initiators[version==1], gd_temp__plat_saf_dfa[version==1]
   :has: doc_concept__safety_analysis[version==1], doc_getstrt__safety_analysis[version==1]

   | With a platform DFA the potential common usage of features shall be analysed. It shall be used as an input for all other DFA's.
   | There will be only one platform DFA.

.. workflow:: Analyse Feature Architecture
   :id: wf__analyse_featarch
   :status: valid
   :version: 1
   :tags: safety_analysis
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :supported_by: rl__contributor[version==1], rl__committer[version==1], rl__security_manager[version==1]
   :input: wp__requirements_feat[version==1], wp__feature_arch[version==1], wp__issue_track_system[version==1]
   :output: wp__feature_fmea[version==1], wp__feature_dfa[version==1]
   :contains: gd_guidl__dfa_failure_initiators[version==1],
              gd_temp__feat_saf_dfa[version==1],
              gd_guidl__fault_models[version==1],
              gd_temp__feat_saf_fmea[version==1]
   :has: doc_concept__safety_analysis[version==1], doc_getstrt__safety_analysis[version==1]

   | The FMEA and DFA for the feature is executed.

.. workflow:: Analyse Component Architecture
   :id: wf__analyse_comparch
   :status: valid
   :version: 1
   :tags: safety_analysis
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :supported_by: rl__contributor[version==1], rl__committer[version==1], rl__security_manager[version==1]
   :input: wp__requirements_comp[version==1], wp__component_arch[version==1], wp__issue_track_system[version==1]
   :output: wp__sw_component_fmea[version==1], wp__sw_component_dfa[version==1]
   :contains: gd_guidl__dfa_failure_initiators[version==1],
              gd_temp__comp_saf_dfa[version==1],
              gd_guidl__fault_models[version==1],
              gd_temp__comp_saf_fmea[version==1]
   :has: doc_concept__safety_analysis[version==1], doc_getstrt__safety_analysis[version==1]

   | The FMEA and DFA for the component is executed.

.. workflow:: Monitor FMEA and DFA
   :id: wf__mr_saf_analyses_dfa
   :status: valid
   :version: 1
   :tags: safety_analysis
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :supported_by: rl__contributor[version==1], rl__committer[version==1], rl__security_manager[version==1]
   :input: wp__feature_fmea[version==1],
           wp__feature_dfa[version==1],
           wp__sw_component_fmea[version==1],
           wp__sw_component_dfa[version==1]
   :output: wp__verification_platform_ver_report[version==1], wp__issue_track_system[version==1], wp__verification_module_ver_report[version==1]
   :contains: gd_guidl__dfa_failure_initiators[version==1],
              gd_temp__feat_saf_dfa[version==1],
              gd_temp__comp_saf_dfa[version==1],
              gd_guidl__fault_models[version==1],
              gd_temp__feat_saf_fmea[version==1],
              gd_temp__comp_saf_fmea[version==1]
   :has: doc_concept__safety_analysis[version==1], doc_getstrt__safety_analysis[version==1]

   | The FMEA and DFA are monitored.

.. workflow:: Verify FMEA and DFA
   :id: wf__vy_saf_analyses_dfa
   :status: valid
   :version: 1
   :tags: safety_analysis
   :responsible: rl__safety_engineer[version==1]
   :approved_by: rl__safety_manager[version==1]
   :supported_by: rl__contributor[version==1], rl__committer[version==1], rl__security_manager[version==1]
   :input: wp__platform_dfa[version==1],
           wp__feature_fmea[version==1],
           wp__feature_dfa[version==1],
           wp__sw_component_fmea[version==1],
           wp__sw_component_dfa[version==1]
   :output: wp__verification_platform_ver_report[version==1], wp__verification_module_ver_report[version==1]
   :contains: gd_guidl__dfa_failure_initiators[version==1],
              gd_temp__feat_saf_dfa[version==1],
              gd_temp__comp_saf_dfa[version==1],
              gd_guidl__fault_models[version==1],
              gd_temp__feat_saf_fmea[version==1],
              gd_temp__comp_saf_fmea[version==1],
              gd_chklst__safety_analysis[version==1]
   :has: doc_concept__safety_analysis[version==1], doc_getstrt__safety_analysis[version==1]

   | The FMEA and DFA are verified. The verification criteria is that it can be proven that the safety requirements for functions and the corresponding safety monitoring are not violated.


RAS(IC) for Safety Analysis  (FMEA and DFA)
*******************************************


.. needtable:: RASIC Overview for Safety Analysis  (FMEA and DFA)
   :tags: safety_analysis
   :filter: "safety_analysis" in tags and type == "workflow" and is_external == False
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
