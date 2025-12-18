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

Process Requirements
####################

.. gd_req:: Static Diagram for Unit Interactions
   :id: gd_req__impl_static_diagram
   :status: valid
   :tags: manual_prio_1, mandatory
   :satisfies: wf__sw_detailed_design
   :complies: std_req__iso26262__software_843, std_req__iso26262__software_844, std_req__iso26262__software_845, std_req__aspice_40__SWE-3-BP1

   The static diagram shall represent the unit and their relationships using UML notations.

Diagram Attributes
------------------

.. gd_req:: Diagram attribute: UID
   :id: gd_req__impl_diagram_uid
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :satisfies: wf__sw_detailed_design
   :complies: std_req__iso26262__software_843, std_req__iso26262__software_844, std_req__iso26262__software_845, std_req__aspice_40__SWE-3-BP2

   Each diagram shall have a unique ID. It shall consist of three parts:

      * type of diagram
      * structural element
      * keyword describing the content of the diagram

   Consider the project's naming convention.

.. gd_req:: Diagram attribute: title
   :id: gd_req__impl_diagram_title
   :status: valid
   :tags: manual_prio_1 attribute, mandatory
   :satisfies: wf__sw_detailed_design
   :complies: std_req__iso26262__software_843, std_req__iso26262__software_844, std_req__iso26262__software_845, std_req__aspice_40__SWE-3-BP3, std_req__aspice_40__SWE-3-BP4

   The title of the diagram shall provide a short summary of the description, but is not an "additional" requirement.

   This means for example that the word "shall" is not allowed in the title for all diagram.

.. gd_req:: Diagram attribute: security
   :id: gd_req__impl_diagram_security
   :status: valid
   :tags: manual_prio_2, attribute, mandatory
   :satisfies: wf__sw_detailed_design

   Each diagram shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Diagram attribute: safety
   :id: gd_req__impl_diagram_safety
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall have a automotive safety integrity level (ASIL) identifier:

      * QM
      * ASIL_B

.. gd_req:: Diagram attribute: status
   :id: gd_req__impl_diagram_status
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall have a status:

      * valid
      * invalid

.. gd_req:: Diagram attribute: description
   :id: gd_req__impl_diagram_description
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall have a description. The description shall provide a needarch or image of the diagram.

.. _detailed_design_linkage:

Diagram Linkage
'''''''''''''''

.. gd_req:: Diagram Linkage check Component Requirement
   :id: gd_req__impl_diagram_check_req
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be linked to the corresponding component requirement via the attribute implements.

.. gd_req:: Diagram Linkage Component Requirement
   :id: gd_req__impl_diagram_linkage_req
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be automatically linked (inverse direction) to the corresponding component requirement via the "implemented by" linkage.

.. gd_req:: Diagram Linkage check Component Architecture
   :id: gd_req__impl_diagram_check_arch
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be linked to the corresponding component architecture via the attribute satisfies.

.. gd_req:: Diagram Linkage Component Architecture
   :id: gd_req__impl_diagram_linkage_arch
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be automatically linked (inverse direction) to the corresponding component architecture via the "satisfied by" linkage.

.. gd_req:: Diagram Linkage check Component ID
   :id: gd_req__impl_diagram_check_id
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be linked to the corresponding component id via the attribute belongs_to.

.. gd_req:: Diagram Linkage Component ID
   :id: gd_req__impl_diagram_linkage_id
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be automatically linked (inverse direction) to the corresponding component id via the "belongs by" linkage.

.. gd_req:: Diagram Linkage includes
   :id: gd_req__impl_diagram_check_includes
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be linked to the corresponding
   - SW Unit
   - SW Unit Interface
   via the attribute includes.

.. gd_req:: Diagram Linkage includes
   :id: gd_req__impl_diagram_linkage_includes
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each diagram shall be automatically linked (inverse direction) to the corresponding
   - SW Unit
   - SW Unit Interface
   via the "included by" linkage.

Diagram Checks
''''''''''''''

.. gd_req:: Diagram mandatory attributes provided
   :id: gd_req__impl_diagram_mandatory
   :status: valid
   :tags: prio_2_automation, attribute, check
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   It shall be checked if all mandatory attributes for each diagram are provided by the user. For all diagrams following attributes shall be mandatory:

   .. needtable:: Overview mandatory Diagram attributes
      :filter: "mandatory" in tags and "attribute" in tags and "implementation" in tags and type == "gd_req"
      :style: table
      :columns: title
      :colwidths: 30

Unit Attributes
---------------

.. gd_req:: Unit attribute: UID
   :id: gd_req__impl_unit_uid
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :satisfies: wf__sw_detailed_design
   :complies: std_req__iso26262__software_843, std_req__aspice_40__SWE-3-BP1

   Each unit shall have a unique ID. It shall consist of three parts:

      * type of unit
      * structural element
      * keyword describing the content of the unit

   Consider the project's naming convention.

.. gd_req:: Unit attribute: description
   :id: gd_req__impl_unit_description
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each unit shall have a description.

Unit Linkage
''''''''''''

.. gd_req:: Unit Linkage check Component ID
   :id: gd_req__impl_unit_check_id
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each unit shall be linked to the corresponding component id via the attribute belongs_to.

.. gd_req:: Unit Linkage Component ID
   :id: gd_req__impl_unit_linkage_id
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each unit shall be automatically linked (inverse direction) to the corresponding component id via the "belongs by" linkage.

Interface Attributes
--------------------

.. gd_req:: Interface attribute: UID
   :id: gd_req__impl_interface_uid
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :satisfies: wf__sw_detailed_design
   :complies: std_req__iso26262__software_843, std_req__aspice_40__SWE-3-BP1

   Each interface shall have a unique ID. It shall consist of three parts:

      * type of interface
      * structural element
      * keyword describing the content of the interface

   Consider the project's naming convention.

.. gd_req:: Interface attribute: description
   :id: gd_req__impl_interface_description
   :status: valid
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each interface shall have a description.

Interface Linkage
'''''''''''''''''

.. gd_req:: Interface Linkage check SW Unit ID
   :id: gd_req__impl_interface_check_id
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each interface shall be linked to the corresponding SW Unit id via the attribute belongs_to.

.. gd_req:: Interface Linkage SW Unit ID
   :id: gd_req__impl_interface_linkage_id
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each interface shall be automatically linked (inverse direction) to the corresponding SW Unit id via the "belongs by" linkage.

.. gd_req:: Interface Linkage check Architecture
   :id: gd_req__impl_interface_check_req
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each interface shall be linked to the corresponding architecture via the attribute implements.

.. gd_req:: Interface Linkage Architecture
   :id: gd_req__impl_interface_linkage_req
   :status: valid
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425
   :satisfies: wf__sw_detailed_design

   Each interface shall be automatically linked (inverse direction) to the corresponding architecture via the "implemented by" linkage.

Dependency Analysis
'''''''''''''''''''

.. gd_req:: Dependency Analysis
   :id: gd_req__impl_dependency_analysis
   :status: valid
   :tags: prio_2_automation
   :satisfies: wf__sw_verify_implementation
   :complies: std_req__iso26262__software_942

   For each component a dependency tree view shall be created to support design inspection and Safety Analysis.
   It shall show the libraries used by the component (i.e. which libraries are linked to the component, defined as CI build tool target) up to the leaves of the tree.

.. needextend:: docname is not None and "process_areas/implementation" in docname
   :+tags: implementation
