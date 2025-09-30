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

Verification Frameworks
#######################

.. doc_concept:: Verification Frameworks
   :id: doc_concept__verification_frameworks
   :status: valid
   :tags: verification

   In this section testing levels and verification frameworks will be discussed.


Test Levels
***********
As described in the :ref:`general_concepts_traceability` the verification activities is splitted into following levels:

* **Unit Tests:** Focus on individual components, typically written and executed by developers using frameworks like Google Test for C++ and Rust's built-in testing framework.
* **Component Integration Tests:** Verify the interaction between integrated components, often executed using Pytest for Python and component's native implementation languages. Ensures components work together as intended.
* **Feature Integration Tests:** Validate the functionality of a complete feature across multiple components, often executed using the ITF (Integration Test Framework) on target hardware or simulation. Ensures the feature meets its requirements and works with other features.
* **Platform Tests:** Ensure the entire platform operates correctly, including system-level tests and performance evaluations.

Test types overview
*******************

.. figure:: _assets/testing.svg
  :width: 100%
  :name: score_wp_testing
  :align: center
  :alt: High level testing overview for project work products


.. needuml::
   :scale: 50%

   package Test_types {
   class FeatureB #LightYellow {
      - internalClassB1: InternalClassB1
      - internalClassB2: InternalClassB2
      + publicClassB1: PublicClassB1
      + publicClassB2: PublicClassB2
   }
   class FeatureA #LightYellow {
      - internalClassA1: InternalClassA1
      - internalClassA2: InternalClassA2
      + publicClassA1: PublicClassA1
      + publicClassA2: PublicClassA2
   }

   class InternalClassA1 {
      - privateMethod()
      + publicMethod()
   }
   class InternalClassA2 {
      - privateMethod()
      + publicMethod()
   }
   class ComponentA1 {
      - privateMethod()
      + publicMethod()
   }
   class ComponentA2 {
      - privateMethod()
      + publicMethod()
   }
   class ComponentB1 {
      - privateMethod()
      + publicMethod()
   }
   class UnitTestA1 #LightGrey {
      type: whitebox
      responsibility: developers
      + testPublicMethod()
      - testPrivateMethodIfNeeded()
   }
   class UnitTestA2 #LightGrey {
      type: whitebox
      responsibility: developers
      + testPublicMethod()
      - testPrivateMethodIfNeeded()
   }
   class FeatureIntegrationTest #LightGrey {
      type: blackbox
      responsibility: testers
      + testIntegrationByPublicMethods()
   }
   class ComponentIntegrationTestX #LightGrey {
      type: blackbox
      responsibility: testers
      + testFunctionalityByPublicMethods()
   }
   class ComponentIntegrationTestY #LightGrey {
      type: blackbox
      responsibility: testers
      + testFunctionalityByPublicMethods()
   }

   FeatureA --> InternalClassA1
   FeatureA --> InternalClassA2
   InternalClassA1 -[hidden]r-> InternalClassA2
   FeatureA --> ComponentA1
   FeatureA --> ComponentA2
   FeatureB --> ComponentB1
   InternalClassA1 <-- UnitTestA1 : uses
   InternalClassA2 <-- UnitTestA2 : uses
   ComponentA1 <-- ComponentIntegrationTestX : uses
   ComponentA2 <-- ComponentIntegrationTestX : uses
   ComponentA1 <-- ComponentIntegrationTestY : uses
   ComponentA1 <-- FeatureIntegrationTest : uses
   ComponentB1 <-- FeatureIntegrationTest : uses
   FeatureA <-- FeatureIntegrationTest : validates
   FeatureB <-- FeatureIntegrationTest : validates
   }

Developers write whitebox :need:`wp__verification_sw_unit_test` for the components, focusing on private and public methods.
Testers perform blackbox integration tests at both component and feature levels. They are executed automatically on each
pull request together with a build.

The goal of :need:`wp__verification_comp_int_test` is to validate that interfaces within a single feature
are consistent and meet functional expectations. Component integration tests are automatically executed
as part of the CI pipeline on every pull requests within the repository. Extensive test suite is run nightly to catch sporadic issues.

:need:`wp__verification_feat_int_test` aims to validate that features
work together as intended. This is done by exercising functionality through public APIs and validating feature behavior,
interactions between them and their components. Feature integration tests are automatically executed
on a pull request when a feature is requested to be integrated in SCORE.


Existing Verification Frameworks
********************************
* **ITF (Integration Test Framework):** Allows execution of Feature Integration Tests on target hardware or simulation.
  `Link to repository <https://github.com/eclipse-score/itf/>`__
* **Scenario Framework:** Supports Component Integration Tests by providing scenarios in C++ and Rust
  that are tested with single Test Case implementation in Pytest.
  `Link to repository <https://github.com/eclipse-score/itftesting_tools/>`__

.. * **SCTF (Software Component Test Framework):** A framework for Component Integration Tests...

All above frameworks are based on Python and Pytest, allowing customization and extension as needed.
