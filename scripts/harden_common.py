#!/usr/bin/env python3
"""Shared Harbor task writer used by the hardened Partner-50 generators."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "tasks"

DOCKERFILE = """\
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \\
        bash \\
        tmux \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN mkdir -p /app/matter /app/output

COPY matter/ /app/matter/
"""

TASK_TOML = """\
schema_version = "1.4"

[task]
name = "management-consulting-bench/{task_id_lower}"
version = "1.1.0"
description = "{description}"
authors = [{{ name = "Management Consulting Bench", email = "bench@example.com" }}]
keywords = ["consulting", "management-consulting", "{level}", "partner-delegated"]

[metadata]
task_id = "{task_id}"
family = "management-consulting"
difficulty = "{level}"
category = "{category}"
delivery = "memo-plus-json"

[verifier]
timeout_sec = 180.0

[agent]
timeout_sec = 900.0

[environment]
network_mode = "no-network"
build_timeout_sec = 300.0
cpus = 1
memory_mb = 1024
storage_mb = 5120
"""

TEST_SH = """\
#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier
MEMO="/app/output/memo.md"
ANSWER="/app/output/answer.json"

if python3 /tests/verify.py "$MEMO" "$ANSWER"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
"""

FIRST_PARAGRAPH = '''
import json
import re
import sys


def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\\r\\n", "\\n").strip().split("\\n\\n") if c.strip()]
    for c in chunks:
        first = c.split("\\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        if re.fullmatch(r"[-*_ ]{3,}", first):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""
'''


def render_verify(
    *,
    lede_any: list[str],
    lede_all: list[str] | None = None,
    decision: str | list[str] | None,
    bands: list[tuple[str, float, float]],
    method_all: list[str] | None = None,
    method_any: list[str] | None = None,
    next_any: list[str],
    reject_values: list[tuple[str, float]] | None = None,
) -> str:
    """Build an all-pass programmatic verifier from structured checks."""
    lede_all = lede_all or []
    method_all = method_all or []
    method_any = method_any or []
    reject_values = reject_values or []

    band_lines = []
    for key, lo, hi in bands:
        band_lines.append(f"    {key} = float(ans[{key!r}])")
        band_lines.append(f"    checks.append({lo} <= {key} <= {hi})")

    if decision is None:
        dec_line = "    # no exact decision required"
    elif isinstance(decision, list):
        dec_line = f"    checks.append(str(ans.get('decision', '')).lower() in { [d.lower() for d in decision]!r })"
    else:
        dec_line = f"    checks.append(str(ans.get('decision', '')).lower() == {decision.lower()!r})"

    reject_lines = []
    for key, val in reject_values:
        reject_lines.append(
            f"    checks.append(abs(float(ans[{key!r}]) - {val}) > 1e-6)"
        )

    return textwrap.dedent(
        FIRST_PARAGRAPH
        + f"""
def main() -> bool:
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path, encoding="utf-8").read()
    ans = json.load(open(answer_path, encoding="utf-8"))
    para = first_paragraph(memo)
    body = memo.lower()
    checks = []

    checks.append(all(tok in para for tok in {lede_all!r}))
    checks.append(any(tok in para for tok in {lede_any!r}))
    checks.append("monitor risks" not in body)
{dec_line}
{chr(10).join(band_lines) if band_lines else "    # no numeric bands"}
{chr(10).join(reject_lines) if reject_lines else "    # no trap-value rejects"}
    checks.append(all(tok in body for tok in {method_all!r}))
    checks.append(any(tok in body for tok in {method_any!r}) if {bool(method_any)!r} else True)
    checks.append(any(tok in body for tok in {next_any!r}))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
"""
    )


def write_task(task_id: str, spec: dict) -> None:
    task_dir = TASKS / task_id
    (task_dir / "environment" / "matter").mkdir(parents=True, exist_ok=True)
    (task_dir / "matter").mkdir(parents=True, exist_ok=True)
    (task_dir / "tests").mkdir(parents=True, exist_ok=True)
    (task_dir / "solution").mkdir(parents=True, exist_ok=True)
    (task_dir / "oracle").mkdir(parents=True, exist_ok=True)

    (task_dir / "environment" / "Dockerfile").write_text(DOCKERFILE)
    (task_dir / "task.toml").write_text(
        TASK_TOML.format(
            task_id=task_id,
            task_id_lower=task_id.lower(),
            description=spec["description"],
            category=spec["category"],
            level=spec.get("level", "l2"),
        )
    )
    (task_dir / "instruction.md").write_text(spec["instruction"].strip() + "\n")

    # Drop leftover stub files so only the new exhibits ship.
    for folder in (task_dir / "matter", task_dir / "environment" / "matter"):
        for old in folder.glob("*"):
            if old.is_file():
                old.unlink()

    for name, content in spec["matter"].items():
        text = content.strip() + "\n"
        (task_dir / "matter" / name).write_text(text)
        (task_dir / "environment" / "matter" / name).write_text(text)

    (task_dir / "tests" / "verify.py").write_text(spec["verify_py"].strip() + "\n")
    test_sh = task_dir / "tests" / "test.sh"
    test_sh.write_text(TEST_SH)
    test_sh.chmod(0o755)

    solve_sh = task_dir / "solution" / "solve.sh"
    solve_sh.write_text(spec["solve_sh"].strip() + "\n")
    solve_sh.chmod(0o755)

    (task_dir / "oracle" / "README.md").write_text(
        f"# Oracle — {task_id}\n\n"
        f"Run `bash solution/solve.sh` to produce `/app/output/memo.md` and "
        f"`/app/output/answer.json`.\n\n"
        f"## answer.json\n\n```json\n{json.dumps(spec['oracle'], indent=2)}\n```\n"
    )


SPECS: dict[str, dict] = {}


def email(
    *,
    sender: str,
    practice: str,
    subject: str,
    date: str,
    body: str,
    schema: str,
    method_hint: str,
) -> str:
    return f"""
**From:** {sender}, Partner — {practice}
**To:** Associate case team
**Subject:** {subject}
**Date:** {date}

Team,

{body.strip()}

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{schema.strip()}
```

{method_hint.strip()}
End with a concrete client next step—not generic risk monitoring.

{sender.split()[0]}
"""


def case(
    *,
    task_id: str,
    level: str,
    category: str,
    description: str,
    instruction: str,
    matter: dict[str, str],
    oracle: dict,
    memo: str,
    lede_any: list[str],
    lede_all: list[str] | None = None,
    decision: str | list[str] | None,
    bands: list[tuple[str, float, float]],
    method_all: list[str],
    method_any: list[str] | None = None,
    next_any: list[str],
    reject_values: list[tuple[str, float]] | None = None,
) -> tuple[str, dict]:
    spec = {
        "level": level,
        "category": category,
        "description": description,
        "instruction": instruction,
        "matter": matter,
        "oracle": oracle,
        "verify_py": render_verify(
            lede_any=lede_any,
            lede_all=lede_all,
            decision=decision,
            bands=bands,
            method_all=method_all,
            method_any=method_any,
            next_any=next_any,
            reject_values=reject_values,
        ),
        "solve_sh": make_solve(memo, oracle),
    }
    return task_id, spec


def add(pair: tuple[str, dict]) -> None:
    tid, spec = pair
    SPECS[tid] = spec


def make_solve(memo: str, oracle: dict) -> str:
    return (
        "#!/bin/bash\n"
        "set -euo pipefail\n"
        "mkdir -p /app/output\n"
        "cat > /app/output/memo.md << 'MEMO_EOF'\n"
        f"{memo.strip()}\n"
        "MEMO_EOF\n"
        "cat > /app/output/answer.json << 'JSON_EOF'\n"
        f"{json.dumps(oracle, indent=2)}\n"
        "JSON_EOF\n"
    )
