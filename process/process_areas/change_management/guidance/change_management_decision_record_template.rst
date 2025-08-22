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

.. _decision_record_template:

========================
Decision Record Template
========================

.. gd_temp:: Decision Record Template
   :id: gd_temp__change_decision_record
   :status: valid
   :complies: std_req__aspice_40__SWE-2-BP3

This template is used to create new Decision Records (DRs) in the project.

Suggest to store close to the artefact which is affected by the DR. For example for platform wide decisions store close to the platform's stakeholder requirements.

In each DR file, include the following sections:

.. code-block:: rst

   .. dec_rec:: <Title>
      :id: dec_rec__<Platform|Feature|Component>__<Title>
      :status: <proposed|accepted|deprecated|rejected|superseded>
      :affects: <link>
      :context: <Your text>
      :decision: <Your text>
      :consequences: <Your text>

.. attention::
    The above directive must be updated according to your decision record.

    - Modify ``dec_rec`` to provide a descriptive and concise title. Summarizing the decision. (manadatory)
    - Modify ``id`` to contain the Platform/Feature/Component name the DR belongs to and the title, in upper snake case preceded by ``dec_rec__`` (manadatory)
    - Adjust ``status`` according to your needs (manadatory)
    - Modify ``affects`` to point to the work product it affects, mostly this will be architecture or design (recommended)
    - Modify ``context`` to describe the issue or motivation behind this decision or change (manadatory)
    - Modify ``decision`` to detail the proposed change or decision (manadatory)
    - Modify ``consequences`` to explain the impact of this change, including what becomes easier or more difficult (recommended)
