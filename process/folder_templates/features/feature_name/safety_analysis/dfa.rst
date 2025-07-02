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

.. document:: [Your Feature Name] DFA
   :id: doc__feature_name_dfa
   :status: draft
   :safety: ASIL_B
   :realizes: wp__feature_dfa
   :tags: template

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__`` and succeeded by ``_dfa``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

Dependent Failure Intitiators
-----------------------------

.. code-block:: rst

  .. feat_saf_dfa:: <Element descriptor>
      :verifies: <Feature architecture>
      :id: feat_saf_DFA__<Feature>__<Element descriptor>
      :violation_id: <ID from DFA failure initiators DFA failure initiators (gd_guidl__dfa_failure_initiators)>
      :violation_cause: “description of failure effect of the failure initiator on the element”
      :mitigation: <ID from Feature Requirement | ID from AoU Feature Requirement>
      :mitigation_issue: <ID from Issue Tracker>
      :sufficient: <yes|no>
      :status: <valid|invalid>

 .. note::   argument is inside the 'content'. Therefore content is mandatory

.. attention::
    The above directive must be updated according to your feature DFA.

    - Remove the ``code-block``
    - Fill in all the needed information in the <brackets>
