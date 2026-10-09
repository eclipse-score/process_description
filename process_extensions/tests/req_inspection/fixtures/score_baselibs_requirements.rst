..
   Public S-CORE baselibs feature requirements, retained as a demonstration snapshot.
   Source: https://eclipse-score.github.io/score/main/features/baselibs/requirements/index.html
   These are example inputs, not independently validated expected inspection results.

.. feat_req:: Utils Library
   :id: feat_req__baselibs__utils_library
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0
   :tags: inspected

   The base libraries shall provide a utils library with general-purpose utility
   functionality, including Base64 encoding and decoding, scoped operations,
   string views, safe integer arithmetic, safe atomic operations, and defined
   program termination handling.

.. feat_req:: Multi-Language APIs
   :id: feat_req__baselibs__multi_language_apis
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dev_experience__prog_languages[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0
   :tags: inspected

   The base libraries shall provide APIs for C++, Rust, or both, depending on
   the requirements of consuming platform components.

.. feat_req:: Result Library
   :id: feat_req__baselibs__result_library
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0
   :tags: inspected

   The base libraries shall provide error handling mechanisms that enable
   development without relying on C++ exceptions.

.. feat_req:: Memory Library
   :id: feat_req__baselibs__memory_library
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :derived_from: stkh_req__functional_req__base_libraries[version==1], stkh_req__dependability__automotive_safety[version==1]
   :satisfied_by: feat__baselibs[version==1]
   :status: valid
   :version: 2
   :valid_from: v1.0.0
   :tags: inspected

   The base libraries shall provide a memory management library that includes
   utilities for shared memory operations, polymorphic memory resources,
   position-independent pointers, endianness conversion, and inter-process
   synchronization mechanisms.
