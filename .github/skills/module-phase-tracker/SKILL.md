---
name: module-phase-tracker
description: "Update the Feature and Process Status table in feature_and_process_status.rst. Use when: checking module status, updating feature status tracker, refreshing work product status, deriving completion status from eclipse-score GitHub repos for Baselibs, Communication, Logging, Orchestrator, Persistency, Time, Config Management, Lifecycle, Security/Crypto."
argument-hint: "optional: module name or 'all'"
---

# Feature and Process Status

Derives and updates the completion status table in
`process/standards/feature_and_process_status.rst` by querying the live eclipse-score GitHub repositories.

## When to Use

- Refresh the tracker table with current data
- After a sprint/release to check progress
- When a module team reports a deliverable is done

## RST File Structure

`feature_and_process_status.rst` consists of a file header followed by 5 Process Area sections. Each section has this exact pattern:

```rst
Process Area N — <Name>
***********************

<Description paragraph.>
<Work products line (optional).>
See :ref:`<workflow_ref>`.

.. rubric:: Process Status

.. list-table::
   :header-rows: 1
   :class: compact-overview-table

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and '<tag>' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and '<tag>' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and '<tag>' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and '<tag>' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(<tag>)
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(<tag>)

.. rubric:: Implementation status: 🔄 NN% (X/Y deliverables complete)

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: module-phase-tracker-table

   * - **Module**
     - **<Deliverable 1>**
     - **<Deliverable 2>**

   * - <Module name>
     - <status>
     ...
```

**Important rules:**
- `.. needpie::` does **NOT** support a `:title:` option — omit it entirely (causes build errors)
- The pie chart table uses CSS class `compact-overview-table`; each cell needs `.. rst-class:: small-pie-cell` before its `.. needpie::`
- The module tracker table uses CSS class `module-phase-tracker-table`
- Both `.. rubric::` directives are plain inline text — NOT RST section headings
- The `.. rubric:: Implementation status:` line is computed (see Step 4 in Procedure) and placed directly before the module tracker table

| Process Area | sphinx-needs tag |
|---|---|
| PA 1 — Change Management | `change_management` |
| PA 2 — Requirements Engineering | `requirements_engineering` |
| PA 3 — Architecture Design | `architecture_design` |
| PA 4 — Implementation | `implementation` |
| PA 5 — Verification | `verification` |

The pie chart diagrams are computed live by sphinx-needs at build time — they **never need manual updates**. Only update the filter `<tag>` when adding a new Process Area.

## Modules and Repos

> **IMPORTANT**: Each module has its own dedicated repo in the `eclipse-score` GitHub org AND content in `eclipse-score/score`. **Always check BOTH** the module's own repo and `eclipse-score/score` when counting needs elements. Never rely on `eclipse-score/score` alone.

| Module | Own Repo (always check!) | Docs in `eclipse-score/score` |
|---|---|---|
| Baselibs | `eclipse-score/baselibs` (no sphinx-needs RST so far) | `docs/modules/baselibs/**`, `docs/features/baselibs/docs` |
| Communication | `eclipse-score/communication` (no sphinx-needs RST so far) | `docs/modules/communication/**`, `docs/features/communication/docs` |
| Logging | `eclipse-score/logging` (no sphinx-needs RST so far) | `docs/modules/logging/**`, `docs/features/analysis-infra/logging/docs` |
| Orchestrator | `eclipse-score/lifecycle` — has `docs/module/health_monitor/` with comp_req/comp_arc | `docs/modules/orchestrator/**`, `docs/features/orchestration` |
| Persistency | `eclipse-score/persistency` — has `docs/persistency/kvs/` with comp_req/comp_arc ✅ | `docs/features/persistency` |
| Time | `eclipse-score/inc_time` (no sphinx-needs RST so far) | `docs/features/time/docs` |
| Config Management | `eclipse-score/config_management` (no sphinx-needs RST so far) | `docs/features/configuration` |
| Lifecycle | `eclipse-score/lifecycle` — has `docs/module/health_monitor/` (comp_arc_sta/dyn valid=15/16), `detailed_design/` (dd_sta/dyn valid=1/2), `tests/integration/` | `docs/modules/lifecycle/index.rst`, `docs/features/lifecycle/**` |
| Security/Crypto | `eclipse-score/inc_security_crypto` — `src/` has no implementation yet; `docs/index.rst` with stkh_req | `docs/features/security_crypto/**` |

**How to search all repos for a module:**
```python
for repo in ["eclipse-score/score", "eclipse-score/<module_own_repo>"]:
    files = [p for p in get_tree(repo) if p.endswith(".rst") and "<relevant_path>" in p]
    for f in files:
        v, t = count_needs_in_file(repo, f)
```

## Status Format

- **``✅ Available (valid/total)``** — Artifact complete and approved: **100% of needs elements are `valid`** (valid == total). Always add the count in parentheses for requirements and architecture rows.
- **``🔄 NN% (valid/total)``** — In Progress: at least one element is `valid` but not all. Always show count.
- **``❌ Open``** — Not started, not found, or 0% valid
- For binary rows (Code, SW Development Plan, Unit Tests, CR approved): no count needed, just ``✅ Available`` or ``❌ Open``

**Percentage calculation per deliverable:**
- **Feature Req / Feature Arch**: count individual needs elements (e.g. `.. feat_req::`, `.. feat_arc::`) inside the doc with `:status: valid`; `valid / total`; 100% (valid == total) → ✅ Available
- **Comp. Req / Comp. Arch**: count individual needs elements across all component docs; `valid / total`; 100% (valid == total) → ✅ Available
- **Req. Inspection / Arch. Inspection**: `valid / total` across all checklists (feature + component combined); 100% (valid == total) → ✅ Available
- **Detailed Design + Code / Impl. Inspection**: `valid / total` across all `chklst_impl_inspection.rst` / `chklst_dd_inspection.rst` files
- **Binary deliverables** (CR approved, SW Dev Plan, Unit Tests, Integration Tests, Verification Report): no percentage
- **Detailed Design + Code / Impl. Inspection**: `valid / total` across all `chklst_impl_inspection.rst` / `chklst_dd_inspection.rst` files
- **Binary deliverables** (CR approved, SW Dev Plan, Unit Tests, Integration Tests, Verification Report): no percentage

## Status Criteria (per Deliverable)

### Process Area 1 — CR approved
- **✅ Available**: A closed GitHub Issue with "Feature Request" or "Contribution Request" for the module exists in `eclipse-score/score`
- **❌ Open**: No such issue found

Known closed CRs: Baselibs (#549), Communication (#69), Logging (#68), Orchestrator (#273), Persistency (#95), Time (#910), Config Management (#754, #1764), Lifecycle (#909), Security/Crypto (#905)

### Process Area 2 — Feature Requirements
- **✅ Available**: 100% of individual needs elements (e.g. `.. feat_req::`) inside the requirements doc have `:status: valid`
- **🔄 NN%**: elements exist but not all are `valid`; show `valid / total` percentage. **This includes `🔄 0% (0/N)` when N elements exist but ALL are `:status: invalid` — do NOT use `❌ Open` in this case.**
- **❌ Open**: no requirements file found, OR zero needs elements found (file is empty/missing `feat_req::` directives)

> **Rule applies to ALL modules consistently**: if a requirements file exists and contains `.. feat_req::` directives (even if all are `:status: invalid`), always show `🔄 0% (0/N)` with a link to the file and a note that entries are all invalid. Never collapse to `❌ Open` when elements are present.

### Process Area 2 — Component Requirements
- **✅ Available**: 100% of all individual needs elements across all component requirements `.rst` files (not just `index.rst` — search all `.rst` files under `docs/modules/<module>/**/requirements/` and the module's own repo under `docs/module/**/requirements/`) have `:status: valid`
- **🔄 NN%**: elements exist but not all are `valid`; show `valid / total` percentage. **Includes `🔄 0% (0/N)` when ALL elements are `:status: invalid` — template placeholder files count as existing elements.**
- **❌ Open**: no component requirement files found, OR all found files contain zero `.. comp_req::` directives (pure template stubs without even a dummy directive)

> **Rule applies to ALL modules consistently**: template placeholder comp_req entries with `:status: invalid` still count as existing elements → show `🔄 0% (0/N)`, not `❌ Open`.

### Process Area 2 — Req. Inspection
- **✅ Available**: 100% of all `chklst_req_inspection.rst` files (feature + component level) have `:status: valid`
- **🔄 In Progress**: checklists exist but not all are `valid`
- **❌ Open**: no checklists found

### Process Area 3 — Feature Architecture
- **✅ Available**: 100% of individual needs elements (e.g. `.. feat_arc::`) inside the architecture doc have `:status: valid`
- **🔄 NN%**: elements exist but not all are `valid`; show `valid / total` percentage. **Includes `🔄 0% (0/N)` when all are `:status: invalid` — do NOT use `❌ Open` when elements exist.**
- **❌ Open**: no architecture file found, OR zero `.. feat_arc::` directives found

### Process Area 3 — Component Architecture
- **✅ Available**: 100% of all individual needs elements across all component architecture files have `:status: valid`
- **🔄 NN%**: elements exist but not all are `valid`; show `valid / total` percentage. **Includes `🔄 0% (0/N)` when all are `:status: invalid` — do NOT use `❌ Open` when elements exist.**
- **❌ Open**: no component architecture docs containing directives found

### Process Area 3 — Arch. Inspection
- **✅ Available**: 100% of all architecture checklists (`chklst_arc_inspection.rst` / `chklst_arch_inspection.rst`) have `:status: valid`
- **🔄 In Progress**: checklists exist but not all are `valid`
- **❌ Open**: no architecture checklists found

### Process Area 4 — SW Development Plan
- **✅ Available**: `eclipse-score/score` contains `docs/platform_management_plan/software_development.rst` (project-wide)
- **❌ Open**: file absent

### Process Area 4 — Code
- **✅ Available**: source files (`.cpp`, `.h`, `.py`, `.rs` etc.) exist in the module's own repo outside of `docs/`
- **❌ Open**: no source files found
- **Check**: `gh api repos/eclipse-score/<repo>/git/trees/main?recursive=1 --jq '.tree[].path'` then filter for source extensions, exclude `docs/`
- **NOTE**: All currently active modules (Baselibs, Communication, Logging, Orchestrator, Persistency, Time, Config Mgmt) have source code → all ✅ Available

### Process Area 4 — Detailed Design
- **✅ Available**: 100% of formal design doc needs elements (`.. dd_sta::`, `.. dd_dyn::`, `.. comp_dd::` or similar) in `detailed_design/` folders have `:status: valid`
- **🔄 NN%**: design docs exist and at least one element is `valid` but not all are `valid`; show `valid / total` %. **Includes `🔄 0% (0/N)` when all design elements are `:status: invalid` — do NOT use `❌ Open` when actual design directives are present.**
- **❌ Open**: no RST files with actual design directives found, OR all existing files contain only `:status: draft` wrapper `.. document::` directives (0 actual `dd_sta/dd_dyn` directives)
- **DO NOT count `chklst_impl_inspection.rst`** — those are inspection checklists, not design documents
- **DO NOT count bare `.. document::` wrapper files** — these are placeholders, not actual design content
- **Search both `eclipse-score/score` and the module's own repo** for `detailed_design/` folders

### Process Area 4 — Impl. Inspection
- **✅ Available**: 100% of `chklst_impl_inspection.rst` / `chklst_dd_inspection.rst` files have `:status: valid`
- **🔄 In Progress**: checklists exist but not all are `valid`
- **❌ Open**: no impl inspection checklists found

### Process Area 5 — Unit Tests
- **✅ Available**: Source repo contains `_test.cpp`, `_test.py`, or `/test(s)/` directories (excluding docs/)
- **❌ Open**: no test files found

### Process Area 5 — C0/C1 Coverage

Coverage data is sourced from the `reference_integration` CI (`Code Quality & Documentation` workflow, job `test_and_docs`).
It runs `bazel coverage --config=ferrocene-coverage` per module and extracts C0 (line) and C1 (branch) coverage via `genhtml`/`lcov` for C++ and `cargo llvm-cov` for Rust.

**Status criteria:**
- **✅ Available**: C0 ≥ 100% AND C1 ≥ 100% (practically never for real modules — use 🔄)
- **🔄 C0: XX% / C1: YY%**: Coverage data exists (regardless of %)
- **❌ Open**: Module not in reference_integration CI, or coverage extraction disabled

**How to fetch the latest values:**
```bash
# Find the latest successful run of the "Code Quality & Documentation" workflow (ID 234977097):
gh api "repos/eclipse-score/reference_integration/actions/workflows/234977097/runs?per_page=10" \
  --jq '.workflow_runs[] | select(.conclusion=="success") | {id: .id, created_at: .created_at}' | head -1

# Get the job ID for test_and_docs from that run:
RUN_ID=<run_id>
JOB_ID=$(gh api "repos/eclipse-score/reference_integration/actions/runs/$RUN_ID/jobs" \
  --jq '.jobs[] | select(.name=="test_and_docs") | .id')

# Extract the coverage summary from the job log:
gh api "repos/eclipse-score/reference_integration/actions/jobs/$JOB_ID/logs" \
  | grep -E "COVERAGE ANALYSIS SUMMARY|'score_.*_cpp'|'score_.*_rust'|lines|functions|branches" \
  | grep -A50 "COVERAGE ANALYSIS SUMMARY"
```

**Module → CI key mapping:**
| Tracker Module | CI key (CPP) | CI key (Rust) |
|---|---|---|
| Baselibs | `score_baselibs_cpp` | `score_baselibs_rust_rust` |
| Communication | `score_communication_cpp` | — (disabled) |
| Logging | `score_logging_cpp` | `score_logging_rust` |
| Orchestrator | — (disabled) | — (disabled) |
| Persistency | `score_persistency_cpp` | `score_persistency_rust` |
| Time | not in CI | — |
| Config Mgmt | not in CI | — |
| Lifecycle | `score_lifecycle_health_cpp` | `score_lifecycle_health_rust` |
| Security/Crypto | not in CI | — |

**Format in table:**
- CPP + Rust: `🔄 C0: 92.4% / C1: 60.4% (cpp)\n\nRust line: 74.4%`
- CPP only: `🔄 C0: 87.9% / C1: 58.8% (cpp)`
- Not available: `❌ Open`

### Process Area 5 — Comp. Integration Tests
- **✅ Available**: Source repo contains integration test source files (`.cpp`/`.py` with "integration" in path)
- **🔄 In Progress**: integration test CI workflow exists but no test source files
- **❌ Open**: no integration test artifacts

### Process Area 5 — Feature Integration Tests
- **🔄 In Progress**: `integration_test_scenarios` or `feature*test*` paths found in source repo
- **❌ Open**: none found

### Process Area 5 — Static Code Analysis

Static analysis CI exists at two levels:
1. **Per-module CI workflow** — zero-tolerance enforcement on `main` (clang-tidy for C++, Clippy for Rust). A passing CI implies 0 open findings.
2. **Central CodeQL** — runs in `eclipse-score/reference_integration` via `codeql-multiple-repo-scan.yml` across all pinned repos. Finding counts require the GitHub Security tab.

**Status criteria:**
- **`✅ 0 findings`**: A zero-tolerance CI workflow enforcing clang-tidy or Clippy exists in the module's own repo AND it passes on `main`. Link directly to the workflow file.
- **`🔄 Configured (...) but no CI enforcement workflow yet`**: Static analysis tools are configured in the repo (`.clang-tidy`, `static_analysis.bazelrc`, CodeQL config etc.) but no CI workflow enforces them on every PR/push. NOT `❌ Open` — the infrastructure exists.
- **`❌ Open`**: No static analysis configuration found at all in the module's own repo.

**Per-module static analysis status** (as of 2026-05):
| Module | Status | CI / Config link |
|---|---|---|
| Baselibs | `✅ 0 findings` | [clang-tidy lint.yml](https://github.com/eclipse-score/baselibs/blob/main/.github/workflows/lint.yml) |
| Communication | `🔄 Configured` | [static_analysis.bazelrc](https://github.com/eclipse-score/communication/blob/main/quality/static_analysis/static_analysis.bazelrc) + [CodeQL/MISRA](https://github.com/eclipse-score/communication/tree/main/quality/static_analysis) — no CI enforcement yet |
| Logging | `❌ Open` | — |
| Orchestrator | `✅ 0 findings` | [Clippy clippy.yml](https://github.com/eclipse-score/orchestrator/blob/main/.github/workflows/clippy.yml) |
| Persistency | `✅ 0 findings` | [Clippy clippy.yml](https://github.com/eclipse-score/persistency/blob/main/.github/workflows/clippy.yml) |
| Time | `❌ Open` | — |
| Config Mgmt | `✅ 0 findings` | [clang-tidy static-analysis.yml](https://github.com/eclipse-score/config_management/blob/main/.github/workflows/static-analysis.yml) |
| Lifecycle | `✅ 0 findings` | [Clippy lint_clippy.yml](https://github.com/eclipse-score/lifecycle/blob/main/.github/workflows/lint_clippy.yml) |
| Security/Crypto | `❌ Open` | — |

**Central CodeQL** (all modules): [codeql-multiple-repo-scan.yml](https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/codeql-multiple-repo-scan.yml) in `reference_integration`. Finding counts require the GitHub Security tab — not tracked per-cell.

### Process Area 5 — Dynamic Code Analysis

Dynamic analysis is performed via sanitizer CI workflows (Bazel `--config=asan_ubsan_lsan` for ASan/UBSan/LSan, `--config=tsan` for TSan). All workflows are zero-tolerance — a passing `main` branch implies 0 sanitizer findings.

**Status criteria:**
- **`✅ 0 findings`**: A zero-tolerance sanitizer CI workflow exists in the module's own repo AND it passes on `main`. Link directly to the workflow file(s).
- **`❌ Open`**: No sanitizer CI workflow found in the module's own repo.

> There is NO `🔄 Configured but not enforced` category for dynamic analysis — either a CI workflow runs and enforces sanitizers (✅) or it is absent (❌).

**Per-module dynamic code analysis status** (as of 2026-05):
| Module | Status | CI link(s) |
|---|---|---|
| Baselibs | `✅ 0 findings` | [sanitizers_linux.yml](https://github.com/eclipse-score/baselibs/blob/main/.github/workflows/sanitizers_linux.yml) — ASan+UBSan+LSan |
| Communication | `✅ 0 findings` | [ASan/UBSan/LSan](https://github.com/eclipse-score/communication/blob/main/.github/workflows/address_undefined_behavior_leak_sanitizer.yml), [TSan](https://github.com/eclipse-score/communication/blob/main/.github/workflows/thread_sanitizer.yml) |
| Logging | `❌ Open` | — |
| Orchestrator | `❌ Open` | — |
| Persistency | `❌ Open` | — |
| Time | `❌ Open` | — |
| Config Mgmt | `❌ Open` | — |
| Lifecycle | `❌ Open` | — |
| Security/Crypto | `❌ Open` | — |

**How to verify**: Check `.github/workflows/` in each module repo for workflows referencing `asan_ubsan_lsan`, `tsan`, `valgrind`, or similar sanitizer configs. Also check `reference_integration` workflows for cross-module sanitizer runs.

### Process Area 5 — Module Verification Report
- **✅ Available**: `verification/module_verification_report.rst` exists AND `:status: valid` **AND** the file contains actual verification data (test coverage lists, DFA results, static analysis results etc.) — not just section headings
- **🔄 In Progress**: file exists with `:status: draft`
- **❌ Open**: file does not exist, OR file is a template placeholder only (section headings with no content)
- **⚠ Consistency check**: A Module Verification Report can only be ✅ Available if all prerequisite Phase 5 deliverables (Unit Tests, Comp. Integration Tests, Feature Integration Tests) are also ✅ Available. If any prerequisite is ❌ Open, mark the report ❌ Open regardless of `:status:` in the file.
- **Known pitfall — Persistency**: `eclipse-score/persistency` has a `module_verification_report.rst` with `:status: valid` but it is an empty template. Feature Integration Tests are ❌ Open → report must be ❌ Open.

## Procedure

### Prerequisites
- `gh` CLI must be authenticated (`gh auth status`)
- Python 3.8+

### Steps

1. **Fetch the repo tree** for `eclipse-score/score` and module source repos:
   ```bash
   gh api repos/eclipse-score/score/git/trees/main?recursive=1 --jq '.tree[].path' > /tmp/tree_score.txt
   ```

2. **Count needs elements** in each requirements/architecture file using this pattern:
   ```python
   import re, base64, subprocess
   def count_needs_status(repo, path):
       content = base64.b64decode(
           subprocess.run(["gh", "api", f"repos/{repo}/contents/{path}",
                           "--jq", ".content"], capture_output=True, text=True).stdout.strip()
       ).decode()
       statuses = re.findall(r'^\s+:status:\s+(\w+)', content, re.MULTILINE)
       valid = sum(1 for s in statuses if s == 'valid')
       return valid, len(statuses)
   ```
   Aggregate `valid` and `total` across all files per deliverable.
   Percentage = `valid * 100 // total`. 100% (valid == total) → ✅ Available, else 🔄 NN%.

3. **Update the RST file** `process/standards/feature_and_process_status.rst`
   with the computed values.

4. **Compute the Implementation status per Process Area** and update the bold status line that appears directly before each table:
   - Count how many deliverable cells (across all modules × all deliverables in that Process Area) are `✅ Available`
   - `complete = number of ✅ Available cells`, `total = number of module × deliverable cells`
   - 100% → `✅ Available (total/total deliverables complete)`
   - >0% → `🔄 NN% (complete/total deliverables complete)`
   - 0% → `❌ Open (0/total deliverables complete)`
   - Format: `**Implementation status: 🔄 NN% (complete/total deliverables complete)**`
   - Binary rows (Code, SW Dev Plan, Unit Tests, CR): count each module cell as 1 deliverable
   - Do NOT include an Overall row inside the table — the status line is placed as plain text before the `.. list-table::` directive

5. **Adding a new module** — add a row to the Modules and Repos table above, define its `feature_path` and `docs_path`, then add a row to each tracker table (one `* - <Module name>` block per PA).

## Interpretation Notes

### Artifacts vs. Checklists — Key Rule
- **Artifacts** (Feature Requirements, Component Requirements, Feature Architecture, Component Architecture, Detailed Design, Code): derive status by **directly inspecting the repos** — look for sphinx-needs elements or source files. Do NOT rely on checklist presence/status.
- **Inspection rows** (Req. Inspection, Arch. Inspection, Impl. Inspection): these rows describe the checklists themselves — report what is found in `chklst_*.rst` files (how many exist, valid vs. draft). Computed as `valid / total` checklist files.

### Additional Notes
- **Requirements/Architecture rows**: count individual needs elements (`:status:` fields inside `.. feat_req::`, `.. feat_arc::`, `.. comp_req::`, `.. comp_arc_sta::`, `.. comp_arc_dyn::`, `.. real_arc_int::`, etc.) — NOT the document-level `:status:` field.
- **Code row**: source files outside of `docs/` in the module's own repo. All active modules currently ✅ Available.
- **Detailed Design row**: actual design directives (`.. dd_sta::`, `.. dd_dyn::`) in `detailed_design/` folders — not `chklst_impl_inspection.rst`, not bare `.. document::` wrappers.
- The SW Development Plan check is project-wide (not per-module) because S-CORE uses a single platform management plan.
- Verification report `status: valid` requires Committer approval in the PR merge.
- **Template vs. real report**: A file with `:status: valid` can still be an empty template. When checking `module_verification_report.rst`, look for actual content (tables, coverage numbers, test results) beyond section headings. If only headings are present, treat as ❌ Open even if `:status: valid`.
- **Phase 5 consistency**: The Module Verification Report cannot be complete if any prerequisite (Unit Tests, Integration Tests) is missing.

## Limitations

- Cannot detect whether requirements have 100% test coverage (needs needs.json analysis)
- **Static analysis findings**: Per-module CI enforcement workflows (clang-tidy/Clippy) are zero-tolerance — a passing `main` branch implies 0 findings. For `Communication` (configured but not enforced), finding counts are unknown without manual clang-tidy run.
- Central CodeQL finding counts require GitHub Security tab access — not available via `gh api` without special permissions.
- Feature integration tests heuristic is weak — manual verification recommended

## Complete RST Snapshot

Full content of `process/standards/feature_and_process_status.rst` as of last update.
Use this to recreate the file from scratch if needed.

```rst
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

Feature and Process Status
##########################

This page tracks the completion status of all 5 process areas per module.
Update the status column for each module after completing the respective deliverable.

**Process Status chart legend:**

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * - 🟢 Valid

       🟡 Draft

       🔴 Invalid

       ⬜ Other
     - 🟢 Ok

       🔵 Recommendation

       🟡 Open

       🟠 Action

       🔴 Deviation

       ⬜ N/A · ◻ Other
     - 🟢 Automated

       🟡 Waiting for automation

       🔵 Inspection list

       ⬜ Other

**Implementation Status Values:**

- ``✅ Available`` — Work product created, reviewed and approved
- ``🔄 NN%`` — In Progress: artifact exists with at least one valid element, percentage shows valid/total
- ``❌ Open`` — Not yet started, not found, or 0% valid
- ``—`` — Not applicable for this module

Process Area 1 — Change Management
***********************************

A Change Request must be created and approved by the Architecture Community before module development begins.
See :ref:`chm_change_workflows`.

.. rubric:: Process Status

.. list-table::
   :header-rows: 1
   :class: compact-overview-table

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'change_management' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'change_management' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'change_management' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'change_management' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(change_management)
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(change_management)

.. rubric:: Implementation status: ✅ Available (9/9 deliverables complete)

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: module-phase-tracker-table

   * - **Module**
     - **CR approved**

   * - Baselibs
     - ✅ Available

   * - Communication
     - ✅ Available

   * - Logging
     - ✅ Available

   * - Orchestrator
     - ✅ Available

   * - Persistency
     - ✅ Available

   * - Time
     - ✅ Available

   * - Config Mgmt
     - ✅ Available

   * - Lifecycle
     - ✅ Available

   * - Security/Crypto
     - ✅ Available

Process Area 2 — Requirements Engineering
*****************************************

Feature and component requirements must be written and inspected.
Work products: ``wp__requirements_feat``, ``wp__requirements_comp``, ``wp__requirements_inspect``.
See :ref:`requirements_workflows`.

.. rubric:: Process Status

.. list-table::
   :header-rows: 1
   :class: compact-overview-table

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'requirements_engineering' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'requirements_engineering' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(requirements_engineering)
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(requirements_engineering)

.. rubric:: Implementation status: 🔄 26% (7/27 deliverables complete)

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: module-phase-tracker-table

   * - **Module**
     - **Feature Requirements**
     - **Component Requirements**
     - **Req. Inspection**

   * - Baselibs
     - 🔄 93% (14/15)
     - 🔄 93% (124/134)
     - 🔄 20% (2/10)
       `bitmanipulation <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/bitmanipulation/docs/requirements/chklst_req_inspection.rst>`__,
       `concurrency <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/concurrency/docs/requirements/chklst_req_inspection.rst>`__,
       `containers <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/containers/docs/requirements/chklst_req_inspection.rst>`__,
       `filesystem <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/filesystem/docs/requirements/chklst_req_inspection.rst>`__,
       `json <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/json/docs/requirements/chklst_req_inspection.rst>`__,
       `safecpp <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/language/safecpp/docs/requirements/chklst_req_inspection.rst>`__,
       `result <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/result/docs/requirements/chklst_req_inspection.rst>`__,
       `srs <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/static_reflection_with_serialization/docs/requirements/chklst_req_inspection.rst>`__,
       `utils <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/utils/docs/requirements/chklst_req_inspection.rst>`__,
       `feature-level <https://github.com/eclipse-score/score/blob/main/docs/features/baselibs/docs/requirements/chklst_req_inspection.rst>`__

   * - Communication
     - ✅ Available (50/50)
     - 🔄 97% (34/35)
     - ❌ Open

   * - Logging
     - ✅ Available (46/46)
     - ❌ Open
     - ❌ Open

   * - Orchestrator
     - 🔄 84% (26/31)
     - ❌ Open
     - ❌ Open
       `executor <https://github.com/eclipse-score/score/blob/main/docs/modules/orchestrator/executor/docs/requirements/chklst_req_inspection.rst>`__,
       `orchestrator <https://github.com/eclipse-score/score/blob/main/docs/modules/orchestrator/orchestrator/docs/requirements/chklst_req_inspection.rst>`__

   * - Persistency
     - ✅ Available (40/40)
     - 🔄 95% (36/38)
     - ✅ Available (2/2)
       `feature-level <https://github.com/eclipse-score/score/blob/main/docs/features/persistency/requirements/chklst_req_inspection.rst>`__,
       `kvs <https://github.com/eclipse-score/persistency/blob/main/docs/persistency/kvs/requirements/chklst_req_inspection.rst>`__

   * - Time
     - ✅ Available (15/15)
     - ❌ Open
     - ❌ Open

   * - Config Mgmt
     - ✅ Available (13/13)
     - ❌ Open
     - ❌ Open

   * - Lifecycle
     - ❌ Open
     - ❌ Open
     - ❌ Open

   * - Security/Crypto
     - ✅ Available (42/42)
     - ❌ Open
     - ❌ Open

Process Area 3 — Architecture Design
************************************

Feature and component architecture must be designed and inspected.
Work products: ``wp__feature_arch``, ``wp__component_arch``, ``wp__sw_arch_verification``.
See :ref:`arch_workflow`.

.. rubric:: Process Status

.. list-table::
   :header-rows: 1
   :class: compact-overview-table

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'architecture_design' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'architecture_design' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(architecture_design)
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(architecture_design)

.. rubric:: Implementation status: 🔄 19% (5/27 deliverables complete)

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: module-phase-tracker-table

   * - **Module**
     - **Feature Architecture**
     - **Component Architecture**
     - **Arch. Inspection**

   * - Baselibs
     - ✅ Available (4/4)
     - 🔄 98% (172/175)
     - 🔄 80% (8/10)
       `bitmanipulation <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/bitmanipulation/docs/architecture/chklst_arc_inspection.rst>`__,
       `concurrency <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/concurrency/docs/architecture/chklst_arc_inspection.rst>`__,
       `containers <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/containers/docs/architecture/chklst_arc_inspection.rst>`__,
       `filesystem <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/filesystem/docs/architecture/chklst_arc_inspection.rst>`__,
       `json <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/json/docs/architecture/chklst_arc_inspection.rst>`__,
       `safecpp <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/language/safecpp/docs/architecture/chklst_arc_inspection.rst>`__,
       `result <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/result/docs/architecture/chklst_arc_inspection.rst>`__,
       `srs <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/static_reflection_with_serialization/docs/architecture/chklst_arc_inspection.rst>`__,
       `utils <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/utils/docs/architecture/chklst_arc_inspection.rst>`__,
       `feature-level <https://github.com/eclipse-score/score/blob/main/docs/features/baselibs/docs/architecture/chklst_arc_inspection.rst>`__

   * - Communication
     - ✅ Available (3/3)
     - 🔄 94% (17/18)
     - ❌ Open

   * - Logging
     - ✅ Available (4/4)
     - ✅ Available (3/3)
     - ❌ Open

   * - Orchestrator
     - 🔄 66% (4/6)
     - 🔄 98% (42/43)
     - ❌ Open
       `executor <https://github.com/eclipse-score/score/blob/main/docs/modules/orchestrator/executor/docs/architecture/chklst_arc_inspection.rst>`__,
       `orchestrator <https://github.com/eclipse-score/score/blob/main/docs/modules/orchestrator/orchestrator/docs/architecture/chklst_arc_inspection.rst>`__

   * - Persistency
     - ✅ Available (12/12)
     - 🔄 25% (1/4)
     - ❌ Open
       `feature-level <https://github.com/eclipse-score/score/blob/main/docs/features/persistency/architecture/chklst_arc_inspection.rst>`__,
       `kvs <https://github.com/eclipse-score/persistency/blob/main/docs/persistency/kvs/architecture/chklst_arc_inspection.rst>`__

   * - Time
     - ❌ Open
     - ❌ Open
     - ❌ Open

   * - Config Mgmt
     - ❌ Open
     - ❌ Open
     - ❌ Open

   * - Lifecycle
     - 🔄 94% (30/32)
     - 🔄 94% (15/16)
     - ❌ Open

   * - Security/Crypto
     - ❌ Open
     - ❌ Open
     - ❌ Open

Process Area 4 — Implementation
********************************

Source code and detailed design must be implemented and inspected.
Work products: ``wp__sw_development_plan``, ``wp__sw_implementation``, ``wp__sw_implementation_inspection``.
See :ref:`workflow_implementation`.

.. rubric:: Process Status

.. list-table::
   :header-rows: 1
   :class: compact-overview-table

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'implementation' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'implementation' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(implementation)
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(implementation)

.. rubric:: Implementation status: 🔄 47% (17/36 deliverables complete)

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: module-phase-tracker-table

   * - **Module**
     - **SW Development Plan**
     - **Code**
     - **Detailed Design**
     - **Impl. Inspection**

   * - Baselibs
     - ✅ Available
     - ✅ Available (~119,400 LOC) `baselibs <https://github.com/eclipse-score/baselibs>`__
     - ❌ Open
     - ❌ Open
       `bitmanipulation <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/bitmanipulation/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `concurrency <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/concurrency/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `containers <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/containers/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `filesystem <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/filesystem/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `json <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/json/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `safecpp <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/language/safecpp/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `result <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/result/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `srs <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/static_reflection_with_serialization/docs/detailed_design/chklst_impl_inspection.rst>`__,
       `utils <https://github.com/eclipse-score/score/blob/main/docs/modules/baselibs/utils/docs/detailed_design/chklst_impl_inspection.rst>`__

   * - Communication
     - ✅ Available
     - ✅ Available (~71,300 LOC) `communication <https://github.com/eclipse-score/communication>`__
     - ❌ Open
     - ❌ Open

   * - Logging
     - ✅ Available
     - ✅ Available (~22,900 LOC) `logging <https://github.com/eclipse-score/logging>`__
     - ❌ Open
     - ❌ Open

   * - Orchestrator
     - ✅ Available
     - ✅ Available (~38,300 LOC) `lifecycle <https://github.com/eclipse-score/lifecycle>`__
     - ❌ Open
     - ❌ Open

   * - Persistency
     - ✅ Available
     - ✅ Available (~8,700 LOC) `persistency <https://github.com/eclipse-score/persistency>`__
     - ❌ Open
     - ❌ Open
       `kvs <https://github.com/eclipse-score/persistency/blob/main/docs/persistency/kvs/detailed_design/chklst_impl_inspection.rst>`__

   * - Time
     - ✅ Available
     - ✅ Available (~11,700 LOC) `inc_time <https://github.com/eclipse-score/inc_time>`__
     - ❌ Open
     - ❌ Open

   * - Config Mgmt
     - ✅ Available
     - ✅ Available (~5,400 LOC) `config_management <https://github.com/eclipse-score/config_management>`__
     - ❌ Open
     - ❌ Open

   * - Lifecycle
     - ✅ Available
     - ✅ Available (~38,300 LOC) `lifecycle <https://github.com/eclipse-score/lifecycle>`__
     - 🔄 50% (1/2)
     - ❌ Open

   * - Security/Crypto
     - ✅ Available
     - ❌ Open
     - ❌ Open
     - ❌ Open

Process Area 5 — Verification
*****************************

All tests must be implemented and a module verification report must be approved.
Work products: ``wp__verification_sw_unit_test``, ``wp__verification_comp_int_test``, ``wp__verification_feat_int_test``, ``wp__verification_module_ver_report``.
See :ref:`verification_workflows`.

.. rubric:: Process Status

.. list-table::
   :header-rows: 1
   :class: compact-overview-table

   * - Process req. status
     - ISO 26262 std_req status
     - Req. verification status
   * -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Valid, Draft, Invalid, Other
          :colors: LimeGreen, Gold, LightCoral, LightGray

          type == 'gd_req' and is_external == False and status == 'valid' and 'verification' in tags
          type == 'gd_req' and is_external == False and status == 'draft' and 'verification' in tags
          type == 'gd_req' and is_external == False and status == 'invalid' and 'verification' in tags
          type == 'gd_req' and is_external == False and status not in ['valid', 'draft', 'invalid'] and 'verification' in tags
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Ok, Recommendation, Open, Action, Deviation, N/A, Other
          :colors: LimeGreen, LightBlue, Gold, Orange, LightCoral, LightGray, Silver
          :filter-func: needs_filters.std_req_status_for_area(verification)
     -

       .. rst-class:: small-pie-cell

       .. needpie::
          :labels: Automated, Waiting for automation, Inspection list, Other
          :colors: LimeGreen, Gold, LightBlue, LightGray
          :filter-func: needs_filters.area_verification_status(verification)

.. rubric:: Implementation status: 🔄 36% (13/36 deliverables complete)

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :class: module-phase-tracker-table

   * - **Module**
     - **Unit Tests**
     - **Comp. Integration Tests**
     - **Feature Integration Tests**
     - **Module Verification Report**

   * - Baselibs
     - ✅ Available (4,663 tests)
     - ✅ Available (13 tests)
     - ❌ Open
     - ❌ Open

   * - Communication
     - ✅ Available (2,374 tests)
     - ✅ Available (42 tests)
     - ❌ Open
     - ❌ Open

   * - Logging
     - ✅ Available (619 tests)
     - ❌ Open
     - ✅ Available (1 test) `reference_integration <https://github.com/eclipse-score/reference_integration>`__ (cross-module)
     - ❌ Open

   * - Orchestrator
     - ✅ Available (2 tests)
     - ✅ Available (9 tests)
     - ✅ Available (3 tests) `reference_integration <https://github.com/eclipse-score/reference_integration>`__ (cross-module)
     - ❌ Open

   * - Persistency
     - ✅ Available (138 tests)
     - ❌ Open
     - ✅ Available (6 tests) `reference_integration <https://github.com/eclipse-score/reference_integration>`__ (cross-module)
     - ❌ Open

   * - Time
     - ✅ Available (296 tests)
     - ✅ Available (11 tests)
     - ❌ Open
     - ❌ Open

   * - Config Mgmt
     - ✅ Available (143 tests)
     - ❌ Open
     - ❌ Open
     - ❌ Open

   * - Lifecycle
     - ✅ Available (2 tests)
     - ✅ Available (9 tests)
     - ❌ Open
     - ❌ Open

   * - Security/Crypto
     - ❌ Open
     - ❌ Open
     - ❌ Open
     - ❌ Open


Done Criteria
*************

A module is considered **complete** when all of the following are true:

#. All ``valid`` component requirements have **100% test coverage** (linked via ``FullyVerifies`` or ``PartiallyVerifies``).
#. All CI metadata checks pass (``TestType``, ``DerivationTechnique``, ``Description`` set on every test).
#. Static analysis has no open ``Critical`` or ``High`` findings.
#. The **Module Verification Report** (``wp__verification_module_ver_report``) is generated and approved by a Committer.
```
