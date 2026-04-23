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

Work Product Process Overview
*****************************

The table below shows work product completion status and requirement verification status.

.. list-table:: Work product process overview
   :header-rows: 1
   :widths: 20 25 15 40

   * - Process area
     - Work product
     - WP status
     - Req. verification status
   * - Requirements Engineering
     - :need:`wp__requirements_stkh`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_stkh_req' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_stkh_req)
   * -
     - :need:`wp__requirements_sw_platform_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_stkh_req' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_stkh_req)
   * -
     - :need:`wp__requirements_feat`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_feat_req' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_feat_req)
   * -
     - :need:`wp__requirements_feat_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_aou' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_feat_aou' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_feat_aou)
   * -
     - :need:`wp__requirements_comp`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_comp_req' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_comp_req)
   * -
     - :need:`wp__requirements_comp_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_aou' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_comp_aou' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_comp_aou)
   * -
     - :need:`wp__requirements_proc_tool`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_proc_tool' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_proc_tool' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_proc_tool)
   * -
     - :need:`wp__requirements_inspect`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__monitor_verify_requirements' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__monitor_verify_requirements' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__monitor_verify_requirements)
   * - Architecture Design
     - :need:`wp__platform_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_platarch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_platarch' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__cr_mt_platarch)
   * -
     - :need:`wp__feature_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_featarch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_featarch' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__cr_mt_featarch)
   * -
     - :need:`wp__component_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_comparch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_comparch' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__cr_mt_comparch)
   * -
     - :need:`wp__sw_arch_verification`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__mr_vy_arch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__mr_vy_arch' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__mr_vy_arch)
   * - Implementation
     - :need:`wp__sw_development_plan`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_development_plan' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_development_plan' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__sw_development_plan)
   * -
     - :need:`wp__sw_implementation`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_detailed_design' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_detailed_design' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__sw_detailed_design)
   * -
     - :need:`wp__sw_implementation_inspection`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_verify_implementation' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_verify_implementation' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__sw_verify_implementation)
   * - Verification
     - :need:`wp__verification_plan`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)` / :need_count:`type == 'gd_req' and is_external == False and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_plan|wf__verification_plan_maintain)
   * -
     - :need:`wp__verification_platform_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_platform_int_test' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_platform_int_test)
   * -
     - :need:`wp__verification_platform_ver_report`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_ver_report' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_platform_ver_report' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_platform_ver_report)
   * -
     - :need:`wp__verification_feat_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_feat_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_feat_int_test' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_feat_int_test)
   * -
     - :need:`wp__verification_module_ver_report`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_mod_ver_report' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_mod_ver_report' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_mod_ver_report)
   * -
     - :need:`wp__verification_comp_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_comp_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_comp_int_test' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_comp_int_test)
   * -
     - :need:`wp__verification_sw_unit_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_unit_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_unit_test' in satisfies`
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_unit_test)
