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

.. _work_products:

Work products
=============

An work product is an items needed as input or created as output of one or more tasks that are the responsibility of a :ref:`single role<roles>`.

The project development work product traceability model overview can be found here: :ref:`general_concepts_traceability`.

Project Work product Linkage
----------------------------

.. needpie:: The project work products contained in exactly one project workflow
   :labels: Not-Linked, Linked Work product, Linked Work product To Multiple Workflows
   :legend:
   :colors: red, green, blue
   :filter-func: score_metamodel.checks.standards.my_pie_workproducts_contained_in_exactly_one_workflow


.. _work_products_overview_list:

Project Work product list
-------------------------

.. needtable::
   :style: table
   :columns: title;id;tags
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["workproduct"]):
      if need['is_external'] == False:
                results.append(need)
