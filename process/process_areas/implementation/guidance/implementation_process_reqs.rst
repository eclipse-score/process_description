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

Please notice, that detail design description files (within MarkDown or RestructuredText) are optional.
Also diagrams are optional, but if they are created, they shall have the following attributes to ensure consistency and traceability.

.. gd_req:: Static Diagram for Unit Interactions
   :id: gd_req__impl_static_diagram
   :status: valid
   :version: 1
   :tags: manual_prio_1, mandatory
   :satisfies: wf__sw_detailed_design[version==1]
   :complies: std_req__iso26262__software_843[version==1],
              std_req__iso26262__software_844[version==1],
              std_req__iso26262__software_845[version==1],
              std_req__aspice_40__SWE-3-BP1[version==1]

   The static diagram shall represent the units and their relationships using UML notations.

Diagram Attributes
------------------

.. gd_req:: Diagram attribute: UID
   :id: gd_req__impl_diagram_uid
   :status: valid
   :version: 1
   :tags: manual_prio_1, attribute, mandatory
   :satisfies: wf__sw_detailed_design[version==1]
   :complies: std_req__iso26262__software_843[version==1],
              std_req__iso26262__software_844[version==1],
              std_req__iso26262__software_845[version==1],
              std_req__aspice_40__SWE-3-BP2[version==1]

   Each diagram shall have a unique identifier (UID) (realized by its file name). It shall consist of three parts:

   * type of diagram
   * structural element
   * keyword describing the content of the diagram

   Consider the project's naming convention.

.. gd_req:: Diagram attribute: title
   :id: gd_req__impl_diagram_title
   :status: valid
   :version: 1
   :tags: manual_prio_1 attribute, mandatory
   :satisfies: wf__sw_detailed_design[version==1]
   :complies: std_req__iso26262__software_843[version==1],
              std_req__iso26262__software_844[version==1],
              std_req__iso26262__software_845[version==1],
              std_req__aspice_40__SWE-3-BP3[version==1],
              std_req__aspice_40__SWE-3-BP4[version==1]

   The title of the diagram shall provide a short summary of the description, but is not an "additional" requirement.

   This means for example that the word "shall" is not allowed in the title for all diagram.

.. gd_req:: Diagram attribute: description
   :id: gd_req__impl_diagram_description
   :status: valid
   :version: 1
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421[version==1], std_req__iso26262__support_6425[version==1]
   :satisfies: wf__sw_detailed_design[version==1]

   Each diagram shall have a description.

.. _detailed_design_linkage:

Diagram Linkage
'''''''''''''''

.. gd_req:: Diagram Linkage check Component ID
   :id: gd_req__impl_diagram_check_id
   :status: valid
   :version: 1
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421[version==1], std_req__iso26262__support_6425[version==1]
   :satisfies: wf__sw_detailed_design[version==1]

   Each diagram shall be linked to the corresponding component id via the attribute belongs_to.

.. gd_req:: Diagram Linkage Component ID
   :id: gd_req__impl_diagram_linkage_id
   :status: valid
   :version: 1
   :tags: prio_2_automation, attribute, automated
   :complies: std_req__iso26262__support_6421[version==1], std_req__iso26262__support_6425[version==1]
   :satisfies: wf__sw_detailed_design[version==1]

   Each diagram shall be automatically linked (inverse direction) to the corresponding component id via the "belongs by" linkage.


Diagram Checks
''''''''''''''

.. gd_req:: Diagram mandatory consistency
   :id: gd_req__impl_diagram_consistency
   :status: valid
   :version: 2
   :tags: prio_3_automation, attribute, check
   :complies: std_req__iso26262__support_6421[version==1], std_req__iso26262__support_6425[version==1]
   :satisfies: wf__sw_detailed_design[version==1]

   It shall be checked if all diagrams are consistent with the source code and the design principles
   outlined in the development plan. This includes checking that the naming of the units, their
   interfaces and functions in any diagrams or descriptions matches the naming in the source code to ensure traceability.
   That means the diagrams and descriptions should not be outdated and be consistent with
   the source code and not introduce new terminology or concepts that are not present in the code.

Unit Attributes
---------------

.. gd_req:: Unit attribute: UID
   :id: gd_req__impl_unit_uid
   :status: valid
   :version: 1
   :tags: manual_prio_1, attribute, mandatory
   :satisfies: wf__sw_detailed_design[version==1]
   :complies: std_req__iso26262__software_843[version==1], std_req__aspice_40__SWE-3-BP1[version==1]

   Each unit shall have a unique ID. It is build by the path and file name(s) of the unit within the component and following a consistent naming convention. The name should be descriptive and reflect
   the functionality of the unit to ensure traceability and understandability.

   The naming convention should be defined in the project guidelines and consistently applied across all units.

.. gd_req:: Unit attribute: description
   :id: gd_req__impl_unit_description
   :status: valid
   :version: 1
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421[version==1], std_req__iso26262__support_6425[version==1]
   :satisfies: wf__sw_detailed_design[version==1]

   Each unit shall have a description in the source code.

Interface Attributes
--------------------

.. gd_req:: Interface attribute: UID
   :id: gd_req__impl_interface_uid
   :status: valid
   :version: 1
   :tags: manual_prio_1, attribute, mandatory
   :satisfies: wf__sw_detailed_design[version==1]
   :complies: std_req__iso26262__software_843[version==1], std_req__aspice_40__SWE-3-BP1[version==1]

   Each interface shall have a unique ID, which is defined by the path and file name(s)
   of the interface within the component and the namespace and name of the interface inside the file.
   The name should be descriptive and reflect the functionality of the interface to ensure
   traceability and understandability.

   Consider the project's naming convention.

.. gd_req:: Interface attribute: description
   :id: gd_req__impl_interface_description
   :status: valid
   :version: 1
   :tags: manual_prio_1, attribute, mandatory
   :complies: std_req__iso26262__support_6421[version==1], std_req__iso26262__support_6425[version==1]
   :satisfies: wf__sw_detailed_design[version==1]

   Each interface shall have a description in the source code if the source code does not
   already provide sufficient information. It should provide a clear and comprehensive explanation
   of the interface's purpose, its inputs and outputs, and how it interacts with other units
   or components. The description should be sufficient to allow users of the interface
   to understand how to interact with it without needing   to read the implementation details.
   It should also include any relevant information about the expected behavior, constraints,
   and any assumptions made in the design of the interface. The documentation should be
   maintained and updated as the implementation evolves to ensure it remains accurate and useful.

Dependency Analysis
'''''''''''''''''''

.. gd_req:: Dependency Analysis
   :id: gd_req__impl_dependency_analysis
   :status: valid
   :version: 1
   :tags: prio_2_automation
   :satisfies: wf__sw_verify_implementation[version==1]
   :complies: std_req__iso26262__software_942[version==1]

   For each component a dependency tree view shall be created to support design inspection and Safety Analysis.
   It shall show the libraries used by the component (i.e. which libraries are linked to the component,
   defined as CI build tool target) up to the leaves of the tree.

.. needextend:: docname is not None and "process_areas/implementation" in docname
   :+tags: implementation

.. _impl_process_requirements_complexity:

Complexity Analyses
'''''''''''''''''''

.. gd_req:: Design Complexity Analysis
   :id: gd_req__impl_complexity_analysis
   :status: valid
   :version: 1
   :tags: prio_3_automation, model, check
   :complies: std_req__iso26262__software_743[version==1], std_req__aspice_40__SWE-3-BP3[version==1]

   A complexity analysis for the components shall be performed by automated tool support. It shall consider appropriate code metrics like lines of code, cyclomatic complexity, number of public interfaces, number of parameters and so on. The results of the analysis shall be documented in the SW Verification Report. As default an exceeds of the following limits shall be reported for the complexity measures (ASIL B / QM):

   * Lines of Code per function: 100 / 200

   * Lines of Code per file : 2000 / 4000

   * Cyclomatic complexity per function: 10 / 20

   * Number of parameters per function: 5 / 7

   * Number of public interfaces per component: 3 / 10

   The project may specify own limits for the complexity measures in the project guidelines, if there is a rationale for deviating from the default limits.
   Therefore the tooling shall support configuration of the limits globally for the project and per component, if the component wants to use own lower (more strict) limits.
