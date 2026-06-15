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

Templates
=========

.. gd_temp:: Platform Release Note Template
   :id: gd_temp__rel_plat_rel_note
   :status: valid
   :version: 1
   :complies: std_req__iso26262__management_64134[version==1],
              std_req__iso26262__management_64135[version==1],
              std_req__aspice_40__SUP-8-BP7[version==1],
              std_req__aspice_40__SPL-2-BP1[version==1],
              std_req__aspice_40__iic-11-03[version==1],
              std_req__aspice_40__iic-18-06[version==1],
              std_req__aspice_40__SPL-2-BP2[version==1],
              std_req__aspice_40__SPL-2-BP3[version==1],
              std_req__aspice_40__iic-11-04[version==1],
              std_req__aspice_40__SPL-2-BP4[version==1],
              std_req__aspice_40__SPL-2-BP6[version==1]

   For the content see here: :need:`doc__platform_release_note`


.. gd_temp:: Module Release Note Template
   :id: gd_temp__rel_mod_rel_note
   :status: valid
   :version: 1
   :complies: std_req__iso26262__management_64134[version==1],
              std_req__iso26262__management_64135[version==1],
              std_req__iso26262__support_12425[version==1],
              std_req__aspice_40__SPL-2-BP1[version==1],
              std_req__aspice_40__iic-11-03[version==1],
              std_req__aspice_40__iic-18-06[version==1],
              std_req__aspice_40__SPL-2-BP2[version==1],
              std_req__aspice_40__SPL-2-BP3[version==1],
              std_req__aspice_40__iic-11-04[version==1],
              std_req__aspice_40__SPL-2-BP4[version==1],
              std_req__aspice_40__SPL-2-BP6[version==1],
              std_req__aspice_40__REU-2-BP6[version==1]

   For the content see here: `Module Release Note Template <https://eclipse-score.github.io/module_template/main/docs/release/release_note.html>`__


.. gd_temp:: Release Issue Template
   :id: gd_temp__rel_issue
   :status: valid
   :version: 1
   :complies: std_req__iso26262__management_64131[version==1],
              std_req__iso26262__management_64132[version==1],
              std_req__iso26262__management_64133[version==1],
              std_req__aspice_40__SPL-2-BP5[version==1],
              std_req__aspice_40__SPL-2-BP8[version==1]

   | Copy the below steps into the release ticket:
   |
   | Release <add version number> for <platform/module_name>
   | -------------------------------------------------------
   |
   | 1. Link this issue to the correct milestone and assign to a project/module lead
   | 2. Check respective Verification report on the release candidate's baseline
   | 3. Check bugfixes or justify failed tests
   | 4. Check the safety package completeness (includes "valid" documents and work products status, supported by the safety manager)
   | 5. Create/update the release note (pull request to close this issue)
   | 6. Document project manager's consent by asking review approval of the release note
   | 7. Create the "release" in version management tool according to :need:`gd_guidl__rel_management`
   | 8. Merge PR and close this issue to complete the release
