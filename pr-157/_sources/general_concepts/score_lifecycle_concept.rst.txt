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

.. _general_concepts_lifecycle:

Lifecycle concept
-----------------

Contributions to the project are driven by Feature/Component Requests.

As features and components are the main structuring elements of the project, new
features and components are requested by feature or components requests. Both are special
types of change requests.

The figure below shows the standard lifecycle of any feature/component in the project.

.. figure:: _assets/score_lifecycle_model.drawio.svg
  :width: 100%
  :align: center
  :alt: Lifecycle model for the project

  Lifecycle model for the project

A new feature or component request starts the **Concept Phase**.
The **Concept Phase** is used to provide feasibility and further decision criteria, which
are needed to finally accept the new feature/component for the project platform.
The request may supported by source code provided within incubator repositories. In this
phase only the the :need:`Change Management<doc_getstrt__change_process>` process must
be applied, all other are optional.

Accepted features must be planned and developed according the defined project processes.
Thus the accepted Feature/Component Request starts the **Development Phase**.
During the **Development Phase** the feature implementation is initially planned, before
it is implemented and verified. The development may based on several iterative
implementation cycles. Any modification of the origin feature/component request may re-
trigger the start of the development phase, as impact analysis and replanning may required.
The development is planned, checked and adjusted to meet the objectives.
Planning is also required from several standards especially to achieve functional safety.
Finally the implemented Features/Components are release.

Released Features/Components are maintained. They may have bugs so a problem report for
a released Feature/Component starts the **Maintenance Phase**. In this phase the
:need:`Problem Resolution<doc_getstrt__problem_process>` process must be applied.
Depending on the reported problem and the agreed resolution, also other process areas may
apply.

Mandatory Processes for each Phase

.. list-table:: Mandatory Processes for each Phase
   :header-rows: 1
   :widths: 30,60

   * - Phase
     - Mandatory processes
   * - Concept
     - :need:`Change Management<doc_getstrt__change_process>`
   * - Development
     - All, if applicable
   * - Maintenance
     - :need:`Problem Resolution<doc_getstrt__problem_process>`, and all applicable to resolve the problem
