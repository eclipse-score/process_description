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

load("@aspect_rules_py//py:defs.bzl", "py_library")
load("@score_docs_as_code//:docs.bzl", "docs")

# Creates all documentation targets:
# - `process:incremental` for building docs incrementally at runtime
# - `process:live_preview` for live preview in the browser without an IDE
# - `process:ide_support` for creating python virtualenv for IDE support
# - `process:docs` for building documentation at build-time

docs(
    conf_dir="process",  # Where 'conf.py' is
    docs_targets=[
        {
            "suffix": "latest",  # latest main branch documentation build
        },
    ],
    source_dir="process",  # Where the RST files are located
    source_files_to_scan_for_needs_links=[
        # Note: you can add filegroups, globs, or entire targets here.
    ],
)
