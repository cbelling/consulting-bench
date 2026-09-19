#!/usr/bin/env python3
"""Validate Harbor task folders against the Consulting Bench contract.

Mirrors the Terminal-Bench "validate task fields" CI check: every task under
tasks/ must have the required Harbor files and a consistent task.toml.
Folder names are kebab-case written slugs, like Terminal-Bench.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

from task_slugs import CIP_TO_SLUG, NAME_PREFIX, SLUG_TO_CIP

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"
REQUIRED_FILES = (
    "task.toml",
    "instruction.md",
    "environment/Dockerfile",
    "tests/test.sh",
    "tests/verify.py",
    "solution/solve.sh",
)
REQUIRED_DIFFICULTIES = {"l1", "l2", "l3"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def validate_task(task_dir: Path) -> list[str]:
    errors: list[str] = []
    tid = task_dir.name

    if not SLUG_RE.fullmatch(tid):
        errors.append(f"{tid}: folder name must be kebab-case (lowercase letters, digits, hyphens)")

    for rel in REQUIRED_FILES:
        if not (task_dir / rel).is_file():
            errors.append(f"{tid}: missing {rel}")

    matter = task_dir / "environment" / "matter"
    if not matter.is_dir() or not any(matter.iterdir()):
        errors.append(f"{tid}: environment/matter/ is missing or empty")

    toml_path = task_dir / "task.toml"
    if not toml_path.is_file():
        return errors

    try:
        data = tomllib.loads(toml_path.read_text())
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"{tid}: invalid task.toml ({exc})")
        return errors

    task = data.get("task") or {}
    meta = data.get("metadata") or {}
    name = task.get("name")
    description = task.get("description")
    schema = data.get("schema_version")
    task_id = meta.get("task_id")
    legacy_id = meta.get("legacy_id")
    difficulty = meta.get("difficulty")
    category = meta.get("category")
    delivery = meta.get("delivery")

    if schema != "1.4":
        errors.append(f"{tid}: schema_version must be 1.4, got {schema!r}")
    if not isinstance(name, str) or not name.startswith(NAME_PREFIX):
        errors.append(f"{tid}: [task].name must start with {NAME_PREFIX!r}")
    elif name != f"{NAME_PREFIX}{tid}":
        errors.append(f"{tid}: [task].name {name!r} does not match folder")
    if not description:
        errors.append(f"{tid}: [task].description is required")
    if task_id != tid:
        errors.append(f"{tid}: [metadata].task_id must equal folder name")
    expected_legacy = SLUG_TO_CIP.get(tid)
    if expected_legacy and legacy_id != expected_legacy:
        errors.append(f"{tid}: [metadata].legacy_id must be {expected_legacy!r}")
    elif tid in CIP_TO_SLUG:
        errors.append(f"{tid}: folder still uses a CIP-XXX id; rename to {CIP_TO_SLUG[tid]!r}")
    if difficulty not in REQUIRED_DIFFICULTIES:
        errors.append(f"{tid}: [metadata].difficulty must be one of {sorted(REQUIRED_DIFFICULTIES)}")
    if not category:
        errors.append(f"{tid}: [metadata].category is required")
    if delivery != "memo-plus-json":
        errors.append(f"{tid}: [metadata].delivery must be 'memo-plus-json'")

    instruction = task_dir / "instruction.md"
    if instruction.is_file() and not instruction.read_text().strip():
        errors.append(f"{tid}: instruction.md is empty")

    return errors


def main() -> int:
    task_dirs = sorted(p for p in TASKS_DIR.iterdir() if p.is_dir())
    if not task_dirs:
        fail("no task directories found under tasks/")
        return 1

    names: dict[str, str] = {}
    legacy_ids: dict[str, str] = {}
    errors: list[str] = []
    for task_dir in task_dirs:
        errors.extend(validate_task(task_dir))
        toml_path = task_dir / "task.toml"
        if toml_path.is_file():
            try:
                data = tomllib.loads(toml_path.read_text())
            except tomllib.TOMLDecodeError:
                continue
            name = data.get("task", {}).get("name")
            if isinstance(name, str):
                if name in names:
                    errors.append(f"{task_dir.name}: duplicate [task].name {name!r} (also {names[name]})")
                names[name] = task_dir.name
            legacy = data.get("metadata", {}).get("legacy_id")
            if isinstance(legacy, str):
                if legacy in legacy_ids:
                    errors.append(
                        f"{task_dir.name}: duplicate [metadata].legacy_id {legacy!r} (also {legacy_ids[legacy]})"
                    )
                legacy_ids[legacy] = task_dir.name

    if len(task_dirs) != 50:
        errors.append(f"expected 50 task folders, found {len(task_dirs)}")

    if errors:
        for item in errors:
            fail(item)
        print(f"Failed: {len(errors)} issue(s) across {len(task_dirs)} tasks", file=sys.stderr)
        return 1

    print(f"OK: {len(task_dirs)} tasks passed field validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
