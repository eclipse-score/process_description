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

.. _definition_architectural_design:

Example model of architectural design
#####################################

This chapter only serves as an example how an architecture could be modeled in *Sphinx Needs*. All the needs are required to print the views which are displayed in the Static- and Interface Views. In the actual process this files would be split into multiple different files:

Feature Architecture File
=========================

.. feat:: Feature 1
   :id: feat__example_feature
   :security: YES
   :safety: QM
   :status: valid
   :includes: logic_arc_int__example_feature__archex_logical_interface_1, logic_arc_int__example_feature__archex_logical_interface_2, logic_arc_int__example_feature__archex_logical_interface_3
   :consists_of: comp__component_example_1

   This is the example feature.

.. feat_arc_sta:: Feature 1 Static View
   :id: feat_arc_sta__example_feature__archdes_static
   :security: YES
   :safety: QM
   :status: valid
   :includes: logic_arc_int__example_feature__archex_logical_interface_1, logic_arc_int__example_feature__archex_logical_interface_2, logic_arc_int__example_feature__archex_logical_interface_3
   :fulfils: feat_req__example_feature__archdes_example_req
   :belongs_to: feat__example_feature

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

.. Logical Interfaces

.. logic_arc_int:: Logical Interface 1
   :id: logic_arc_int__example_feature__archex_logical_interface_1
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__example_feature__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}


.. logic_arc_int:: Logical Interface 2
   :id: logic_arc_int__example_feature__archex_logical_interface_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__example_feature__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}


.. logic_arc_int:: Logical Interface 3
   :id: logic_arc_int__example_feature__archex_logical_interface_3
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__example_feature__archdes_example_req


.. Logical Interface Operation

.. logic_arc_int_op:: Logical Operation 1
   :id: logic_arc_int_op__example_feature__archex_logical_operation_1
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_1

.. logic_arc_int_op:: Logical Operation 2
   :id: logic_arc_int_op__example_feature__archex_logical_operation_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_1

.. logic_arc_int_op:: Logical Operation 3
   :id: logic_arc_int_op__example_feature__archex_logical_operation_3
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_2

.. logic_arc_int_op:: Logical Operation 4
   :id: logic_arc_int_op__example_feature__archex_logical_operation_4
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_2

.. logic_arc_int_op:: Logical Operation 5
   :id: logic_arc_int_op__example_feature__archex_logical_operation_5
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_3

.. logic_arc_int_op:: Logical Operation 6
   :id: logic_arc_int_op__example_feature__archex_logical_operation_6
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_3

.. logic_arc_int_op:: Logical Operation 7
   :id: logic_arc_int_op__example_feature__archex_logical_operation_7
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_3

.. logic_arc_int_op:: Logical Operation 8
   :id: logic_arc_int_op__example_feature__archex_logical_operation_8
   :security: YES
   :safety: ASIL_B
   :status: valid
   :included_by: logic_arc_int__example_feature__archex_logical_interface_3


Module Viewpoint
================

.. mod:: Module 1
   :id: mod__example_feature_archex_module_1
   :security: YES
   :safety: ASIL_B
   :status: valid
   :includes: comp__component_example_1, comp__component_example_2

   This is Module 1.

.. mod_view_sta:: Module 1 Static View
   :id: mod_view_sta__example_feature__archex_1
   :includes: comp__component_example_1, comp__component_example_2

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

.. mod:: Module 2
   :id: mod__example_feature_archex_module_2
   :security: YES
   :safety: ASIL_B
   :status: valid
   :includes: comp__component_example_3

   This is Module 2.

.. mod_view_sta:: Module 2 Static View
   :id: mod_view_sta__example_feature__archex_2
   :includes: comp__component_example_3

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Component Architecture File(s)
==============================

.. comp:: Component 1
   :id: comp__component_example_1
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :implements: logic_arc_int__example_feature__archex_logical_interface_1
   :consists_of: comp__archex_sub_component_1, comp__archex_sub_component_2, comp__archex_sub_component_3

   Example Component 1 description.

.. comp:: Component 2
   :id: comp__component_example_2
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :implements: logic_arc_int__example_feature__archex_logical_interface_2

   Example Component 2 description.

.. comp:: Component 3
   :id: comp__component_example_3
   :security: YES
   :safety: QM
   :status: invalid
   :implements: logic_arc_int__example_feature__archex_logical_interface_3

   Example Component 3 description.

.. comp_arc_sta:: Component 1 Static View
   :id: comp_arc_sta__example_feature__archdes_component_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :belongs_to: comp__component_example_1
   :fulfils: comp_req__example_feature__archex_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

.. Subcomponents

.. comp:: Component 1_1
   :id: comp__archex_sub_component_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__example_feature__archex_logical_interface_2
   :implements: logic_arc_int__example_feature__archex_logical_interface_1

.. comp:: Component 1_2
   :id: comp__archex_sub_component_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :uses: logic_arc_int__example_feature__archex_logical_interface_2
   :implements: logic_arc_int__example_feature__archex_logical_interface_2

.. comp:: Component 1_3
   :id: comp__archex_sub_component_3
   :status: valid
   :safety: ASIL_B
   :security: NO

Requirements for the Example
=============================

.. Requirements

.. stkh_req:: Example Stkh Req
   :id: stkh_req__example_feature__archdes_example_req
   :reqtype: Functional
   :safety: ASIL_B
   :security: YES
   :rationale: needed for archdes example
   :status: valid

   The platform shall provide the feature ....

.. feat_req:: Example Feature Req
   :id: feat_req__example_feature__archdes_example_req
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__example_feature__archdes_example_req
   :status: valid
   :belongs_to: feat__example_feature

   The feature shall provide the functionality to ....

.. comp_req:: Example Component Req
   :id: comp_req__example_feature__archex_example_req
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: feat_req__example_feature__archdes_example_req
   :status: valid
   :belongs_to: comp__component_example_2

   The component shall provide the Logical Operation 4 to get the ..
