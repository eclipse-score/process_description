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

SUP.11 Machine Learning Data Management
---------------------------------------

The purpose is to define and align ML data with ML data requirements, maintain the integrity
and quality of the ML data, and make them available to affected parties.

Process outcomes
~~~~~~~~~~~~~~~~

1. A ML data management system including an ML data lifecycle is established.
2. A ML data quality approach is developed including ML data quality criteria.
3. Collected ML data are processed for consistency with ML data requirements.
4. ML data are verified against defined ML data quality criteria and updated as needed.
5. ML data are agreed and communicated to all affected parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: SUP.11.BP1: Establish an ML data management system
   :id: std_req__aspice_40__SUP-11-BP1
   :status: valid
   :links: std_req__aspice_40__iic-16-52

   Establish an ML data management system which supports

   * ML data management activities,
   * relevant sources of ML data,
   * ML data life cycle including a status model, and
   * interfaces to affected parties.

   .. note::

      Supported ML data management activities may include data collection, labeling/annotation, and structuring.

.. std_req:: SUP.11.BP2: Develop an ML data quality approach
   :id: std_req__aspice_40__SUP-11-BP2
   :status: valid
   :links: std_req__aspice_40__iic-19-50

   Develop an approach to ensure that the quality of ML data is analyzed based on defined ML data quality criteria and activities are performed to support avoidance of biases of data.

   .. note::

      Examples of ML data quality criteria are relevant data sources, reliability and consistency of labelling, completeness against ML data requirements.

   .. note::

      The ML data management system should support the quality criteria and activities of the ML data quality approach.

   .. note::

      Biases to avoid may include sampling bias (e.g., gender, age) and feedback loop bias.

   .. note::

      For creation of ML data sets see MLE.3.BP2 and MLE.4.BP2.

.. std_req:: SUP.11.BP3: Collect ML data
   :id: std_req__aspice_40__SUP-11-BP3
   :status: valid
   :links: std_req__aspice_40__iic-03-53

   Relevant sources for raw data are identified and continuously monitored for changes. The raw data is collected according to the ML data requirements.

   .. note::

      The identification and collection of ML data might be an organizational responsibility.

   .. note::

      Continuous monitoring should include the ODD and may lead to changes of the ML requirements.

.. std_req:: SUP.11.BP4: Process ML data
   :id: std_req__aspice_40__SUP-11-BP4
   :status: valid
   :links: std_req__aspice_40__iic-03-53

   The raw data are processed (annotated, analyzed, and structured) according to the ML data requirements.

.. std_req:: SUP.11.BP5: Assure quality of ML data
   :id: std_req__aspice_40__SUP-11-BP5
   :status: valid
   :links: std_req__aspice_40__iic-03-53

   Perform the activities according to the ML data quality approach to ensure that the ML data meets the defined ML data quality criteria.

   .. note::

      These activities may include sample-based reviews or statistical methods.

.. std_req:: SUP.11.BP6: Communicate agreed processed ML data
   :id: std_req__aspice_40__SUP-11-BP6
   :status: valid
   :links: std_req__aspice_40__iic-13-52

   Inform all affected parties about the agreed processed ML data and provide them to the affected parties.


.. needextend:: "c.this_doc()"
   :+tags: aspice40_sup11
