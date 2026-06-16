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

Change Management Work Products
###############################

.. workproduct:: Platform Change Management Plan
   :id: wp__chm_plan
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__support_851[version==1]

   Change Management Plan (Part of the Platform Management Plan)

.. workproduct:: Issue tracking system
   :id: wp__issue_track_system
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_1
   :complies: std_wp__iso26262__management_554[version==1],
              std_wp__iso26262__management_652[version==1],
              std_wp__iso26262__support_852[version==1],
              std_wp__iso26262__support_853[version==1],
              std_wp__iso26262__support_854[version==1],
              std_wp__isopas8926__4527[version==1],
              std_req__aspice_40__iic-13-16[version==1],
              std_req__aspice_40__iic-13-07[version==1],
              std_req__aspice_40__iic-14-02[version==1],
              std_req__aspice_40__iic-15-55[version==1],
              std_req__aspice_40__iic-15-12[version==1],
              std_req__aspice_40__iic-14-01[version==1],
              std_wp__isosae21434__continual_8333[version==1],
              std_wp__isosae21434__continual_8431[version==1],
              std_wp__isosae21434__continual_8531[version==1],
              std_wp__isosae21434__continual_8631[version==1]

   | - Change request
   | - Change request plan
   | - Change report
   | - Identified safety anomaly report
   | - Impact analysis
   |
   | Safety anomaly: Conditions that deviate from expectations and that can lead to harm.
   | The documentation of a change request shall contain the list of changed work products,
   | the details of the change and the planned date of deployment of the change.
   | In case a anomaly cannot be closed it shall be escalated to the :need:`Project Lead <rl__project_lead>`.

.. workproduct:: Feature Request
   :id: wp__feat_request
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__support_852[version==1], std_wp__iso26262__support_853[version==1], std_req__aspice_40__iic-13-16[version==1]

   | - Feature request for a new feature or a feature modification
   |
   | Change Request for a new feature or a modification of an existing feature,
   | which changes the scope of the feature.

.. workproduct:: Component Request
   :id: wp__cmpt_request
   :status: valid
   :version: 1
   :tags: doc_lifecycle_model_2
   :complies: std_wp__iso26262__support_852[version==1], std_wp__iso26262__support_853[version==1], std_req__aspice_40__iic-13-16[version==1]

   | - Component request for a new component or a component modification
   |
   | Change Request for a new component or a modification of an existing component,
   | which changes the scope of the component.
   | This includes the allocation of components into SW Modules.
