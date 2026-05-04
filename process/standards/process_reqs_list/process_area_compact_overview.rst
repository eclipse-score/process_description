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

.. _process_area_compact_overview:

Process Area Status Overview (Compact)
#######################################

The table below shows process requirement status, ISO 26262 std_req compliance
status, requirement verification status, and tooling per process area — one row
per area, without further splitting by work product.

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

.. raw:: html

   <div class="compact-overview-wrapper">

.. list-table:: Process area status overview (compact)
   :header-rows: 1
   :class: compact-overview-table
   :widths: 13 20 20 20 15 12

   * - Process area
     - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
     - Tools
     - Tooling available
   * - `Requirements Engineering <process_status_overview.html#requirements-engineering>`_
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
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(requirements_engineering)
     - sphinx-needs
     - 100%

   * - `Architecture Design <process_status_overview.html#architecture-design>`_
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
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(architecture_design)
     - sphinx-needs, PlantUML
     - 75%

   * - `Implementation <process_status_overview.html#implementation>`_
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
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(implementation)
     - sphinx-needs, C++/RUST toolchain
     - 67%

   * - `Verification <process_status_overview.html#verification>`_
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
     -

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(verification)
     - sphinx-needs, ITF, gtest
     - 57%

.. raw:: html

   </div>
