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

MLE.1 Machine Learning Requirements Analysis
---------------------------------------------

The purpose is to refine the machine learning-related software requirements into a set of ML
requirements.

Process outcomes
~~~~~~~~~~~~~~~~

1. The ML requirements including ML data requirements are identified and specified based on
   the software requirements and the components of the software architecture.
2. ML requirements are structured and prioritized.
3. ML requirements are analyzed for correctness and verifiability.
4. The impact of ML requirements on the ML operating environment is analyzed.
5. Consistency and bidirectional traceability are established between ML requirements and
   software requirements, and between ML requirements and software architecture.
6. The ML requirements are agreed and communicated to all affected parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: MLE.1.BP1: Specify ML requirements
   :id: std_req__aspice_40__MLE-1-BP1
   :status: valid
   :links: std_req__aspice_40__iic-17-00

   Use the software requirements and the software architecture to identify and specify functional and non-functional ML requirements, as well as ML data requirements specifying data characteristics (e.g., gender, weather conditions, street conditions within the ODD) and their expected distributions.

   .. note::

      Non-functional requirements may include relevant characteristics of the ODD and KPIs as robustness, performance, and level of trustworthiness.

   .. note::

      The ML data requirements are input for SUP.11 Machine Learning Data Management but also for other MLE processes.

   .. note::

      In case of ML development only, stakeholder requirements represent the software requirements.

.. std_req:: MLE.1.BP2: Structure ML requirements
   :id: std_req__aspice_40__MLE-1-BP2
   :status: valid
   :links: std_req__aspice_40__iic-17-00, std_req__aspice_40__iic-17-54

   Structure and prioritize the ML requirements.

   .. note::

      Examples for structuring criteria can be grouping (e.g., by functionality) or variants identification.

   .. note::

      Prioritization can be done according to project or stakeholder needs via e.g., definition of release scopes. Refer to SPL.2.BP1.

.. std_req:: MLE.1.BP3: Analyze ML requirements
   :id: std_req__aspice_40__MLE-1-BP3
   :status: valid
   :links: std_req__aspice_40__iic-17-54,std_req__aspice_40__iic-15-51

   Analyze the specified ML requirements including their interdependencies to ensure correctness, technical feasibility, and ability for machine learning model testing, and to support project management regarding project estimates.

   .. note::

      See MAN.3.BP3 for project feasibility and MAN.3.BP5 for project estimates.

.. std_req:: MLE.1.BP4: Analyze the impact on the ML operating environment
   :id: std_req__aspice_40__MLE-1-BP4
   :status: valid
   :links: std_req__aspice_40__iic-15-51

   Analyze the impact that the ML requirements will have on interfaces of software components and the ML operating environment.

   .. note::

      The ML operating environment is defined as the infrastructure and information which both the trained ML model and the deployed ML model need for execution.

.. std_req:: MLE.1.BP5: Ensure consistency and establish bidirectional traceability
   :id: std_req__aspice_40__MLE-1-BP5
   :status: valid
   :links: std_req__aspice_40__iic-13-51

   Ensure consistency and establish bidirectional traceability between ML requirements and software requirements and between ML requirements and the software architecture.

   .. note::

      Bidirectional traceability supports consistency, facilitates impact analyses of change requests, and verification coverage demonstration. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

   .. note::

      Redundant traceability is not intended, but at least one out of the given traceability paths.

.. std_req:: MLE.1.BP6: Communicate agreed ML requirements and impact on the operating environment
   :id: std_req__aspice_40__MLE-1-BP6
   :status: valid
   :links: std_req__aspice_40__iic-13-52

   Communicate the agreed ML requirements, and the results of the impact analysis on the ML operating environment to all affected parties.


.. needextend:: "c.this_doc()"
   :+tags: aspice40_mle1
