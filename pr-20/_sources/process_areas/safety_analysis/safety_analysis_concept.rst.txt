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

Concept Description
###################

.. doc_concept:: Safety Analysis Concept
   :id: doc_concept__safety__analysis
   :status: valid
   :tags: safety_analysis

This section discusses a concept for safety analyses. Inputs for this concept are the requirements of ISO26262 Part 6 Chapter 7 and Part 9 Chapter 7 and 8.

Inputs
******

#. Stakeholders for the safety analysis?
#. Who needs which information?
#. How to analyze existing safety mitigation?
#. How to add new safety mitigations?

Stakeholders for the Safety Analysis
====================================

#. :need:`Safety Engineer <rl__safety_engineer>`

   * Analyse the platform feature architecture with a DFA
   * Analyse the feature architecture with a Safety Analysis and DFA
   * Analyse the component architecture with a Safety Analysis and DFA
   * Monitor/verify the Safety Analysis and DFA

#. :need:`Safety Manager <rl__safety_manager>`

   * Approve the safety analysis and DFA
   * Approve the verification of the safety analysis and DFA   

#. :need:`Contributor <rl__contributor>`

   * Support the safety analyses and DFA
   * Support the monitoring and verifying of the safety analyses and DFA

#. :need:`Committer <rl__committer>`

   * Support the safety analyses and DFA
   * Support the monitoring and verifying of the safety analyses and DFA

#. :need:`Security Manager <rl__security_manager>`

   * Support the safety analyses and DFA
   * Support the monitoring and verifying of the safety analyses and DFA


Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO26262
* ISO SAE 21434

How to analyze?
===============

The safety analysis is done on the feature and component architecture. The safety analysis shall be done accompanying to the development.
So the results can directly be used for the development of the feature and component. With a iterative approach it is needed to proof
the evidence of the functional safety of the functions.

The analysis starts at feature level. With a DFA shall be analysed if there are dependent failures which have to be considered. The analysis
shall be done in the way that we use the static and dynamic diagrams. The following picture shall show the perspective of the User.

.. _safety_analysis_feature_example:

.. figure:: _assets/safety_analysis_feature.drawio.svg
   :align: center
   :width: 80%
   :name: safety_analysis_feature_fig

   Dynamic Architecture 

The safety analysis is done with the shown diagrams. The interface 1 and 2 are the interfaces of the feature. These interfaces shall be analyzed with the
fault models :need:`gd_guidl__fault_models` that here could be applied. With the dynamic diagrams the communication between the components can be analysed. 
The static diagrams are used to analyse the dependencies. For violations a failure mitigation shall be defined. 

.. figure:: _assets/safety_analysis_component.drawio.svg
   :align: center
   :width: 80%
   :name: safety_analysis_component_fig

   Safety Analysis Component Perspective

At component level you can see inside of the component when the component consists of two or more subcomponents. If the component consists of 
only one subcomponent there results of the analysis are the same as for the feature level. So no additional consideration is needed.
The component kvstorage consists of two subcomponents, kvs and fs. The dynamic diagram shows the communication between the subcomponents.

DFA
^^^

A DFA :ref:`dfa_templates` shall be used to proof the absence of dependent failures. For the analysis a list
of DFA failure initiators :need:`gd_guidl__dfa_failure_initiators` is available. A step by step approach is recommended to
ensure that all dependent failures are identified :need:`gd_guidl__safety_analysis`. Every failure initiator shall be checked
and if it applies to the feature or component, a mitigation shall be defined. If the failure initiator doesn't apply, a short description
shall be added to the violation cause of the analysis so it could be recognized that the analysis is done. 

Safety Analysis
^^^^^^^^^^^^^^^

For the safety analyses the templates :ref:`safety_analysis_templates` shall be used. For the safety analysis we selected
the method FMEA on feature and component level. The safety analysis is done on architectural diagrams (state and sequence diagrams).
For the safety analysis fault models shall be used :need:`gd_guidl__fault_models`.  A step by step approach is recommended to
ensure that all dependent failures are identified :need:`gd_guidl__safety_analysis`. Every fault model shall be checked
and if it applies to the feature or component, a mitigation shall be defined. If the fault model doesn't apply, a short description
shall be added to the violation cause of the analysis so it could be recognized that the analysis is done.

How to add new safety mitigations?
==================================

Identified faults without a mitigation remain open and are tracked in the issue tracking system :need:`wp__issue_track_system` until they are resolved.

.. _examples_fmea_dfa:

Examples for FMEA and DFA at feature level
==========================================

**FMEA:**

| .. feat_saf_fmea:: Remove key
|    :verifies: feat_arc_dynamic__kvstorage__remove_key
|    :id: FEAT_SAF_FMEA__KVSTORAGE__RemoveKey
|    :failure_mode: "MF_01_01"
|    :failure_effect: "message is not received"
|    :mitigation: Detetion and error handling shall be done outside of the middleware.
|    :mitigation_issue: ID from Issue Tracker that defined mitigation will be documented in the assumtions of use (AoU)
|    :sufficient: yes
|    :argument: This error is handled by the calling application.
|    :status: valid

Use the fault models :need:`gd_guidl__fault_models` to ensure a structured analysis. If a fault model doesn't apply, 
please fill in a short description in the violation cause of the analysis so it could be recognized that the analysis 
is done. If there are additional fault models needed, please enlarge the list of fault models.

**DFA:**

| .. feat_saf_dfa:: Static Architecture Persistency
|    :verifies: feat_arc_sta_persistency_static
|    :id: feat_saf_DFA__persistency__json_al
|    :violation_id: "CO_01_02"
|    :violation_cause: "Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information. Failures will lead to falsified execution or to a not available feature.
|    :mitigation: feat_req__persistency__integrity_check
|    :mitigation_issue: None
|    :sufficient: yes
|    :argument: The integrity check will ensure that the data is not corrupted and the feature will work as expected.
|    :status: valid

Use the DFA failure initiators :need:`gd_guidl__dfa_failure_initiators` to ensure a structured analysis. If a failure initiator doesn't apply,
please fill in a short description in the violation cause of the analysis so it could be recognized that the analysis is done. If there are 
additional failure initiators needed, please enlarge the list of fault models.