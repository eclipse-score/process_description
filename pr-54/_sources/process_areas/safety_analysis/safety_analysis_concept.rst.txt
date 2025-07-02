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

This section discusses a concept for safety analyses. As methods for safety analysis were used DFA (Dependent Failure Analysis)
and FMEA (Failure Mode and Effects Analysis). Inputs for this concept are the requirements of ISO26262 Part 6 Chapter 7 and Part 9 Chapter 7 and 8.

The objectives of the DFA are to show that the required freedom from interference is achieved. Therefore the potential causes or initiators are
analysed. The DFA is focussed on common cause failures. With a DFA architectural features are analysed if

 | - there are redundant elements (similar or non-similar)
 | - identical software is implemented in different features or components
 | - failures can violate a functions and the safety mechanisms for the function
 | - failures an violate partitions of features or components

With the DFA shall be shown that the freedom from interference is achieved by the absence of common cause failures.

The objective of the FMEA is to show that the risk of systematic faults is reduced to an acceptable level. This shall be done by showing that
systematic faults can be excluded by a full test coverage. Or, if this is not possible, that the systematic faults are mitigated by a sufficient mitigation.
Cascading failures are also considered in the FMEA and not in the DFA. Is is because it it's not applicable to use within S-CORE a ASIL decomposition.

Inputs
******

#. Stakeholders for the safety analysis (DFA and FMEA)?
#. Who needs which information?
#. How to analyse existing safety mitigation?
#. How to add new safety mitigations?

Stakeholders for the Safety Analysis (DFA and FMEA)
===================================================

#. :need:`Safety Engineer <rl__safety_engineer>`

   * Analyse the platform feature architecture with a Platform Feature DFA
   * Analyse the feature architecture with a Feature FMEA and Feature DFA
   * Analyse the component architecture with a Component FMEA and Component DFA
   * Monitor/verify the FMEA and DFA

#. :need:`Safety Manager <rl__safety_manager>`

   * Approve the FMEA and DFA
   * Approve the verification of the FMEA and DFA

#. :need:`Contributor <rl__contributor>`

   * Support the FMEA and DFA
   * Support the monitoring and verifying of the FMEA and DFA

#. :need:`Committer <rl__committer>`

   * Support the FMEA and DFA
   * Support the monitoring and verifying of the FMEA and DFA

#. :need:`Security Manager <rl__security_manager>`

   * Support the FMEA and DFA
   * Support the monitoring and verifying of FMEA and DFA


Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO26262
* ISO SAE 21434

How to analyse?
===============

The safety analysis (DFA and FMEA) is done on the feature and component architecture. The safety analysis (DFA and FMEA) shall be done accompanying to the development.
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

The FMEA is done with the shown diagrams. The interface 1 and 2 are the interfaces of the feature. These interfaces shall be analysed with the
fault models :need:`gd_guidl__fault_models` that here could be applied. With the dynamic diagrams the communication between the components can be analysed.
The static diagrams are used to analyse the dependencies. For violations a failure mitigation shall be defined.

.. figure:: _assets/safety_analysis_component.drawio.svg
   :align: center
   :width: 80%
   :name: safety_analysis_component_fig

   Safety Analysis Component Perspective

At component level you can see inside of the component when the component consists of two or more sub-components. If the component consists of
only one sub-component there results of the analysis are the same as for the feature level. So no additional consideration is needed.
The component kvstorage consists of two sub-components, kvs and fs. The dynamic diagram shows the communication between the sub-components.


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
|    :mitigation: Detection and error handling shall be done outside of the middleware.
|    :mitigation_issue: ID from Issue Tracker that defined mitigation will be documented in the assumptions of use (AoU)
|    :sufficient: yes
|    :status: valid
        This error is handled by the calling application.

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
|    :status: valid
        The integrity check will ensure that the data is not corrupted and the feature will work as expected.

Use the DFA failure initiators :need:`gd_guidl__dfa_failure_initiators` to ensure a structured analysis. If a failure initiator doesn't apply,
please fill in a short description in the violation cause of the analysis so it could be recognized that the analysis is done. If there are
additional failure initiators needed, please enlarge the list of fault models.
