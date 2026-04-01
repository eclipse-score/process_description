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

Feature Requirements
####################

.. document:: [Your Feature Name] Requirements
   :id: doc__feature_name_requirements
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_feat
   :tags: template

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__`` and followed by ``_requirements``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

<Headlines (for the list of requirements if structuring is needed)>
===================================================================

.. code-block:: rst

   .. feat_req:: Some Title
      :id: feat_req__feature_name__some_title
      :reqtype: Process
      :security: NO
      :safety: ASIL_B
      :satisfies: stkh_req__requirements__template
      :valid_from: v0.0.1
      :valid_until: v1.0.1
      :status: invalid
      :belongs_to: feat__feature_name

      The Feature shall do xyz to the user to bring him to this condition at this time.

      Note: (optional, not to be verified)

.. code-block:: rst

   .. aou_req:: Some Other Title
      :id: aou_req__feature_name__some_other_title
      :reqtype: Process
      :security: NO
      :safety: ASIL_B
      :status: invalid

      The Feature User shall do xyz to use the feature safely.

.. attention::
    The above directives must be updated according to your feature requirements.

    - Replace the example content by the real content for your first requirement (according to :need:`gd_guidl__req_engineering`)
    - Set ``belongs_to`` with a link to feature ID
    - Set ``reqtype`` with a link to the right value (<Functional|Interface|Process|Non-Functional>)
    - Set ``satisfies`` with a link to the right stakeholder requirement
    - Adjust ``safety`` and ``security`` to the right value (ASIL B/QM; YES/NO)
    - Add other needed requirements for your feature
    - Adjust ``valid_from`` and ``valid_until`` to the right version numbers
    - Set ``status`` to ``valid`` and start the review/merge process

.. needextend:: docname is not None and "feature_name" in id
   :+tags: feature_name
