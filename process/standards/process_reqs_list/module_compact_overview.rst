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

.. include:: module_completeness_summary.rst

.. _module_compact_overview:

Module Status Overview (Compact)
##################################

The table below shows the average functional completeness per module and process
area as a single Harvey ball. The ball is computed as the mean of all work
product completeness values in each area, rounded up to the nearest 25%.

To update the values, edit the numbers in
:download:`functional_completeness_definitions.rst <functional_completeness_definitions.rst>`.
The Harvey balls are recomputed automatically during the next documentation build.

.. raw:: html

   <div class="chart-legend-block">
     <div class="chart-legend-group">
       <strong>Functional completeness (average per area)</strong>
       <span class="chart-legend-item"><span class="harvey-legend harvey-legend-0"></span>0%</span>
       <span class="chart-legend-item"><span class="harvey-legend harvey-legend-25"></span>25%</span>
       <span class="chart-legend-item"><span class="harvey-legend harvey-legend-50"></span>50%</span>
       <span class="chart-legend-item"><span class="harvey-legend harvey-legend-75"></span>75%</span>
       <span class="chart-legend-item"><span class="harvey-legend harvey-legend-100"></span>100%</span>
     </div>
   </div>

.. raw:: html

   <div class="compact-overview-wrapper">

.. list-table:: Module functional completeness overview
   :header-rows: 1
   :class: compact-overview-table module-compact-table
   :widths: 20 20 20 20 20

   * - Module
     - Requirements Engineering
     - Architecture Design
     - Implementation
     - Verification

   * - `Baselibs <process_status_overview.html#baselibs>`_
     - |fc_avg_baselibs_requirements_engineering|
     - |fc_avg_baselibs_architecture_design|
     - |fc_avg_baselibs_implementation|
     - |fc_avg_baselibs_verification|

   * - `Communication <process_status_overview.html#communication>`_
     - |fc_avg_communication_requirements_engineering|
     - |fc_avg_communication_architecture_design|
     - |fc_avg_communication_implementation|
     - |fc_avg_communication_verification|

   * - `Logging <process_status_overview.html#logging>`_
     - |fc_avg_logging_requirements_engineering|
     - |fc_avg_logging_architecture_design|
     - |fc_avg_logging_implementation|
     - |fc_avg_logging_verification|

.. raw:: html

   </div>
