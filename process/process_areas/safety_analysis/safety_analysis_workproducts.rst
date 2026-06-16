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

Safety Analysis Work Products
#############################

.. workproduct:: Platform DFA
   :id: wp__platform_dfa
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__analysis_751[version==1], std_wp__iso26262__software_753[version==1], std_wp__isopas8926__4524[version==1]

   Analyse the dependencies between features that references all platform feature static architecture diagrams, highlighting potential shared use of features.

.. workproduct:: Feature FMEA
   :id: wp__feature_fmea
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__analysis_851[version==1], std_wp__iso26262__software_752[version==1], std_wp__isopas8926__4524[version==1]

   FMEA verifies the feature architecture (as part of SW Safety Concept)

   Detections, preventions, mitigations linked to Software Feature Requirements or Feature Assumptions of Use.

.. workproduct:: Feature DFA
   :id: wp__feature_dfa
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__analysis_751[version==1], std_wp__iso26262__software_753[version==1], std_wp__isopas8926__4524[version==1]

   Dependent Failure Analysis on feature level.

   Detections, preventions, mitigations linked to Software Feature Requirements or Feature Assumptions of Use.

   Perform analysis on interactions between safety related and non-safety related components or components with different ASIL of one feature.

.. workproduct:: Component FMEA
   :id: wp__sw_component_fmea
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__analysis_851[version==1],
              std_wp__iso26262__software_752[version==1],
              std_wp__isopas8926__4524[version==1],
              std_wp__iso26262__software_752[version==1]

   FMEA, verifies the component architecture (as part of SW Safety Concept)

   Detections, preventions, mitigations linked to Software Component Requirements or Assumptions of Use.

.. workproduct:: Component DFA
   :id: wp__sw_component_dfa
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__analysis_751[version==1],
              std_wp__iso26262__software_753[version==1],
              std_wp__isopas8926__4524[version==1],
              std_wp__iso26262__software_752[version==1]

   Dependent Failure Analysis on component level.

   Detections, preventions, mitigations linked to Software Component Requirements or Assumptions of Use.

   Perform analysis of safety related and non-safety related sub-elements or sub-elements with different ASIL.

   Perform analysis on interactions between safety related and non-safety related lower level components or lower level components with different ASIL of one (higher level) component.
