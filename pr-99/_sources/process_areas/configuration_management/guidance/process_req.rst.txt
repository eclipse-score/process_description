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

Configuration Management Process Requirements
=============================================

.. gd_req:: Permanent Storage
   :id: gd_req__config__workproducts_storage
   :status: valid
   :tags: prio_3_automation, config_mgt
   :complies: std_req__iso26262__support_745, std_req__aspice_40__SUP-8-BP8

   At least every platform release shall be stored permanently as a collection of text documents
   (docs and code) including the used OSS tooling outside of github servers.

   Note: This is to ensure to have the development artefacts available during the complete lifetime of the
   products (cars) the SW platform is used in.

.. gd_req:: Storage of pull requests documentation
   :id: gd_req__config__pull_request_storage
   :status: valid
   :tags: prio_2_automation, config_mgt
   :complies: std_req__iso26262__support_6433, std_req__iso26262__software_7414
   :satisfies: wf__monitor_verify_requirements, wf__mr_vy_arch

   The content of pull requests (conversation, commits, files changed) shall be stored permanently
   for every release.

   Note: The reason is that the PRs could be altered after the release and therefore for example the inspection documented within the review would be corrupted.

.. gd_req:: Baseline Differences
   :id: gd_req__config__baseline_diff
   :status: valid
   :tags: prio_2_automation, config_mgt
   :complies: std_req__iso26262__support_741

   It shall be possible to show the differences between two baselines.

   Note: This could be done by showing all the commits which happened between these baselines in one release branch.
