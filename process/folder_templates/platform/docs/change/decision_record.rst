..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

Decision Record Template
========================

This template is used to create new Decision Records (DRs) in the project using rst files.
For markdown files, please convert the sphinx directive to markdown syntax yourself.
The content of the DR is the same, only the syntax differs.

Suggest to store close to the artefact which is affected by the DR. For example for
platform wide decisions store close to the platform's stakeholder requirements.

In each DR file, include the following sections:

.. code-block:: rst

   .. dec_rec:: <Title>
      :id: dec_rec__<Platform|Feature|Component>__<Title>, dec_rec__<arch|proc|strat|infra|int>__<slug>
      :status: <proposed|accepted|deprecated|rejected|superseded>
      :tracking: <link to GitHub issue URL, required once a DR is confirmed>
      :version: 2
      :affects: <link>

      <Description>
      Descriptions shall contain at least the following sections:
      Context: <Your text>
      Decision: <Your text>
      Consequences: <Your text>

      or use the the provided template below (if not marked as optional, it is mandatory content):

      <Decision>

      Context
      -------
      <your text, diagrams, etc>

      Consequences
      ------------
      <your text, diagrams, etc>

      (optional)
      [
      Alternatives Considered
      -----------------------

      <Alternative A>
      ^^^^^^^^^^^^^^^
      <description of the alternative>

      Advantages
      """"""""""
      *  **<Advantage 1>:** <Explanation>
      *  **<Advantage 2>:** <Explanation>

      Disadvantages
      """""""""""""
      *  **<Disadvantage 1>:** <Explanation>
      *  **<Disadvantage 2>:** <Explanation>
      ]

      Note:
      Throughout the discussion of a CR, various ideas will be proposed which are not accepted.
      Those rejected ideas should be recorded along with the reasoning as to why they were rejected.
      This both helps record the thought process behind the final version of the CR as well as preventing people from bringing up the same rejected idea again in subsequent discussions.
      In a way this section can be thought of as a breakout section of the Rationale section that is focused specifically on why certain ideas were not ultimately pursued.

      Justification for the Decision
      ------------------------------
      <your text>


      Impact Analysis (Optional)
      --------------------------
      The impact analysis template can be used to detail out the impact on the platform
      and if applicable for other aspects, especially for safety/security.
      Either reference here to the filled-out template or copy the content from
      the template in this chapter and fill it out here.
      The impact analysis template is available in [1].

The impact analysis template is available here [1]_.

.. attention::
    The above directive must be updated according to your decision record.

    - Modify ``dec_rec`` to provide a descriptive and concise title. Summarizing the decision. (mandatory)
    - Modify ``id`` to contain the Platform/Feature/Component name the DR belongs to and the title, in upper snake case preceded by ``dec_rec__`` (mandatory)
    - Adjust ``status`` according to your needs (mandatory)
    - Modify ``tracking`` to point to the implementation issue, required once a DR is confirmed for implementation (recommended)
    - Modify ``version`` if original scope is changed (mandatory)
    - Modify ``affects`` to point to the work product it affects, mostly this will be requirements, architecture or design (recommended)
    - Provide ``Description`` (mandatory)
    - Add ``Context`` to describe the issue or motivation behind this decision or change (mandatory)
    - Add ``decision`` to detail the proposed change or decision (mandatory)
    - Add ``consequences`` to explain the impact of this change, including what becomes easier or more difficult (recommended)

.. [1] The impact analysis template is available here: :ref:`Impact Analysis Template <chm_impact_analysis_templates>`
