# process_description

S-CORE process description

## Overview

The S-CORE process model aims to establish organization rules for developing open source software in the automotive industry, which can be used in safety and security context.

## Features

The process model provide processes, which conform to state-of the art standards

- ASPICE PAM 4.0
- ISO 26262
- ISO/SAE 21434
- ISO PAS 8926

## Building process documentation

#### Run a documentation build:

#### Integrate latest score main branch

```bash
bazel run //process:incremental_latest
bazel build //process:docs_latest
```

#### Integrate latest score release

This should also work with proxy configuration if latest is not working.

```bash
bazel run //process:incremental_release
bazel build //process:docs_release
```

#### Access your documentation at:

- `_build/` for incremental
- `bazel-bin/bazel-bin/<BUILD FILE FOLDER NAME>/docs/_build/html`

#### Getting IDE support

Create the virtual environment via `bazel run //process:ide_support`.\
If your IDE does not automatically ask you to activate the newly created environment you can activate it.

- In VSCode via `ctrl+p` => `Select Python Interpreter` then select `.venv/bin/python`
- In the terminal via `source .venv/bin/activate`

#### Format your documentation with:

```bash
bazel test //:format.test
bazel run //:format.fix
```

#### Find & fix missing copyright

```bash
bazel test //:copyright.test
bazel run //:copyright.fix
```

