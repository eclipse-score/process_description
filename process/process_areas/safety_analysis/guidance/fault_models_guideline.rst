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

FMEA Fault Models
=================

.. gd_guidl:: FMEA Fault Models
  :id: gd_guidl__fault_models
  :status: valid
  :complies: std_req__iso26262__software_7410, std_req__iso26262__analysis_846

  | Fault Model for sequence diagrams

.. note:: Use the applicable fault models to ensure a structured analysis. If there are additional fault models needed, please enlarge the list of fault models.


.. note:: An ASIL related message is trustable in that manner that it is not corrupted, repeated, lost, delayed, masqueraded or addressed incorrectly.


Fault Models for sequence diagrams
------------------------------------

.. fmea_fault_model:: message is not received
   :id: fmea_fault_model__mf_01_01
   :status: valid
   :element: message
   :failure_mode: message is not received,Is a subset/more precise description of fmea_fault_model__mf_01_05.
   :importance: High
   :hide:




.. fmea_fault_model:: message received too late
   :id: fmea_fault_model__mf_01_02
   :status: valid
   :element: message
   :failure_mode: message received too late ,Only relevant if delay is a realistic fault
   :importance: Medium
   :hide:





.. fmea_fault_model:: message received too early
   :id: fmea_fault_model__mf_01_03
   :status: valid
   :element: message
   :failure_mode: message received too early,Usually not a problem
   :importance: Low
   :hide:





.. fmea_fault_model:: message not received correctly by all recipients
   :id: fmea_fault_model__mf_01_04
   :status: valid
   :element: message
   :failure_mode: message not received correctly by all recipients,Different messages or messages partly lost. Only relevant if the same message goes to multiple recipients.
   :importance: High
   :hide:




.. fmea_fault_model:: message is corrupted
   :id: fmea_fault_model__mf_01_05
   :status: valid
   :element: message
   :failure_mode: message is corrupted
   :importance: High
   :hide:

.. fmea_fault_model:: message is not sent
   :id: fmea_fault_model__mf_01_06
   :status: valid
   :element: message
   :failure_mode: message is not sent
   :importance: High
   :hide:

.. fmea_fault_model:: message is unintended sent
   :id: fmea_fault_model__mf_01_07
   :status: valid
   :element: message
   :failure_mode: message is unintended sent
   :importance: High
   :hide:

.. fmea_fault_model:: minimum constraint boundary is violated
   :id: fmea_fault_model__co_01_01
   :status: valid
   :element: duration/time constraint
   :failure_mode: minimum constraint boundary is violated
   :importance: Medium
   :hide:

.. fmea_fault_model:: maximum constraint boundary is violated
   :id: fmea_fault_model__co_01_02
   :status: valid
   :element: duration/time constraint
   :failure_mode: maximum constraint boundary is violated
   :importance: High
   :hide:

.. fmea_fault_model:: process calculates wrong results
   :id: fmea_fault_model__ex_01_01
   :status: valid
   :element: execution
   :failure_mode: process calculates wrong results,   Is a subset/more precise description of fmea_fault_model__mf_01_05 or fmea_fault_model__mf_01_04. This failure mode is relevant to the analysis if e.g. internal safety mechanisms are required (level 2 function, plausibility check of the output, …) because of the size/complexity of the feature.
   :importance: High
   :hide:





.. fmea_fault_model:: processing too slow
   :id: fmea_fault_model__ex_01_02
   :status: valid
   :element: execution
   :failure_mode: processing too slow,Only relevant if timing is considered
   :importance: Medium
   :hide:





.. fmea_fault_model:: processing too fast
   :id: fmea_fault_model__ex_01_03
   :status: valid
   :element: execution
   :failure_mode: processing too fast,Only relevant if timing is considered
   :importance: Medium
   :hide:





.. fmea_fault_model:: loss of execution
   :id: fmea_fault_model__ex_01_04
   :status: valid
   :element: execution
   :failure_mode: loss of execution
   :importance: High
   :hide:

.. fmea_fault_model:: processing changes to arbitrary process
   :id: fmea_fault_model__ex_01_05
   :status: valid
   :element: execution
   :failure_mode: processing changes to arbitrary process
   :importance: Medium
   :hide:

.. fmea_fault_model:: processing is not complete
   :id: fmea_fault_model__ex_01_06
   :status: valid
   :element: execution
   :failure_mode: processing is not complete
   :importance: High
   :hide:

   Infinite loop.



.. needtable::
   :style: table
   :columns: element;id;failure_mode;importance
   :colwidths: 10,15,35,10

   results = []

   for need in needs.filter_types(["fmea_fault_model"]):
      if need['is_external'] == False:
         results.append(need)
