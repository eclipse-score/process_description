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

.. _guideline_quality_management:

Quality Management Guideline
############################

.. gd_guidl:: Quality Management Guideline
   :id: gd_guidl__quality_management
   :status: valid
   :complies: std_wp__iso26262__management_553, std_req__iso26262__management_5423, std_req__aspice_40__SUP-1-BP1, std_req__aspice_40__SUP-1-BP2, std_req__aspice_40__SUP-1-BP3, std_req__aspice_40__SUP-1-BP4, std_req__aspice_40__SUP-1-BP7, std_req__aspice_40__PIM-3-BP1, std_req__aspice_40__PIM-3-BP2, std_req__aspice_40__PIM-3-BP3, std_req__aspice_40__PIM-3-BP4, std_req__aspice_40__PIM-3-BP5, std_req__aspice_40__PIM-3-BP6, std_req__aspice_40__PIM-3-BP7, std_req__aspice_40__SUP-1-BP5, std_req__aspice_40__SUP-1-BP6, std_req__aspice_40__PIM-3-BP8

   This document describes the general guidances for quality management based on the concept which is defined :need:`doc_concept__quality__process`.


General Hints
=============

The following steps are required to ensure the quality in the project:

#. Create/maintain Quality Management Plan
   For the creation of the Quality Management Plan, the template :need:`gd_temp__qlm_plan` can be used. As a reference also the
   Platform Quality Management Plan can be considered. Derivations to the platform plan should
   be documented in the Quality Management Plan. Also the project individual definitions like used resources and milestones.

#. Quality Plan (released)
   The Quality Management Plan is created and maintained by the :need:`rl__quality_manager`. It shall be continuously maintained
   during the project.

#. Verify/Aprove Platform Release
   The verification of a platform releas is done by the :need:`rl__quality_manager` and supported by the :need:`rl__technical_lead`.
   A checklist is used to ensure that all required items are checked. The checklist is based on the :need:`gd_chklst__review_checklist`.
   Every Platform Release needs at least one process audit.

#. Execute Platform Process Audit
   The results of the process audit are documented in the :need:`wp__process_impr_report`. For the release 100% of the audit has to be done.

#. Execute Feature Process Compliance Checks
   For the feature process compliance checks the :need:`gd_chklst__review_checklist` is used. Also spot checks shall be done to ensure that
   the processes are followed.

#. Execute Feature Work Product Reviews
   For the work product reviews the :need:`gd_chklst__review_checklist` is used. Derivations shall be documented in the issue tracking system with
   the label "q_wp_review" as described in the :need:`gd_guidl__wp_review`.

#. Monitor/Improve Quality Activities
   The issues for the improvment shall describe the scope, estimation of impact and time, measures as defined in :need:`wp__process_impr_report`.
   With the issue tracking system the status of the issues can be monitored. The issues are assigned to the :need:`rl__quality_manager`.

#. Update Issue Tracking System
   The actual status of the issues is updated in the issue tracking system. If necessary the :need:`rl__quality_manager` has to escalate the
   issues to the :need:`rl__project_lead`.
