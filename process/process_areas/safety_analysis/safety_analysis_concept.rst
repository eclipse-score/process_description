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

This section discusses a concept for safety analyses. As methods for safety analysis are used DFA (Dependent Failure Analysis)
and FMEA (Failure Mode and Effects Analysis). Inputs for this concept are the requirements of ISO26262 Part 6 Chapter 7 and Part 9 Chapter 7 and 8.

The objectives of the DFA are to show that the required freedom from interference is achieved. Therefore the potential causes or initiators are
analysed. The DFA is focussed on common cause failures. With a DFA architectural features are analysed if

 | - there are redundant elements (similar or non-similar)
 | - failures can violate a functions and the safety mechanisms for the function
 | - failures can violate sub-elements

With the DFA shall be shown that the freedom from interference is achieved by the absence of common cause failures. Common cause failures
shall be analysed at feature platform level and for complex components. A complex component is defined as a component where not directly
in the architecture can be seen that the freedom from interference is achieved.

The objective of the FMEA is to show that the risk of systematic faults is reduced to an acceptable level. This shall be done by showing that
systematic faults can be excluded by a full test coverage. Or, if this is not possible, that the systematic faults are mitigated by a sufficient mitigation.
Cascading failures are also considered in the FMEA and not in the DFA. It's because a ASIL decomposition is not applicable at S-CORE.

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

At component level you can see inside of the component when the component consists of two or more sub-components. If the component consists of
only one sub-component there results of the analysis are the same as for the feature level. So no additional consideration is needed.
The component kvstorage consists of two sub-components, kvs and fs. The dynamic diagram shows the communication between the sub-components.


How to add new safety mitigations?
==================================

Identified faults without a mitigation remain open and are tracked in the issue tracking system :need:`wp__issue_track_system` until they are resolved.
A new safety mitigation could be needed if it can't be shown that the feature or component is completely deterministic and testable. In this case an
additional safety mitigation is needed.

.. _examples_fmea_dfa:

Examples for FMEA and DFA at feature level
==========================================

**FMEA:**

The dynamic architecture is analysed with the FMEA. Therefore the template :ref:`FMEA_templates` is used.

.. code-block:: rst

   .. feat_saf_fmea:: <Element descriptor>
      :verifies: <Feature architecture>
      :id: feat_saf_fmea__<Feature>__<Element descriptor>
      :violation_id: <ID from fault model :need:`gd_guidl__fault_models`>
      :violation_cause: "description of failure effect of the fault model on the element"
      :mitigation: <ID from Feature Requirement  ID from AoU Feature Requirement>
      :mitigation_issue: <ID from Issue Tracker>
      :sufficient: <yesno>
      :status: <valid|invalid>
   .. note::   argument is inside the 'content'. Therefore content is mandatory

Use the fault models :need:`gd_guidl__fault_models` to ensure a structured analysis.
Use the content of the document :need:`doc__feature_name_dfa`, :need:`doc__feature_name_fmea`,
:need:`doc__component_name_dfa`, :need:`doc__component_name_fmea` to describe e.g. why
a fault model is not applicable for the diagram.
If there are additional fault models needed, please enlarge the list of fault models.

The dynamic architecture for
"check if key contains default value" is used as an example. The attributes of the template (:ref:`process_requirements_safety_analysis_attributes`)
shall be filled in as follows:

.. code-block:: rst

   .. feat_saf_fmea:: Persistency
      :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
      :id: feat_saf_FMEA__persistency__message_nreived
      :violation_id: MF_01_01
      :violation_cause: Message is not received.
      :mitigates: aou_req__persistency__error_handling
      :sufficient: yes
      :status: valid

      User is not able to use the feature. Middleware cant be used.

.. code-block:: rst

   .. feat_saf_fmea:: Persistency
      :verifies: feat_arc_dyn__persistency__check_key_default, feat_arc_dyn__persistency__delete_key, feat_arc_dyn__persistency__flush, feat_arc_dyn__persistency__read_key, feat_arc_dyn__persistency__read_from_storage, feat_arc_dyn__persistency__write_key, feat_arc_dyn__persistency__snapshot_restore
      :id: feat_saf_FMEA__persistency__late_message
      :violation_id: MF_01_02
      :violation_cause: message received too late.
      :mitigates: aou_req__persistency__error_handling
      :sufficient: yes
      :status: valid

      User is not able to use the feature. Middleware cant be used.

The FMEA is finished, if all fault models are checked and for each identified fault a sufficient mitigation exists. For the validation of the
FMEA the checklist :need:`gd_chklst__safety_analysis` shall be used.

**DFA:**

The static architecture is analysed with the DFA. Therefore the template :ref:`DFA_templates` is used. The goal is to show that
the freedom from interference is achieved.

.. code-block:: rst

      .. feat_saf_dfa:: <Element descriptor>
         :verifies: <Feature architecture>
         :id: feat_saf_DFA__<Feature>__<Element descriptor>
         :violation_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
         :violation_cause: "description of failure effect of the failure initiator on the element"
         :mitigates: <ID from Feature Requirement  ID from AoU Feature Requirement>
         :mitigation_issue: <ID from Issue Tracker>
         :sufficient: <yesno>
         :status: <valid|invalid>
      .. note::   argument is inside the 'content'. Therefore content is mandatory

Use the DFA failure initiators :need:`gd_guidl__dfa_failure_initiators` to ensure a structured analysis.
Use the content of the document :need:`doc__feature_name_dfa`, :need:`doc__feature_name_fmea`,
:need:`doc__component_name_dfa`, :need:`doc__component_name_fmea` to describe e.g. why
a fault model is not applicable for the diagram.
If there are additional failure initiators needed, please enlarge the list of failure initiators.

.. code-block:: rst

   .. feat_saf_dfa:: Persistency
      :verifies: feat_arc_sta__persistency__static
      :id: feat_saf_dfa__persistency__config
      :violation_id: SR_01_07
      :violation_cause: Configuration data. Return values might be falsified.
      :mitigates: feat_req__persistency__integrity_check
      :sufficient: yes
      :status: valid

      Integrity check will fail, so the failure will be detected.


.. code-block:: rst

   .. feat_saf_dfa:: Persistency
      :verifies: feat_arc_sta__persistency__static
      :id: feat_saf_dfa__persistency__arg_passed
      :violation_id: CO_01_01
      :violation_cause: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
      :mitigates: feat_req__persistency__cpp_rust_interop
      :sufficient: yes
      :status: valid

      Failure initiator not applicable at persistency, so no mitigates is needed.

The DFA is finished, if all fault models are checked and for each identified fault a sufficient mitigation exists. For the validation of the
DFA the checklist :need:`gd_chklst__safety_analysis` shall be used.
