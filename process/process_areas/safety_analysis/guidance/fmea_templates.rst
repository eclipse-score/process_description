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

.. _FMEA_templates:

FMEA Templates
==============

.. gd_temp:: Feature FMEA Template
   :id: gd_temp__feat_saf_fmea
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_wp__isopas8926__4524, std_req__iso26262__software_7410, std_req__iso26262__software_7412, std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_845, std_req__iso26262__analysis_846, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431

.. code-block:: rst

    .. feat_saf_fmea:: <Element descriptor>
       :violates: <Feature architecture>
       :id: feat_saf_fmea__<Feature>__<Element descriptor>
       :fault_id: <ID from fault model :need:`gd_guidl__fault_models`>
       :failure_effect: "description of failure effect of the fault model on the element"
       :mitigated_by: <ID from Feature Requirement | ID from AoU Feature Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>
.. note::   argument is inside the 'content'. Therefore content is mandatory

.. gd_temp:: Component FMEA Template
   :id: gd_temp__comp_saf_fmea
   :status: valid
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_wp__isopas8926__4524, std_req__iso26262__software_7410, std_req__iso26262__software_7412, std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_845, std_req__iso26262__analysis_846, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431

.. code-block:: rst

    .. comp_saf_fmea:: <Element descriptor>
       :violates: <Component architecture>
       :id: comp_saf_fmea__<Component>__<Element descriptor>
       :fault_id: <ID from fault model :need:`gd_guidl__fault_models`>
       :failure_effect: "description of failure effect of the fault model on the element"
       :mitigated_by: <ID from Component Requirement | ID from AoU Component Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>
.. note::   argument is inside the 'content'. Therefore content is mandatory
