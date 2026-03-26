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

.. doc_concept:: Concept Description
   :id: doc_concept__change_process
   :status: valid
   :tags: change_management

In this section a concept for the Change Management will be discussed. Inputs for this concepts
are both the requirements of ISO26262 Part-8 and ASPICE Requirements from SUP.10 additionally
including the requirements of the different stakeholders for the Change Management process.

Key concept
***********
A *Change Request* is the **ONLY** way to contribute new features or to modify the scope
of existing features in the project.
As features are built-up by components a Change Request is also needed to add new
components or to modify the scope of existing components.
All statements here for components are also valid for *SW Modules*.

Inputs
******

#. Stakeholders for the Change Requests?
#. Which attributes are required?
#. Which activities are required?

Stakeholders for the Change Requests
************************************

#. :need:`Contributor <rl__contributor>`

   * In general contributes features and components to grow the project content
   * Creates change requests
   * Supports all change request activities

#. :need:`Architecture Team <rl__architecture_community>`

   * Supports all change request activities
   * Approves the creation of the change request
   * Verifies that the contribution including change requests fulfills the project policies

#. :need:`Platform Team <rl__platform_team>`

   * Supports creation and the analysis of change requests
   * Is responsible and approves the implementation and the closure of the feature change request

#. :need:`Delivery Team <rl__delivery_team>`

   * Is responsible and approves the implementation and the closure of the component change request

#. :need:`Project Lead <rl__project_lead>`

   * Supports all change request activities
   * Approves the analysis of the change request
   * Verifies that the contribution including change requests fulfills the project policies


Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO SAE 21434

.. _chm_attributes:

Attributes of Change Requests
*****************************

The required attributes for the Change Request are defined here: :ref:`chm_process_change_request_attributes`.


Activities for a Change Request
*******************************

.. _chm_creation:

Creation of the Change Request
==============================
Use the content :ref:`Feature Request Template <chm_feature_templates>` or
:ref:`Component Request Template <chm_component_templates>` to create a Change Request.

In case safety or security is affected, in addition the impact analysis template
: :ref:`Impact Analysis Template <chm_impact_analysis_templates>` can be used to detail
out the impact on safety/security.

The impact analysis tool (:need:`gd_req__change_tool_impact_analysis`) can support to
here to identify the affected work products.

.. _chm_analysis:

Analysis of the Change Request
==============================
Based on the analysis results decision about the acceptance or rejection must be taken
by authorized persons.

Authorized person, as members of the :need:`Platform Team <rl__platform_team>`, includes

#. :need:`Project Lead <rl__project_lead>`
#. :need:`Safety Manager <rl__safety_manager>`
#. :need:`Security Manager <rl__security_manager>`
#. :need:`Quality Manager <rl__quality_manager>`
#. :need:`Committer <rl__committer>`

Further prioritization must be done, e.g. based on release planning.

.. _chm_implementation_monitoring:

Implementation and Monitoring of the Change Request
===================================================
If the Change Request is accepted, the implementation of the change must be initiated and
monitored.

The Change Request implementation must be tracked until it is closed.

The status of the Change Request must be communicated by the
:need:`Project Lead <rl__project_lead>` (for feature requests) and the lead of the
:need:`Delivery Team <rl__delivery_team>` (for component requests) until
the implementation is completed and confirmed.

.. _chm_closing:

Closing of the Change Request
=============================

Use the :ref:`Change Request Review Checklist <chm_checklist>` to control the completeness of the
Change Request to be closed.

Especially the effectiveness of the solution measures must be shown, based on convincing
arguments, e.g. verification measures must be used to confirm the implementation.

The standards require that a Change Request can be traced throughout the complete
hierarchy levels including all affected work products.

In general the traceability is visualized in the general traceability concept (:ref:`general_concepts_traceability`).
