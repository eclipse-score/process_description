Execute the Requirements Inspection Demonstrator
=================================================

Start in Copilot Chat
-----------------------

Open this repository in a Copilot-enabled editor and use Chat Agent mode.
You do not need to prepare input, copy JSON, enter tool versions, run import
commands, or finalize in a separate terminal. Paste this into a new conversation:

.. code-block:: text

   Inspect baselibs using #file:process_extensions/chat_workflow.prompt.md
   Prepare the draft, present the editable review, and stop for my confirmation.

If the reference is not resolved, attach ``chat_workflow.prompt.md`` using Add
Context. Alternatively, open that file and use its Run Prompt button where the
editor supports it, supplying ``Inspect baselibs``. The prompt stays inside this
directory; it is not installed globally or automatically discovered as a slash
command. Reattach it when starting a new Chat.

For other input, name a feature/component requirements file, feature, safety-level
context, and permitted scope. Stakeholder requirements remain part of the
existing S-CORE workflow and may be parent context, but the demonstrator does
not assess them because their checklist differs. Assumptions of use are also
unsupported. The agent asks for missing details rather than guessing them.
Check organizational sharing rules before supplying input. The public baselibs
fixture is example input, not independently validated qualification evidence.

Judgment and Pause
------------------

The agent prepares a fresh uniquely named run, detects available tool metadata,
judges the requirements, validates the JSON response, and creates ``review.md``
under ``process_extensions/out/<run>/``. It presents the file link, revision,
and findings, then **ends its turn**. No approved report is written at this stage.

Input, prompt, original judgment, and manifest are preserved separately. Existing
runs, including older ``out/baselibs/`` artifacts, are not overwritten or
migrated. Start a fresh inspection for this chat-first format. Helpers never
invoke Copilot or transmit input; the Chat conversation performs judgment.

Edit or Request Corrections
---------------------------

Open the linked ``review.md``. There is one set of editable verdicts, rationales,
and findings, not a duplicate checklist. Independently review every entry,
including evidence gaps; an ``n/a`` is not proof of successful verification.

- Edit existing table cells or ask for a precise correction in Chat, identifying
  the requirement and checklist item.
- Add, correct, or remove findings consistently with the reviewed verdicts.
- Keep requirement/checklist IDs and table headers unchanged. Put assessment
  content in table cells, not additional free-form notes. Escape literal pipes
  as ``\|`` or ``&#124;``; use ``<br>`` for a line break within a cell.
- After requested changes, the agent validates and shows a new revision, then
  stops again. It must not treat requested edits as approval.

After direct edits, reply:

.. code-block:: text

   Ready. Show the current review revision for confirmation.

The agent snapshots and presents the current revision. ``Ready``, positive
feedback, file editing, and tool-permission approval are not named confirmation.

Confirm or Reject in Chat
---------------------------

After reviewing the revision already presented, reply:

.. code-block:: text

   Approve as Jane Reviewer

Use your own identity, not the example name. An unchanged presented draft can
be confirmed directly; you need not reproduce every verdict. If any file changed
after presentation, the agent must show the changed revision and stop for a new
confirmation. It must not stage and approve new edits using an earlier approval.

To reject, state the rejection and reason. The run closes without final output;
drafts and history remain available. On named confirmation, the agent writes
``report.rst`` and ``audit.json`` with approver, relayed message and timestamp,
revision/hash, original/reviewed judgments, changes, input/prompt/response hashes,
and detected tool information. Full rationales and snapshots are retained.
Final artifacts are not overwritten.

Automatic Tool Information
--------------------------

The collector reads non-secret version metadata and workflow files, not chat
logs, credentials, or arbitrary environment-variable dumps. It detects Python,
Markdown parser and workflow versions, code hashes, available editor metadata,
and installed Copilot Chat versions, recording a source for each value.

Installed inventories do not prove the active extension instance. A local helper
cannot read the built-in Chat request's selected model or backend chosen by
``Auto``. These fields and unexposed agent tool IDs remain unknown; no manual
placeholders or guesses are needed. Exact request metadata would require a
supported editor integration, which this demonstrator does not provide.

The audit lists logical workflow tools and available versions, not an invented
complete trace of hidden agent tools. Installation metadata is not authenticated
session metadata.

Approval and Safety Boundary
-----------------------------

Chat confirmation is declared user approval relayed by the agent. Helpers enforce
valid structure, a named message, revision/hash matching, and no overwrite, but
cannot authenticate the author or prove the agent stopped between Chat turns.
A privileged agent could supply a fabricated message or modify local files.
The reusable prompt governs the pause; it is not an access control. Hashes are
not signatures. Project review, reviewer competence, tool acceptance, and the
public S-CORE qualification decision remain separate.

Environment and Developer Checks
-----------------------------------

The parser accepts simple ``feat_req`` and ``comp_req`` directives only, with
single-line options and three-space-indented bodies. It rejects stakeholder
requirements (``stkh_req``), assumptions of use (``aou_req``), and mixed-level
files rather than applying a mismatched checklist. Parent IDs are assessed only
from supplied information; parent requirement text is not fetched automatically.
Use the applicable separate S-CORE checklist for direct stakeholder inspection.

Helpers require Python 3.11+ and Markdown as declared in ``pyproject.toml``.
The agent uses an existing suitable interpreter and asks before installing
missing dependencies. Setup can use ``pip install -e .`` from this directory
in an appropriate environment; this is not a per-inspection user step.

Developers run offline tests from ``process_extensions/``:

.. code-block:: bash

   python -m unittest discover -s tests/req_inspection -v

Tests use constructed responses without invoking Copilot. They do not establish
inspection quality or qualification. Earlier helper commands remain for legacy
compatibility but are not the chat-first path.

From the repository root publish these pages with the existing command:

.. code-block:: bash

   bazel run //:docs

The Bazel bundle mounts only the publication pages under ``process_extensions``.
Runtime prompts, templates, fixtures, tests, and run outputs are not Sphinx
document inputs. Documentation builds never invoke Copilot.
