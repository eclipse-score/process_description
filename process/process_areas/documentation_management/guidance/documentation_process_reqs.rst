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

.. _documentation_process_requirements:

Document Management Process Requirements
========================================

.. gd_req:: Document Types
   :id: gd_req__doc_types
   :status: valid
   :complies: std_req__iso26262__support_1043

   There is only one generic document type:
   * document

    .. note::
      This type is the ONLY type, which can be used for realizing concrete work products,
      e.g. Safety Plan

   .. note::
      Process documents are not generic documents and types for that shall only used for
      process definition, as defined

      * gd_chklst
      * gd_guidl
      * gd_req
      * gd_temp
      * doc_concept
      * doc_getstrt
      * workproduct
      * workflow
      * role


.. gd_req:: Document attributes
   :id: gd_req__doc_attributes
   :status: valid
   :complies: std_req__iso26262__support_1043

   Documents shall have the following manual attributes:

   * id
   * status
   * security
   * safety
   * realizes

   Compare also  :need:`gd_temp__documentation`

   Documents shall have automatic added attributes:

   * author
   * approver
   * reviewer

.. gd_req:: Document Author
   :id: gd_req__doc_author
   :status: valid
   :complies: std_req__iso26262__support_1045

   Documents headers shall contain an "author" attribute. Every committer who adds more than 50%
   of the content shall put his name.

   Note: In the future this may also be automated based on an analysis of content during the
   documentation build for every commit of the file containing the document.

.. gd_req:: Document Reviewer
   :id: gd_req__doc_reviewer
   :status: valid
   :complies: std_req__iso26262__support_1043

   Documents headers shall contain "reviewer" attribute, which is added during documentation build
   and contains only the names of the last PR reviewers, which actually reviewed the file
   containing the document, which were not covered by :need:`gd_req__doc_approver`.

.. gd_req:: Document Approver
   :id: gd_req__doc_approver
   :status: valid
   :complies: std_req__iso26262__support_1045

   Documents headers shall contain an "approver" attribute, which is added during documentation build
   and contains only the names of the last approval reviewers, which actually approved the file containing the document.
