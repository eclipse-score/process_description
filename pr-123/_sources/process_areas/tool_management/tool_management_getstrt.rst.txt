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

Getting Started
###############

.. doc_getstrt:: Getting Started on Tool Management
   :id: doc_getstrt__tool__process
   :status: valid
   :tags: tool_management

This document describes the steps to evaluate tools and qualify them according to
ISO 26262 and ISO/SAE 21434 as used standards in the project.

Therefore guidelines :need:`gd_temp__tool_management__verif_rpt_template` and a
 :need:`doc_concept__tool__process` are available.


General Workflow
****************

The workflows are defined in the :ref:`tlm_workflows` section.

For every tool identified, the following workflows are executed:

* Create tool verification report according to :need:`wf__tool__create_tool_verification_report`
* Evaluate tool and update tool verification report according to :need:`wf__tool__evaluate_tool`
* Qualify tool and update tool verification report according to :need:`wf__tool__qualify_tool`
* Approve tool verification report according to :need:`wf__tool__approve_tool_verification_report`

In addition create a tool management plan as part of the platform management plan according to :need:`wf__platform__cr_mt_platform_mgmt_plan`.
