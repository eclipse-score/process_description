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

.. _dfa_templates:

DFA Templates
=============

.. gd_temp:: Feature Platform DFA Templates
   :id: gd_temp__feat_plat_saf_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749, std_req__isopas8926__44432

.. code-block:: rst

    .. feat_plat_saf_dfa:: <Title>
       :violates: <Feature architecture>
       :id: feat_saf_dfa__<Feature>__<Element descriptor>
       :failure_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
       :failure_effect: "description of failure effect of the failure initiator on the element"
       :mitigated_by: <ID from Feature Requirement | ID from AoU Feature Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>
.. note::   argument is inside the 'content'. Therefore content is mandatory


.. gd_temp:: Feature DFA Templates
   :id: gd_temp__feat_saf_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749, std_req__isopas8926__44432

   For the content see here: :need:`doc__feature_name_dfa`


.. gd_temp:: Component DFA Templates
   :id: gd_temp__comp_saf_dfa
   :status: valid
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753, std_wp__isopas8926__4524, std_req__iso26262__software_7411, std_req__iso26262__analysis_741, std_req__iso26262__analysis_742, std_req__iso26262__analysis_743, std_req__iso26262__analysis_745, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747, std_req__iso26262__analysis_748, std_req__iso26262__analysis_749, std_req__isopas8926__44432

   For the content see here: :need:`doc__component_name_dfa`
