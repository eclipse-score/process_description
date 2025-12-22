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


Document lifecycle models
-------------------------

Each released document shall have the status: “VALID”.

Depending on the document assigned lifecycle Model, as defined here
:ref:`work_products_overview_list`, the document can either reach this state directly,
or some prior states are required.

Thus different document lifecycle models exists (as defined in
:need:`gd_req__doc_attr_status`):

* Model1: "VALID"
* Model2: "DRAFT" -> "VALID"
* Model3: "DRAFT" -> "VALID" -> "VALID(INSPECTED)"


**Guidance for lifecycle model 1:**

Example: :need:`wp__issue_track_system`

The document has the state “VALID” after creation.

Recommendation: Author should do a self verification for the correctness and completeness
of the content and th fulfillment of required formal aspects.


**Guidance for lifecycle model 2:**

Example: :need:`wp__feat_request`

The document has the state “VALID” after creation and a reviewer as confirmed
the correctness and completeness of the content and th fulfillment of required formal
aspects.

The figure below shows an overview of the review workflow for lifecycle model 2 (Simple
Workflow) based on Pull Requests.

Nevertheless, it is still recommended for author to do a self verification for the
correctness and completeness of the content and the fulfillment of required formal
aspects before asking for a review.

In case of any discussions are needed between author and reviewer, or still some ambiguities
exists, the document can also be published first with the status "DRAFT".

This indicates, that the document is created, may have no mature structure yet, content
is not complete and correct or formal aspects are not considered.

The figure below shows an overview of the review workflow for lifecycle model 2
(Extended Workflow) based on Pull Requests.

After some iterations between author and reviewer, the document can be set to status
"VALID", when all issues are resolved.

Due to updates, findings, other issues or change request, the document status may set
back from "VALID" to "DRAFT". This triggers a new review cycle.


.. figure:: _assets/review_workflow.drawio.svg
  :width: 100%
  :align: center
  :alt: Overview review lifecycle model 2

  Overview review lifecycle model 2 for PRs


**Guidance for lifecycle model 3:**

In principle same as lifecycle model 2, but an additional inspection step is required,
as described here: :ref:`review_concept`.

Example: :need:`wp__requirements_stkh`
