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

```bash
bazel run //process:incremental
bazel build //process:docs
bazel run //process:ide_support
```

#### Access your documentation at:

- `_build/` for incremental
- `bazel-bin/bazel-bin/<BUILD FILE FOLDER NAME>/docs/_build/html`

#### Format your documentation with:

```bash
bazel test //:format.test
bazel run //:format.fix
```