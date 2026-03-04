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

Stakeholder Requirements
########################

.. document:: Platform Requirements
   :id: doc__platform_name_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_feat
   :tags: template

.. attention::
    The above directive must be updated.

    - Adjust ``status`` to ``valid``
    - Adjust ``safety``, ``security`` and ``tags`` according to your needs

<Headlines (for the list of requirements if structuring is needed)>
===================================================================

.. stkh_req:: Template
   :id: stkh_req__requirements__template
   :reqtype: Functional
   :safety: ASIL_B
   :security: YES
   :rationale: <The rationale provides the reason that the requirement is needed.>
   :valid_from: v0.0.1
   :valid_until: v1.0.1
   :status: invalid

   The platform shall ...

.. aou_req:: Some Other Title
   :id: aou_req__platform__some_other_title
   :reqtype: Interface
   :security: YES
   :safety: ASIL_B
   :status: invalid

   The Platform User shall do xyz to use the platform safely.

.. attention::
    The above directives must be updated according to platform requirements.

    - Replace the example content by the real content for your requirements (according to :need:`gd_guidl__req_engineering`)
    - Set ``safety`` and ``security`` to the right value (ASIL B/QM; YES/NO)
    - Set ``valid_from`` and ``valid_until`` to the right milestones
    - Set ``reqtype`` with a link to the right value (<Functional|Interface|Process|Non-Functional>)
    - Provide the appropriate rationale
    - Adjust ``valid_from`` and ``valid_until`` to the right version numbers
    - Add other needed requirements for the platform
    - Set ``status`` to ``valid`` and start the review/merge process

.. needextend:: "platform" in id
   :+tags: platform
