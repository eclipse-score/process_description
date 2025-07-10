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

Getting Started
###############

.. doc_getstrt:: Getting Started on Safety Analysis
   :id: doc_getstrt__safety_analysis
   :status: valid
   :tags: safety_analysis

This document outlines the steps for performing, monitoring, and verifying safety analysis. Safety analysis is used as a umbrella term for the methods
DFA (Dependent Failure Analysis) and FMEA (Failure Mode and Effects Analysis).
The concept of performing safety analysis is described in :need:`doc_concept__safety__analysis`. The verification of the architecture is described
in :need:`doc_concept__arch__process`.

Safety Analysis Workflow
************************

The goal of the safety analysis is to proof that a function and the corresponding safety monitoring are not effected both by a violation.
The safety analysis is performed in three steps. Analyse the considered element (Feature or Component) architecture with a DFA and FMEA.
Monitor the DFA and FMEA and log any issues in the Issue Tracking system with the ``safety`` label until the analysis is completed.
The safety analysis is completed when the verification is done, no issues are open and the status is "valid".

The details of what needs to be done in each step are described in the :need:`gd_guidl__safety_analysis`. For the safety analysis
templates are used. The templates are described in the :ref:`FMEA_templates` and :ref:`DFA_templates`. A checklist for the safety analysis is provided in
:need:`gd_chklst__safety_analysis`.
