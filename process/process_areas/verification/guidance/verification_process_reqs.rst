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

.. _verification_process_reqs:

Process Requirements
====================

.. gd_req:: Linking Requirements to Tests
    :id: gd_req__verification_link_tests
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies: std_req__iso26262__support_6432


    For linking test suites to requirements following metadata shall be used:

    * Verifies
        * PartiallyVerifies
        * FullyVerifies
    * Description
    * TestType
        * Fault Injection (fault-injection)
        * Interface Test (interface-test)
        * Requirements-based Test (requirements-based)
        * Resource Usage Evaluation (resource-usage)
    * DerivationTechnique
        * Analysis of requirements (requirements-analysis)
        * Analysis of design (design-analysis)
        * Analysis of boundary values (boundary-values)
        * Analysis of equivalence classes (equivalence-classes)
        * Fuzzy testing (fuzz-testing)
        * Error guessing based on knowledge or experience (error-guessing)
        * Explorative testing (explorative-testing)


    More information can be found in the :need:`gd_guidl__verification_guide`, :need:`doc_concept__verification_process`,
    and :need:`gd_guidl__verification_specification` .

.. gd_req:: Linking Requirements to Tests (C++)
    :id: gd_req__verification_link_tests_cpp
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies: std_req__iso26262__support_6432, std_req__aspice_40__SWE-4-BP4, std_req__aspice_40__SWE-5-BP6, std_req__aspice_40__SWE-6-BP4


    For linking C++ tests to requirements **record properties** shall be used. Attributes
    which are common for all test cases can be specified in the Setup Function (SetUp()), the other
    attributes which are specific for each test case need to be specified within the test case:

    A more detailed description of how to link code to requirements looks like is available in the :ref:`verification_template_cpp`


.. gd_req:: Linking Requirements to Tests (Python)
    :id: gd_req__verification_link_tests_python
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies: std_req__iso26262__support_6432, std_req__aspice_40__SWE-4-BP4, std_req__aspice_40__SWE-5-BP6, std_req__aspice_40__SWE-6-BP4


    For linking python tests to requirements **metadata** shall be used.
    For this the 'add_test_properties' decorator has been provided.
    You need to add it to the test and fill out:

    * partially_verifies OR fully_verifies
    * test_type
    * derivation_technique

    For allowed values for test_type & derivation_technique please check :need:`gd_req__verification_link_tests`
    Further more, this decorator will also check if your test has a `docstring` which should act as the description of the test.

    A more detailed description of how to link code to requirements looks like is available in the :ref:`verification_template_python`


.. gd_req:: Linking Requirements to Tests (Rust)
    :id: gd_req__verification_link_tests_rust
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies: std_req__iso26262__support_6432, std_req__aspice_40__SWE-4-BP4, std_req__aspice_40__SWE-5-BP6, std_req__aspice_40__SWE-6-BP4

    For linking Rust tests to requirements **#[record_property]** shall be used:

    A more detailed description of how to link code to requirements looks like is available in the :ref:`verification_template_rust`

.. gd_req:: Independence
    :id: gd_req__verification_independence
    :status: valid
    :tags: done_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies: std_req__aspice_40__SWE-4-BP4, std_req__aspice_40__SWE-5-BP6, std_req__aspice_40__SWE-6-BP4

    The approver of a pull request shall differ from the author(s) of the pull request in all pull requests.

.. gd_req:: Verification Reporting
    :id: gd_req__verification_reporting
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_mod_ver_report
    :complies:

    The tool automation shall automatically generate the Verification reports.
    These may be independent documents (i.e. not integrated into docs-as-code based repositories).
    The content of the reports is specified in :need:`gd_temp__platform_ver_report` and :need:`gd_temp__mod_ver_report`.

.. gd_req:: Verification Report Archiving
    :id: gd_req__verification_report_archiving
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_mod_ver_report
    :complies:

    The tool automation shall automatically archive the Verification reports for releases.
    The reports are generated according to :need:`gd_req__verification_reporting`.

.. gd_req:: Verification Documentation Checks
    :id: gd_req__verification_checks
    :status: valid
    :tags: prio_1_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies:

    The following checks shall be implemented on test metadata:

    - TestType and DerivationTechnique shall be set
    - Description shall not be empty
    - In a Platform Integration Test Partially/FullyVerifies shall be set to a Platform Requirement
    - If Partially/FullyVerifies are set in Feature Integration Test these shall link to Feature Requirements
    - If Partially/FullyVerifies are set in Component Integration Test these shall link to Component Requirements
    - If Partially/FullyVerifies are set in Unit Test these shall link to Component Requirements

.. gd_req:: Verification Documentation Checks Extended
    :id: gd_req__verification_checks_extended
    :status: draft
    :tags: verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies:

    The following checks shall be implemented on test metadata:

    - If TestType is set to requirements-based then PartiallyVerifies or FullyVerifies shall contain a link to at least one requirement
    - If TestType is set to interface-test then PartiallyVerifies or FullyVerifies shall contain a link to at least one interface

.. gd_req:: Verification of External Components AoUs
    :id: gd_req__verification_external_aou
    :status: valid
    :tags: prio_2_automation, verification
    :satisfies: wf__verification_comp_int_test, wf__verification_feat_int_test
    :complies:

    External components AoUs shall be verified by integration tests or static analysis tooling.

    Note1: These external components AoU need to be checked generally for the complete platform, so we create a process automation requirement for this.

    Note2: One example would be the checking if safety components are only using "safe" functions of the operating system.

.. gd_req:: Static Code Analysis Classification
    :id: gd_req__verification_sca_classification
    :status: valid
    :tags: prio_2_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies:

    Static code analysis findings shall be classified according to the following categories:

    - Critical
    - High
    - Medium
    - Low

    The actual classification shall be either provided by the tool as a suggestion or defined manually by :need:`rl__quality_manager` together with :need:`rl__committer`.

    Alternative rating like class A, B, C, D or 1, 2, 3, 4 can be used as well, but the principle mapping to the above categories shall be preserved and documented.

.. gd_req:: CI reference integration execution
    :id: gd_req__verification_ci_reference_execution
    :status: valid
    :tags: prio_2_automation, verification
    :satisfies: wf__verification_unit_test, wf__verification_comp_int_test, wf__verification_feat_int_test, wf__verification_platform_int_test
    :complies:

    The CI reference integration execution shall be triggered on regular basis to guarantee the inter-operation of all integrated components
    when a new component is added to the system or an existing component is updated via a PR.

    **TODO: Align this to the ongoing work in https://github.com/eclipse-score/reference_integration/pull/190 which reworks the CI reference integration execution.**
