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

.. _prm_process_requirements:

Process Requirements
====================

.. _prm_process_problem_attributes:

Problem Attributes
------------------

.. gd_req:: Problem attribute: UID
   :id: gd_req__problem_attr_uid
   :status: valid
   :version: 1
   :tags: done_automation, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   Each Problem shall have a unique ID. It shall be in an integer number.

.. gd_req:: Problem attribute: status
   :id: gd_req__problem_attr_status
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   Each Problem shall have a status:

      * open
      * in review
      * in implementation
      * closed
      * rejected

.. gd_req:: Problem attribute: title
   :id: gd_req__problem_attr_title
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   Reason for Problem Report

.. gd_req:: Problem attribute: description
   :id: gd_req__problem_attr_impact_description
   :status: valid
   :version: 2
   :tags: manual_prio_1, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1], std_req__aspice_40__SUP-9-BP2[version==1]

   Exact description of the Problem, including potential cause and impact of the problem.

   Record especially whether functional safety or cybersecurity may be affected.

   Record affected parties, whether notification is needed and why, and who was notified
   and when. See :ref:`prm_notifications`.

.. gd_req:: Problem attribute: affected versions
   :id: gd_req__problem_attr_affected_versions
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP2[version==1]

   Each Problem shall record the detection version and the first and last affected versions,
   including versions derived from the faulty version. Identify affected branches and
   dependent integrations where applicable. Record unknowns as under investigation and
   update them during analysis.

.. gd_req:: Problem attribute: analysis results
   :id: gd_req__problem_attr_analysis_results
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP2[version==1]

   Record analysis results (e.g. reason for rejection, safety, security, quality impact) as comments.

.. gd_req:: Problem attribute: stakeholder
   :id: gd_req__problem_attr_stakeholder
   :status: valid
   :version: 1
   :tags: prio_1_automation, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP2[version==1], std_req__aspice_40__SUP-9-BP5[version==1]

   Assign responsible stakeholder for analyzing the problem
   Assign responsible stakeholder to resolve the problem

.. gd_req:: Problem attribute: classification
   :id: gd_req__problem_attr_classification
   :status: valid
   :version: 1
   :tags: prio_1_automation, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1], std_req__aspice_40__SUP-9-BP2[version==1]

   Each Problem shall have a classification identifier:

      * minor
      * major
      * critical
      * blocker

.. gd_req:: Problem attribute:: safety affected
   :id: gd_req__problem_attr_safety_affected
   :status: valid
   :version: 2
   :tags: prio_1_automation, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   Each Problem shall have a safety relevance identifier:

      * Yes
      * No

   Where safety may be affected, the responsible :need:`Safety Manager <rl__safety_manager>`
   shall confirm or disconfirm safety relevance and record the reason.

   Note: If neither safety nor security is affected, the problem is quality relevant.

.. gd_req:: Problem attribute:: security affected
   :id: gd_req__problem_attr_security_affected
   :status: valid
   :version: 2
   :tags: prio_1_automation, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   Each Problem shall have a security relevance identifier:

      * Yes
      * No

   Where security may be affected, the responsible :need:`Security Manager <rl__security_manager>`
   shall confirm or disconfirm security relevance and record the reason.

   Note: If neither safety nor security is affected, the problem is quality relevant.

.. gd_req:: Problem attribute: milestone
   :id: gd_req__problem_attr_milestone
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, attribute, mandatory
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1], std_req__aspice_40__SUP-9-BP6[version==1]

   Milestone until the Problem must be implemented (used for prioritization)


Problem Resolution Checks
'''''''''''''''''''''''''

.. gd_req:: Problem Resolution mandatory attributes provided
   :id: gd_req__problem_check_mandatory
   :status: valid
   :version: 1
   :tags: prio_2_automation, problem_resolution, attribute, check
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   It shall be checked if all mandatory attributes for each Problem
   is provided by the user. Following attributes shall be mandatory:

   .. needtable:: Overview of mandatory problem attributes
      :filter: "mandatory" in tags and "attribute" and "problem_resolution" in tags and is_external == False
      :style: table
      :columns: title
      :colwidths: 30

   Note: See also template for problem report: :need:`gd_temp__problem_template`

.. gd_req:: Problem Report issues closing constraints
   :id: gd_req__problem_check_closing
   :status: valid
   :version: 1
   :tags: prio_1_automation, problem_resolution, attribute, check
   :satisfies: wf__problem_create_pr[version==1],
               wf__problem_analyze_pr[version==1],
               wf__problem_initiate_monitor_pr[version==1],
               wf__problem_close_pr[version==1]
   :complies: std_req__aspice_40__SUP-9-BP1[version==1]

   ISSUEs related to Problem Reports shall not automatically closed, if linked ISSUEs or PRs are closed or merged and
   these ISSUEs shall be closed only manually from the :need:`Committer <rl__committer>`.

.. gd_req:: Closure conditions for problems where safety is affected
   :id: gd_req__problem_check_safety_closure
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, check
   :satisfies: wf__problem_close_pr[version==1]
   :complies: std_req__iso26262__management_5433[version==1]

   A problem classified as Safety affected shall be considered managed to closure only
   when a rationale supports either an implemented adequate safety measure whose
   effectiveness has been verified, or an evaluation that the problem does not constitute
   an unreasonable risk.

.. gd_req:: Documentation and review of closure rationale where safety is affected
   :id: gd_req__problem_check_safety_rationale
   :status: valid
   :version: 1
   :tags: manual_prio_1, problem_resolution, check
   :satisfies: wf__problem_close_pr[version==1]
   :complies: std_req__iso26262__management_5434[version==1]

   For either safety-specific closure condition, the rationale shall be documented and
   reviewed. Record the review result. See :ref:`prm_safety_affected_closure`.

.. needextend:: "c.this_doc()"
   :+tags: problem_resolution
