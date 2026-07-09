---
# *******************************************************************************
# Copyright (c) 2026 Contributors to the Eclipse Foundation
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
# AI Disclosure: This file was largely AI-generated. The AI-generated
# portions are made available under CC0-1.0 and not subject to the
# project's license. The human contributor has reviewed and verified
# that the code is correct.
# SPDX-License-Identifier: CC0-1.0
# Assisted-by: Claude Sonnet 4.6
# *******************************************************************************
id: module-N                             # replace N with 1, 2, 3, …
title: "[Module Title]"
breadcrumb: "Module N: [Module Title]"
day: 1
module_number: N                         # integer, e.g. 1
duration: "~XX min"
standard: "[ProcessArea]"               # short tag displayed in header, e.g. "Requirements"
quiz_pass_mark: 70
prev:
  url: index.html                        # or module-(N-1).html
  label: "Course Overview"              # or "Module N-1: [Prev Title]"
next:
  url: module-2.html                    # or quiz-1.html for last module
  label: "Module 2: [Next Title]"       # or "[Quiz Title]"
---

# [Module Title]

[One-paragraph introduction: what this module covers and why it matters in the
context of the process area and applicable standards.]

## N.1 [First Section Title]

[Content paragraph.]

:::definition [Key Term]
[Definition of the key term, referencing the applicable standard where relevant.]
:::

[More content paragraphs, tables, lists.]

## N.2 [Second Section Title]

[Content paragraph.]

:::important [Key Point Label]
[The most critical takeaway from this section — keep it to 2-3 sentences.]
:::

[Tables are useful for comparing concepts:]

| Concept A | Concept B | Notes |
|-----------|-----------|-------|
| ... | ... | ... |

## N.3 [Third Section Title]

[Content paragraph.]

:::example [Example Label]
[A concrete worked example with a realistic scenario from the automotive/S-CORE context.]
:::

:::collapsible [Click-to-expand Section Title]
[Detailed background information or extended explanation that is useful but not
essential on the first read.]
:::

## N.4 [Fourth Section Title] (optional)

[Additional content if needed.]

:::tip [Tip Label]
[A practical hint for applying this concept day-to-day.]
:::

<!-- ─────────────────────────────────────────────────────────────────
     MODULE CHECK-IN QUIZ — 3 questions, rendered inline.
     Remove or replace the block below; keep id unique per module.
     ───────────────────────────────────────────────────────────────── -->
:::quiz module-N-check

- q: "[Question 1 text — tests understanding of Section N.1]"
  options:
    - text: "[Correct answer]"
      correct: true
    - text: "[Distractor 1]"
    - text: "[Distractor 2]"
  feedback: >-
    Correct: A. [Brief explanation linking back to the module content.]

- q: "[Question 2 text — tests understanding of Section N.2]"
  options:
    - text: "[Distractor 1]"
    - text: "[Correct answer]"
      correct: true
    - text: "[Distractor 2]"
  feedback: >-
    Correct: B. [Brief explanation.]

- q: "[Question 3 text — scenario-based, covering Section N.3 or N.4]"
  options:
    - text: "[Distractor 1]"
    - text: "[Distractor 2]"
    - text: "[Correct answer]"
      correct: true
  feedback: >-
    Correct: C. [Brief explanation.]
:::
