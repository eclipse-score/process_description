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


Safety Analysis : FMEA
======================

.. document:: [Your Component Name] FMEA
   :id: doc__component_name_fmea
   :status: draft
   :safety: ASIL_B
   :realizes: wp__sw_component_safety_analysis
   :tags: template

.. attention::
    The above directive must be updated according to your Component.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and succeeded by ``_fmea``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

Failure Mode List
-----------------

.. code-block:: rst

    .. comp_saf_fmea:: <Element descriptor>
       :verifies: <Component architecture>
       :id: comp_saf_FMEA__<Component>__<Element descriptor>
       :violation_id: <ID from fault model :need:`gd_guidl__fault_models`>
       :violation_cause: "description of failure effect of the fault model on the element"
       :mitigation: <ID from Component Requirement | ID from AoU Component Requirement>
       :mitigation_issue: <ID from Issue Tracker>
       :sufficient: <yes|no>
       :argument: <text to argument why mitigation is sufficient>
       :status: <valid|invalid>

.. attention::
    The above directive must be updated according to your component FMEA.

    - Remove the ``code-block``
    - Fill in all the needed information in the <brackets>
