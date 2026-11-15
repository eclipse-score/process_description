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

load("@score_docs_as_code//:docs.bzl", "docs", "docs_bundle")

package(default_visibility = ["//visibility:public"])

docs_bundle(
    name = "ai_process_extension",
    source_dir = "process_extensions/docs",
    data = [
        "process_extensions/docs/_assets/ai_supported_sldc_review_example.drawio.svg",
        "process_extensions/docs/_assets/ai_supported_sldc_tw_pr_review.drawio.svg",
        "process_extensions/docs/_assets/ai_supported_sldc_wf__platform_cr_mt_platform_mgmt_plan.drawio.svg",
    ],
)

docs(
    source_dir = "process",
    bundles = [{
        "bundle": ":ai_process_extension",
        "mount_at": "process_extensions",
        "attach_to": "index",
        "toctree_index": 11,
    }],
)
