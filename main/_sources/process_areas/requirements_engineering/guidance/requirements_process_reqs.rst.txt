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

.. _process_requirements:

Process Requirements
====================

.. gd_req:: Requirements Structure
   :id: gd_req__req__structure
   :status: valid
   :tags: structure
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6431, std_req__iso26262__support_6432

   Requirements shall be hierarchically grouped into three levels.

   Following levels are defined:

      * Stakeholder requirement
      * Feature requirement
      * Component requirement

   Additionally there shall be the following logical groups of requirements:
      * Assumption of use requirement
      * Process requirement
      * Tool requirement

.. _process_requirement_attributes:

Process Requirement Attributes
------------------------------

.. gd_req:: Requirement attribute: UID
   :id: gd_req__req__attr_uid
   :status: valid
   :tags: attribute,mandatory
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6432

   Each requirement shall have a unique ID. It shall consist of three parts:

      * type of requirement
      * structural element (e.g. some part of the feature tree, component acronym)
      * keyword describing the content of the requirement.

   Consider the project's naming convention.

.. gd_req:: Requirement attribute: title
   :id: gd_req__requirements_attr_title
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6424

   The title of the requirement shall provide a short summary of the description, but is not an "additional" requirement.

   This means for example that the word "shall" is not allowed in the title for all requirements.

.. gd_req:: Requirement attribute: description
   :id: gd_req__requirements_attr_description
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6424

   Each requirement shall have a description.

   .. note::

      *ISO/IEC/IEEE/29148 - Systems and software engineering — Life cycle processes — Requirements engineering* defines general concepts including terms and examples for functional requirements syntax.

      The concepts shall apply.

.. gd_req:: Requirement attribute: type
   :id: gd_req__req__attr_type
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   Each requirement, apart from process and tool requirements, shall have a type of one of following options:

      * Functional
      * Interface
      * Process
      * Non-Functional

.. gd_req:: Requirements attribute: security
   :id: gd_req__requirements_attr_security
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__req__feat_req, wf__req__comp_req

   Each requirement, apart from process and tool requirements, shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Requirement attribute: safety
   :id: gd_req__req__attr_safety
   :status: valid
   :tags: attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   Each requirement, apart from process and tool requirements, shall have a automotive safety integrity level (ASIL) identifier:

      * QM
      * ASIL_B
      * ASIL_D

.. gd_req:: Requirement attribute: status
   :id: gd_req__req__attr_status
   :status: valid
   :tags: attribute, mandatory
   :complies: std_req__iso26262__support_6425
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   Each requirement, apart from process and tool requirements, shall have a status:

      * valid
      * invalid

.. gd_req:: Requirement attribute: rationale
   :id: gd_req__req__attr_rationale
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__req__stkh_req

   Each stakeholder requirement shall provide an attribute called rationale.
   The rationale shall contain the reason why the requirement is needed.

.. _process_requirement_linkage:

Process Requirement Linkage
'''''''''''''''''''''''''''

.. gd_req:: Requirement Linkage
   :id: gd_req__req__linkage
   :status: valid
   :tags: attribute, automated
   :complies: std_req__iso26262__support_6432
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   Requirements shall be linked to its adjacent level via the attribute satisfies.

      * stakeholder requirements <- feature requirements
      * feature requirements <- component requirements
      * workflow <- process requirements
      * process requirements <- tool requirements

.. gd_req:: Requirement Traceability
   :id: gd_req__req__traceability
   :status: valid
   :tags: attribute, automated
   :complies: std_req__iso26262__support_6432
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   Bi-directional traceability shall be provided by adding a "back-link" via attribute satisfied by (i.e. make a <-> out of the <- in :need:`gd_req__req__linkage`).

.. gd_req:: Requirement attribute: requirement covered
   :id: gd_req__req__attr_req_cov
   :status: valid
   :tags: attribute, automated
   :complies: std_req__iso26262__support_6423
   :satisfies: wf__req__stkh_req, wf__req__feat_req

   It shall be possible to specify the requirement coverage.

      * Yes
      * No

.. gd_req:: Requirement attribute: link to implementation
   :id: gd_req__req__attr_impl
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__req__feat_req, wf__req__comp_req

   It shall be possible to link requirements to code and include a link to github to the respective line of code in an attribute of the requirement.

.. gd_req:: Requirement attribute: link to test
   :id: gd_req__req__attr_testlink
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6433, std_req__iso26262__software_944

   It shall be possible to link requirements to tests and automatically include a link to the test case in the attribute testlink.

.. gd_req:: Requirement attribute: test covered
   :id: gd_req__req__attr_test_covered
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6433, std_req__iso26262__software_944

   It shall be possible to specify if requirements are completely covered by the linked test cases.

      * Yes
      * No

.. gd_req:: Requirement attribute: versioning
   :id: gd_req__req__attr_version
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6434

   A versioning for requirements shall be provided. For this all mandatory attributes shall be taken into account: :need:`gd_req__req__attr_mandatory`

.. _process_requirement_checks:

Process Requirements Checks
'''''''''''''''''''''''''''

.. gd_req:: Requirement check: suspicious
   :id: gd_req__req__attr_suspicious
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6434

   Based on the requirement versioning it shall be checked if a parent requirement was updated but not the linked child requirements.
   In case an update was detected, the attribute requirement covered shall be set to "No"

.. gd_req:: Requirements mandatory attributes provided
   :id: gd_req__req__attr_mandatory
   :status: valid
   :tags: attribute, check
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   It shall be checked if all mandatory attributes for each requirement is provided by the user. For all requirements following attributes shall be mandatory:

   .. needtable:: Overview mandatory requirement attributes
      :filter: "mandatory" in tags and "attribute" in tags and "requirements_engineering" in tags and type == "gd_req" and is_external == False
      :style: table
      :columns: title
      :colwidths: 30

.. gd_req:: Requirements no weak words
   :id: gd_req__req__attr_desc_weak
   :status: valid
   :tags: attribute, check
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   It shall be ensured that no *weak words* are contained in the requirement description for:

   * Stakeholder Requirements
   * Feature Requirements
   * Component Requirements
   * Tool Requirements

   List of these weak words: just, about, really, some, thing, absolutely (to be extended)


.. gd_req:: Requirements linkage level
   :id: gd_req__req__linkage_fulfill
   :status: valid
   :tags: attribute, check
   :complies: std_req__iso26262__support_6432
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req

   Every feature- and component requirement shall be linked to at least one valid parent requirement according to the defined traceability scheme:

   :ref:`traceability concept for requirements`

.. gd_req:: Requirements linkage architecture
   :id: gd_req__req__linkage_architecture
   :status: valid
   :tags: attribute, check
   :complies: std_req__iso26262__support_6423
   :satisfies: wf__req__feat_req, wf__req__comp_req

   It shall be checked if every feature- and component requirement is linked at least to one valid architectural element on the same level.

.. gd_req:: Requirements linkage safety
   :id: gd_req__req__linkage_safety
   :status: valid
   :tags: attribute, check
   :satisfies: wf__req__stkh_req, wf__req__feat_req, wf__req__comp_req
   :complies: std_req__iso26262__support_6422

   It shall be checked that safety requirements (Safety != QM) can only be linked against safety requirements.

.. needextend:: docname is not None and "process_areas/requirements_engineering" in docname
   :+tags: requirements_engineering
