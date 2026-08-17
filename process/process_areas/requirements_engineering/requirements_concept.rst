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

Concept Description
###################

.. doc_concept:: Requirements Concept
   :id: doc_concept__req_process
   :status: valid
   :version: 2

In this section a concept for the requirements management will be discussed. Inputs for this concepts are both the requirements of ISO26262 Part-8 and ASPICE Requirements from SWE.1 additionally including the requirements of the different stakeholders for the requirement process.

Inputs
******

#. Stakeholders for the requirements?
#. Who needs which information?
#. Which Requirement Levels can we derive from that?
#. Which Attributes are required?
#. How do the different requirement levels correlate to each other?

Stakeholders for the requirements
=================================

#. :need:`Project Lead Circle <rl__project_lead>`

   * Define specification and content for the platform
   * Creation of a project timeline
   * Track project progress

#. :need:`SW Architect <rl__committer>`

   * Break down the platform specification into features (High Level)
   * Derive feature/component architecture for each feature
   * Allocate requirements to architecture elements for specification of features/components
   * Define AoUs which arise from architecture

#. :need:`Tester <rl__committer>`

   * Verify that the specification is satisfied by the elements under test
   * Consider AoUs for test case specification

#. :need:`Safety Architect <rl__safety_engineer>`

   * *Dependent Failure Analysis*

     * Requires inputs towards independence and interference of the element under investigation
     * Initiates additional requirements and AoU to cover failures

   * *Qualitative safety analysis* (e.g. FMEA)

     * Detailed element description to identify systematic errors within the element under investigation
     * Initiates additional requirements and AoU to cover failures

#. :need:`Security Architect <rl__security_engineer>`

   * Trust Boundary Analysis
   * Defense in Depth Analysis
   * Qualitative Security Analysis (TARA or at least Attack Potential Analysis with impact category Safety)

#. :need:`Module/Tooling SW Developer <rl__delivery_team>`

   * Implement the SW according to its specification
   * Create traceability by linking its specification to code
   * Consider AoUs of other components
   * Create AoUs for component under development

#. Feature User

   * Get detailed information concerning the specification of a feature
   * Be informed about its boundary conditions (AoUs)

#. :need:`Platform SW Developer of the Reference Integration <rl__platform_team>`

   * Implements Requirements for Integration

As the platform is developed in an open source working mode, in principle every :need:`rl__contributor`
can create SW requirements (as can be seen in :ref:`requirements_workflows`) but always
a :need:`rl__committer` or :need:`rl__project_lead` has to approve.
In practice the expectation is that the above stakeholders also define requirements,
mostly the :need:`SW Architect <rl__committer>` and competent persons from the module's :need:`rl__delivery_team`.
The person responsible is planned in the issue tickets for requirements definition.

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO26262
* ASPICE
* ISO SAE 21434

Requirement Levels
******************

Based on the inputs of the previous chapter the types of requirements which need to be implemented in the project can be derived. The defined levels are shown in the :ref:`Traceability Concept <score_wp_traceability>`.

Stakeholder Requirements
========================

On the platform level the *Stakeholder (=customer) Requirements* are defined. These requirements describe which content (functionality and safety mechanisms) the platform needs to contain, and serve as a project description of the top-level functionality. An example could be:

.. code-block:: text

   The platform shall support configuration of applications via files (e.g. yaml, json)

Note that the *Stakeholder Requirements* represent the assumed technical safety requirements for the platform SEooC,
i.e. the assumption on what content is needed, which shall be matched by the user to their expectations.

Feature Requirements
====================

The *Feature Requirements* derived from stakeholder requirements address mainly the integration level of SW components. These shall describe the behaviour of the feature on platform level independent from a decomposition into components. They serves mainly as an input for (SW + Safety) Architects, Testers, Integrators. Example:

.. code-block:: text

   The feature shall use JSON formatted string according to RFC-8259 for configuration.

However the detailed interaction of the underlying components itself which is required to form a feature shall be defined in the feature architecture.

Component Requirements
======================

The lowest abstraction level is represented by the *component requirements*. They are derived from *feature requirements* and describe component specific implementation details. It is described which behaviour a component itself needs to satisfy in the context of the feature, for example:

.. code-block:: text

   The component shall provide API calls to read and interpret every field of a JSON body in C++.

Assumption of Use Requirements
==============================

Last but not least a requirement type is needed which describes e.g. the boundary conditions which need to be fulfilled when using a software element. Those requirements are called *Assumption of Use* (AoUs) and can be defined on every level (stakeholder/SW-platform, feature, component). Example:

.. code-block:: text

   The user shall provide a string as input which is not corrupted due to HW or QM SW errors.

Process Requirements
====================

Besides those four types of requirements which describe the contents of the platform also a type, describing the requirements towards the tooling from a process point of view, needs to be specified. These *process requirements* can be derived from a process description. Here it is defined which part of the process need to be performed manually and which parts of the process should be implemented by tooling. Example:

.. code-block:: text

   It shall be checked that safety requirements (Safety != QM) can only be linked against safety requirements.

.. _attributes of the requirements:

Attributes of the Requirements
******************************

The required attributes for the requirements are defined in this subchapter. On the top level we can distinguish between attributes which need to be filled manually and attributes which are generated during the *docs build*.

Following attributes need to be filled manually for each requirement:

.. list-table:: Manual Attributes
   :header-rows: 1
   :widths: 15,85

   * - Attribute
     - Description
   * - Status
     - The status for a requirement can either be valid or invalid. The reasoning for this is that the goal is to only have valid requirements in the main branch. So a status *draft* is not required. It is obvious that the requirement is in the status draft as long as the PR is not merged.
   * - Unique ID
     - The unique id consist of a prefix for the requirement type followed by a keyword for the feature/component and a short keyword describing its content. It is used as a unique identifier for a requirement which can be used e.g. for linking the requirements.
   * - Title
     - The title of the requirement shall be expressive and rely to the description of the requirement.
   * - Description
     - In this attribute the content for the requirement will be specified. Please be aware that a note in a requirement is not part of the requirement itself. This means that notes should only be used to give additional explanation or context to the requirement.
   * - Version
     - Version of the requirement adapted with each significat change, see :ref:`significant_requirement_changes`.
   * - Rationale / Linkage
     - In either of those attributes the reasoning for the requirement is included.
       For *Stakeholder Requirements* a rationale which provides some more background infos shall be provided.
       For any other requirement the reasoning can be deduced from the top level requirement.
   * - Safety
     - This attribute describes the impact of the requirement on functional safety. Currently only following values are defined [QM, ASIL_B]. Other values are not required at the moment as *ASIL decomposition* is not used so far.
   * - Security
     - This attribute describes if the requirement has any impact on security of the platform.
   * - Requirements Type
     - The requirement type defines which category the requirement relates to. Following categories are defined: [Functional, Interface, Process, Non-Functional]

       - Functional: If implemented can be verified by a test (unit, integration)
       - Interface: Does not define a functionality but the API provided to use the functionality
       - Process: If implemented can be verified by reviewing the process description (sub-type of non-functional)
       - Non-Functional: If implemented can be checked by review/analysis (of e.g. code, documentation)

       Note that the linking to the requirements is affected by these types, see :need:`gd_req__req_linkage_architecture`.

Following attributes are automatically generated:

.. list-table:: Automated Attributes
   :header-rows: 1
   :widths: 15,70,15

   * - Attribute
     - Description
     - Tool
   * - Derives
     - This attribute is automatically generated into the parent requirement based on the attribute derived_from of the current requirement
     - Docs-as-Code
   * - Implemented by
     - During Build the code files are parsed for a defined tag which includes the requirement id. If this is located a link to the code will be added in the requirement
     - Docs-as-Code
   * - Verified by
     - During build the test files are parsed for a defined marker which includes the requirement id. If the marker is located in the test a link to the test case will be added to the requirement
     - Docs-as-Code

More details about the generation of the automated attributes are explained in the following chapter where the general workflow for generating requirements including their status is shown.

.. _requirement_versioning:

Requirements Versioning
***********************

Individual Requirements
=======================

For the requirements the version management is basically provided by version management tooling (e.g. git history). However it needs to be identified if the content of a requirement changed. So this concept aims only at identifying a significant change in the attributes of a requirement.

.. _significant_requirement_changes:

Versioning on Significant Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only significant changes to the attributes of a requirement shall result in a version change,
generally this is everything which may affect the content of the child requirements:

.. list-table:: Significant Attributes
   :header-rows: 1
   :widths: 30,35, 35

   * - Attribute link
     - What is significant
     - What is not significant
   * - :need:`gd_req__req_attr_description`
     - Functional changes and also re-writes which might lead to a better understanding of the content
     - typo corrections, formal adaptions (e.g. layout), modifications of the requirement's notes
   * - :need:`gd_req__req_attr_safety`
     - every change
     - n/a
   * - :need:`gd_req__req_attr_security`
     - every change
     - n/a
   * - :need:`gd_req__req_attr_type`
     - every change
     - n/a

Linking child requirements including versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a requirement is linked to a top level requirement also the version of the target requirement shall be part of the link. Upon docs build it shall be checked if the version contained in the link matches the *version* attribute of the requirement which is linked via *derived_from*.

As this check is included in the docs build as a warning it can be guaranteed that a change of a parent requirement can only be merged if the derived child requirements are also updated accordingly.


Sets of Requirements / Baselines
================================

Version management tooling standard functionality provides the means to version sets of requirements, as those are collected in files:

* The files commit history can be displayed, to show change date, author and differences
* Also the changes on every line are available (e.g. via git "Blame")

Requirement baseline generation is part of the configuration management, it is done by tagging a complete set of artifacts/files in a repository.

.. _reviews of the requirements:

Reviews of the Requirements
***************************

Some of the checks cannot be performed automatically. Therefore a manual inspection of the requirements is needed. The requirement review itself is triggered when a contributor wants to trigger a requirement review.

In the general for the reviews a :ref:`guideline <review_concept>` exists.

.. _coverage_of_requirements:

Coverage of Requirements
************************

According to the standards, requirements shall be derived from top to bottom. This means that at the point in time when the parent requirement is generated the coverage (by child requirements) can not be evaluated. In a second step every parent requirements need to be completely broken down into child requirements which are linked to the parent requirement.

The completeness of all the child requirements (i.e. that their parent requirement is "covered") will be confirmed latest in the formal review (inspection) of the child requirements.

If after the creation of the child requirements any of the parent requirements would be touched again the version of the parent requirement would change and the linkage from the child to the parent requirement would be invalid again.

Therefore the link from child to parent also contains the version of the parent - a mismatch should be detected automatically (e.g. during the documentation build).

.. _traceability concept for requirements:

Traceability Concept for Requirements
*************************************

The standards require that a requirement can be traced throughout the complete hierarchy levels including its :ref:`implementation <implementation>` and :ref:`verification <process_verification>`.

In general the traceability is visualized in main development work product traceability model (:ref:`general_concepts_traceability`).

.. needextend:: "c.this_doc()"
   :+tags: requirements_engineering
