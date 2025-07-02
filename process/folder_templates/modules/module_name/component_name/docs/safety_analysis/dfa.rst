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


Dependent Failure Analysis
==========================

.. document:: [Your Component Name] DFA
   :id: doc__component_name_dfa
   :status: draft
   :safety: ASIL_B
   :realizes: wp__sw_component_dfa
   :tags: template

.. attention::
    The above directive must be updated according to your Component.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and succeeded by ``_dfa``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

Dependent Failure Intitiators
-----------------------------

.. code-block:: rst


   .. comp_saf_dfa:: <Element descriptor>
      :verifies: <Component architecture>
      :id: comp_saf_DFA__<Component>__<Element descriptor>
      :violation_id: <ID from DFA failure initiators DFA failure initiators (gd_guidl__dfa_failure_initiators)>
      :violation_cause: “description of failure effect of the failure initiator on the element”
      :mitigation: <ID from Component Requirement | ID from AoU Component Requirement>
      :mitigation_issue: <ID from Issue Tracker>
      :sufficient: <yes|no>
      :status: <valid|invalid>

.. note::   argument is inside the 'content'. Therefore content is mandatory

.. attention::
    The above directive must be updated according to your component DFA.

    - Remove the ``code-block``
    - Fill in all the needed information in the <brackets>
