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

.. gd_guidl:: Change Request Guideline
   :id: gd_guidl__change_change_request
   :status: valid
   :tags: change_management
   :complies: std_req__iso26262__support_8414, std_req__iso26262__support_8432, std_req__iso26262__support_8442, std_req__iso26262__support_8451


This document describes the general guidances for Change Management based on the concept which is defined :need:`[[title]]<doc_concept__change_process>`.

General Hints
=============

The detailed implementation of the Change Management for the project shall be described in the :ref:`Workflow Platform Management <workflow_platform_management>`.

Templates
---------

To create change request, the project shall provide the content of the following templates
in project's selected Issue Tracking System: :need:`[[title]] <gd_temp__change_feature_request>`
and :need:`[[title]] <gd_temp__change_component_request>`.

.. note::
  An example template for the Issue Tracking System in GitHub (`GitHub Issues <https://github.com/features/issues>`_)
  can be found here:
  `Issue Template Change Request <https://github.com/eclipse-score/process_description/blob/main/.github/ISSUE_TEMPLATE/3-change.yml>`_

Attributes
----------

For all Change Requests following mandatory attributes need to be defined:

.. needtable:: Overview of mandatory change request attributes
   :tags: change_management
   :filter: "mandatory" in tags and "attribute" in tags and "change_management" in tags and is_external == False
   :style: table
   :columns: title
   :colwidths: 30


A more detailed description can be found here: :ref:`chm_process_change_request_attributes`.


.. _workflow_chm_requirements:

Activities for Change Requests
==============================

This section describes in detail which steps need to be performed for a Change Request.

.. list-table:: Activities for Change Request
   :header-rows: 1
   :widths: 10,60,30,30

   * - Step
     - Description
     - Responsible
     - Approver
   * - :ref:`1. <chm_create_change_request>`
     - Create Change Request
     - :need:`[[title]] <rl__contributor>`
     - :need:`[[title]] <rl__committer>`
   * - :ref:`2. <chm_analyze_change_request>`
     - Analyze Change Request
     - :need:`[[title]] <rl__contributor>`
     - :need:`[[title]] <rl__committer>`
   * - :ref:`3. <chm_imp_mon_change_request>`
     - Implement and Monitor Change Request
     - :need:`[[title]] <rl__contributor>`
     - :need:`[[title]] <rl__committer>`
   * - :ref:`4. <chm_close_change_request>`
     - Close Change Request
     - :need:`[[title]] <rl__committer>`
     - :need:`[[title]] <rl__technical_lead>`, :need:`[[title]] <rl__module_lead>`


.. _chm_create_change_request:

Create Change Request
---------------------

:need:`[[title]] <rl__contributor>` (as author, submitter) creates the Change Request
in the defined Issue Tracking System of the project based on the content of the
provided templates: :need:`[[title]] <gd_temp__change_feature_request>` or
:need:`[[title]] <gd_temp__change_component_request>`.

It is expected that the select Issue Tracking system supports template definition. Best
practice is to define a template with the required content, so that it can be copied
from the different users.

.. note::
  For the Issue Tracking System in GitHub, there is a template created, which can be
  be found here:
  `Issue Template Change <https://github.com/eclipse-score/process_description/blob/main/.github/ISSUE_TEMPLATE/3-change.yml>`_

.. note::
  A Change Request Example based on that template is here:
  `Example Change Request <https://github.com/eclipse-score/process_description/issues/168>`_

It is expected, that the UID will be provided automatically by the Issue Tracking System.

It is expected, that the status of the change request is set to "open" automatically.
As long as the content is updated, the status of the change request is kept "open".

It is expected, that the change request submitter will be set automatically by the Issue
Tracking System.

The title of the change request should reflect the topic accordingly.

The change request type should reflect level of the change: feature or component.

The description should reflect in detail:
   Exact description of the Change Request including reason, including impact analysis
   on user, effort for implementation (schedule, risks, resources) and
   verification (measures defined).

If details for the realization of the change are from interest, they may be added.

It is expected, that the affected work products from high level perspective are identified.

It it expected, that an detailed impact analysis is available.

If the change affects safety or security it should be stated explicitly.
If safety is affected, the ASIL classification should be added, if applicable.

.. note::
  | For the Change Request Example:
  | * The UID is provided by the Issue Tracking System as: **#168**
  | * The status of the issue is provided by the Issue Tracking System as: **Open**
  | * The submitter is provided by the Issue Tracking System as: **masc2023**
  | * The title contains the change reason, as API of a component modified
  | * The change request type is selected as Component Request/Modification
  | * The descriptions considers reason and effort for implementation, verification, impact for user
  | * There are no details for the implementation given
  | * The affected high level work products are identified: Requirements, Architecture and Detailed Design
  | * The detailed affected work products are listed.
  | * Checkboxes are selected to highlight, that Safety is affected with classification ASLI_B

When ready to review and to analyze, the author sets the status to "in review" manually.

.. note::
  | For the Change Request Example:
  | * The "Process Development Community" dashboard is added and the status must be changed to **Todo**
  | * The combination of the issue**Open** and **Todo** defines the status **in review**


.. _chm_analyze_change_request:

Analyze Change Request
----------------------

The projects :need:`[[title]] <rl__committer>` analyzes the change request together with
the :need:`[[title]] <rl__contributor>` and takes a decision for accepting or rejecting it.

The analysis will start by reviewing all the information given during the creation of the
change request. All topics are revisited and checked for correctness, completeness and
consistency.

If required, the information is updated accordingly.

If accepted, the stakeholder of the change and the expected release, where the change
should be closed, shall be defined. Optionally, the corresponding milestone can be set.

.. note::
  | For the Change Request Example:
  | * The stakeholder are provided using Assignees field: **masc2023**
  | * The expected closure version is provided: *0.5*
  | * The "Milestone" is provided: **Release 2.0.0 - Maturity Level 2**

If accepted, :need:`[[title]] <rl__contributor>` can start with the implementation of the
Change Request.

The author has the freedom to cancel it at any time by setting the status to "rejected".

.. note::
  | For the Change Request Example:
  | * For rejection the status of the issue must be changed to **Closed as not planned**
  | * The combination of **Closed as not planned** and any "Process Development Community" status defines the status **rejected**


.. _chm_imp_mon_change_request:

Implement and Monitor Change Request
------------------------------------

If accepted, the projects :need:`[[title]] <rl__committer>` initiates the implementation
of the change together with the :need:`[[title]] <rl__contributor>`.

The description may reflect details for the implementation.

.. note::
  | For the Change Request Example:
  | * The descriptions has a section for **How is the change realized**, but it is empty.

The concrete implementation of the solution may require several additional activities.
In this case additional issues may created and linked to the Change Request.

.. note::
  | For the Change Request Example:
  | * The **Create sub-issue** should be used to create further linked issues.

Minimal a Pull Request is sufficient to implement the change, which shall be linked
to the Change Request. It is expected, that the status of the Pull Request is set to
"draft" or "open" automatically.

When ready to implement, the author sets the status to "in implementation" manually.

.. note::
  | For the Change Request Example:
  | * The "Process Development Community" status must be changed to **In Progress**
  | * The linked Pull Request status is either "Draft" or "Open"
  | * The combination of **Open** and any "Process Development Community" status **In Progress** and the Pull Request status **Draft** or **Open** defines the status **in implementation**

.. note::
  | For the Change Request Example:
  | * The **Development** section should be used to link to an pull request
  | * The **Create a branch** action may used to create automatically a linked pull request

During the implementation of the change the responsible lead :need:`[[title]] <rl__technical_lead>`
or :need:`[[title]] <rl__module_lead>` reports regularly the status to the affected
projects teams.

The author has the freedom to cancel it at any time by setting the status to "rejected".


.. _chm_close_change_request:

Close Change Request
--------------------

During implementation the :need:`[[title]] <rl__contributor>` monitors all activities linked to
the change, until they are closed.

:need:`[[title]] <rl__committer>` checks finally if the Change Request implementation
is sufficient before the status is finally closed. To check, if it is sufficient,
:need:`Change Request Checklist <gd_chklst__change_cr_review>` may used.
Further the effectiveness of the implemented measure is confirmed and the availability
of the required reports, as verification results, if applicable.

When confirmed, the author sets the status to "closed" manually, if not done automatically.

.. note::
  | For the Change Request Example:
  | * For closing the status of the issue must be changed to **Closed**
  | * The "Process Development Community" status must be changed to **Done**
  | * The PR status must be changed to **Merged**
  | * The combination of **Closed** and any "Process Development Community" status **Done** and the Pull Request status **Merged** defines the status **closed**

:need:`[[title]] <rl__committer>` has the freedom to reject it at any time by setting the status
to "reject".
