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
   :id: doc_concept__imp_concept
   :status: valid
   :version: 1
   :tags: implementation

In this section a concept for the implementation will be discussed. Inputs for this concepts are
both the requirements of ISO26262 Part-6 Chapter 8+9 and ASPICE SWE 3+4.

Inputs
******

#.  ISO 26262 Part-6 Chapter 8+9
#.  ASPICE SWE 3+4
#.  Component Requirements :need:`wp__requirements_comp` and Architecture :need:`wp__component_arch`
#.  Software Development Plan :need:`gd_temp__software_development_plan`

Outputs
*******

Detailed Design
===============

In this step, the **components** are broken down into smaller, independent **units** that can be
**tested separately** during the unit testing phase. The basis for this decomposition are the
:need:`Component Requirements <wp__requirements_comp>` and the :need:`Component Architecture <wp__component_arch>`.
The decomposition shall support the implementation and testing of the component's requirements while
adhering to the design principles and patterns established in the architecture.

Following the **Detailed Design Template** :need:`gd_temp__detailed_design`, we must document the
**design decisions** and **constraints** that guide the decomposition of the component into multiple
units. These decisions should be made based on the following ideas:

-  **Design principles**
-  **Design patterns**
-  **Testability strategies**

The goal is to ensure that the decomposition supports **reusability**, **maintainability**,
**scalability**, **extensibility** and **ease of testing**.

The detailed design and implementation should follow an **iterative approach**, allowing for
continuous improvements in quality through multiple cycles of refinement.

The implementation concept intentionally stays at a high level. Practical guidance for
unit decomposition, source-code documentation, optional diagrams and naming consistency
for traceability is defined in :need:`Implementation Guideline <gd_guidl__implementation>`.

.. needextend:: "c.this_doc()"
   :+tags: implementation
