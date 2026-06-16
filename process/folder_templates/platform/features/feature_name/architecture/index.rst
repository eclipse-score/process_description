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

.. note::
   The complete feature architecture template as shown here is intended to document the idea about the architecture of a feature (if needed) when a CR is created. After the CR is granted, it is moved and further detailed / maintained in the module where the feature resides. See `module template documentation <https://eclipse-score.github.io/module_template/main/>`__. Only the logical interfaces remains in the feature architecture platform documentation, as they are relevant for the overall platform architecture. The detailed architecture of the feature is documented in the module documentation, and the logical interfaces are linked from there to the platform documentation. This is to avoid that the platform documentation becomes too detailed and hard to maintain, while still providing the necessary information about the feature architecture in the platform documentation. Depending from the project it might be that in the reference integration of the platform the full feature architecture including the implementation of the features and its components becomes visible in the platform documentation. See :ref:`Deployment example <deployment_example>`.

.. document:: [Your Feature Name] Architecture
   :id: doc__feature_name_architecture
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_arch[version==1]
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

The live feature architecture template snippets are maintained in the
`module template documentation <https://eclipse-score.github.io/module_template/main/>`__.


Logical Interfaces
------------------

.. code-block:: rst

   .. logic_arc_int:: Interface Name
      :id: logic_arc_int__feature_name__interface_name1
      :security: YES
      :safety: ASIL_B
      :status: invalid
      :version: 1
      :fulfils: feat_req__feature_name__some_title

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
      :version: 1
      :included_by: logic_arc_int__feature_name__interface_name1

      General Operation Description
