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

.. _dfa failure initiators:

DFA failure initiators
======================

.. gd_guidl:: DFA failure initiators
  :id: gd_guidl__dfa_failure_initiators
  :status: valid
  :complies: std_req__iso26262__software_7411, std_req__iso26262__analysis_744, std_req__iso26262__software_748, std_req__iso26262__software_749


.. note:: Use all applicable failure initiators to ensure a structured analysis. If there are additional failure initiators needed, please enlarge the list of fault models.

.. note:: An ASIL related message is trustable in that manner that it is not corrupted, repeated, lost, delayed, masqueraded or addressed incorrectly.


**Purpose**

In order to identify all cascading and common cause failures, which may initiated from your feature or components to the platform, other features, components, etc.,
use the following framework of dependent failure initiators to check your completeness of the analysis.

DFA failure initiators
----------------------

Shared resources
~~~~~~~~~~~~~~~~

.. note:: Shared libraries are only than to be considered as a shared resource if the feature and the related safety mechanisms are using this specific library. If the library is not used by the feature or the related safety mechanisms, it is not a shared resource.

.. dfa_failure_initiator:: Reused software components
   :id: dfa_failure_initiator__sr_01_01
   :status: valid
   :element: shared resource
   :failure_mode: Reused software components
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Libraries
   :id: dfa_failure_initiator__sr_01_02
   :status: valid
   :element: shared resource
   :failure_mode: Libraries
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Basic software
   :id: dfa_failure_initiator__sr_01_04
   :status: valid
   :element: shared resource
   :failure_mode: Basic software
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Operating system including scheduler
   :id: dfa_failure_initiator__sr_01_05
   :status: valid
   :element: shared resource
   :failure_mode: Operating system including scheduler
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Any service stack, e.g. communication stack
   :id: dfa_failure_initiator__sr_01_06
   :status: valid
   :element: shared resource
   :failure_mode: Any service stack, e.g. communication stack
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Configuration data
   :id: dfa_failure_initiator__sr_01_07
   :status: valid
   :element: shared resource
   :failure_mode: Configuration data
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Execution time
   :id: dfa_failure_initiator__sr_01_09
   :status: valid
   :element: shared resource
   :failure_mode: Execution time
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Allocated memory
   :id: dfa_failure_initiator__sr_01_10
   :status: valid
   :element: shared resource
   :failure_mode: Allocated memory
   :importance: Medium
   :hide:

.. needtable::
   :style: table
   :columns: id;failure_mode;importance
   :colwidths: 20,60,20
   :filter: type == "dfa_failure_initiator" and element == "shared resource" and is_external == False


Communication between elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.

.. dfa_failure_initiator:: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
   :id: dfa_failure_initiator__co_01_01
   :status: valid
   :element: communication
   :failure_mode: Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
   :id: dfa_failure_initiator__co_01_02
   :status: valid
   :element: communication
   :failure_mode: Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Insertion / sequence of information
   :id: dfa_failure_initiator__co_01_03
   :status: valid
   :element: communication
   :failure_mode: Insertion / sequence of information
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Corruption of information, inconsistent data
   :id: dfa_failure_initiator__co_01_04
   :status: valid
   :element: communication
   :failure_mode: Corruption of information, inconsistent data
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same information
   :id: dfa_failure_initiator__co_01_05
   :status: valid
   :element: communication
   :failure_mode: Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same information
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Information from a sender received by only a subset of the receivers
   :id: dfa_failure_initiator__co_01_06
   :status: valid
   :element: communication
   :failure_mode: Information from a sender received by only a subset of the receivers
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Blocking access to a communication channel
   :id: dfa_failure_initiator__co_01_07
   :status: valid
   :element: communication
   :failure_mode: Blocking access to a communication channel
   :importance: Medium
   :hide:

.. needtable::
   :style: table
   :columns: id;failure_mode;importance
   :colwidths: 20,60,20
   :filter: type == "dfa_failure_initiator" and element == "communication" and is_external == False

Shared information inputs
~~~~~~~~~~~~~~~~~~~~~~~~~

Same information input used by multiple functions.

.. dfa_failure_initiator:: Configuration data
   :id: dfa_failure_initiator__si_01_02
   :status: valid
   :element: shared information input
   :failure_mode: Configuration data
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Constants, or variables, being global to the two software functions
   :id: dfa_failure_initiator__si_01_03
   :status: valid
   :element: shared information input
   :failure_mode: Constants, or variables, being global to the two software functions
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
   :id: dfa_failure_initiator__si_01_04
   :status: valid
   :element: shared information input
   :failure_mode: Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Data / function parameter arguments / messages delivered by software function to more than one other function
   :id: dfa_failure_initiator__si_01_05
   :status: valid
   :element: shared information input
   :failure_mode: Data / function parameter arguments / messages delivered by software function to more than one other function
   :importance: Medium
   :hide:

.. needtable::
   :style: table
   :columns: id;failure_mode;importance
   :colwidths: 20,60,20
   :filter: type == "dfa_failure_initiator" and element == "shared information input" and is_external == False

Unintended impact
~~~~~~~~~~~~~~~~~

Unintended impacts to function due to various failures.

.. dfa_failure_initiator:: Memory miss-allocation and leaks
   :id: dfa_failure_initiator__ui_01_01
   :status: valid
   :element: unintended impact
   :failure_mode: Memory miss-allocation and leaks
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Read/Write access to memory allocated to another software element
   :id: dfa_failure_initiator__ui_01_02
   :status: valid
   :element: unintended impact
   :failure_mode: Read/Write access to memory allocated to another software element
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Stack/Buffer under-/overflow
   :id: dfa_failure_initiator__ui_01_03
   :status: valid
   :element: unintended impact
   :failure_mode: Stack/Buffer under-/overflow
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Deadlocks
   :id: dfa_failure_initiator__ui_01_04
   :status: valid
   :element: unintended impact
   :failure_mode: Deadlocks
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Livelocks
   :id: dfa_failure_initiator__ui_01_05
   :status: valid
   :element: unintended impact
   :failure_mode: Livelocks
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Blocking of execution
   :id: dfa_failure_initiator__ui_01_06
   :status: valid
   :element: unintended impact
   :failure_mode: Blocking of execution
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Incorrect allocation of execution time
   :id: dfa_failure_initiator__ui_01_07
   :status: valid
   :element: unintended impact
   :failure_mode: Incorrect allocation of execution time
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Incorrect execution flow
   :id: dfa_failure_initiator__ui_01_08
   :status: valid
   :element: unintended impact
   :failure_mode: Incorrect execution flow
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Incorrect synchronization between software elements
   :id: dfa_failure_initiator__ui_01_09
   :status: valid
   :element: unintended impact
   :failure_mode: Incorrect synchronization between software elements
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: CPU time depletion
   :id: dfa_failure_initiator__ui_01_10
   :status: valid
   :element: unintended impact
   :failure_mode: CPU time depletion
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Memory depletion
   :id: dfa_failure_initiator__ui_01_11
   :status: valid
   :element: unintended impact
   :failure_mode: Memory depletion
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Other HW unavailability
   :id: dfa_failure_initiator__ui_01_12
   :status: valid
   :element: unintended impact
   :failure_mode: Other HW unavailability
   :importance: Medium
   :hide:

.. needtable::
   :style: table
   :columns: id;failure_mode;importance
   :colwidths: 20,60,20
   :filter: type == "dfa_failure_initiator" and element == "unintended impact" and is_external == False

Development failure initiators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section is **only applicable if a divers SW development is needed** due to decomposition.

.. note:: Section shall be applied only once to analyse all dependencies of the features. Results shall be checked during of the analysis of new features if this is applicable to the feature.

.. dfa_failure_initiator:: Same development approaches (e.g. IDE, programming and/or modelling language)
   :id: dfa_failure_initiator__sc_01_02
   :status: valid
   :element: development
   :failure_mode: Same development approaches (e.g. IDE, programming and/or modelling language)
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Same personal
   :id: dfa_failure_initiator__sc_01_03
   :status: valid
   :element: development
   :failure_mode: Same personal
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
   :id: dfa_failure_initiator__sc_01_04
   :status: valid
   :element: development
   :failure_mode: Same social-cultural context (even if different personnel). Only applicable if diverse development is needed.
   :importance: Medium
   :hide:

.. dfa_failure_initiator:: Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
   :id: dfa_failure_initiator__sc_01_05
   :status: valid
   :element: development
   :failure_mode: Development fault (e.g. human error, insufficient qualification, insufficient methods). Only applicable if diverse development is needed.
   :importance: Medium
   :hide:

.. needtable::
   :style: table
   :columns: id;failure_mode;importance
   :colwidths: 20,60,20
   :filter: type == "dfa_failure_initiator" and element == "development" and is_external == False
