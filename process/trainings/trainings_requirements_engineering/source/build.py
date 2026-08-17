#!/usr/bin/env python3
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
"""
S-CORE Requirements Engineering Training Portal — Build Script

Converts trainings_requirements_engineering/source/content/*.md
→ trainings_requirements_engineering/portal/*.html

Dependencies:
    pip install markdown pyyaml jinja2
    (or:  pip install -r requirements.txt)

Usage:
    python build.py              # rebuild everything
    python build.py module-3     # rebuild one page by id
    python build.py --list       # list all source files
"""

import os, re, sys, shutil
from pathlib import Path

# ── Dependency check ─────────────────────────────────────────────────────────
try:
    import yaml
    import markdown as _mdlib
    from jinja2 import Environment, FileSystemLoader
    from markupsafe import Markup
except ImportError as e:
    sys.exit(
        f"\nMissing package: {e}\n"
        f"Fix with:  pip install markdown pyyaml jinja2\n"
        f"       or:  pip install -r requirements.txt\n"
    )

# ── Paths ────────────────────────────────────────────────────────────────────
SRC     = Path(__file__).parent.resolve()
CONTENT = SRC / 'content'
ASSETS  = SRC / 'assets'
OUT     = SRC.parent.parent / '_portals' / 'requirements_engineering'
TMPL    = SRC          # template.html lives here

CALLOUT_TYPES = 'definition|example|important|tip'
LETTERS       = 'ABCDE'


# ── Frontmatter ──────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple:
    """Return (frontmatter_dict, body_str). Body starts after closing ---."""
    if not text.startswith('---\n'):
        return {}, text
    try:
        end = text.index('\n---\n', 4)
    except ValueError:
        return {}, text
    fm   = yaml.safe_load(text[4:end]) or {}
    body = text[end + 5:]
    return fm, body


# ── Markdown conversion ───────────────────────────────────────────────────────

def _md(text: str) -> str:
    """Convert a markdown string to an HTML fragment."""
    return _mdlib.markdown(
        text.strip(),
        extensions=['tables', 'fenced_code'],
    )


# ── Custom block substitutions ────────────────────────────────────────────────

def _sub_callout(m: re.Match) -> str:
    ctype = m.group(1)
    label = (m.group(2) or '').strip()
    body  = m.group(3)
    label_html = f'<div class="callout-label">{label}</div>\n' if label else ''
    return (
        f'<div class="callout {ctype}">\n'
        f'{label_html}'
        f'{_md(body)}\n'
        f'</div>'
    )


def _sub_collapsible(m: re.Match) -> str:
    title  = (m.group(1) or '').strip()
    inner  = _md(m.group(2))
    return (
        f'<div class="collapsible">\n'
        f'  <div class="collapsible-header">{title}'
        f' <span class="arrow">▼</span></div>\n'
        f'  <div class="collapsible-body">{inner}</div>\n'
        f'</div>'
    )


_RE_CALLOUT    = re.compile(
    rf'^:::({CALLOUT_TYPES})(?:\s+([^\n]+))?\n(.*?)^:::',
    re.M | re.S,
)
_RE_COLLAPSIBLE = re.compile(
    r'^:::collapsible(?:\s+([^\n]+))?\n(.*?)^:::',
    re.M | re.S,
)
_RE_QUIZ        = re.compile(
    r'^:::quiz\s+(\S+)\s*\n(.*?)^:::',
    re.M | re.S,
)


def extract_quiz_block(text: str) -> tuple:
    """Remove :::quiz block from body; return (clean_body, quiz_dict | None)."""
    m = _RE_QUIZ.search(text)
    if not m:
        return text.strip(), None
    quiz_id   = m.group(1)
    questions = yaml.safe_load(m.group(2)) or []
    clean     = text[:m.start()] + text[m.end():]
    return clean.strip(), {'id': quiz_id, 'questions': questions}


def convert_body(text: str) -> str:
    """Full pipeline: callouts → collapsibles → markdown → HTML."""
    text = _RE_CALLOUT.sub(_sub_callout, text)
    text = _RE_COLLAPSIBLE.sub(_sub_collapsible, text)
    return _md(text)


# ── Quiz HTML generators ──────────────────────────────────────────────────────

def _question_html(idx: int, q: dict, standalone: bool = False) -> str:
    """Render one question block."""
    scenario_html = ''
    if standalone and q.get('scenario'):
        s = q['scenario'].replace('\n', ' ').strip()
        scenario_html = f'<div class="scenario-box">{s}</div>\n  '

    opts_html = '\n    '.join(
        f'<li data-correct="{"true" if o.get("correct") else "false"}">'
        f'<span class="opt-letter">{LETTERS[j]}</span> {o["text"]}</li>'
        for j, o in enumerate(q.get('options', []))
    )
    fb = q.get('feedback', '')
    return (
        f'<div class="question-block">\n'
        f'  <p class="question-text">'
        f'<span class="question-num">Q{idx}.</span> {scenario_html}{q["q"]}</p>\n'
        f'  <ul class="options">\n    {opts_html}\n  </ul>\n'
        f'  <div class="feedback">{fb}</div>\n'
        f'</div>'
    )


def render_inline_quiz(quiz: dict, pass_mark: int = 67) -> str:
    """3-question module check-in quiz section."""
    qs = '\n'.join(_question_html(i, q) for i, q in enumerate(quiz['questions'], 1))
    return (
        f'<div class="quiz-section" id="{quiz["id"]}">\n'
        f'  <h2>Module Check-In</h2>\n'
        f'  <p class="quiz-intro">'
        f'Answer all questions and click Submit to check your understanding.</p>\n'
        f'  {qs}\n'
        f'  <button class="quiz-submit">Submit Answers</button>\n'
        f'  <div class="quiz-result"></div>\n'
        f'</div>'
    )


def render_checkpoint_questions(questions: list) -> str:
    """All question blocks for a standalone checkpoint quiz page."""
    return '\n'.join(
        _question_html(i, q, standalone=True)
        for i, q in enumerate(questions, 1)
    )


# ── Page builder ──────────────────────────────────────────────────────────────

def build_page(md_path: Path, env: Environment) -> None:
    raw      = md_path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(raw)
    page_id  = fm.get('id', md_path.stem)
    ptype    = fm.get('page_type', 'module')

    # strip keys we pass explicitly to avoid duplicate-keyword errors
    _STRIP = {'page_type', 'questions'}
    fm_ctx = {k: v for k, v in fm.items() if k not in _STRIP}

    tmpl = env.get_template('template.html')

    if ptype == 'quiz':
        questions      = fm.get('questions', [])
        questions_html = Markup(render_checkpoint_questions(questions))
        html = tmpl.render(
            page_type      = 'quiz',
            questions_html = questions_html,
            content        = Markup(''),
            quiz_html      = Markup(''),
            quiz_init      = '',
            **fm_ctx,
        )

    elif ptype == 'index':
        content_html = convert_body(body)
        html = tmpl.render(
            page_type = 'index',
            content   = Markup(content_html),
            quiz_html = Markup(''),
            quiz_init = '',
            **fm_ctx,
        )

    else:  # module
        body, quiz     = extract_quiz_block(body)
        content_html   = convert_body(body)
        quiz_html      = Markup(render_inline_quiz(quiz)) if quiz else Markup('')
        quiz_init      = ''
        if quiz:
            pm       = fm.get('quiz_pass_mark', 67)
            on_pass  = fm.get('quiz_on_pass', None)
            op_js    = f'"{on_pass}"' if on_pass else 'null'
            quiz_init = f"initQuiz('{quiz['id']}', {pm}, {op_js});"

        html = tmpl.render(
            page_type  = 'module',
            content    = Markup(content_html),
            quiz_html  = quiz_html,
            quiz_init  = quiz_init,
            **fm_ctx,
        )

    out = OUT / f'{page_id}.html'
    out.write_text(html, encoding='utf-8')
    print(f'  ✓  {page_id}.html')


# ── Main ──────────────────────────────────────────────────────────────────────

def build_all(target_id: str | None = None) -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    # copy shared assets
    for name in ('style.css', 'app.js'):
        src = ASSETS / name
        if src.exists():
            shutil.copy2(src, OUT / name)
            print(f'  →  {name}  (copied)')

    env   = Environment(loader=FileSystemLoader(str(TMPL)), autoescape=False)
    files = sorted(CONTENT.glob('*.md'))

    if not files:
        sys.exit(f"No .md files found in {CONTENT}")

    built = 0
    for f in files:
        pid = f.stem
        if target_id and pid != target_id:
            continue
        build_page(f, env)
        built += 1

    if target_id and built == 0:
        sys.exit(f"No file found with id '{target_id}' in {CONTENT}")

    print(f'\nDone — {built} page(s) written to {OUT}')


if __name__ == '__main__':
    args = sys.argv[1:]

    if '--list' in args:
        for f in sorted(CONTENT.glob('*.md')):
            fm, _ = parse_frontmatter(f.read_text(encoding='utf-8'))
            print(f"  {f.stem:20s}  {fm.get('title', '—')}")
        sys.exit(0)

    build_all(args[0] if args else None)
