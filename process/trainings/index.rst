.. *******************************************************************************
.. Copyright (c) 2026 Contributors to the Eclipse Foundation
..
.. See the NOTICE file(s) distributed with this work for additional
.. information regarding copyright ownership.
..
.. This program and the accompanying materials are made available under the
.. terms of the Apache License Version 2.0 which is available at
.. https://www.apache.org/licenses/LICENSE-2.0
..
.. SPDX-License-Identifier: Apache-2.0
.. *******************************************************************************

.. AI Disclosure: This file was largely AI-generated. The AI-generated
.. portions are made available under CC0-1.0 and not subject to the
.. project's license. The human contributor has reviewed and verified
.. that the code is correct.
.. SPDX-License-Identifier: CC0-1.0
.. Assisted-by: Claude Sonnet 4.6

.. _trainings:

Trainings
=========

Self-paced interactive training portals for the Eclipse S-CORE process areas.
Each portal is built from editable Markdown source files and rendered as a
standalone HTML site with progress tracking and embedded quizzes.

.. note::
   The portals open as self-contained HTML applications.
   Progress is saved locally in your browser — no server or login required.

Available Trainings
-------------------

.. grid:: 1 1 2 2
   :class-container: score-grid

   .. grid-item-card::
      :class-card: card-ml2

      Requirements Engineering
      ^^^^^^^^^^^^^^^^^^^^^^^^
      A focused 4-module training covering the S-CORE requirements engineering
      process: concepts, requirement levels, attributes, and workflows.

      | **Duration:** ~3.5 hours
      | **Modules:** 4 + Checkpoint Quiz
      | **Standards:** ISO 26262 · ASPICE SWE.1 · ISO/SAE 21434

      .. raw:: html

         <a href="../requirements_engineering/index.html"
            class="sd-btn sd-btn-primary sd-text-wrap"
            style="margin-top:12px;display:inline-block;">
           Open Training Portal →
         </a>

Training Source and Build
-------------------------

Each training is maintained under
``process/trainings/<training_name>/source/`` as editable Markdown files and
rebuilt automatically whenever the documentation is built via
``bazel run //:docs``.

To rebuild a specific training manually:

.. code-block:: bash

   cd process/trainings/trainings_requirements_engineering/source
   python build.py

Adding a new training
---------------------

1. Copy the template from ``process/trainings/trainings_templates/content/``
   into a new ``trainings_<area>/source/content/`` directory.
2. Copy ``build.py``, ``template.html``, ``requirements.txt``, and ``assets/``
   from an existing training source folder.
3. Update the ``MODULES`` array in ``assets/app.js`` and the ``OUT`` path in
   ``build.py``.
4. Add a grid card above pointing to the generated portal.
