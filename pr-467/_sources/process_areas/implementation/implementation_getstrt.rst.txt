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

.. doc_getstrt:: Getting Started on Implementation
   :id: doc_getstrt__imp_getstrt
   :status: valid
   :tags: Implementation

This document describes the steps which need to be done to document detailed design and implement the code.

Therefore a detailed guideline :need:`gd_guidl__implementation` and a :need:`doc_concept__imp_concept` are available.


General Workflow
################

Overview of the implementation workflow.

.. figure:: _assets/implementation_workflow.drawio.svg
   :align: center
   :width: 80%
   :name: implementation_workflow_fig

The details of what needs to be done in each step are described in the :need:`gd_guidl__implementation`.


Relevant Documents
******************

Concept Document: :need:`doc_concept__imp_concept` provides a high-level overview of the integration concept.

Implementation Guideline: :need:`gd_guidl__implementation` Details on the implemenation.

SW Development Plan: :need:`gd_temp__software_development_plan` Process description of SW development including

  - Selection of design and programming language
  - Design guideline
  - Coding guideline (e.g. MISRA, can also include style guide or naming convention)
  - SW configuration guideline
  - Method selection (e.g. for Architecture Verification)
  - Development tools

.. _developer_experience:

Developer Experience
====================

There are some tests intended to check e.g. format which are described in
https://github.com/eclipse-score/score?tab=readme-ov-file#score-platform.
