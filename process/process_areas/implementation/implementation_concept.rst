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
**tested separately** during the unit testing phase. This decomposition shall support the implementation
and testing of the component's requirements while adhering to the design principles and patterns
established in the architecture.

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

Definition of a Unit
--------------------

A **unit** is a **granular, independent entity** of a component that can be **tested separately**
during the unit testing phase. Each unit represents a **self-contained functionality** and is
derived from the decomposition of a component.

**Characteristics of a Unit**

-  **Independent** – Can be tested in isolation.
-  **Granular** – Represents a small, well-defined part of the system.
-  **Relational** – Has associations with other units, defined using **UML 2.0 notations** such as
   aggregation, composition, and generalization.

**Examples:**
The definition of a unit depends on the used programming language. Examples for a unit are
a source file, a definition file (e.g. c++ header), classes, structs, and functions.
This list is not complete or exclusive.

**Units in UML Diagrams**

-  **C++ development** – Each **class** can be considered a **unit** in the design.
-  **Rust development** – A **unit** is modeled using a **combination of `struct` and `trait`**,
   as Rust does not have traditional classes.

Units within the Component
--------------------------

The relationship between a unit and its parent component is established implicitly through the
**file path** — each component has its own directory, and units residing within that directory
belong to it and therefore inherit the accordance to the architecture. A separate static diagram
per unit is **not required**; the unit's attributes and behaviour are documented in the source
code itself as the source code is sufficiently self-explanatory and adheres to the design principles outlined in the development plan.

This is sufficient for ASIL B compliance per :need:`ISO 26262-6 §8 <std_req__iso26262__software_841>`, as the structural decomposition
is evident from the directory layout and the component-level static view already captures the
relevant unit relationships.

However, for components with complex interactions or a large number of units, a static view can be beneficial for understanding the overall structure and relationships between units. The developer may choose to add a additional unit-level static and dynamic view if they believe it helps to explain the source code better.

Design Principles of the Units
``````````````````````````````

The unit design shall achieve quality attributes (like simplicity, modularity, and encapsulation) which shall be enforced through coding guidelines and static analysis tooling appropriate for the programming language in use (e.g. MISRA C for C/C++, Clippy lints for Rust) as specified in the project development plan to fulfill the guidelines :need:`ISO 26262-6 §8.4.5, Table 6 <std_req__iso26262__software_845>` and :need:`ASPICE SWE.3/SWE.4<std_req__aspice_40__SWE-3-BP3>` requirements.

The **source code** itself shall be self-documenting with meaningful naming and structure.
**Code comments** may be used where the logic is not self-evident and to give an rationale.
These comments, along with commit messages, and any additional documentation accompanying the
source code shall use natural language.

The interface documentation of a software unit is part of the source code (e.g. public API headers,
trait definitions, or documented function signatures).

Diagrams
--------

Developers may add **class diagrams** or **sequence diagrams** at the unit level if they believe
it helps to explain the source code better. These are optional and serve as supplementary
documentation — they are not required by the process.

Static View
```````````

If a static view is used it shall provide an overview of the **units** and their
relationships using **UML 2.0 notations**, such as **aggregation, composition, and
generalization**. It is depicted through **UML structural diagrams**, including:

-  **Class Diagrams** – Define classes, attributes, methods, and relationships (e.g.,
   inheritance, associations, dependencies).
- **Component Diagrams** – Show the organization and dependencies among software units,
   which can be used to represent the units within a component.
-  **Rust** – Uses `struct` and `trait` combinations to represent units in UML diagrams.

The static view need not cover every class or struct in the implementation — it should show
the units and relationships that are necessary to understand the detailed design.
The naming of the units and their interfaces in the static view should match the naming
in the source code to ensure traceability. Implementation  details that are not relevant
at the design level may be omitted.

According to the software development plan of the project the developer may use tools
like PlantUML or DrawIo for such diagrams.

Dynamic View
````````````

An optional **dynamic view** illustrates how the **units** within a component interact over their
**interfaces** to fulfill a specific **use case** or **functionality**. This is a
**component-level** view — individual per-unit dynamic diagrams are **not required**.

It is represented using **UML behavioural diagrams**, including:

-  **Sequence Diagrams** – Depict the interactions between objects in a time-ordered sequence,
   highlighting how methods are invoked and how control flows between objects over time.
-  **State Machine Diagrams** – Show how the state of an object changes in response to events,
   allowing for the modeling of complex state transitions (if there is stateful behaviour).

A dynamic view is **optional** when the component's behaviour is straightforward and can be
understood from the static view and interface documentation alone (similar to the rules
depicted in :need:`gd_guidl__arch_design`).

Example using PlantUML:

.. uml::

   @startuml
   participant UnitA
   participant UnitB

   UnitA -> UnitB : request()
   UnitB --> UnitA : response()
   @enduml
