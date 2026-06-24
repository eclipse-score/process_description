..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

Test Specification Guideline
============================

.. gd_guidl:: Test Specification Guideline
   :id: gd_guidl__verification_specification
   :status: valid
   :version: 1
   :complies: std_req__iso26262__software_941[version==1],
              std_req__iso26262__software_942[version==1],
              std_req__iso26262__software_943[version==1],
              std_req__iso26262__support_9421[version==1],
              std_req__iso26262__support_9422[version==1],
              std_req__iso26262__support_9423[version==1],
              std_req__iso26262__support_9424[version==1],
              std_req__iso26262__software_app_c_42[version==1],
              std_req__iso26262__software_app_c_44[version==1],
              std_req__iso26262__software_app_c_45[version==1],
              std_req__aspice_40__iic-08-60[version==1]

Test specification
------------------

A test specification contains the following attributes.

.. list-table:: Test specification properties
   :header-rows: 1
   :widths: 10 30 40 20

   * - Property
     - Type / Values
     - Description
     - Helpful links
   * - Partially and/or Fully Verifies
     - Docs-as-code Id(s) for traceable elements
     - Links to one or more requirement Ids. Can be partial or full coverage of a
       requirement, as per test property.
     -
   * - Description
     - Text
     - The description should include

       - The objective of the test.
       - Inputs
       - Expected outcome/output/result (e.g. "A success message is displayed." or "Result should be 42.")
       - Test environment (e.g. network configuration, clean system state)
       - Expected time sequence of events and behavior (where applicable and an expectation)
     -
   * - TestType
     - Examples are:

       - requirements-based
       - interface-test
       - coverage (various types apply, shall be tool supported)
     - These are example values and an incomplete list.
       A full list of test types is available in :need:`doc_concept__verification_process` at
       :ref:`verification_concept_types_methods`.
     -
   * - DerivationTechnique
     - Examples are:

       - requirements-analysis
       - boundary-values
       - equivalence-classes
       - error-guessing
     - These are example values and an incomplete list.
       A full list of test methods is available in :need:`doc_concept__verification_process` at
       :ref:`verification_concept_types_methods`.
     -

The implementation of :need:`wp__verification_plan` defines the full list of allowed types and methods.

It is assumed that tests will be written as code (also for manual tests, which are script based)
and each test case will have a unique identifier, by its script, execution call, or function name.
The call used to execute the test marks the uniqueness of the test case and its identification,
e.g. guaranteeing proper traceability and reproducibility.

As the tests are stored in a repository close to the implementation code, versioning is done by the versioning of the repository.

Any specification and resulting implementation ends with a clear passed or failed result.

Test description
----------------

Following Given-When-Then is a preferred way to write test specifications.

* | Given (alternatively // Setup  )
  | This section contains the setup of the input.
* | Expected
  | This Section contains the expectation for calls to mocks or stubs
* | When (alternatively  // Call   )
  | This section contains the call to the software under test.
* | Then (alternatively // Expect )
  | This section contains the verification criteria of the test (e.g. all EXPECT statements).

.. code-block:: cpp

   TEST(CreateObjectHistory, GivenVehicleInFront_ExpectHistoryBehindFrontVehicle)
   {
      // Given
      const auto whatever_input_values = CreateVehicleInFront();

      // Expected
      EXPECT_CALL(..., ...);

      // When
      const auto history = CreateObjectHistory(whatever_input_values, ...);

      // Then
      for (const auto point : history)
      {
         EXPECT_EQ(..., ...);
      }
   }

Another example for a good test description could be:

  | Verify successful login with valid credentials.
  | Input:
  | - Username: testuser
  | - Password: password123
  | Expected Outcome:
  | - User is redirected to the home page and the welcome message "Hello, testuser!" is displayed.

A example for a bad test description could be:

   Test user login

Additional information can also be found in :need:`gd_guidl__verification_guide`.

The specification is part of the test implementation and has to comply to the requirements
specified in :need:`gd_req__verification_link_tests`.
