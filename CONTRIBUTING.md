# Contributing to Consulting Bench

Consulting Bench follows the same Harbor task layout as
[Terminal-Bench](https://github.com/harbor-framework/terminal-bench-2-1).
New work should land as a pull request against `main`.

## Prerequisites

- [Harbor](https://www.harborframework.com/docs)
- Docker (for `harbor run`) or just Python 3.11+ (for local oracle checks)
- Copy `.env.example` to `.env` if you are running a model-backed agent

## Add or change a task

Each task lives under `tasks/<TASK-ID>/` and must include:

```
tasks/CIP-054/
├── task.toml
├── instruction.md
├── environment/
│   ├── Dockerfile
│   └── matter/
├── matter/                 # local-oracle convenience copy of the exhibits
├── tests/
│   ├── test.sh
│   └── verify.py
└── solution/
    └── solve.sh
```

See [docs/task-format.md](docs/task-format.md) for the deliverable contract
and verifier rules.

Before opening a PR:

1. `python3 scripts/validate_task_fields.py` — required files and `task.toml` fields
2. `bash scripts/verify_oracles_local.sh CIP-054` — oracle produces reward `1`
3. Prefer `harbor run -p tasks/CIP-054 -a oracle` if Docker is available

`task.toml` `[task].name` must be unique and stay in `management-consulting-bench/cip-XXX`
form until a dataset rename is coordinated.

## Pull requests

Use the PR template. Task PRs should say what the partner is asking, how the
verifier checks it, and that the oracle still passes. Do not put the numeric
answer in `instruction.md` or in matter files.

## Development notes

See [docs/development.md](docs/development.md) for the remaining check and
run helpers.
