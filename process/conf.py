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

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Process Description"
project_url = "https://eclipse-score.github.io/process_description/"
version = "0.1"

extensions = [
    # TODO: remove plantuml here once
    # https://github.com/useblocks/sphinx-needs/pull/1508 is merged and docs-as-code
    # is updated with new sphinx-needs version
    "sphinxcontrib.plantuml",
    "score_sphinx_bundle",
]

# :need:`{title}` is used in the needs templates to display the title of the need
needs_role_need_template = "{title}"


def setup(app):
    # Register the FMEA Fault Model need type.
    # This type is used for fault models listed in the FMEA fault models guideline
    # so they can be linked to from FMEA analyses instead of using plain IDs.
    fmea_fault_model_type = {
        "directive": "fmea_fault_model",
        "title": "FMEA Fault Model",
        "prefix": "fmea_fault_model__",
        "tags": [],
        "parts": 2,
        "mandatory_options": {
            "id": "^fmea_fault_model__[0-9a-z_]+$",
            "status": "^(valid|draft)$",
            "element": "^.*$",
            "importance": "^(High|Medium|Low)$",
        },
        "optional_options": {},
        "mandatory_links": {},
        "optional_links": {},
    }
    app.config.needs_types.append(fmea_fault_model_type)
    for opt in ("element", "importance"):
        if opt not in app.config.needs_extra_options:
            app.config.needs_extra_options.append(opt)
