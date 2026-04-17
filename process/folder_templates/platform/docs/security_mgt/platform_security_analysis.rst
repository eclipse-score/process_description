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


Platform Security Analysis Template
====================================

.. document:: [Your Platform Name] Security Analysis Template
   :id: doc__platform_name_security_analysis
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__platform_security_analysis
   :tags: template


.. ..  attention::
..     The above directive must be updated according to your Platform.

..     - Modify ``Your Platform Name`` to be your Platform Name
..     - Modify ``id`` to be your Platform Name in lower snake case preceded by ``doc__`` and followed by ``_security_analysis_fdr``
..     - Adjust ``status`` to be ``valid``
..     - Adjust ``safety``, ``security`` and ``tags`` according to your needs


Purpose
------------------
The purpose of this Security Analysis template is to document the results of the platform security analysis.



Platform Security Analysis Template
-----------------------------------
The following deliverables are the outcome of a security analysis on the platform.

#. Identification of threats and mitigations
#. Stakeholder security requirements definition
#. Security assumptions definition

Threat and Risk Identification Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: Threat and Risk Identification Template
        :header-rows: 1

        * - Id
          - Identified Threat
          - Corresponding mitigation
          - Comment/Remark

        * - 1
          - Eg: A backend attacker performs MiTM between the OEM cloud and the platform component
          - Eg: End to end TLS between the platform component and the OEM cloud service mitigates the MiTM attacks
          - <Rationale for mitigation>

        * - 2
          - Eg: Unauthorized access to the onboard diagnostic stack from external interfaces
          - Eg: Authentication and authorization mechanisms such as usage of tokens prevents such unauthorized access
          - <Rationale for result>

        * - 3
          - Eg: Static configuration files are manipulated by an inside attacker
          - Eg: OS specific access control mechanisms and least privilege principle prevents such unauthorized manipulation
          - <Rationale for result>



Stakeholder Security Requirements Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: Stakeholder Security Requirements Template
        :header-rows: 1

        * - Id
          - Security Requirement
          - Comment/Remark

        * - 1
          - Eg: The platform shall use end to end mutual TLS and 2 factor authentication for communication between components and OEM cloud services.
          - <Rationale for the requirement>

        * - 2
          - Eg: Tokens shall be used for authorizing access to the onboard diagnostic APIs.
          - <Rationale for the requirement>

        * - 3
          - Eg: OS specific DAC (discretionary access control) and MAC (mandatory access control) shall be used for restricting access to assets such as configuration files.
          - <Rationale for the requirement>

Security Assumptions
~~~~~~~~~~~~~~~~~~~~
The assumptions of use shall be documented under :need:`wp__platform_security_manual`.

.. To be filled as part of https://github.com/eclipse-score/process_description/issues/452.


.. To be filled as part of https://github.com/eclipse-score/process_description/issues/452.
