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

.. _feature_template:

[Your Feature Name]
###################

.. note:: Document header

.. document:: [Your Feature Name]
   :id: doc__feature_name
   :status: draft
   :version: 2
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feat_request[version==1]
   :tags: template

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``document`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety``, ``security`` and ``tags`` according to your needs

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_[your_feature_name]``

.. note::
   The feature flag must reflect the feature name in snake_case. Further, it is prepended with ``experimental_``, as
   long as the feature is not yet stable.

Abstract
========

[Provide the feature and a brief summary of the feature]

.. code-block:: rst

   .. feat:: Feature Name
      :id: feat__feature_name
      :security: YES
      :safety: ASIL_B
      :status: invalid
      :version: 1
      :includes: logic_arc_int__feature_name__interface_name1

      General Feature Description

[A short (~200 word) description of the contribution being addressed.]

Motivation
==========

[Clearly explain why the existing platform/project solution is inadequate to address the topic that the CR solves.]

.. note::
   The motivation is critical for CRs that want to change the existing features or infrastructure.
   It should clearly explain why the existing solution is inadequate to address the topic that the CR solves.
   Motivation may based on criteria as resource requirements, scheduling issues, risks, benefits, etc.
   CRs submissions without sufficient motivation may be rejected.

Specification
=============

[Describe the requirements, architecture of any new feature.] or
[Describe the change to requirements, architecture, implementation, process, documentation, infrastructure of any change request.]

.. note::
   A CR shall specify the stakeholder requirements as part of our platform/project.
   Thereby the :need:`rl__project_lead` will approve these requirements as part of accepting the CR (e.g. merging the PR with the CR).

How to Teach This
=================

[How to teach users, new and experienced, how to apply the CR to their work.]

.. note::
   For a CR that adds new functionality or changes behaviour, it is helpful to include a section on how to teach users, new and experienced, how to apply the CR to their work.

Footnotes
=========

[A collection of footnotes cited in the CR, and a place to list non-inline hyperlink targets.]


.. toctree::
   :hidden:

   architecture/index.rst
   requirements/index.rst
   requirements/chklst_req_inspection.rst
