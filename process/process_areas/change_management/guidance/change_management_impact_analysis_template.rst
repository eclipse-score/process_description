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

.. _chm_impact_analysis_templates:

Impact Analysis Template
========================

.. gd_temp:: Impact Analysis Template
   :id: gd_temp__change_impact_analysis
   :status: valid
   :version: 2
   :complies: std_req__aspice_40__SUP-10-BP2[version==1],
              std_req__aspice_40__iic-18-57[version==1],
              std_req__iso26262__support_8431[version==1],
              std_req__iso26262__support_8432[version==1],
              std_req__isopas8926__44612[version==1],
              std_req__isopas8926__4462[version==1],
              std_req__iso26262__management_644[version==1],
              std_req__isopas8926__4431[version==1],
              std_req__iso26262__management_6452[version==1]

Type of Change Request
----------------------

[New Feature/Component, Modification of an existing Feature/Component]


Dependencies on other Change Requests
-------------------------------------

[List all dependencies on other Change Requests]


Estimates for Realization
-------------------------

[List all work products and elements affected by the Change Request]

    .. note::
     For the identification of the affected work products use the Traceability Analysis approach.
     Traceability analysis uses the existing links between different elements (requirements, architecture, implementation, etc.)
     for the identification of the affected work products and elements.

[Describe here which work products to be modified by the Change Request]

[Describe here the verification methods used for the changed work products or elements]

[Estimate the effort, resources, risk for the realization]

[Describe here which stakeholder and which roles of the stakeholder are involved to execute the Change Request]

   .. note::
      Typically the :need:`Project Leads <rl__project_lead>` are involved
      for planning and approval activities. As well as :need:`Safety Manager <rl__safety_manager>` or :need:`Security Manager <rl__security_manager>`
      are responsible for Change Request which has impact on functional safety or security.

[Describe here which Milestones are considered to realize the Change Request]

    .. note::
     A draft realization plan may support the realization proposal.


Potential Impact on the platform
--------------------------------

[How could the platform be impacted by the new/modified feature?]

[Describe potential impact and severity on pre-existing platform/project elements.]


Potential Impact on Security
-----------------------------

[How could a malicious user take advantage of this new/modified feature?]

.. note::
   If there are security concerns in relation to the CR, those concerns should be explicitly written out to make sure reviewers of the CR are aware of them.

Which security requirements are affected or has to be changed?
Could the new/modified feature enable new threat scenarios?
Could the new/modified feature enable new attack paths?
Could the new/modified feature impact functional safety?
If applicable, which additional security measures must be implemented to mitigate the risk?

.. note::
   Use Trust Boundary, Defense in Depth Analysis and/or Security Software Critically Analysis,
   Vulnerability Analysis.
   [Methods will be defined later in Process area Security Analysis]
   These analyses may not be available at the time of creation of the feature (request) but content will be improved iteratively.


Potential Impact on Safety
--------------------------

[How could the safety be impacted by the new/modified feature?]

.. note::
   If there are safety concerns in relation to the CR, those concerns should be explicitly written out to make sure reviewers of the CR are aware of them.
   Link here to the filled out :need:`Impact Analysis Template <gd_temp__change_impact_analysis>` or copy the template in this chapter.

Which safety requirements are affected or has to be changed?
Could the new/modified feature be a potential common cause or cascading failure initiator?
If applicable, which additional safety measures must be implemented to mitigate the risk?

.. note::
   Use Dependency Failure Analysis and/or Safety Software Critically Analysis.
   [Methods will be defined later in Process area Safety Analysis]
   These analyses may not be available at the time of creation of the feature (request) but content will be improved iteratively.

For new feature contributions:

[What is the expected ASIL level?]


License Impact
==============

[How could the copyright impacted by the license of the new contribution?]
