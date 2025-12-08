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

Guideline
#########

.. gd_guidl:: Documentation
   :id: gd_guidl__documentation
   :status: valid
   :complies: std_req__iso26262__support_1041, std_req__iso26262__support_1042, std_req__iso26262__support_1043, std_req__iso26262__support_1044, std_req__iso26262__support_1045, std_req__iso26262__support_1046

The planning for the documents is part of the :need:`wp__document_mgt_plan` within the Platform Management Plan.
This plan includes the configuration item list containing all work products created in the project
as well as additional artifacts as defined in :need:`doc_concept__configuration_process`.


For manual review of the formal elements the
:need:`Documentation Review Checklist <gd_chklst__documentation_review>` may used.

The review of each document is done as defined for this type of work product in the respective
process description.


Document life cycle models
--------------------------

Each official document shall have the status: “VALID”.

Depending on the document type (report, checklist, plan, etc.) the document can
either reach this state directly, or some prior states are required.

Thus different document life cycle models exists:

* Model1: "VALID"
* Model2: "DRAFT" -> "VALID"
* Model3: "DRAFT" -> "VALID" -> "VALID(INSPECTED)"

**The document types below require life cycle model 1:**

Report

Guidance:

The document has the state “VALID”, if the
Author has successfully done a self verification for the three aspects of content,
valid structure and formal aspects.

**The document types below require life cycle model 2:**

Compare :need:`gd_req__process_management_build_blocks`, except their are part of the
life cycle model 3, thus the need inspection.

Guidance:

The document has the state “DRAFT”, if the
Document is created, may have no mature structure, content or formal aspects considered.
Author writes the document, creates content, creates a valid structure and considers
formal aspects.

The document has the state “VALID”, if the
Document is reviewed. In this state the reviewer has successfully checked the document
for content, structure and formal aspects.

Due to updates, findings, other issues or change request, the document status may set
back from "VALID" to "DRAFT". This triggers a new review cycle.


.. figure:: _assets/review_workflow.drawio.svg
  :width: 100%
  :align: center
  :alt: Overview review life cycle model 2

  Overview review life cycle model 2

**The document types below require life cycle model 3:**

Compare :ref:`review_concept`.

Guidance:

In principle same as life cycle model 2, but an additional inspection step is required,
as described here: :ref:`review_concept`.
