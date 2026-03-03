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

.. _requirement templates:

Templates
=========

.. gd_temp:: Stakeholder Requirements Template
   :id: gd_temp__req_stkh_req
   :status: valid
   :complies: std_req__iso26262__system_6411, std_req__iso26262__system_6413, std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425, std_req__aspice_40__SWE-1-BP1

   See :need:`stkh_req__requirements__template`

.. gd_temp:: Feature Requirements Template
   :id: gd_temp__req_feat_req
   :status: valid
   :complies: std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425, std_req__aspice_40__SWE-1-BP1

   See :need:`feat_req__feature_name__some_title`

.. gd_temp:: Component Requirements Template
   :id: gd_temp__req_comp_req
   :status: valid
   :complies: std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425, std_req__iso26262__support_12425, std_req__aspice_40__SWE-1-BP1

   See :need:`comp_req__component_name__some_title`

.. gd_temp:: AoU Requirement Template
   :id: gd_temp__req_aou_req
   :status: valid
   :complies: std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425, std_req__aspice_40__SWE-1-BP1

   See :need:`aou_req__platform__some_other_title`, :need:`aou_req__feature_name__some_other_title`, :need:`aou_req__component_name__another_title`

.. gd_temp:: Process Requirements Template
   :id: gd_temp__req_process_req
   :status: valid
   :complies: std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425

   .. code-block:: rst

      .. gd_req:: <Title>
         :id: gd_req__<process>__<Title>
         :satisfies: <link to guidance id>
         :complies: <link to standard requirement>
         :status: <valid|invalid>

.. gd_temp:: Tool Requirements Template
   :id: gd_temp__req_tool_req
   :status: valid
   :complies: std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425

   .. code-block:: rst

      .. tool_req:: <Title>
         :id: tool_req__<tool>__<Title>
         :security: <YES|NO>
         :safety: <QM|ASIL_B>
         :satisfies: <link to process req id>
         :status: <valid|invalid>
         :implemented: <YES|PARTIAL|NO>

.. gd_temp:: Requirement Formulation Template
   :id: gd_temp__req_formulation
   :status: valid
   :complies: std_req__iso26262__support_641, std_req__iso26262__support_6421, std_req__iso26262__support_6425

   Requirements shall be specified according to the following schema:

   <The SW Platform|Feature|Component> shall <main verb> <object> <parameter> <temporal/logical conjunction>

   <Note: (optional, not to be verified)>

   .. list-table:: Sentence Table
      :header-rows: 1

      * - Addressee of the requirement (subject)
        - shall
        - main verb
        - object of the requirement
        - parameter of the requirement
        - temporal/logical conjunction
      * - The development object (who/what)
        - shall
        - do something
        - for whom or what
        - which target value/condition
        - when, under which conditions
      * - Example 1: The component
        - shall
        - detect
        - if a key-value pair got corrupted
        - and set its status to INVALID
        - during every restart of the SW platform.
      * - Example 2: The software platform
        - shall
        - enable
        - users
        - to ensure the compatibility of application software
        - across vehicle variants and vehicle software releases.
      * - Example 3: The linter-tool
        - shall
        - check
        - correctness of .rst files format
        -
        - upon each commit.


   .. note::
      Of the last three columns of the above sentence template table, filling one is mandatory the others are optional.
