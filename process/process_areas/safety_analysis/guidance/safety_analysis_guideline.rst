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


Safety Analysis Guidelines
##########################

.. gd_guidl:: Safety Analysis (DFA and FMEA) Guideline
   :id: gd_guidl__safety_analysis
   :status: valid
   :complies: std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431, std_req__isopas8926__44432

This document describes the general guidances for Safety Analysis (DFA and FMEA) based on the concept which is defined :need:`Safety Analysis Concept<doc_concept__safety__analysis>`.

Workflow for Platform Feature DFA
=================================

The dependencies between platform features are analysed by performing a **single platform feature DFA**. The platform feature DFA shall be updated for every platform release.

#. Analyse the dependencies between features by performing a single platform feature DFA that references all platform feature static architecture diagrams, highlighting potential shared use of modules.
#. Monitor the results of the platform feature DFA and log any issues in the Issue Tracking system with the ``safety`` label.
#. Verify the platform feature DFA results by using :need:`gd_chklst__safety_analysis`.
#. Platform feature DFA is completed when the verification is done, no issues are open and the status is "valid". The verification criteria is that it can be proven that a function and the corresponding safety monitoring are not both affected.

Workflow for Safety Analysis at Feature and Component Level
===========================================================

For the safety analysis (FMEA and DFA) this workflow shall be applied at feature and component level:

#. Analyse the Architecture (Feature and Component) with a FMEA and a DFA. If it's not applicable to perform a safety analysis a argumentation shall be documented in the content field of the analysis. The results of other safety analysis also from platform feature DFA can be used as an input.
#. Monitor the results of the FMEA and DFA and log any issues in the Issue Tracking system with the ``safety`` label.
#. Verify the FMEA and DFA results by using :need:`gd_chklst__safety_analysis`.
#. The safety analysis are completed when the verification is done, no issues are open and the status is "valid".

Step-by-Step-approach FMEA:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template :ref:`FMEA_templates` on the feature or component architectural diagrams. By using the fault models <:need:`gd_guidl__fault_models`>
it can be ensured that the analysis is done in a structured way.
Apply the fault model to the diagram and document the results in the template. Use the content of the document :need:`doc__feature_name_fmea`, :need:`doc__component_name_fmea`
to describe e.g. why a fault model is not applicable for the diagram. If a FMEA can't be applied, the reason has to be documented in the
content of the document, so it can be recognized.

The attributes of the template are described in :ref:`process_requirements_safety_analysis_attributes`.

**Steps:**

#. For each architectural element check if a fault from the fault model :need:`gd_guidl__fault_models` applies.
#. If a fault model applies, use the template :need:`gd_temp__feat_saf_fmea` or :need:`gd_temp__comp_saf_fmea` to perform the analysis.
#. Fill out the title of the analysis with the element descriptor. So it should be easily recognizable which element is analysed.
#. Link the violated architecture with the "violates" attribute.
#. Fill out the id of the FMEA with in the style of ``feat_saf_fmea__<Feature>__<Element descriptor>`` or ``comp_saf_fmea__<Component>__<Element descriptor>``.
#. Document the fault ID from the fault model :need:`gd_guidl__fault_models` that applies to the element in the "fault_id" attribute.
#. Describe the failure effect of the fault model on the element in the "failure_effect" attribute. Use the generic failure effect descriptions and enlarge the if it's applicable to the considered element.
#. Document the safety mitigation. This can be a detection, prevention or mitigation of the fault.
#. If there is no mitigation or existing mitigation is not sufficient a mitigation issue has to be created in the Issue Tracking system and linked in the "mitigation_issue" attribute.
#. The analysis is finished, if for each identified fault a sufficient mitigation exists.
#. Unless the attribute sufficient is yes, mitigation and argument attribute can be still empty.
#. Continue the analysis until all applicable fault models are checked.
#. The verification is done by applying the checklist :need:`gd_chklst__safety_analysis`.

.. note:: If there are changes they have to be analysed with a impact analysis :need:`gd_temp__change__impact_analysis`. If needed the safety analysis (DFA or FMEA) has to be updated accordingly. Therefore all necessary steps have to be repeated.


Step-by-Step-approach DFA:
^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template :ref:`dfa_templates` on the feature or component architectural diagrams using a list of DFA failure initiators <:need:`gd_guidl__dfa_failure_initiators`>.
Use the content of the document :need:`doc__feature_name_dfa`, :need:`doc__component_name_dfa` to describe e.g. why
a failure initiator is not applicable for the diagram. If a DFA can't be applied, the reason has to be documented in the content of the document, so it
can be recognized.

The attributes of the template are described in :ref:`process_requirements_safety_analysis_attributes`.

**Steps:**

#. For each architectural element check if a failure from the failure initiators :need:`gd_guidl__dfa_failure_initiators` applies.
#. If a failure initiator applies, use the template :need:`gd_temp__feat_saf_dfa` or :need:`gd_temp__comp_saf_dfa` to perform the analysis.
#. Fill out the title of the analysis with the element descriptor. So it should be easily recognizable which element is analysed.
#. Link the violated architecture with the "violates" attribute.
#. Fill out the id of the DFA with in the style of ``feat_saf_dfa__<Feature>__<Element descriptor>`` or ``comp_saf_dfa__<Component>__<Element descriptor>``.
#. Document the failure ID from the failure initiator :need:`gd_guidl__dfa_failure_initiators` that applies to the element in the "failure_id" attribute.
#. Describe the failure effect of the fault model on the element in the "failure_effect" attribute. Use the generic failure effect descriptions and enlarge the if it's applicable to the considered element.
#. Document the safety mitigation. This can be a detection, prevention or mitigation of the fault.
#. If there is no mitigation or the mitigation is not sufficient a mitigation issue has to be created in the Issue Tracking system and linked in the "mitigation_issue" attribute.
#. The analysis is finished, if for each identified fault a sufficient mitigation exists.
#. Unless the attribute sufficient is yes, mitigation and argument attribute can be still empty.
#. Continue the analysis until all applicable fault models are checked.
#. The verification is done by applying the checklist :need:`gd_chklst__safety_analysis`.

.. note:: If there are changes they have to be analysed with a impact analysis :need:`gd_temp__change__impact_analysis`. If needed the safety analysis (DFA or FMEA) has to be updated accordingly. Therefore all necessary steps have to be repeated.

.. _examples_fmea_dfa:

Examples for FMEA and DFA at feature level
==========================================

For the examples the architectural diagrams :ref:`safety_analysis_feature_example` are used. The feature architecture is shown in the figure :ref:`safety_analysis_feature_fig`.

**FMEA:**

The dynamic architecture is analysed with the FMEA. Therefore the template :ref:`FMEA_templates` is used.

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

Use the fault models :need:`gd_guidl__fault_models` to ensure a structured analysis.
Use the content of the document :need:`doc__feature_name_fmea`, :need:`doc__component_name_fmea` to describe e.g. why
a fault model is not applicable for the diagram. If there are additional fault models needed, please enlarge the list of fault models.

The dynamic architecture of the feature architecture is used as an example. The attributes of the template (:ref:`process_requirements_safety_analysis_attributes`)
shall be filled in as follows:

.. code-block:: rst

    .. feat_saf_fmea:: Component 1 Call message not received
       :violates: feat_arc_dyn__Mab__dynamic
       :id: feat_saf_fmea__Mab__Component_1
       :fault_id: MF_01_01
       :failure_effect: Message is not received. Component 1 will not be called.
       :mitigated_by: aou_req__Mab__func_call
       :mitigation_issue:
       :sufficient: yes
       :status: valid

      If the message is not received the feature will not be called. Therefore possible faults have to be mitigated, detected or avoided
      by the Use. This requirement is addressed by the AoU requirement aou_req__Mab__func_call. Because of a mitigation exists there is no
      need to create an mitigation issue.

.. code-block:: rst

    .. feat_saf_fmea:: Component 2 unintended triggered
       :violates: feat_arc_dyn__Mab__dynamic
       :id: feat_saf_fmea__Mab__Component_2
       :fault_id: MF_01_07
       :failure_effect: Message is unintended sent. Component 2 will be unintended triggered.
       :mitigated_by: feat_req__Mab__func_call_monitor
       :mitigation_issue:
       :sufficient: yes
       :status: valid

      An unintended trigger of the component 2 is detected shall be detected. Therefore the requirement feat_req__Mab__func_call_monitor is created.

The FMEA is finished, if all fault models are checked and for each identified fault a sufficient mitigation (e.g. prevention, detection or mitigation) exists. For the validation of the
FMEA the checklist :need:`gd_chklst__safety_analysis` shall be used. For all fault models that are not applicable, the reason has to be documented
in the content of the document, so it can be recognized.

**DFA:**

The static architecture is analysed with the DFA. Therefore the template :ref:`DFA_templates` is used. The goal is to show that
the freedom from interference is achieved.

.. code-block:: rst

    .. feat_saf_dfa:: <Element descriptor>
       :violates: <Feature architecture>
       :id: feat_saf_DFA__<Feature>__<Element descriptor>
       :failure_id: <ID from DFA failure initiators :need:`gd_guidl__dfa_failure_initiators`>
       :failure_effect: "description of failure effect of the failure initiator on the element"
       :mitigated_by: <ID from Feature Requirement | ID from AoU Feature Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :status: <valid|invalid>
.. note::   argument is inside the 'content'. Therefore content is mandatory

Use the DFA failure initiators :need:`gd_guidl__dfa_failure_initiators` to ensure a structured analysis.
Use the content of the document :need:`doc__feature_name_dfa`, :need:`doc__component_name_fmea` to describe e.g. why
a fault model is not applicable for the diagram. If there are additional failure initiators needed, please enlarge the list of failure initiators.

.. code-block:: rst

    .. feat_saf_dfa:: <Element descriptor>
       :violates: feat_arc_sta__Mab__static
       :id: feat_saf_DFA__Mab__call_Component_1
       :failure_id: SI_01_03
       :failure_effect: Constants, or variables, being global to the two software functions
       :mitigated_by:
       :mitigation_issue: link_to_issue_tracker/issues/issue_1234
       :sufficient: no
       :status: invalid

      To avoid the failure cause a issue is created in the issue tracker. The issue is not resolved yet, therefore the mitigation (e.g. prevention, detection or mitigation) is not sufficient.


.. code-block:: rst

    .. feat_saf_dfa:: <Element descriptor>
       :violates: feat_arc_sta__Mab__static
       :id: feat_saf_DFA__<Feature>__<Element descriptor>
       :failure_id: UI_01_11
       :failure_effect: Memory depletion
       :mitigated_by: feat_req__Mab__MMU
       :mitigation_issue:
       :sufficient: yes
       :status: valid

      The memory will be managed by the MMU. Therefore the requirement feat_req__Mab__MMU is created.

The DFA is finished, if all fault models are checked and for each identified fault a sufficient mitigation (e.g. prevention, detection or mitigation) exists. For the validation of the
DFA the checklist :need:`gd_chklst__safety_analysis` shall be used.
