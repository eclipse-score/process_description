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


Guidelines
##########

.. gd_guidl:: Safety Analysis Guideline
   :id: gd_guidl__safety_analysis
   :status: valid
   :complies: std_req__iso26262__analysis_841, std_req__iso26262__analysis_842, std_req__iso26262__analysis_843, std_req__iso26262__analysis_844, std_req__iso26262__analysis_847, std_req__iso26262__analysis_848, std_req__iso26262__analysis_849, std_req__iso26262__analysis_8410, std_req__isopas8926__44431, std_req__isopas8926__44432

This document describes the general guidances for Safety Analysis based on the concept which is defined :need:`Safety Analysis Concept<doc_concept__safety__analysis>`.

Workflow for Safety Analysis
============================

Detailed description which steps are need for a safety analysis. In general the workflow is shown in :need:`doc_getstrt__safety_analysis`.

#. Analyze the dependencies between features by performing a **single platform feature DFA** that references all platform feature static architecture diagrams, highlighting potential shared use of modules.
#. To analyse the Feature Architecture a Safety Analysis and a DFA shall be executed. The resutls of the platform feature DFA shall be used as an input.
#. Perform Safety Analysis on the Feature Architecture.
#. Perform DFA on the Feature Architecture.
#. To analyse the Component Architecture a Safety Analysis and a DFA shall be executed. This only applies if there is a component architecture which decomposes into lower level components.
#. Perform Safety Analysis on the Component Architecture.
#. Perform DFA on the Component Architecture.
#. The performance of the Safety Analysis and DFA (Feature and Component) shall be monitored.
#. For any unresolved findings from the Safety Analysis and DFA, log an issue in the Issue Tracking system and assign the ``safety`` label to safety-relevant items. The safety analysis remains "valid" but "not sufficient" as long as such issues are open.
#. If the analysis is completed, a verification of the analysis shall be done and a report of the analysis shall be created.

A example for the safety analysis (FMEA and DFA) is shown in the :ref:`examples_fmea_dfa`.

Step-by-Step-approach Safety Analysis:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template :ref:`safety_analysis_templates` on the feature or component architectural diagrams
(activity and/or sequence diagrams) using a diagram specific applied fault model <:need:`gd_guidl__fault_models`>. Apply the fault
model to the diagram and document the results in the template. If a fault model is not applicable, fill in a short remark in the
violation cause that it's not apllicable. So it could be shown that the analysis was done and no fault model is applicable.
The analysis considers single faults that can mitigate a safety requirement.

**Steps:**

* For each dynamic diagram, assign the faults by ID from the fault model and document it as a sphinx-needs directive.
* Document the resulting failure mode and effect and link to a safety requirement that mitigates the violation. 
* Document safety mitigation to avoid or control the failure.
* The attributes of the template are described in :ref:`process_requirements_safety_analysis_attributes`.
* Judge if this is sufficient. 
* If not, request to update the diagram and the requirements with additional safety mitigation to come to a sufficient outcome by creating an issue.
* The analysis is finished, if for each identified faults a sufficient mitigation exists. 
* Unless the attribute sufficient is yes, mitigation and argument attribute can be still empty.
* Continue the analysis until all fault models are checked.
* The verification is done by applying the safety analysis checklist :need:`gd_chklst__safety_analysis`.

Step-by-Step-approach DFA:
^^^^^^^^^^^^^^^^^^^^^^^^^^

The analysis is done by using the template :ref:`dfa_templates` on the feature or component architectural diagrams using a list of DFA failure initiators <:need:`gd_guidl__dfa_failure_initiators`>.
If a element of the failure initiators is not applicable, fill in a short remark in the violation cause that it's not applicable.
So it could be shown that the analysis was done and no fault model is applicable.

**Steps:**

* For each failure initiator assign the violation by ID from the DFA failure initiators and document it as a sphinx-needs directive.
* Document the resulting violation causes and effect and link to a safety requirement that mitigates the violation. 
* The attributes of the template are described in :ref:`process_requirements_safety_analysis_attributes`.
* Judge if the mitigation is sufficient. If not, request to update the requirements with additional safety mitigation to come to a sufficient outcome.
* The analysis is finished, if for each identified violation a mitigation exists.
* Unless the attribute "sufficient" is "yes", mitigation and argument attribute can be still empty.
* Continue the analysis until all failure initiators are checked.
* The verification is done by appling the safety analysis checklist :need:`gd_chklst__safety_analysis`.


