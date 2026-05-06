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
"""
Sphinx extension: Harvey ball build-time substitution generator.

Usage in RST (functional_completeness_definitions.rst):
  .. |fc_baselibs_wp__requirements_stkh| harvey:: 75

During the Sphinx build this extension:
  1. Transforms every ``harvey:: N`` substitution into a proper
     ``image:: harvey-N.svg`` substitution (with width/height/alt).
  2. Auto-generates module_completeness_summary.rst by computing the
     mean per module x process-area and rounding to the nearest 25%.

No manual script needs to be run.
"""

from __future__ import annotations

import re
import pathlib
from typing import Any

# ---------------------------------------------------------------------------
# Configuration: process areas and their work products
# ---------------------------------------------------------------------------

AREAS: dict[str, list[str]] = {
    "requirements_engineering": [
        "wp__requirements_stkh",
        "wp__requirements_sw_platform_aou",
        "wp__requirements_feat",
        "wp__requirements_feat_aou",
        "wp__requirements_comp",
        "wp__requirements_comp_aou",
        "wp__requirements_proc_tool",
        "wp__requirements_inspect",
    ],
    "architecture_design": [
        "wp__platform_arch",
        "wp__feature_arch",
        "wp__component_arch",
        "wp__sw_arch_verification",
    ],
    "implementation": [
        "wp__sw_development_plan",
        "wp__sw_implementation",
        "wp__sw_implementation_inspection",
    ],
    "verification": [
        "wp__verification_plan",
        "wp__verification_platform_int_test",
        "wp__verification_platform_ver_report",
        "wp__verification_feat_int_test",
        "wp__verification_module_ver_report",
        "wp__verification_comp_int_test",
        "wp__verification_sw_unit_test",
    ],
}

# Docnames (relative to srcdir, without .rst) that this extension handles
DEFS_DOCNAME    = "standards/process_reqs_list/functional_completeness_definitions"
SUMMARY_DOCNAME = "standards/process_reqs_list/module_completeness_summary"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Matches:  .. |fc_<module>_<wp>| harvey:: <N>
_HARVEY_RE = re.compile(
    r"^\.\. \|(?P<name>[^|]+)\|\s+harvey::\s+(?P<val>\d+)\s*$",
    re.MULTILINE,
)

# Matches:  .. |fc_<module>_<wp>|   (captures module and wp from name)
_FC_NAME_RE = re.compile(r"^fc_(?P<module>[^_]+(?:_[^_]+)*)_(wp__\S+)$")


def _round25(v: float) -> int:
    """Round to the nearest multiple of 25, using ceiling so that any
    positive average value shows at least 25% (i.e. 'started')."""
    import math
    if v <= 0:
        return 0
    return min(100, math.ceil(v / 25) * 25)


def _image_sub(name: str, value: int) -> str:
    return (
        f".. |{name}| image:: harvey-{value}.svg\n"
        f"   :width: 64px\n"
        f"   :height: 64px\n"
        f"   :alt: {value}%"
    )


def _parse_values(rst_source: str) -> dict[tuple[str, str], int]:
    """Return {(module, wp): value} from harvey:: substitutions in source."""
    data: dict[tuple[str, str], int] = {}
    for m in _HARVEY_RE.finditer(rst_source):
        name = m.group("name").strip()
        val  = int(m.group("val"))
        nm   = _FC_NAME_RE.match(name)
        if nm:
            # Greedy match: module may contain underscores, wp starts with wp__
            # We split at the last occurrence of _wp__ to separate module from wp
            idx = name.rfind("_wp__")
            if idx != -1:
                module = name[3:idx]   # strip leading "fc_"
                wp     = name[idx + 1:]
                data[(module, wp)] = val
    return data


def _transform_defs(source: str) -> str:
    """Replace every ``harvey:: N`` substitution with a full image:: block."""
    def replace(m: re.Match) -> str:
        return _image_sub(m.group("name").strip(), int(m.group("val")))
    return _HARVEY_RE.sub(replace, source)


def _generate_summary(data: dict[tuple[str, str], int]) -> str:
    """Generate the full content of module_completeness_summary.rst."""
    modules = sorted({mod for mod, _ in data})

    lines = [
        ":orphan:",
        "",
        "..",
        "   # **************************************************************************",
        "   # Copyright (c) 2025 Contributors to the Eclipse Foundation",
        "   #",
        "   # See the NOTICE file(s) distributed with this work for additional",
        "   # information regarding copyright ownership.",
        "   #",
        "   # This program and the accompanying materials are made available under the",
        "   # terms of the Apache License Version 2.0 which is available at",
        "   # https://www.apache.org/licenses/LICENSE-2.0",
        "   #",
        "   # SPDX-License-Identifier: Apache-2.0",
        "   # **************************************************************************",
        "",
        ".. Auto-generated during Sphinx build by harvey_balls.py.",
        ".. Do not edit — values come from functional_completeness_definitions.rst.",
        "",
    ]

    for module in modules:
        lines.append(f".. {module.capitalize()}")
        lines.append("")
        for area, wps in AREAS.items():
            vals = [data.get((module, wp), 0) for wp in wps]
            val  = _round25(sum(vals) / len(vals))
            lines.append(_image_sub(f"fc_avg_{module}_{area}", val))
            lines.append("")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Sphinx event hooks
# ---------------------------------------------------------------------------

# Module-level cache so we only parse the defs file once per build
_cached_data: dict[tuple[str, str], int] | None = None


def _on_builder_inited(app: Any) -> None:
    """Parse the defs file from disk before any source-read events fire."""
    global _cached_data
    defs_path = pathlib.Path(app.srcdir) / (DEFS_DOCNAME.replace("/", pathlib.os.sep) + ".rst")
    if defs_path.exists():
        _cached_data = _parse_values(defs_path.read_text(encoding="utf-8"))
    else:
        _cached_data = {}


def _on_source_read(app: Any, docname: str, source: list[str]) -> None:
    """Transform source on the fly for the two managed documents,
    and inline transformed content where either file is ``.. include::``-d."""

    # 1. Defs file itself: replace harvey:: with image:: substitutions
    if docname == DEFS_DOCNAME:
        source[0] = _transform_defs(source[0])
        return

    # 2. Summary file: regenerate entirely from cached data
    if docname == SUMMARY_DOCNAME:
        data = _cached_data if _cached_data is not None else {}
        source[0] = _generate_summary(data)
        return

    # 3. Any other file that uses ``.. include::`` for our two files:
    #    inline the transformed / generated content in-place so that
    #    docutils never reads the raw source files from disk.
    src = source[0]

    if "include:: functional_completeness_definitions.rst" in src:
        defs_path = (
            pathlib.Path(app.srcdir)
            / DEFS_DOCNAME.replace("/", pathlib.os.sep)
        ).with_suffix(".rst")
        transformed = _transform_defs(defs_path.read_text(encoding="utf-8"))
        src = src.replace(
            ".. include:: functional_completeness_definitions.rst",
            transformed,
        )

    if "include:: module_completeness_summary.rst" in src:
        data = _cached_data if _cached_data is not None else {}
        src = src.replace(
            ".. include:: module_completeness_summary.rst",
            _generate_summary(data),
        )

    source[0] = src


# ---------------------------------------------------------------------------
# Extension setup
# ---------------------------------------------------------------------------

def setup(app: Any) -> dict:
    app.connect("builder-inited", _on_builder_inited)
    app.connect("source-read",    _on_source_read)
    return {
        "version":     "1.0",
        "parallel_read_safe":  True,
        "parallel_write_safe": True,
    }
