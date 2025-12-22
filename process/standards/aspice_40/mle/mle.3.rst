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

MLE.3 Machine Learning Training
--------------------------------

The purpose is to optimize the ML model to meet the defined ML requirements.

Process outcomes
~~~~~~~~~~~~~~~~

1. A ML training and validation approach is specified.
2. The data set for ML training and ML validation is created.
3. The ML model, including hyperparameter values, is optimized to meet the defined ML
   requirements.
4. Consistency and bidirectional traceability are established between the ML training and
   validation data set and the ML data requirements.
5. Results of optimization are summarized, and the trained ML model is agreed and
   communicated to all affected parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: MLE.3.BP1: Specify ML training and validation approach
   :id: std_req__aspice_40__MLE-3-BP1
   :status: valid
   :links: std_req__aspice_40__iic-08-65

   Specify an approach which supports the training and validation of the ML model to meet the defined ML requirements. The ML training and validation approach includes

   * entry and exit criteria of the training and validation,
   * approaches for hyperparameter tuning / optimization,
   * approach for data set creation and modification, and
   * training and validation environment

   .. note::

      The ML training and validation approach may include random dropout and other robustification methods.

   .. note::

      ML validation is the optimization of the hyperparameters during Machine Learning Training (MLE.3). The term "validation" has a different meaning than VAL.1.

   .. note::

      The training environment should reflect the environment of the deployed model.

.. std_req:: MLE.3.BP2: Create ML training and validation data set
   :id: std_req__aspice_40__MLE-3-BP2
   :status: valid
   :links: std_req__aspice_40__iic-03-51

   Select data from the ML data collection provided by SUP.11 and assign them to the data set for training and validation of the ML model according to the specified ML training and validation approach.

   .. note::

      The ML training and validation data set may include corner cases, unexpected cases, and normal cases depending on the ML requirements.

   .. note::

      A separated data set for training and validation might not be required in some cases (e.g., k-fold cross validation, no optimization of hyperparameters).

.. std_req:: MLE.3.BP3: Create and optimize ML model
   :id: std_req__aspice_40__MLE-3-BP3
   :status: valid
   :links: std_req__aspice_40__iic-01-53,std_req__aspice_40__iic-01-54

   Create the ML model according to the ML architecture and train it, using the identified ML training and validation data set according to the ML training and validation approach to meet the defined ML requirements, and training and validation exit criteria.

.. std_req:: MLE.3.BP4: Ensure consistency and establish bidirectional traceability
   :id: std_req__aspice_40__MLE-3-BP4
   :status: valid
   :links: std_req__aspice_40__iic-13-51

   Ensure consistency and establish bidirectional traceability between the ML training and validation data set and the ML data requirements.

   .. note::

      Bidirectional traceability supports consistency and facilitates impact analyses of change requests. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

.. std_req:: MLE.3.BP5: Summarize and communicate agreed trained ML model
   :id: std_req__aspice_40__MLE-3-BP5
   :status: valid
   :links: std_req__aspice_40__iic-13-52

   Summarize the results of the optimization and inform all affected parties about the agreed trained ML model.


.. needextend:: "c.this_doc()"
   :+tags: aspice40_mle3
