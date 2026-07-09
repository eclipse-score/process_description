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

html_static_path = ["_assets"]
html_css_files = ["custom.css"]

# Training portals are pre-generated into trainings/_portals/ by build.py.
# This copies the subdirectory tree (e.g. requirements_engineering/) verbatim
# into the Sphinx HTML output root so portals are served alongside the docs.
html_extra_path = ["trainings/_portals"]

# Exclude training source files and generated portal files from Sphinx processing.
# - trainings/*/source/**   : Markdown source files for the training portals
# - trainings/trainings_templates/** : Template files, not Sphinx documents
# - trainings/_portals/**   : Generated portal HTML (served via html_extra_path)
exclude_patterns = [
    "trainings/*/source/**",
    "trainings/trainings_templates/**",
    "trainings/_portals/**",
]

# :need:`{title}` is used in the needs templates to display the title of the need
needs_role_need_template = "{title}"


# ---------------------------------------------------------------------------
# Training portal build hook
#
# Automatically regenerates all training portals before Sphinx processes the
# documentation.  build.py requires the 'markdown' package which is NOT part
# of the docs-as-code Sphinx environment, so it is run via the dedicated
# .venv virtual environment.  If that venv is absent it is created
# and the required packages are installed automatically.
# ---------------------------------------------------------------------------

def _build_training_portals(app):
    """Sphinx builder-inited event handler: regenerate all training portals."""
    import os, subprocess, sys
    from pathlib import Path

    conf_dir  = Path(app.confdir)           # …/process/
    repo_root = conf_dir.parent             # …/process_description/
    venv_dir  = repo_root / ".venv"
    venv_python = venv_dir / "bin" / "python"

    # Locate all training source build scripts
    build_scripts = sorted(conf_dir.glob(
        "trainings/*/source/build.py"
    ))
    if not build_scripts:
        return

    # Ensure the venv exists with the required packages
    if not venv_python.exists():
        reqs_file = build_scripts[0].parent / "requirements.txt"
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(venv_dir)],
                check=True, capture_output=True,
            )
            if reqs_file.exists():
                subprocess.run(
                    [str(venv_python), "-m", "pip", "install", "-q",
                     "-r", str(reqs_file)],
                    check=True, capture_output=True,
                )
        except Exception as exc:
            import warnings
            warnings.warn(
                f"[trainings] Could not create .venv_training: {exc}\n"
                "  Training portals will not be regenerated. "
                "Run source/build.py manually.",
                stacklevel=1,
            )
            return

    # Run each build script
    for script in build_scripts:
        try:
            subprocess.run(
                [str(venv_python), str(script)],
                cwd=str(script.parent),
                check=True, capture_output=True,
            )
            print(f"[trainings] Built portal: {script.parent.parent.name}")
        except subprocess.CalledProcessError as exc:
            import warnings
            warnings.warn(
                f"[trainings] Portal build failed for {script.parent.parent.name}:\n"
                f"  {exc.stderr.decode(errors='replace').strip()}",
                stacklevel=1,
            )


def setup(app):
    app.connect("builder-inited", _build_training_portals)
