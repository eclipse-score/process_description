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

.. gd_req:: Unique Id
   :id: gd_req__configuration_uid
   :status: valid
   :version: 1
   :tags: done_automation, config_mgt
   :complies: std_req__iso26262__support_745[version==1], std_req__aspice_40__SUP-8-BP8[version==1]
   :satisfies: wf__monitor_verify_requirements[version==1],
               wf__mr_vy_arch[version==1],
               wf__mr_saf_analyses_dfa[version==1],
               wf__vy_saf_analyses_dfa[version==1],
               wf__platform_mr_im_platform_mgmt_plan[version==1]

   The Docs-as-Code tool shall check that the Id's of the configuration items (documented in doc-as-code) are unique.

   Note: For definition of configuration items see :need:`doc_concept__configuration_process`

.. gd_req:: Permanent Storage
   :id: gd_req__config_workproducts_storage
   :status: valid
   :version: 1
   :tags: prio_3_automation, config_mgt
   :complies: std_req__iso26262__support_745[version==1], std_req__aspice_40__SUP-8-BP8[version==1]
   :satisfies: wf__rel_platform_rel_note[version==1], wf__rel_mod_rel_note[version==1]

   At least every platform release shall be stored permanently as a collection of text documents
   (docs and code) including the used OSS tooling on project owned servers.

   Note: This is to ensure to have the development artefacts available during the complete lifetime of the
   products (cars) the SW platform is used in.

.. gd_req:: Storage of pull requests documentation
   :id: gd_req__config_pull_request_storage
   :status: valid
   :version: 1
   :tags: prio_2_automation, config_mgt
   :complies: std_req__iso26262__support_6433[version==1], std_req__iso26262__software_7414[version==1]
   :satisfies: wf__monitor_verify_requirements[version==1], wf__mr_vy_arch[version==1]

   The content of pull requests (conversation, commits, files changed) shall be stored permanently
   for every release.

   Note: This requirement exists because PRs may be modified after a release, which could corrupt the documented inspection results recorded during the review.

.. gd_req:: Baseline Differences
   :id: gd_req__config_baseline_diff
   :status: valid
   :version: 1
   :tags: prio_2_automation, config_mgt
   :complies: std_req__iso26262__support_741[version==1]
   :satisfies: wf__rel_platform_rel_note[version==1], wf__rel_mod_rel_note[version==1]

   It shall be possible to show the differences between two baselines.

   Note: This could be done by showing all the commits which happened between these baselines in one release branch.

.. gd_req::  Document attributes
   :id: gd_req__config_consistent_attributes
   :status: valid
   :version: 1
   :tags: prio_2_automation
   :complies: std_req__aspice_40__SUP-8-BP3[version==1], std_req__aspice_40__SUP-8-BP4[version==1]
   :satisfies: wf__platform_cr_mt_platform_mgmt_plan[version==1]

   It shall be prohibited to override any mandatory attribute value of an docs-as-code element.

   Note: This requirement exists because docs-as-code attributes may be globally overridden, which leads to a mismatch of code and the representing generated documentation.
   Exception only exists for optional tags, which can be used for filtering and reporting purposes.

.. gd_req::  Global tags extension
   :id: gd_req__config_global_tags
   :status: valid
   :version: 1
   :tags: prio_3_automation
   :satisfies: wf__platform_cr_mt_platform_mgmt_plan[version==1]

   It shall be possible to define global tags with the docs-as-code tool, which can be used for filtering and reporting.

   Note: This requirement exists to enable the use of global tags for filtering and reporting purposes, while still prohibiting the overriding of mandatory attributes or elements globally.
