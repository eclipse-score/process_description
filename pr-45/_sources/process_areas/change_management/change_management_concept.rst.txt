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
   :id: doc_concept__change__process
   :status: valid
   :tags: change_management

In this section a concept for the Change Management will be discussed. Inputs for this concepts
are both the requirements of ISO26262 Part-8 and ASPICE Requirements from SUP.10 additionally
including the requirements of the different stakeholders for the Change Management process.

Key concept
***********
A Change Request is the **ONLY** way to contribute (compare `REPLACE_doc__contr_guideline`)
new features or to modify the scope of existing features in the **S-CORE** project.
As features are built-up by Components a Change Request is also needed to add new Components or
to modify the scope of existing Components.
As a Software Module is defined as the top-level Component, all statements here for Components
are also valid for Software Modules.

Inputs
******

#. Stakeholders for the Change Requests?
#. Which Change Requests types can we derive from that?
#. Which attributes are required?
#. Which activities are required?

Stakeholders for the Change Requests
************************************

#. :need:`Contributor <rl__contributor>`

   * Contributes features and components to grow the **S-CORE** content

   Contribution include scope modification of existing features/components or adding new
   features/components.

#. :need:`Committer <rl__committer>`

   * Verifies that the contribution fulfills the **S-CORE** policies
   * Approves the contribution

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO SAE 21434

Change Request Types
********************

Feature
=======

This Change Request describes a potential new feature for the platform.
The Change Request uses the Feature request template: :ref:`chm_feature_templates`.

Feature Modification
====================

This Change Request describes a scope modification of an existing feature (requirement or work
product). The Change Request modifies the already existing Feature Request template: :ref:`chm_feature_templates`.

Component
=========

This Change Request describes a potential new component for the platform.
The Change Request uses the Component request template: :ref:`chm_component_templates`.

Component Modification
======================

This Change Request describes a scope modification of an existing component (requirement or work
product). The Change Request modifies the already existing Component Request template: :ref:`chm_component_templates`.


.. _chm_attributes:

Attributes of Change Requests
*****************************

The required attributes for the Change Requests are defined in this subchapter.

Following attributes need to be filled manually for each Change Request:

.. list-table:: Manual Attributes
   :header-rows: 1
   :widths: 15,85

   * - Attribute
     - Description
   * - Unique ID
     - The unique id
   * - Status
     - The status of a Change Request can either be "draft", "in review", "accepted" or "rejected".
   * - Title
     - Reason for the Change Request
   * - Description
     - Exact description of the Change Request
   * - Safety
     - These attribute describes the impact on functional safety.
   * - Security
     - This attribute describes the impact on security
   * - Change Request Type
     - Following types are defined: [Feature, Feature Modification, Component, Component Modification]
   * - Affected work products
     - Links to the work products affected by the Change Request
   * - Milestone
     - Planned date (milestone) of deployment of the Change Request


Activities for a Change Request
*******************************

.. _chm_analysis:

Analysis of the Change Request
==============================

The affected work products must be identified.
The potential impact on functional safety and security must be addressed.
Schedule, risks, resources for the realization must be evaluated.
Verification measures must be defined.
Use therefore the : :ref:`Impact Analysis Template <chm_impact_analysis_templates>`.

.. _chm_evaluation:

Evaluation of the Change Request
================================

Based on the analysis results decision about the acceptance, rejection or delay must be taken
by authorized persons.

Authorized person includes

#. :need:`Technical Lead <rl__technical_lead>`
#. :need:`Module Lead <rl__module_lead>`
#. :need:`Safety Manager <rl__safety_manager>`
#. :need:`Security Manager <rl__security_manager>`
#. :need:`Quality Manager <rl__quality_manager>`

Further prioritization must be done, e.g. based on release planning.


.. _chm_implementation:

Implementation of the Change Request
====================================
If the Change Request is accepted, it must be implemented.


.. _chm_verification:

Verification of the Change Request
==================================

The defined verification measures must be use to confirm the implementation.


.. _chm_reporting:

Reporting of the Change Request
===============================

The status of the Change Request must be communicated by the
:need:`Technical Lead <rl__technical_lead>` or :need:`Module Lead <rl__module_lead>` until
the implementation is completed and confirmed.


.. _chm_traceability:

Traceability Concept for Change Requests
========================================

The standards require that a Change Request can be traced throughout the complete hierarchy levels
including all affected work products.

In general the traceability is visualized in the general traceability concept (:ref:`general_concepts_traceability`).
