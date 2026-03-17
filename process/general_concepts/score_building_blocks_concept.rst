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

.. _general_concepts_building_blocks:

Building blocks concept
-----------------------

.. doc_concept:: Building Block Concept
   :id: doc_concept__general_building_blocks
   :status: valid
   :tags: process_management

.. attention::
   The meta model is not intended to be complete.
   The meta model is intended to give an overview about the building blocks of the
   platform and their relationships. It is not intended to give a detailed description
   of the building blocks and their relationships.

Building blocks meta model
++++++++++++++++++++++++++

The following figure gives an overview about the building blocks of the project **Platform**
(blue box, top, 2nd column). The objectives of the project platform include
enabling of feature integration for different use cases and domains. This includes
safety-critical applications. Thus the intention is, that the platform can be developed
as a Safety Element out of Context (**SEooC**) and it can be delivered as part of a
Delivery Container (green box, top, 1st column). The objectives of the platform are
expressed as concrete **Stakeholder Requirements** (blue box, top, 4th column), which
can be tested by provided **Platform Integration Tests** (blue box, top, 6th column)
for reference hardware platforms. A **Platform Safety/Security Analysis**
(blue box, top, 7th column) is required to verify the Feature Architectures, whereby
violations of safety/security requirements must be documented. Potential faults
may mitigated by updating the Stakeholder Requirements or by **Assumptions of Use**
(white box, 8th column).

The platform consists of **Features** (yellow box, middle, 2nd column).

Further the project provides **Dependable Elements** (red box, middle, 1st column),
which can also be developed as a SEooC and are delivered as part of a **Delivery
Container**. This Delivery Container can contain one or more Dependable Elements,
it is versioned and can be depended on by other Delivery Containers.
A Dependable Element consists of one or more **Components** (green box, middle, 2nd column),
which are in the same Delivery Container as the Dependable Element.
In this sense a Dependable Element is the highest abstraction level in our model. A Dependable Element,
delivered in a Delivery Container represents e.g. executable code or a library.
The **Dependable Element View** (red box, middle, 1st column) documents the mapping of
components to a Dependable Element. Note that the term "Dependable" hints that the
element can have safety and/or security relevance (but also none of these).

.. attention::
   Throughout the process description workspace, the term "Module" or "SW  Module" is
   used for convenience reason as a synonym for "Dependable Element".

Components are the major building blocks of the platform. Components consists of **Units**
(grey box, bottom, 2nd column), the lowest level in our model. It represents the source code,
which implements the Unit. Units have a **Detailed Design** (grey box, middle, 4th column),
which is also implemented by the **Source Code** (grey box, bottom, 4th column).
The Detailed Design is verified by **Unit Tests** (grey box, middle, 6th column).

Components are defined by **Component Requirements** (green box, middle, 4th column) and
the **Component Architecture** (green box, middle, 5th column).
A **Component Safety/Security Analysis** (green box, middle, 7th column) is required to
verify the Component Architecture, whereby violations of safety/security requirements
must be documented. Potential faults may mitigated by updating the Component Requirements
or by **Assumptions of Use** (white box, 8th column). The latter
one must be considered by the user of the Component. **Component Integration Tests**
(green box, middle, 6th column) verify the Component  requirements, and the Component
Architecture as well as the Integration of multiple Units to a Component.

Features consists of components and are defined by **Feature Requirements**
(yellow box, middle, 4th column) and the **Feature Architecture** (yellow box, middle, 5th column).
A **Feature Safety/Security Analysis** (yellow box, middle, 7th column) is required to
verify the Feature Architecture, whereby violations of safety/security requirements must
be documented. Potential faults may mitigated by updating the Feature Requirements or by
**Assumptions of Use** (white box, 8th column). The latter one must
be considered by the user of the Feature. **Feature Integration Tests**
(yellow box, middle, 6th column) verify the Feature Requirements and the Feature
Architecture.
Features have **Logical Architecture Interfaces** (green box, middle, 3rd column), which
are implemented (and can be used) by the components.

**Assumptions of Use** are not specific for a level as it is not fixed where they will be
fulfilled and verified, so they are depicted "white". In the picture one can also see two
variants of Assumptions of Use: "own" AoU required by the own element towards other elements and
the "other" AoU asked from other element towards the own element and fulfilled by it.
Generally the metamodel refers only within own architecture element (=component/feature), but
AoUs need the fulfills link own -> other.

.. figure:: _assets/score_building_blocks_meta_model.drawio.svg
  :width: 100%
  :align: center
  :alt: Building blocks overview for project platform

  Building blocks overview for the project platform

Building blocks example
+++++++++++++++++++++++

The following figure is an example to explain the elements from the meta model.
The user of the project platform wants to use the feature Persistency. For that the
user must integrate the dependable element "Key-Value-Store", which is delivered by the
container "Persistency". As this dependable elements depends on
another dependable element, the user must also integrate "JSON-Library", which is
delivered by the container "Baselibs".
The dependable element "Key-Value-Storage" is built-up by the components "kvs" and "fs",
where the dependable element "JSON-Library" contains only one component "json".
The latter example is more or less a corner case. Components may optionally built-up
by other components. Delivery container may also contain dependable elements, which are
developed as safety element out of context (SEooC).

.. figure:: _assets/score_building_blocks_example.drawio.svg
  :width: 100%
  :align: center
  :alt: Building blocks example

  Building blocks example


Deployment example
++++++++++++++++++

The following figure is an example how the meta model may deployed on several repositories.
The project main repository has the information about the platform and the features.
These include stakeholder requirements, platform architecture, safety/security analysis
and platform assumptions of use. Further the features, their requirements and their
logical interfaces.

The project dependable element repository has the remaining feature artifacts and
the components and units. There may several repositories of them.

The project reference_integration repository includes only the platform integrations
tests.

.. figure:: _assets/score_building_blocks_meta_model_deployment_example.drawio.svg
  :width: 100%
  :align: center
  :alt: Building blocks deployment example

  Building blocks deployment example
