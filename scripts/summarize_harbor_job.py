#!/usr/bin/env python3
"""Write evals/<job>-results.json from a Harbor job directory."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"


def task_level(task_id: str) -> str:
    toml = TASKS_DIR / task_id / "task.toml"
    if not toml.exists():
        return "unknown"
    for line in toml.read_text().splitlines():
        if line.startswith("difficulty"):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            return value.upper()
    return "unknown"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def summarize(job_dir: Path) -> dict:
    job = load_json(job_dir / "result.json")
    stats = job.get("stats") or {}
    evals = stats.get("evals") or {}
    eval_block = next(iter(evals.values()), {}) if evals else {}
    reward_stats = ((eval_block.get("reward_stats") or {}).get("reward")) or {}

    passed = sorted({name.split("__", 1)[0] for name in reward_stats.get("1.0") or []})
    failed = sorted({name.split("__", 1)[0] for name in reward_stats.get("0.0") or []})

    started = job.get("started_at")
    finished = job.get("finished_at") or job.get("updated_at")
    runtime_sec = None
    if started and finished:
        try:
            t0 = datetime.fromisoformat(started.replace("Z", "+00:00"))
            t1 = datetime.fromisoformat(finished.replace("Z", "+00:00"))
            runtime_sec = int((t1 - t0).total_seconds())
        except ValueError:
            runtime_sec = None

    model = None
    trials = []
    errors = 0
    for child in sorted(job_dir.iterdir()):
        result_path = child / "result.json"
        if not result_path.exists():
            continue
        trial = load_json(result_path)
        name = trial.get("trial_name") or child.name
        task_id = name.split("__", 1)[0]
        agent = trial.get("agent_result") or {}
        verifier = trial.get("verifier_result") or {}
        rewards = verifier.get("rewards") or {}
        reward = rewards.get("reward")
        if reward is None and trial.get("exception_info"):
            errors += 1
        if model is None:
            agent_cfg = (trial.get("config") or {}).get("agent") or {}
            model = agent_cfg.get("model_name")
        trials.append(
            {
                "task": task_id,
                "level": task_level(task_id),
                "reward": reward,
                "episodes": ((agent.get("metadata") or {}).get("n_episodes")),
                "cost_usd": agent.get("cost_usd"),
                "n_input_tokens": agent.get("n_input_tokens"),
                "n_output_tokens": agent.get("n_output_tokens"),
                "exception": (trial.get("exception_info") or {}).get("exception_type")
                if trial.get("exception_info")
                else None,
            }
        )

    n_pass = sum(1 for t in trials if t.get("reward") == 1.0)
    n_fail = sum(1 for t in trials if t.get("reward") == 0.0)
    n_trials = len(trials)
    mean = (n_pass / n_trials) if n_trials else None

    return {
        "job_name": job_dir.name,
        "finished_at": finished,
        "environment": "modal",
        "agent": "terminus-2",
        "model": model,
        "n_concurrent_trials": 20,
        "n_trials": n_trials,
        "n_pass": n_pass,
        "n_fail": n_fail,
        "n_errors": errors or stats.get("n_errored_trials") or 0,
        "mean_reward": mean,
        "total_runtime_sec": runtime_sec,
        "cost_usd": stats.get("cost_usd"),
        "n_input_tokens": stats.get("n_input_tokens"),
        "n_output_tokens": stats.get("n_output_tokens"),
        "failed_tasks": failed or [t["task"] for t in trials if t.get("reward") == 0.0],
        "passed_tasks": passed or [t["task"] for t in trials if t.get("reward") == 1.0],
        "trials": trials,
        "summarized_at": datetime.now(timezone.utc).isoformat(),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: summarize_harbor_job.py <job-dir>", file=sys.stderr)
        return 2
    job_dir = Path(sys.argv[1]).resolve()
    if not (job_dir / "result.json").exists():
        print(f"missing {job_dir / 'result.json'}", file=sys.stderr)
        return 2
    summary = summarize(job_dir)
    out = ROOT / "evals" / f"{job_dir.name}-results.json"
    out.write_text(json.dumps(summary, indent=2) + "\n")
    print(
        f"wrote {out}  {summary['n_pass']}/{summary['n_trials']}  "
        f"${summary['cost_usd'] or 0:.2f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
