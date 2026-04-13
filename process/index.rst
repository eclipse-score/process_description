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

.. _process_description:

Process description
===================

Processes are the basis to describe the way of working within a project.

Introduction
------------

The introduction page outlines the code-centric, workflow-driven process model which ensures compliance with ASPICE and ISO standards, establishes end-to-end traceability from the start, and leverages tool automation for verification. It shows and explains the model's key concepts, their parts and interactions.

.. toctree::
   :maxdepth: 1
   :glob:

   introduction/index.rst


General Concepts
----------------

The general concepts like traceability of work products, life cycle model, building blocks can be found here:

.. toctree::
   :maxdepth: 1

   general_concepts/index.rst


Process Model
-------------
The project process model is described by workflows, executed by roles and is creating work products.
Workflow activities are supported by guidances. For further details (like motivation, objectives and approach) please refer to the :ref:`introduction page<processes_introduction>` and the respective sections below.


Process Areas
~~~~~~~~~~~~~

The process description for the project (e.g. requirements, architecture, safety management) can be found here:

.. toctree::
   :maxdepth: 1

   process_areas/index.rst

Management
**********

.. grid:: 1 1 3 3
   :class-container: score-grid

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Platform Management <platform_management>`
      ^^^
      Manage the common platform, its modules and integration.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Safety Management <process_safety_management>`
      ^^^
      Plan and oversee safety activities across the project lifecycle.

   .. grid-item-card::
      :class-card: card-ml1

      :ref:`Security Management <security_management>`
      ^^^
      Plan and oversee cybersecurity activities across the project lifecycle.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Quality Management <quality_management>`
      ^^^
      Define and monitor quality objectives, measures and improvements.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Change Management <change_management>`
      ^^^
      Control and track changes to work products and configurations.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Problem Resolution <problem_resolution>`
      ^^^
      Identify, analyse and resolve problems found during development.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Release Management <release_management>`
      ^^^
      Plan, prepare and control the release of deliverables.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Process Management <process_management>`
      ^^^
      Define, deploy and improve the organisational process.

Development
***********

.. grid:: 1 1 3 3
   :class-container: score-grid

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Requirements Engineering <requirements_engineering>`
      ^^^
      Elicit, specify and manage stakeholder and system requirements.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Architecture Design <arch_design_process>`
      ^^^
      Define and document the system and software architecture.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Implementation <implementation>`
      ^^^
      Develop and unit-test software units according to the design.

   .. grid-item-card::
      :class-card: card-ml1

      :ref:`Verification <process_verification>`
      ^^^
      Verify that work products fulfil their specified requirements.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Safety Analysis <safety_analysis>`
      ^^^
      Identify and assess safety hazards and derive mitigation measures.

   .. grid-item-card::
      :class-card: card-ml1

      :ref:`Security Analysis <security_analysis>`
      ^^^
      Identify and assess security threats and derive mitigation measures.

Support
*******

.. grid:: 1 1 3 3
   :class-container: score-grid

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Configuration Management <process_configuration_management>`
      ^^^
      Control versions and baselines of all project artefacts.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Tool Management <tool_management>`
      ^^^
      Qualify and manage tools used in the development process.

   .. grid-item-card::
      :class-card: card-ml2

      :ref:`Documentation Management <process_documentation_management>`
      ^^^
      Plan, create and maintain project and product documentation.


.. figure :: _assets/score_process_area_overview.drawio.svg
  :width: 0%
  :align: center
  :alt: Process area overview for the **Project**

  Process area overview for **Project**

.. raw:: html

   <figure>
     <object data="_images/score_process_area_overview.drawio.svg" type="image/svg+xml"
             width="100%"></object>
     <figcaption>Process area overview for Project</figcaption>
   </figure>


Process Role definition
~~~~~~~~~~~~~~~~~~~~~~~

The general roles that are not part of any process area and the project roles list can be found here:

.. toctree::
   :maxdepth: 1

   roles/index.rst

Work Products
~~~~~~~~~~~~~

The general work products that are not part of any process area and the work product overview list can be found here:

.. toctree::
   :maxdepth: 1

   workproducts/index.rst

Workflows
~~~~~~~~~

The general workflows that are not part of any process area and workflow overview list can be found here:

.. toctree::
   :maxdepth: 1

   workflows/index.rst

Standards & Requirements
------------------------

The standard references the project's processes are derived from and the coverage of the requirements and the work products from the standards can be found here:

.. toctree::
   :maxdepth: 1

   standards/index.rst

Trustable Software Framework
----------------------------

The trustable measure based on sphinx-needs for OSS project's can be found here:

.. toctree::
   :maxdepth: 1

   trustable/index.rst

Folder Templates
----------------

These template folders for features, modules and components can be copied to establish the intended structure
and they include the available templates for the work products already in the right place:

.. toctree::
   :maxdepth: 1

   folder_templates/index.rst


Glossary
--------

This glossary defines key terms used throughout the process description workspace.
These terms are fundamental to understanding the different process areas including
their workflows, work products, roles and guidances.

.. toctree::
   :maxdepth: 1

   glossary/index.rst

Release Notes
-------------

Release notes collection.

.. toctree::
   :maxdepth: 1

   release_notes/index.rst
