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
**tested separately** during the unit testing phase.

Following the **Detailed Design Template** :need:`gd_temp__detailed_design`, we must document the
**design decisions** and **constraints** that guide the decomposition of the component into multiple
units. These decisions should be made based on the following ideas:

-  **Design principles**
-  **Design patterns**
-  **Testability strategies**

The goal is to ensure that the decomposition supports **reusability** , **maintainability**,
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

-  **C++ development** Each **class** can be considered a **unit** in the design.
-  For **Rust development**, a **unit** is modeled using a **combination of `struct` and `trait`**,
   as Rust does not have traditional classes.

Static View
```````````
The **static view** represents the **units** and their relationships using **UML 2.0 notations**,
such as **aggregation, composition, and generalization**. This is depicted through
**UML structural diagrams**, including:

-  **Class Diagrams** – Define **classes, attributes, methods, and relationships** (e.g., inheritance, associations, dependencies).
   Each **class** can be considered a **unit** in the design.
-  **Rust Development Approach** – Instead of traditional classes, **Rust uses `struct` and `trait`
   combinations** to represent **units** in UML diagrams.

This view focuses **only on units and their relationships**.
Details such as **attributes and interfaces** are documented under the **Units within the Component section**
(refer to the template for details).

Note that the detailed design may not be complete in the way that it covers every class which is coded.
These not covered parts may contain implementation detail and should not be needed to understand the
the detailed design.

.. code-block:: rst

   .. dd_sta:: <Title>
      :id: dd_sta__<Component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B>
      :status: <valid|invalid>
      :implements: <link to component requirement id>
      :satisfies: <link to component architecture id>
      :belongs_to: <link to component id>
      :includes: <link to sw_unit id>

      .. needarch:: or .. image:: <link to drawio image>

Dynamic View
````````````
The **dynamic view** illustrates how the **units** interact with each other to fulfill a specific
**use case** or **functionality**. This view captures the **behavioral aspects** of the component as it executes.
It is represented using **UML behavioral diagrams**, including:

- **Sequence Diagrams** – Depict the interactions between objects in a **time-ordered sequence**,
  highlighting how methods are invoked and how control flows between objects over time.
- **State Machine Diagrams** – Show how the **state of an object changes** in response to events,
  allowing for the modeling of complex state transitions (if there is stateful behaviour).

These diagrams are essential for understanding the **dynamic behavior** of the component and how
units collaborate to perform tasks. But this also means that if the dynamic behaviour is simple
it does not require a dynamic diagram at all (similar to the rules depicted in :need:`gd_guidl__arch_design`).

.. code-block:: rst

   .. dd_dyn:: <Title>
      :id: dd_dyn__<Component>__<Title>
      :security: <YES|NO>
      :safety: <QM|ASIL_B>
      :status: <valid|invalid>
      :implements: <link to component requirement id>
      :satisfies: <link to component architecture id>
      :belongs_to: <link to component id>
      :includes: <link to sw_unit id>

      .. needarch:: or .. image:: <link to drawio image>

Units within the Component
--------------------------

For each unit it will have a id and the interfaces are shown in the interface view per unit.
The description of unit and its attributes can be seen in the code documentation.
For this we use the tracing to the documentation generated from the code comments.

We link the unit id to the comments in the code like:

-  Maintain your units in rst files and link them to the source code

   Use `score_source_code_linker` from `docs-as-code` repo with
   `user docu <https://eclipse-score.github.io/docs-as-code/main/how-to/source_to_doc_links.html>`__.

   In your rst file:

   .. code-block:: rst

      .. sw_unit:: cpp unit
         :id: sw_unit__<Component>__<title>
         :belongs_to: <link to component id>

         This implements the ....

   In your source file, any porgramming language, here with C++:

   .. code-block:: cpp

      # need-Id: sw_unit__<Component>__<title>
      class <class name> {
         public:

      };

-  For cpp using doxygen style comments

   .. code-block:: cpp

      /**
         * @rst
         * .. sw_unit:: cpp unit
         *    :id: sw_unit__<Component>__<title>
         *    :belongs_to: <link to component id>
         *
         *    This implements the ....
         * @endrst
      */

- for rust

   .. code-block:: rust

      //! .. sw_unit:: rust unit
      //!     :id: sw_unit__<Component>__<title>
      //!     :belongs_to: <link to component id>
      //!
      //!     This implements the ....


Interface View
``````````````
For every unit, the Interface View should display the interfaces provided by that unit.
For each unit and its corresponding interfaces, an implementation and documentation must
be created.

The following section provides templates for defining needs within the source code:

-  Maintain your units in rst files and link them to the source code

   Use `score_source_code_linker` from `docs-as-code` repo with
   `user docu <https://eclipse-score.github.io/docs-as-code/main/how-to/source_to_doc_links.html>`__.

   In your rst file:

   .. code-block:: rst

      .. sw_unit_int:: <here InterfaceDemo - change it>
         :id: sw_unit_int__<Component>__<title>
         :belongs_to: <link to sw_unit id>

         This implements the ....

   In your source file, any porgramming language, here with C++:

   .. code-block:: cpp

      # need-Id: sw_unit__<Component>__<title>
      class InterfaceDemo
      {
         public:
            virtual ~InterfaceDemo() {}
            virtual void OverrideMe() = 0;
      };

-  For cpp using doxygen comments

   .. code-block:: cpp

      /**
         * @rst
         * .. sw_unit_int:: cpp unit
         *    :id: sw_unit_int__<Component>__<title>
         *    :belongs_to: <link to sw_unit id>
         *
         *    This implements the ....
         * @endrst
      */

-  For rust

   .. code-block:: rust

      //! .. sw_unit_int:: rust unit
      //!     :id: sw_unit_int__<Component>__<title>
      //!     :belongs_to: <link to sw_unit id>
      //!
      //!     This implements the ....
