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

Building blocks meta model
++++++++++++++++++++++++++

The following figure gives an overview about the building blocks of the project **Platform**
(blue box, top, 2nd column). The objectives of the project platform include
enabling of feature integration for different use cases and domains. This includes
safety-critical applications. Thus the intention is, that the platform can be developed
as a Safety Element out of Context (**SEooC**) and it can be delivered as part of a
Delivery Container (green box, top, 1st column). The objectives of the platform are
expressed as concrete **Stakeholder Requirements** (blue box, top, 2nd column), which
can be tested by provided **Platform Integration Tests** (blue box, top, 6th column)
for reference hardware platforms. A **Platform Safety/Security Analysis**
(blue box, top, 6th column) is required to verify the Feature Architectures, whereby
violations of safety/security requirements must be documented. Potential faults
may mitigated by updating the Stakeholder Requirements or by the **SW-platform
Assumptions of Use** (blue box, top, 7nd column).

The platform consists of **Features** (yellow box, middle, 2nd column).

Further the project provides **Dependable Elements** (red box, middle, 1st column),
which can also be developed as a SEooC and it can be delivered as part of a Delivery
Container. A Dependable Element is consists of **Components** (green box, middle, 2nd column)
or a set of components realizing a Feature of the platform. In this sense a Dependable
Element is the highest abstraction level in our model. A Dependable Element,
delivered in a Delivery Container represents e.g. executable code or a library.
The **Dependable Element View** (red box, middle, 1st column) documents the mapping of
components to a Dependable Element.

Components are the major building blocks of the platform. Components consists of **Units**
(grey box, bottom, 2nd column), the lowest level in our model. The represent the source code,
which implements the Unit. Units has a **Detailed Design** (grey box, middle, 3rd column),
which is also implemented by the **Source Code** (grey box, bottom, 3rd column).
The Detailed Design is verified by **Unit Tests** (grey box, middle, 5th column).

Components are defined by **Component Requirements** (green box, middle, 3rd column) and
the **Component Architecture** (green box, middle, 4th column).
A **Component Safety/Security Analysis** (green box, middle, 6th column) is required to
verify the Component Architecture, whereby violations of safety/security requirements
must be documented. Potential faults may mitigated by updating the Component Requirements
or by the **Component Assumptions of Use** (green box, middle, 8nd column). The latter
one must be considered by the user of the Component. **Component Integration Tests**
(green box, middle, 5th column) verify the Component  requirements, and the Component
Architecture as well as the Integration of multiple Units to a Component.

Features consists of components and are defined by **Feature Requirements**
(yellow box, middle, 3rd column) and the **Feature Architecture** (yellow box, middle, 4th column).
A **Feature Safety/Security Analysis** (yellow box, middle, 6th column) is required to
verify the Feature Architecture, whereby violations of safety/security requirements must
be documented. Potential faults may mitigated by updating the Feature Requirements or by
the **Feature Assumptions of Use** (yellow box, middle, 8nd column). The latter one must
be considered by the user of the Feature. **Feature Integration Tests**
(yellow box, middle, 5th column) verify the Feature Requirements and the Feature
Architecture.
Feature has **Logical Architecture Interfaces** (green box, middle, 3th column), which
are implemented by the components.

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
