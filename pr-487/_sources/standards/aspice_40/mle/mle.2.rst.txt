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

MLE.2 Machine Learning Architecture
------------------------------------

The purpose is to establish an ML architecture supporting training and deployment, consistent
with the ML requirements, and to evaluate the ML architecture against defined criteria.

Process outcomes
~~~~~~~~~~~~~~~~

1. A ML architecture is developed.
2. Hyperparameter ranges and initial values are determined as a basis for the training.
3. Evaluation of ML architectural elements is conducted.
4. Interfaces of the ML architectural elements are defined.
5. Resource consumption objectives for the ML architectural elements are defined.
6. Consistency and bidirectional traceability are established between the ML architectural
   elements and the ML requirements.
7. The ML architecture is agreed and communicated to all affected parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: MLE.2.BP1: Develop ML architecture
   :id: std_req__aspice_40__MLE-2-BP1
   :status: valid
   :links: std_req__aspice_40__iic-04-51, std_req__aspice_40__iic-01-54, std_req__aspice_40__iic-15-51

   Develop and document the ML architecture that specifies ML architectural elements including details of the ML model, pre- and postprocessing, and hyperparameters which are required to create, train, test, and deploy the ML model.

   .. note::

      Necessary details of the ML model may include layers, activation functions, and backpropagation. The level of detail of the ML model may not need to cover aspects like single neurons.

   .. note::

      The details of the ML model may differ between the ML model used during training and the deployed ML model.

.. std_req:: MLE.2.BP2: Determine hyperparameter ranges and initial values
   :id: std_req__aspice_40__MLE-2-BP2
   :status: valid
   :links: std_req__aspice_40__iic-04-51,std_req__aspice_40__iic-01-54

   Determine and document the hyperparameter ranges and the initial values as a basis for the training.

.. std_req:: MLE.2.BP3: Analyze ML architectural elements
   :id: std_req__aspice_40__MLE-2-BP3
   :status: valid
   :links: std_req__aspice_40__iic-04-51,std_req__aspice_40__iic-15-51

   Define criteria for analysis of the ML architectural elements. Analyze ML architectural elements according to the defined criteria.

   .. note::

      Trustworthiness and explainability might be criteria for the analysis of the ML architectural elements.

.. std_req:: MLE.2.BP4: Define interfaces of the ML architectural elements
   :id: std_req__aspice_40__MLE-2-BP4
   :status: valid
   :links: std_req__aspice_40__iic-04-51

   Determine and document the internal and external interfaces of each ML architectural element including its interfaces to related software components.

.. std_req:: MLE.2.BP5: Define resource consumption objectives for the ML architectural elements
   :id: std_req__aspice_40__MLE-2-BP5
   :status: valid
   :links: std_req__aspice_40__iic-04-51

   Determine and document the resource consumption objectives for all relevant ML architectural elements during training and deployment.

.. std_req:: MLE.2.BP6: Ensure consistency and establish bidirectional traceability
   :id: std_req__aspice_40__MLE-2-BP6
   :status: valid
   :links: std_req__aspice_40__iic-13-51

   Ensure consistency and establish bidirectional traceability between the ML architectural elements and the ML requirements.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analyses of change requests, and verification coverage demonstration. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

   .. note::

      The bidirectional traceability should be established on a reasonable level of abstraction to the ML architectural elements.

.. std_req:: MLE.2.BP7: Communicate agreed ML architecture
   :id: std_req__aspice_40__MLE-2-BP7
   :status: valid
   :links: std_req__aspice_40__iic-13-52

   Inform all affected parties about the agreed ML architecture including the details of the ML model and the initial hyperparameter values.


.. needextend:: "c.this_doc()"
   :+tags: aspice40_mle2
