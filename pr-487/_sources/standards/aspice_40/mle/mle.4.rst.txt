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

MLE.4 Machine Learning Model Testing
-------------------------------------

The purpose is to ensure compliance of the trained ML model and the deployed ML model with
the ML requirements.

Process outcomes
~~~~~~~~~~~~~~~~

1. A ML test approach is defined.
2. A ML test data set is created.
3. The trained ML model is tested.
4. The deployed ML model is derived from the trained ML model and tested.
5. Consistency and bidirectional traceability are established between the ML test approach and
   the ML requirements, and the ML test data set and the ML data requirements; and
   bidirectional traceability is established between the ML test approach and ML test results.
6. Results of the ML model testing are summarized and communicated with the deployed ML
   model to all affected parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: MLE.4.BP1: Specify an ML test approach
   :id: std_req__aspice_40__MLE-4-BP1
   :status: valid
   :links: std_req__aspice_40__iic-08-64

   Specify an ML test approach suitable to provide evidence for compliance of the trained ML model and the deployed ML model with the ML requirements. The ML test approach includes

   * ML test scenarios with distribution of data characteristics (e.g., gender, weather conditions, street conditions within the ODD) defined by ML requirements,
   * distribution and frequency of each ML test scenario inside the ML test data set,
   * expected test result per test datum,
   * entry and exit criteria of the testing,
   * approach for data set creation and modification, and
   * the required testing infrastructure and environment setup.

   .. note::

      Expected test result per test datum might require labeling of test data to support comparison of output of the ML model with the expected output.

   .. note::

      Test datum is the smallest amount of data which is processed by the ML model into only one output. E.g., one image in photo processing or an audio sequence in voice recognition.

   .. note::

      Data characteristic is one property of the data that may have different expressions in the ODD. E.g., weather condition may contain expressions like sunny, foggy or rainy.

   .. note::

      An ML test scenario is a combination of expressions of all defined data characteristics e.g., weather conditions = sunny, street conditions = gravel road.

.. std_req:: MLE.4.BP2: Create ML test data set
   :id: std_req__aspice_40__MLE-4-BP2
   :status: valid
   :links: std_req__aspice_40__iic-03-51

   Create the ML test data set needed for testing of the trained ML model and testing of the deployed ML model from the ML data collection provided by SUP.11 considering the ML test approach. The ML test data set shall not be used for training.

   .. note::

      The ML test data set for the trained ML model might differ from the test data set of the deployed ML model.

   .. note::

      Additional data sets might be used for special purposes like assurance of safety, fairness, robustness.

.. std_req:: MLE.4.BP3: Test trained ML model
   :id: std_req__aspice_40__MLE-4-BP3
   :status: valid
   :links: std_req__aspice_40__iic-13-50

   Test the trained ML model according to the ML test approach using the created ML test data set. Record and evaluate the ML test results.

   .. note::

      Evaluation of test logs might include pattern analysis of failed test data to support e.g., trustworthiness.

.. std_req:: MLE.4.BP4: Derive deployed ML model
   :id: std_req__aspice_40__MLE-4-BP4
   :status: valid
   :links: std_req__aspice_40__iic-11-50, std_req__aspice_40__iic-13-50

   Derive the deployed ML model from the trained ML model according to the ML architecture. The deployed ML model shall be used for testing and delivery to software integration.

   .. note::

      The deployed ML model will be integrated into the target system and may differ from the trained ML model which often requires powerful hardware and uses interpretative languages.

.. std_req:: MLE.4.BP5: Test deployed ML model
   :id: std_req__aspice_40__MLE-4-BP5
   :status: valid
   :links: std_req__aspice_40__iic-11-50, std_req__aspice_40__iic-13-50

   Test the deployed ML model according to the ML test approach using the created ML test data set. Record and evaluate the ML test results.

.. std_req:: MLE.4.BP6: Ensure consistency and establish bidirectional traceability
   :id: std_req__aspice_40__MLE-4-BP6
   :status: valid
   :links: std_req__aspice_40__iic-13-51

   Ensure consistency and establish bidirectional traceability between the ML test approach and the ML requirements, and the ML test data set and the ML data requirements; and bidirectional traceability is established between the ML test approach and ML test results.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analyses of change requests, and verification coverage demonstration. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

.. std_req:: MLE.4.BP7: Summarize and communicate results
   :id: std_req__aspice_40__MLE-4-BP7
   :status: valid
   :links: std_req__aspice_40__iic-13-52

   Summarize the ML test results of the ML model. Inform all affected parties about the agreed results and the deployed ML model.


.. needextend:: "c.this_doc()"
   :+tags: aspice40_mle4
