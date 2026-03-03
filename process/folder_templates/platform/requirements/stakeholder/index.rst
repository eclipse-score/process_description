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
   :security: <YES|NO>
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
   :reqtype: <Functional|Interface|Process|Non-Functional>
   :safety: <QM|ASIL_B>
   :security: <YES|NO>
   :rationale: <The rationale provides the reason that the requirement is needed.>
   :valid_from: <milestone version>
   :valid_until: <milestone version>
   :status: invalid

   The platform shall ...

.. aou_req:: Some Other Title
   :id: aou_req__platform__some_other_title
   :reqtype: <Functional|Interface|Process|Non-Functional>
   :security: <YES|NO>
   :safety: <QM|ASIL_B>
   :mitigates: <link to safety analysis>
   :status: invalid

   The Platform User shall do xyz to use the platform safely.

.. attention::
    The above directives must be updated according to platform requirements.

    - Replace the example content by the real content for your requirements (according to :need:`gd_guidl__req_engineering`)
    - Set ``safety`` and ``security`` to the right value
    - Set ``valid_from`` and ``valid_until`` to the right milestones
    - Provide the appropriate rationale
    - Add other needed requirements for the platform
    - Set ``status`` to ``valid`` and start the review/merge process

.. needextend:: Tag as platform
   :+tags: platform
