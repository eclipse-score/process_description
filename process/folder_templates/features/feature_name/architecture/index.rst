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

.. _feature_architecture_template:

Feature Architecture
====================

.. document:: [Your Feature Name] Architecture
   :id: doc__feature_name_architecture
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_arch
   :tags: template

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__`` and followed by ``_architecture``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

Overview
--------
<Brief summary>

Description
-----------

<General Description>

<Design Decisions - For the documentation of the decision the :need:`gd_temp__change_decision_record` can be used.>

<Design Constraints>

Requirements
------------

.. code-block:: none

   .. needtable:: Overview of Feature Requirements
      :style: table
      :columns: title;id
      :filter: search("feat_arch_sta__archdes$", "fulfils_back")
      :colwidths: 70,30


.. needtable:: Overview of Feature Requirements
   :style: table
   :columns: title;id
   :filter: search("feat_arch_sta__archdes$", "fulfils_back")
   :colwidths: 70,30


Rationale Behind Architecture Decomposition
*******************************************

Mandatory: A motivation for the decomposition

.. note:: Common decisions across features / cross cutting concepts is at the high level.

Static Architecture
-------------------

.. feat:: Feature Name
   :id: feat__feature_name
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :includes: logic_arc_int__feature_name__interface_name1
   :consists_of: comp__component_name_template

   General Feature Description

.. feat_arc_sta:: Feature Static View
   :id: feat_arc_sta__feature_name__static_view
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :fulfils: feat_req__feature_name__some_title
   :includes: logic_arc_int__feature_name__interface_name1
   :belongs_to: feat__feature_name

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

Dynamic Architecture
--------------------

.. feat_arc_dyn:: Dynamic View
   :id: feat_arc_dyn__feature_name__dynamic_view
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :fulfils: feat_req__feature_name__some_title
   :belongs_to: feat__feature_name

   Put here a sequence diagram

Logical Interfaces
------------------

.. logic_arc_int:: Interface Name
   :id: logic_arc_int__feature_name__interface_name1
   :security: YES
   :safety: ASIL_B
   :status: invalid

   General Interface Description

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: Operation
   :id: logic_arc_int_op__feature_name__operation
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :included_by: logic_arc_int__feature_name__interface_name1

   General Operation Description

Module Viewpoint
----------------

The following modules are needed to be defined to be able to draw the static feature view.
They will be replaced by linking the proper module definitions in the used module's repositories as soon as those exist.

.. mod:: Module Name
   :id: mod__module_name
   :includes: comp__component_name_template


.. mod_view_sta:: Module Name Static View
   :id: mod_view_sta__feature_name__module_name
   :includes: comp__component_name_template

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Used Components
---------------

The following components are needed to be defined to be able to draw the static feature view.
They will be replaced by linking the proper SW component definitions in the used module's repositories as soon as those exist.

.. code-block:: rst

   .. comp:: Component Name
      :id: comp__component_name_template
      :safety: ASIL_B
      :security: YES
      :status: invalid
      :implements: logic_arc_int__feature_name__interface_name1

.. note::
   Architecture can be split into multiple files, it is an high level architecture design
   which can be shown without actual c++/rust interfaces and data types
   and there will be link to internal architecture till code to get actual api descriptions.

.. attention::
    The above directives must be updated according to your feature architecture.

    - Replace the example content by the real content (according to :need:`gd_guidl__arch_design`)
    - Set the status to valid and start the review/merge process
