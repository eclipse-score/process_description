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

.. include:: tooling_definitions.rst

.. _process_status_overview:

Process Status Overview
#######################

Combined Process Area and Work Product Status Overview
******************************************************

The table below combines process requirement status, ISO 26262 std_req
compliance status, work product completion status, and tooling in a single overview.
For each process area the pie charts appear on the first work product row;
subsequent rows carry only the work product and its completion badge.

.. raw:: html

   <div class="chart-legend-block">
     <div class="chart-legend-group">
       <strong>Process req. status</strong>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#32CD32"></span>Valid</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#FFD700"></span>Draft</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#F08080"></span>Invalid</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#D3D3D3"></span>Other</span>
     </div>
     <div class="chart-legend-group">
       <strong>ISO 26262 std_req status</strong>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#32CD32"></span>Ok</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#ADD8E6"></span>Recommendation</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#FFD700"></span>Open</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#FFA500"></span>Action</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#F08080"></span>Deviation</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#D3D3D3"></span>N/A</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#C0C0C0"></span>Other</span>
     </div>
     <div class="chart-legend-group">
       <strong>Req. verification status</strong>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#32CD32"></span>Automated</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#FFD700"></span>Waiting for automation</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#ADD8E6"></span>Inspection list</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#D3D3D3"></span>Other</span>
     </div>
   </div>

.. list-table:: Combined process area and work product status overview
   :header-rows: 1
   :widths: 10 13 13 20 7 15 11 11
   :class: combined-status-table

   * - Process area
     - Process req. status
     - ISO 26262 std_req status
     - Work product
     - WP status
     - Req. verification status
     - Tooling
     - Tooling Status
   * - Requirements Engineering
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'requirements_engineering' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(requirements_engineering)

     - :need:`wp__requirements_stkh`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_stkh_req' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_stkh_req)
     - |tooling_name_wp__requirements_stkh|
     - |tooling_status_wp__requirements_stkh|
   * -
     -
     -
     - :need:`wp__requirements_sw_platform_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_stkh_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_stkh_req' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_stkh_req)
     - |tooling_name_wp__requirements_sw_platform_aou|
     - |tooling_status_wp__requirements_sw_platform_aou|
   * -
     -
     -
     - :need:`wp__requirements_feat`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_feat_req' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_feat_req)
     - |tooling_name_wp__requirements_feat|
     - |tooling_status_wp__requirements_feat|
   * -
     -
     -
     - :need:`wp__requirements_feat_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_feat_aou' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_feat_aou' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_feat_aou)
     - |tooling_name_wp__requirements_feat_aou|
     - |tooling_status_wp__requirements_feat_aou|
   * -
     -
     -
     - :need:`wp__requirements_comp`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_req' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_comp_req' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_comp_req)
     - |tooling_name_wp__requirements_comp|
     - |tooling_status_wp__requirements_comp|
   * -
     -
     -
     - :need:`wp__requirements_comp_aou`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_comp_aou' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_comp_aou' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_comp_aou)
     - |tooling_name_wp__requirements_comp_aou|
     - |tooling_status_wp__requirements_comp_aou|
   * -
     -
     -
     - :need:`wp__requirements_proc_tool`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__req_proc_tool' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__req_proc_tool' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__req_proc_tool)
     - |tooling_name_wp__requirements_proc_tool|
     - |tooling_status_wp__requirements_proc_tool|
   * -
     -
     -
     - :need:`wp__requirements_inspect`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__monitor_verify_requirements' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__monitor_verify_requirements' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__monitor_verify_requirements)
     - |tooling_name_wp__requirements_inspect|
     - |tooling_status_wp__requirements_inspect|
   * - Architecture Design
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'architecture_design' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(architecture_design)

     - :need:`wp__platform_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_platarch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_platarch' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__cr_mt_platarch)
     - |tooling_name_wp__platform_arch|
     - |tooling_status_wp__platform_arch|
   * -
     -
     -
     - :need:`wp__feature_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_featarch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_featarch' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__cr_mt_featarch)
     - |tooling_name_wp__feature_arch|
     - |tooling_status_wp__feature_arch|
   * -
     -
     -
     - :need:`wp__component_arch`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__cr_mt_comparch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__cr_mt_comparch' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__cr_mt_comparch)
     - |tooling_name_wp__component_arch|
     - |tooling_status_wp__component_arch|
   * -
     -
     -
     - :need:`wp__sw_arch_verification`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__mr_vy_arch' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__mr_vy_arch' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__mr_vy_arch)
     - |tooling_name_wp__sw_arch_verification|
     - |tooling_status_wp__sw_arch_verification|
   * - Implementation
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'implementation' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(implementation)

     - :need:`wp__sw_development_plan`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_development_plan' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_development_plan' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__sw_development_plan)
     - |tooling_name_wp__sw_development_plan|
     - |tooling_status_wp__sw_development_plan|
   * -
     -
     -
     - :need:`wp__sw_implementation`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_detailed_design' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_detailed_design' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__sw_detailed_design)
     - |tooling_name_wp__sw_implementation|
     - |tooling_status_wp__sw_implementation|
   * -
     -
     -
     - :need:`wp__sw_implementation_inspection`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__sw_verify_implementation' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__sw_verify_implementation' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__sw_verify_implementation)
     - |tooling_name_wp__sw_implementation_inspection|
     - |tooling_status_wp__sw_implementation_inspection|
   * - Verification
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'verification' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'verification' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'verification' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'verification' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(verification)

     - :need:`wp__verification_plan`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)` / :need_count:`type == 'gd_req' and is_external == False and ('wf__verification_plan' in satisfies or 'wf__verification_plan_maintain' in satisfies)`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_plan|wf__verification_plan_maintain)
     - |tooling_name_wp__verification_plan|
     - |tooling_status_wp__verification_plan|
   * -
     -
     -
     - :need:`wp__verification_platform_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_platform_int_test' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_platform_int_test)
     - |tooling_name_wp__verification_platform_int_test|
     - |tooling_status_wp__verification_platform_int_test|
   * -
     -
     -
     - :need:`wp__verification_platform_ver_report`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_platform_ver_report' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_platform_ver_report' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_platform_ver_report)
     - |tooling_name_wp__verification_platform_ver_report|
     - |tooling_status_wp__verification_platform_ver_report|
   * -
     -
     -
     - :need:`wp__verification_feat_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_feat_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_feat_int_test' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_feat_int_test)
     - |tooling_name_wp__verification_feat_int_test|
     - |tooling_status_wp__verification_feat_int_test|
   * -
     -
     -
     - :need:`wp__verification_module_ver_report`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_mod_ver_report' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_mod_ver_report' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_mod_ver_report)
     - |tooling_name_wp__verification_module_ver_report|
     - |tooling_status_wp__verification_module_ver_report|
   * -
     -
     -
     - :need:`wp__verification_comp_int_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_comp_int_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_comp_int_test' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_comp_int_test)
     - |tooling_name_wp__verification_comp_int_test|
     - |tooling_status_wp__verification_comp_int_test|
   * -
     -
     -
     - :need:`wp__verification_sw_unit_test`
     -

       .. rst-class:: wp-status-cell

       :need_count:`type == 'gd_req' and is_external == False and status == 'valid' and 'wf__verification_unit_test' in satisfies` / :need_count:`type == 'gd_req' and is_external == False and 'wf__verification_unit_test' in satisfies`
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.wp_tag_status(wf__verification_unit_test)
     - |tooling_name_wp__verification_sw_unit_test|
     - |tooling_status_wp__verification_sw_unit_test|

.. raw:: html

   <script>
   document.addEventListener('DOMContentLoaded', function() {
     var combinedTable = null;
     document.querySelectorAll('table').forEach(function(t) {
       var cap = t.querySelector('caption');
       if (cap && cap.textContent.trim().toLowerCase().includes('combined process area')) {
         combinedTable = t;
       }
     });
     if (!combinedTable) return;
     var rows = Array.from(combinedTable.querySelectorAll('tbody tr'));
     function hasContent(cell) {
       return cell.querySelector('img') !== null || cell.textContent.trim() !== '';
     }
     var firstGroup = true;
     rows.forEach(function(row) {
       var cells = row.querySelectorAll('td');
       if (cells.length > 0 && hasContent(cells[0])) {
         if (!firstGroup) { row.classList.add('group-start'); }
         firstGroup = false;
       }
     });
     [2, 1, 0].forEach(function(colIdx) {
       var anchorCell = null;
       var span = 1;
       rows.forEach(function(row) {
         var cells = row.querySelectorAll('td');
         if (cells.length <= colIdx) return;
         var cell = cells[colIdx];
         if (hasContent(cell)) {
           anchorCell = cell;
           span = 1;
           cell.style.verticalAlign = 'middle';
           cell.style.textAlign = 'center';
         } else if (anchorCell) {
           span += 1;
           anchorCell.rowSpan = span;
           cell.parentNode.removeChild(cell);
         }
       });
     });
   });
   </script>

Module Status by Work Product
*****************************

The following tables provide module-specific placeholders for manual status tracking.
Rows are grouped by process area and list the related work products.

.. raw:: html

   <div class="chart-legend-block">
     <div class="chart-legend-group">
       <strong>Done automation status</strong>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#32CD32"></span>done_automation</span>
       <span class="chart-legend-item"><span class="chart-legend-dot" style="background:#D3D3D3"></span>rest</span>
     </div>
   </div>

Baselibs
========

.. list-table:: Baselibs module status
   :header-rows: 1
   :widths: 50 25 25
   :class: module-status-table

   * - `Baselibs <https://github.com/eclipse-score/baselibs>`_
     - Functional complete
     - Done automation / rest
   * - **Requirements Engineering**
     -
     -
   * - :need:`wp__requirements_stkh`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_stkh_req)
   * - :need:`wp__requirements_sw_platform_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_stkh_req)
   * - :need:`wp__requirements_feat`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_feat_req)
   * - :need:`wp__requirements_feat_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_feat_aou)
   * - :need:`wp__requirements_comp`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_comp_req)
   * - :need:`wp__requirements_comp_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_comp_aou)
   * - :need:`wp__requirements_proc_tool`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_proc_tool)
   * - :need:`wp__requirements_inspect`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__monitor_verify_requirements)
   * - **Architecture Design**
     -
     -
   * - :need:`wp__platform_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_platarch)
   * - :need:`wp__feature_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_featarch)
   * - :need:`wp__component_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_comparch)
   * - :need:`wp__sw_arch_verification`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__mr_vy_arch)
   * - **Implementation**
     -
     -
   * - :need:`wp__sw_development_plan`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_development_plan)
   * - :need:`wp__sw_implementation`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_detailed_design)
   * - :need:`wp__sw_implementation_inspection`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_verify_implementation)
   * - **Verification**
     -
     -
   * - :need:`wp__verification_plan`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_plan|wf__verification_plan_maintain)
   * - :need:`wp__verification_platform_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_platform_int_test)
   * - :need:`wp__verification_platform_ver_report`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_platform_ver_report)
   * - :need:`wp__verification_feat_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_feat_int_test)
   * - :need:`wp__verification_module_ver_report`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_mod_ver_report)
   * - :need:`wp__verification_comp_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_comp_int_test)
   * - :need:`wp__verification_sw_unit_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_unit_test)

Communication
=============

.. list-table:: Communication module status
   :header-rows: 1
   :widths: 50 25 25
   :class: module-status-table

   * - `Communication <https://github.com/eclipse-score/communication>`_
     - Functional complete
     - Done automation / rest
   * - **Requirements Engineering**
     -
     -
   * - :need:`wp__requirements_stkh`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_stkh_req)
   * - :need:`wp__requirements_sw_platform_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_stkh_req)
   * - :need:`wp__requirements_feat`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_feat_req)
   * - :need:`wp__requirements_feat_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_feat_aou)
   * - :need:`wp__requirements_comp`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_comp_req)
   * - :need:`wp__requirements_comp_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_comp_aou)
   * - :need:`wp__requirements_proc_tool`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_proc_tool)
   * - :need:`wp__requirements_inspect`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__monitor_verify_requirements)
   * - **Architecture Design**
     -
     -
   * - :need:`wp__platform_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_platarch)
   * - :need:`wp__feature_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_featarch)
   * - :need:`wp__component_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_comparch)
   * - :need:`wp__sw_arch_verification`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__mr_vy_arch)
   * - **Implementation**
     -
     -
   * - :need:`wp__sw_development_plan`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_development_plan)
   * - :need:`wp__sw_implementation`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_detailed_design)
   * - :need:`wp__sw_implementation_inspection`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_verify_implementation)
   * - **Verification**
     -
     -
   * - :need:`wp__verification_plan`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_plan|wf__verification_plan_maintain)
   * - :need:`wp__verification_platform_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_platform_int_test)
   * - :need:`wp__verification_platform_ver_report`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_platform_ver_report)
   * - :need:`wp__verification_feat_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_feat_int_test)
   * - :need:`wp__verification_module_ver_report`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_mod_ver_report)
   * - :need:`wp__verification_comp_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_comp_int_test)
   * - :need:`wp__verification_sw_unit_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_unit_test)

Logging
=======

.. list-table:: Logging module status
   :header-rows: 1
   :widths: 50 25 25
   :class: module-status-table

   * - `Logging <https://github.com/eclipse-score/logging>`_
     - Functional complete
     - Done automation / rest
   * - **Requirements Engineering**
     -
     -
   * - :need:`wp__requirements_stkh`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_stkh_req)
   * - :need:`wp__requirements_sw_platform_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_stkh_req)
   * - :need:`wp__requirements_feat`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_feat_req)
   * - :need:`wp__requirements_feat_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_feat_aou)
   * - :need:`wp__requirements_comp`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_comp_req)
   * - :need:`wp__requirements_comp_aou`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_comp_aou)
   * - :need:`wp__requirements_proc_tool`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__req_proc_tool)
   * - :need:`wp__requirements_inspect`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__monitor_verify_requirements)
   * - **Architecture Design**
     -
     -
   * - :need:`wp__platform_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_platarch)
   * - :need:`wp__feature_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_featarch)
   * - :need:`wp__component_arch`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__cr_mt_comparch)
   * - :need:`wp__sw_arch_verification`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__mr_vy_arch)
   * - **Implementation**
     -
     -
   * - :need:`wp__sw_development_plan`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_development_plan)
   * - :need:`wp__sw_implementation`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_detailed_design)
   * - :need:`wp__sw_implementation_inspection`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__sw_verify_implementation)
   * - **Verification**
     -
     -
   * - :need:`wp__verification_plan`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_plan|wf__verification_plan_maintain)
   * - :need:`wp__verification_platform_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_platform_int_test)
   * - :need:`wp__verification_platform_ver_report`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_platform_ver_report)
   * - :need:`wp__verification_feat_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_feat_int_test)
   * - :need:`wp__verification_module_ver_report`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_mod_ver_report)
   * - :need:`wp__verification_comp_int_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_comp_int_test)
   * - :need:`wp__verification_sw_unit_test`
     -
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Done, Rest
          :colors: LimeGreen, LightGray
          :filter-func: needs_filters.wp_done_automation_status(wf__verification_unit_test)
