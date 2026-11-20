Execute the Requirements Inspection Demonstrator
=================================================

Start in Copilot Chat
-----------------------

Open this repository in a Copilot-enabled editor and use Chat Agent mode.
For the bundled example, paste this into a new conversation:

.. code-block:: text

   Inspect baselibs using #file:process_extensions/chat_workflow.prompt.md
   Prepare the draft, present the editable checklist, and stop.

If the reference is not resolved, attach ``chat_workflow.prompt.md`` using Add
Context. Alternatively, open that file and use its Run Prompt button where the
editor supports it, supplying ``Inspect baselibs``. The prompt stays at
``process_extensions/chat_workflow.prompt.md``; it is not installed globally or
automatically discovered as a slash command. Reattach it when starting a new Chat.

For other input, name a feature/component requirements file, feature, safety-level
context, and permitted scope. Stakeholder requirements remain part of the
existing S-CORE workflow and may be parent context, but the demonstrator does
not assess them because their checklist differs. Assumptions of use are also
unsupported. The agent asks for missing details rather than guessing them.
Check organizational sharing rules before supplying input. The public baselibs
fixture is example input, not independently validated qualification evidence.

Optionally supply ``--context <file.json>``, mapping requirement IDs to
supplied parent/related requirement text, so the linkage and completeness
checklist items can be genuinely assessed instead of being forced to
``not_assessed``. Optionally supply ``--model-label <label>`` to explicitly
record which model you selected; nothing infers this automatically.

This demonstrator runs while a requirements change is under review in a pull
request: the requirements file being inspected is the one proposed by that PR,
and the checked checklist is meant to become part of that same PR. The
inspection itself happens locally in Chat and is independent of any CI
trigger; nothing here opens, reacts to, or merges a PR automatically.

Judgment and Pause
------------------

Following the prompt, the agent uses local helpers to prepare a new run,
collect available tool metadata, and validate its draft assessment against the
public checklist. The helpers create ``inspection.md`` under
``process_extensions/out/<run>/``. The prompt instructs the agent to present the
file link and verdict counts, then **end its turn** for human review.

Input, prompt, original judgment, and manifest are preserved separately in the
same run directory for local traceability only; they are not evidence by
themselves. Helpers never invoke Copilot or transmit input; the Chat
conversation performs judgment.

Edit or Request Corrections
---------------------------

Open the linked ``inspection.md``. There is one editable checklist, in the
same Review ID / Acceptance Criteria / Guidance / Passed / Remarks / Issue
link columns as the public template, not an invented schema. Independently
review every entry, including evidence gaps; ``not_assessed`` is not proof of
successful verification, and neither is ``n/a``.

- Edit the **Passed**, **Remarks**, and **Issue link** cells, or ask for a
  precise correction in Chat, identifying the requirement and checklist item.
  The **Criterion** and **Guidance** cells are read-only: they are always
  re-derived from the canonical template, so edits to them are ignored.
- An issue link is mandatory for every ``no`` and not allowed otherwise.
- Keep requirement/checklist IDs and table headers unchanged. Put assessment
  content in table cells, not additional free-form notes. Escape literal pipes
  as ``\|`` or ``&#124;``; use ``<br>`` for a line break within a cell.
- After requested or direct changes, re-run the check (see below); the agent
  reports the current verdict counts and any open issue links.

.. code-block:: bash

   python -m workflows.req_safety_inspection.workflow check <run>

Run this command from ``process_extensions/``, or ask the agent to run it after
corrections. The helper does not detect file edits automatically.
Checking the file is not approval.

Hand Off to the Project's Own Review
-------------------------------------

Once satisfied with ``inspection.md``, copy its checklist content into the
project's real requirements inspection document (for example
``doc__<feature>_req_inspection``), or into a comment on the existing
inspection PR, and commit it as part of that same pull request (or a
dedicated follow-up PR) before it is merged. The normal Git/GitHub review of
that change — authenticated by the platform, requiring a reviewer distinct
from the content's author, and retained in the project's own history — is the
only approval this tool recognizes. This repository does not script that
commit, PR, or merge step; it remains a normal, reviewed Git/GitHub action.

Automatic Tool Information
--------------------------

The collector reads non-secret version metadata and workflow files, not chat
logs, credentials, or arbitrary environment-variable dumps. It detects Python,
Markdown parser and workflow versions, code hashes, available editor metadata,
and installed Copilot Chat versions, recording a source for each value.

Installed inventories do not prove the active extension instance. A local helper
cannot read the built-in Chat request's selected model or backend chosen by
``Auto``. These fields and unexposed agent tool IDs remain unknown unless the
engineer explicitly supplies ``--model-label``, which is recorded as
"reviewer supplied", never inferred or defaulted. Exact request metadata would
require a supported editor integration, which this demonstrator does not provide.

Safety Boundary
-----------------------------

The helpers validate structure, not the correctness of the assessment. They
cannot enforce the agent's turn boundary or authenticate a reviewer.
Human review and approval take place through the project's existing process.
Tool evaluation is separate; see :doc:`../process_guidance/tool_management`.

Environment and Developer Checks
-----------------------------------

The parser accepts simple ``feat_req`` and ``comp_req`` directives only, with
single-line options and three-space-indented bodies. It rejects stakeholder
requirements (``stkh_req``), assumptions of use (``aou_req``), and mixed-level
files rather than applying a mismatched checklist. Parent IDs are recorded
from supplied information; parent requirement text is only used when supplied
through ``--context``, never fetched automatically. Use the applicable
separate S-CORE checklist for direct stakeholder inspection.

Helpers require Python 3.11+ and Markdown as declared in ``pyproject.toml``.
The agent uses an existing suitable interpreter and asks before installing
missing dependencies. Setup can use ``pip install -e .`` from ``process_extensions/``
in an appropriate environment; this is not a per-inspection engineer step.

Developers run offline tests from ``process_extensions/``:

.. code-block:: bash

   python -m unittest discover -s tests/req_inspection -v

Tests use constructed responses without invoking Copilot. They check helper
behavior, not inspection quality or qualification.

From the repository root publish these pages with the existing command:

.. code-block:: bash

   bazel run //:docs

The Bazel bundle mounts publication sources from ``process_extensions/docs/``
at the published ``process_extensions`` location.
Runtime prompts, templates, fixtures, tests, and run outputs are not Sphinx
document inputs. Documentation builds never invoke Copilot.
