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

.. _process_req_area_status_summary:

Process Requirement Status by Process Area
##########################################

The table below summarizes all internal ``gd_req`` needs found in each process area.
The charts are calculated dynamically during the Sphinx build via sphinx-needs
filters.

Color mapping:

- Green: valid
- Gold: draft
- Red: invalid
- Gray: other

.. list-table:: Process requirement status overview
   :header-rows: 1
   :widths: 20 40 40

   * - Process area
     - Process req. status
     - Referenced std_req status
   * - Requirements Engineering
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'requirements_engineering' in tags
     -

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(requirements_engineering)

   * - Architecture Design
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'architecture_design' in tags
     -

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(architecture_design)

   * - Implementation
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'implementation' in tags
     -

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(implementation)

   * - Verification
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'verification' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'verification' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'verification' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'verification' in tags
     -

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(verification)

Referenced std_req Needs in "Other" Category
*********************************************

The following ``std_req`` needs are referenced via ``complies`` from process
requirements but carry none of the recognized tags (``ok``, ``recommendation``,
``open``, ``action``, ``deviation``, ``n/a``).
The actual tags of each need are shown in brackets.

.. needlist::

   RECOGNIZED = {"ok", "recommendation", "open", "action", "deviation", "n/a"}
   needs_by_id = {n["id"]: n for n in needs}

   std_req_ids = set()
   for need in needs:
       if (
           need.get("type") == "gd_req"
           and not need.get("is_external", False)
       ):
           for ref_id in need.get("complies", []):
               if ref_id.startswith("std_req__iso26262__"):
                   std_req_ids.add(ref_id)

   results = []
   for sid in sorted(std_req_ids):
       n = needs_by_id.get(sid)
       if n and not (RECOGNIZED & set(n.get("tags", []))):
           results.append(n)

Work Products by Process Area
*****************************

The table below lists the official work products defined per process area.

.. list-table:: Work product overview by process area
   :header-rows: 1
   :widths: 28 72

   * - Process area
     - Work products
   * - Requirements Engineering
     -

       - :need:`wp__requirements_stkh`
       - :need:`wp__requirements_sw_platform_aou`
       - :need:`wp__requirements_feat`
       - :need:`wp__requirements_feat_aou`
       - :need:`wp__requirements_comp`
       - :need:`wp__requirements_comp_aou`
       - :need:`wp__requirements_proc_tool`
       - :need:`wp__requirements_inspect`
   * - Architecture Design
     -

       - :need:`wp__platform_arch`
       - :need:`wp__feature_arch`
       - :need:`wp__component_arch`
       - :need:`wp__sw_arch_verification`
   * - Implementation
     -

       - :need:`wp__sw_development_plan`
       - :need:`wp__sw_implementation`
       - :need:`wp__sw_implementation_inspection`
   * - Verification
     -

       - :need:`wp__verification_plan`
       - :need:`wp__verification_platform_int_test`
       - :need:`wp__verification_platform_ver_report`
       - :need:`wp__verification_feat_int_test`
       - :need:`wp__verification_module_ver_report`
       - :need:`wp__verification_comp_int_test`
       - :need:`wp__verification_sw_unit_test`

Relevant Requirements by Work Product
*************************************

The table below derives relevant process requirements for each work product.
The derivation is based on the relation process requirement ``satisfies``
workflow and workflow ``output`` work product.

.. list-table:: Relevant process requirements by work product
   :header-rows: 1
   :widths: 15 22 32 31

   * - Process area
     - Work product
     - Relevant requirements
     - Status distribution
   * - Requirements Engineering
     - :need:`wp__requirements_stkh`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_stkh" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_stkh_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_stkh_req' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_stkh_req' in satisfies
   * -
     - :need:`wp__requirements_sw_platform_aou`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_sw_platform_aou" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_stkh_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_stkh_req' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_stkh_req' in satisfies
   * -
     - :need:`wp__requirements_feat`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_feat" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_feat_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_feat_req' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_feat_req' in satisfies
   * -
     - :need:`wp__requirements_feat_aou`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_feat_aou" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_aou' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_feat_aou' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_feat_aou' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_feat_aou' in satisfies
   * -
     - :need:`wp__requirements_comp`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_comp" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_comp_req' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_comp_req' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_comp_req' in satisfies
   * -
     - :need:`wp__requirements_comp_aou`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_comp_aou" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_aou' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_comp_aou' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_comp_aou' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_comp_aou' in satisfies
   * -
     - :need:`wp__requirements_proc_tool`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_proc_tool" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_proc_tool' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__req_proc_tool' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__req_proc_tool' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__req_proc_tool' in satisfies
   * -
     - :need:`wp__requirements_inspect`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "requirements_engineering" in workflow["tags"] and "wp__requirements_inspect" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__monitor_verify_requirements' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__monitor_verify_requirements' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__monitor_verify_requirements' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__monitor_verify_requirements' in satisfies
   * - Architecture Design
     - :need:`wp__platform_arch`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "architecture_design" in workflow["tags"] and "wp__platform_arch" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_platarch' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__cr_mt_platarch' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__cr_mt_platarch' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__cr_mt_platarch' in satisfies
   * -
     - :need:`wp__feature_arch`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "architecture_design" in workflow["tags"] and "wp__feature_arch" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_featarch' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__cr_mt_featarch' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__cr_mt_featarch' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__cr_mt_featarch' in satisfies
   * -
     - :need:`wp__component_arch`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "architecture_design" in workflow["tags"] and "wp__component_arch" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_comparch' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__cr_mt_comparch' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__cr_mt_comparch' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__cr_mt_comparch' in satisfies
   * -
     - :need:`wp__sw_arch_verification`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "architecture_design" in workflow["tags"] and "wp__sw_arch_verification" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__mr_vy_arch' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__mr_vy_arch' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__mr_vy_arch' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__mr_vy_arch' in satisfies
   * - Implementation
     - :need:`wp__sw_development_plan`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "implementation" in workflow["tags"] and "wp__sw_development_plan" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_development_plan' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__sw_development_plan' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__sw_development_plan' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__sw_development_plan' in satisfies
   * -
     - :need:`wp__sw_implementation`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "implementation" in workflow["tags"] and "wp__sw_implementation" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_detailed_design' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__sw_detailed_design' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__sw_detailed_design' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__sw_detailed_design' in satisfies
   * -
     - :need:`wp__sw_implementation_inspection`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "implementation" in workflow["tags"] and "wp__sw_implementation_inspection" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_verify_implementation' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__sw_verify_implementation' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__sw_verify_implementation' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__sw_verify_implementation' in satisfies
   * - Verification
     - :need:`wp__verification_comp_int_test`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_comp_int_test" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_comp_int_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__verification_comp_int_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__verification_comp_int_test' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__verification_comp_int_test' in satisfies
   * -
     - :need:`wp__verification_feat_int_test`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_feat_int_test" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_feat_int_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__verification_feat_int_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__verification_feat_int_test' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__verification_feat_int_test' in satisfies
   * -
     - :need:`wp__verification_platform_int_test`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_platform_int_test" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_int_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__verification_platform_int_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__verification_platform_int_test' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__verification_platform_int_test' in satisfies
   * -
     - :need:`wp__verification_plan`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_plan" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)
          type == 'gd_req' and is_external == False and status == 'draft' and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)
          type == 'gd_req' and is_external == False and status == 'invalid' and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)
   * -
     - :need:`wp__verification_module_ver_report`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_module_ver_report" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_mod_ver_report' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__verification_mod_ver_report' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__verification_mod_ver_report' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__verification_mod_ver_report' in satisfies
   * -
     - :need:`wp__verification_platform_ver_report`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_platform_ver_report" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_ver_report' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__verification_platform_ver_report' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__verification_platform_ver_report' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__verification_platform_ver_report' in satisfies
   * -
     - :need:`wp__verification_sw_unit_test`
     -

       .. needlist::

          results = []
          requirement_ids = set()

          for requirement in needs.filter_types(["gd_req"]):
              if requirement["is_external"] is False:
                  for workflow_id in requirement["satisfies"]:
                      workflow = needs.get_need(workflow_id)
                      if workflow and workflow["is_external"] is False and "verification" in workflow["tags"] and "wp__verification_sw_unit_test" in workflow["output"]:
                          if requirement["id"] not in requirement_ids:
                              requirement_ids.add(requirement["id"])
                              results.append(requirement)
                          break

          results = sorted(results, key=lambda requirement: requirement["title"])
     -

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_unit_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'draft' and 'wf__verification_unit_test' in satisfies
          type == 'gd_req' and is_external == False and status == 'invalid' and 'wf__verification_unit_test' in satisfies
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'wf__verification_unit_test' in satisfies

Work Product Requirement Completion Status
******************************************

The table below shows for each work product the completion status of its
relevant process requirements. **Valid** (green) means all requirements are
valid; **Draft** (yellow) means at least one requirement is not yet valid.
The number shows valid / total requirements.

.. list-table:: Work product requirement completion status
   :header-rows: 1
   :widths: 15 35 50

   * - Process area
     - Work product
     - Status
   * - Requirements Engineering
     - :need:`wp__requirements_stkh`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_stkh_req' in satisfies`
   * -
     - :need:`wp__requirements_sw_platform_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_stkh_req' in satisfies`
   * -
     - :need:`wp__requirements_feat`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_feat_req' in satisfies`
   * -
     - :need:`wp__requirements_feat_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_aou' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_feat_aou' in satisfies`
   * -
     - :need:`wp__requirements_comp`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_comp_req' in satisfies`
   * -
     - :need:`wp__requirements_comp_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_aou' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_comp_aou' in satisfies`
   * -
     - :need:`wp__requirements_proc_tool`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_proc_tool' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_proc_tool' in satisfies`
   * -
     - :need:`wp__requirements_inspect`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__monitor_verify_requirements' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__monitor_verify_requirements' in satisfies`
   * - Architecture Design
     - :need:`wp__platform_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_platarch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_platarch' in satisfies`
   * -
     - :need:`wp__feature_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_featarch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_featarch' in satisfies`
   * -
     - :need:`wp__component_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_comparch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_comparch' in satisfies`
   * -
     - :need:`wp__sw_arch_verification`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__mr_vy_arch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__mr_vy_arch' in satisfies`
   * - Implementation
     - :need:`wp__sw_development_plan`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_development_plan' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_development_plan' in satisfies`
   * -
     - :need:`wp__sw_implementation`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_detailed_design' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_detailed_design' in satisfies`
   * -
     - :need:`wp__sw_implementation_inspection`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_verify_implementation' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_verify_implementation' in satisfies`
   * - Verification
     - :need:`wp__verification_plan`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)` / :need_count:`type == 'gd_req' and is_external == False and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)`
   * -
     - :need:`wp__verification_platform_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_platform_int_test' in satisfies`
   * -
     - :need:`wp__verification_platform_ver_report`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_ver_report' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_platform_ver_report' in satisfies`
   * -
     - :need:`wp__verification_feat_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_feat_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_feat_int_test' in satisfies`
   * -
     - :need:`wp__verification_module_ver_report`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_mod_ver_report' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_mod_ver_report' in satisfies`
   * -
     - :need:`wp__verification_comp_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_comp_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_comp_int_test' in satisfies`
   * -
     - :need:`wp__verification_sw_unit_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_unit_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_unit_test' in satisfies`

.. raw:: html

   <script>
   document.addEventListener('DOMContentLoaded', function() {
     document.querySelectorAll('p.wp-status-cell').forEach(function(p) {
       var match = p.textContent.match(/(\d+)\s*\/\s*(\d+)/);
       if (match) {
         var valid = parseInt(match[1], 10);
         var total = parseInt(match[2], 10);
         var badge = document.createElement('span');
         badge.style.fontWeight = 'bold';
         badge.style.padding = '3px 10px';
         badge.style.borderRadius = '4px';
         badge.style.display = 'inline-block';
         if (total > 0 && valid >= total) {
           badge.textContent = 'Valid (' + valid + '/' + total + ')';
           badge.style.backgroundColor = 'LimeGreen';
           badge.style.color = 'white';
         } else {
           badge.textContent = 'Draft (' + valid + '/' + total + ')';
           badge.style.backgroundColor = 'Gold';
           badge.style.color = 'black';
         }
         p.innerHTML = '';
         p.appendChild(badge);
       }
     });
   });
   </script>

