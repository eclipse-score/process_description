# Example for Requirements review

Edit the verdicts, rationales, and findings in these tables. Keep the
requirement/checklist IDs and table headers unchanged. Missing context
is not a pass. Return to Chat when ready; editing is not approval.

## `feat_req__baselibs__utils_library`

Utils Library

### Checklist

| Check | Verdict | Rationale |
| --- | --- | --- |
| REQ_01_01 | yes | The requirement text uses the required formulation template: "The base libraries shall provide a utils library ...". |
| REQ_02_01 | yes | The description is comprehensible: it names a concrete deliverable (a utils library) and enumerates its contained capabilities in plain language. |
| REQ_02_02 | yes | The qualifier "general-purpose" is a non-binding descriptive phrase, but the enumerated list (Base64 encoding/decoding, scoped operations, string views, safe integer arithmetic, safe atomic operations, defined program termination handling) grounds the scope with concrete, unambiguous items. |
| REQ_02_03 | no | Six distinct capabilities (Base64 encoding/decoding, scoped operations, string views, safe integer arithmetic, safe atomic operations, program termination handling) are bundled into a single requirement. Each is independently verifiable and could fail or pass separately, which is a multi-part rather than atomic statement. Grouping them under one feature-level "utils library" umbrella may be a readability choice, but it is not explicitly justified as such in the supplied text. |
| REQ_02_04 | yes | All listed capabilities (Base64 codec, scoped operations, string views, safe integer/atomic operations, termination handling) are well-established, commonly implemented techniques; nothing in the text suggests infeasibility. |
| REQ_02_05 | yes | The capabilities are described functionally (what the library provides) rather than by naming a specific internal implementation approach, algorithm, or class design. |
| REQ_03_01 | n/a | Only parent requirement IDs are supplied (stkh\_req\_\_functional\_req\_\_base\_libraries[version==1], stkh\_req\_\_dependability\_\_automotive\_safety[version==1]); no parent requirement text was provided. Correctness of the linkage content cannot be assessed from IDs alone, and parent content must not be inferred from the ID. |
| REQ_04_01 | n/a | No contradiction was found against the other three requirements supplied in this run. External consistency against the full baselibs requirement baseline or other feature sets cannot be assessed because that material was not supplied. |
| REQ_05_01 | n/a | Nothing in the text indicates timing or real-time constraints apply to these utility functions (encoding, scoped operations, string views, safe arithmetic); timing does not appear relevant to this requirement. |
| REQ_06_01 | no | The requirement names capabilities (e.g., Base64 encoding/decoding implies byte/string input-output) but does not describe external interfaces or input/output data types/formats for any of the listed utilities. |
| REQ_07_01 | n/a | A safety attribute value (ASIL\_B) is present on the requirement, but no justification or supporting evidence for that classification was supplied in the input; this cannot be assessed as present/absent evidence rather than concluding it is unjustified. |
| REQ_07_02 | n/a | A security attribute value (YES) is present on the requirement, but no justification or supporting evidence for that classification was supplied in the input. |
| REQ_08_01 | yes | Each listed capability is independently testable with unit tests (e.g., round-trip Base64 encode/decode, string view behavior, integer/atomic overflow and wraparound handling, termination behavior checks). |
| REQ_08_02 | n/a | Not applicable: the requirement is verifiable by testing (see REQ\_08\_01), so the design/code-review fallback for untestable requirements does not apply. |
| REQ_09_01 | n/a | This requirement describes general-purpose utility functionality, not a safety mechanism with a defined error-detection/reaction behavior, so this checklist item does not apply. |
| REQ_10_01 | n/a | Completeness relative to parent and related requirements cannot be assessed because parent requirement text was not supplied, only IDs. |

### Findings

| Check | Severity | Description | Suggestion |
| --- | --- | --- | --- |
| REQ\_02\_03 | minor | The requirement bundles six independently verifiable utility capabilities (Base64 codec, scoped operations, string views, safe integer arithmetic, safe atomic operations, program termination handling) into a single requirement statement. | Consider splitting into separate child requirements per capability (or explicitly document the grouping as a justified readability exception) to allow independent pass/fail tracking and verification. |
| REQ\_06\_01 | minor | External interfaces and input/output data (e.g., expected data types for Base64 encode/decode, string view semantics) are not described. | Add or reference interface/API details (data types, pre/post-conditions) for each listed capability, e.g. in a linked interface specification. |

## `feat_req__baselibs__multi_language_apis`

Multi-Language APIs

### Checklist

| Check | Verdict | Rationale |
| --- | --- | --- |
| REQ_01_01 | yes | The requirement uses the required formulation template: "The base libraries shall provide APIs for C++, Rust, or both ...". |
| REQ_02_01 | yes | The description is comprehensible: it states that APIs are provided for C++, Rust, or both, based on consumer needs. |
| REQ_02_02 | no | The clause "depending on the requirements of consuming platform components" does not state who decides this or by what criteria, leaving the condition for choosing C++, Rust, or both open to interpretation. |
| REQ_02_03 | yes | The requirement expresses a single, atomic statement about API language availability driven by consumer needs. |
| REQ_02_04 | yes | Providing C++ and/or Rust APIs is a feasible, commonly implemented engineering practice. |
| REQ_02_05 | yes | Naming C++ and Rust is the subject matter of this requirement (API language availability) rather than an internal implementation detail of how functionality is achieved, so this is a justified exception to implementation independence. |
| REQ_03_01 | n/a | Only parent requirement IDs are supplied (functional\_req\_base\_libraries, dev\_experience\_prog\_languages, dependability\_automotive\_safety); no parent text was provided to verify correctness of the linkage content. |
| REQ_04_01 | n/a | No contradiction was found against the other three supplied requirements. External consistency against material not supplied cannot be assessed. |
| REQ_05_01 | n/a | Nothing in the text suggests timing constraints are relevant to API language availability. |
| REQ_06_01 | yes | The requirement's entire subject is the external interface surface (language bindings for consumers); at feature level this is an appropriate consideration of external interfaces, with detailed data contracts expected to be deferred to component-level interface specifications. |
| REQ_07_01 | n/a | A safety attribute value (ASIL\_B) is present, but no justification or supporting evidence for that classification was supplied. |
| REQ_07_02 | n/a | A security attribute value (YES) is present, but no justification or supporting evidence for that classification was supplied. |
| REQ_08_01 | yes | Verifiable by tests, e.g. confirming the C++ and/or Rust API surfaces exist, compile, and can be called by representative consuming components. |
| REQ_08_02 | n/a | Not applicable: the requirement is verifiable by testing, so the design/code-review fallback does not apply. |
| REQ_09_01 | n/a | This requirement describes API language availability, not a safety mechanism with defined error-reaction behavior. |
| REQ_10_01 | n/a | Completeness relative to parent and related requirements cannot be assessed because parent requirement text was not supplied, only IDs. |

### Findings

| Check | Severity | Description | Suggestion |
| --- | --- | --- | --- |
| REQ\_02\_02 | minor | The decision criterion for choosing C++, Rust, or both ("depending on the requirements of consuming platform components") is not defined, nor is the responsible party for making that determination. | State who determines the API language choice and on what basis (e.g., a per-component configuration or a referenced decision record). |

## `feat_req__baselibs__result_library`

Result Library

### Checklist

| Check | Verdict | Rationale |
| --- | --- | --- |
| REQ_01_01 | yes | The requirement uses the required formulation template: "The base libraries shall provide error handling mechanisms ...". |
| REQ_02_01 | yes | The description is comprehensible: it states the library provides error handling that avoids reliance on C++ exceptions. |
| REQ_02_02 | no | The term "error handling mechanisms" is not defined concretely; it does not state whether this refers to a Result/Expected type, error codes, status objects, or another approach, leaving the mechanism open to multiple interpretations. |
| REQ_02_03 | yes | The requirement expresses a single atomic statement: exception-free error handling support. |
| REQ_02_04 | yes | Exception-free error handling (e.g., Result/Expected-style types) is a well-established, feasible pattern, particularly common in safety-critical C++ guidance. |
| REQ_02_05 | yes | Excluding reliance on C++ exceptions is a functional/safety constraint on the capability being requested, not a description of internal implementation, and is a common safety-related coding restriction rather than an implementation detail. |
| REQ_03_01 | n/a | Only parent requirement IDs are supplied; no parent text was provided to verify correctness of the linkage content. |
| REQ_04_01 | n/a | No contradiction was found against the other three supplied requirements. External consistency against material not supplied cannot be assessed. |
| REQ_05_01 | n/a | Nothing in the text indicates timing constraints are relevant to this error handling capability. |
| REQ_06_01 | no | The requirement does not describe the external interface shape of the error handling mechanism (e.g., function/return signatures, how errors propagate across module boundaries). |
| REQ_07_01 | n/a | A safety attribute value (ASIL\_B) is present, but no justification or supporting evidence for that classification was supplied. |
| REQ_07_02 | n/a | A security attribute value (YES) is present, but no justification or supporting evidence for that classification was supplied. |
| REQ_08_01 | yes | Verifiable by tests, e.g. confirming error paths propagate without throwing C++ exceptions and that error states are correctly represented and checked. |
| REQ_08_02 | n/a | Not applicable: the requirement is verifiable by testing, so the design/code-review fallback does not apply. |
| REQ_09_01 | n/a | This requirement provides general-purpose error handling infrastructure; it does not itself specify an error reaction leading to a safe state or repair, though it may underpin safety mechanisms defined elsewhere. |
| REQ_10_01 | n/a | Completeness relative to parent and related requirements cannot be assessed because parent requirement text was not supplied, only IDs. |

### Findings

| Check | Severity | Description | Suggestion |
| --- | --- | --- | --- |
| REQ\_02\_02 | minor | "Error handling mechanisms" is not defined concretely, leaving the specific approach (e.g., Result/Expected type vs. error codes) open to interpretation. | Name the specific mechanism(s) the library provides (e.g., a Result&lt;T, E&gt; type) or reference a design document that defines it. |
| REQ\_06\_01 | minor | The external interface shape of the error handling mechanism (signatures, propagation across boundaries) is not described. | Add or reference interface details describing how callers construct, propagate, and inspect error results. |

## `feat_req__baselibs__memory_library`

Memory Library

### Checklist

| Check | Verdict | Rationale |
| --- | --- | --- |
| REQ_01_01 | yes | The requirement uses the required formulation template: "The base libraries shall provide a memory management library ...". |
| REQ_02_01 | yes | The description is comprehensible: it enumerates concrete memory-management capabilities in plain language. |
| REQ_02_02 | yes | The listed terms (shared memory operations, polymorphic memory resources, position-independent pointers, endianness conversion, inter-process synchronization mechanisms) are concrete and well-understood in the domain, limiting ambiguity. |
| REQ_02_03 | no | Five distinct capabilities (shared memory operations, polymorphic memory resources, position-independent pointers, endianness conversion, inter-process synchronization mechanisms) are bundled into a single requirement, each independently verifiable. |
| REQ_02_04 | yes | All listed capabilities are established techniques with known implementation approaches; nothing suggests infeasibility. |
| REQ_02_05 | no | "Polymorphic memory resources" names a specific C++ standard library design pattern (std::pmr) rather than describing the functional need in implementation-independent terms, which ties the requirement to a particular technology/idiom. |
| REQ_03_01 | n/a | Only parent requirement IDs are supplied; no parent text was provided to verify correctness of the linkage content. |
| REQ_04_01 | n/a | No contradiction was found against the other three supplied requirements. External consistency against material not supplied cannot be assessed. |
| REQ_05_01 | no | Inter-process synchronization mechanisms typically carry timing-relevant properties (e.g., bounded waiting, deadlock/priority-inversion avoidance), which are especially pertinent for an ASIL\_B context, but no timing considerations are addressed in the text. |
| REQ_06_01 | yes | The requirement inherently addresses external/cross-boundary interface concerns: shared memory operations, endianness conversion (cross-format data interchange), and inter-process synchronization are all about data crossing process boundaries. |
| REQ_07_01 | n/a | A safety attribute value (ASIL\_B) is present, but no justification or supporting evidence for that classification was supplied. |
| REQ_07_02 | n/a | A security attribute value (YES) is present, but no justification or supporting evidence for that classification was supplied. |
| REQ_08_01 | yes | Each listed capability is independently testable (e.g., shared memory round-trip tests, allocator behavior tests, pointer rebasing tests, endianness conversion correctness tests, synchronization primitive tests). |
| REQ_08_02 | n/a | Not applicable: the requirement is verifiable by testing, so the design/code-review fallback does not apply. |
| REQ_09_01 | n/a | This requirement describes memory-management infrastructure capabilities; it does not itself specify an error reaction leading to a safe state or repair, though it may underpin safety mechanisms defined elsewhere. |
| REQ_10_01 | n/a | Completeness relative to parent and related requirements cannot be assessed because parent requirement text was not supplied, only IDs. |

### Findings

| Check | Severity | Description | Suggestion |
| --- | --- | --- | --- |
| REQ\_02\_03 | minor | The requirement bundles five independently verifiable memory-management capabilities into a single requirement statement. | Consider splitting into separate child requirements per capability (or explicitly document the grouping as a justified readability exception) to allow independent pass/fail tracking and verification. |
| REQ\_02\_05 | observation | "Polymorphic memory resources" names a specific C++ standard library mechanism (std::pmr) rather than an implementation-independent functional need. | Consider rephrasing in functional terms (e.g., "support for custom/pluggable memory allocators") unless tying the requirement to this specific C++ idiom is intentional and justified. |
| REQ\_05\_01 | minor | Timing properties relevant to inter-process synchronization (e.g., bounded waiting, deadlock avoidance) are not addressed. | State the required timing/determinism properties for the synchronization mechanisms, or reference a timing requirement that covers this. |
