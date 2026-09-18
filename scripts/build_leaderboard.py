#!/usr/bin/env python3
"""Build website/leaderboard.json and website/data.js from evals/*-results.json."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
WEBSITE = ROOT / "website"

TASK_CATALOG = [
    ("CIP-003", "L2", "AeroTread NB tire TAM (exclude cargo/spares)"),
    ("CIP-005", "L2", "US economy-hotel room revenue (exclude midscale)"),
    ("CIP-006", "L2", "India smartphone sell-out (exclude gray sell-in)"),
    ("CIP-010", "L3", "Piano tunings — unusual stock × frequency"),
    ("CIP-012", "L3", "Golf balls lost — conflicting exhibits"),
    ("CIP-015", "L3", "Hospital outpatient surgery profit gap"),
    ("CIP-016", "L2", "SaaS gross margin compression"),
    ("CIP-018", "L2", "Hotel F&B profit mix"),
    ("CIP-019", "L2", "Pharma plant utilization"),
    ("CIP-021", "L3", "Logistics last-mile Zone C contribution"),
    ("CIP-025", "L3", "Media streaming contribution layers"),
    ("CIP-028", "L3", "Hospital urgent-care adjacency"),
    ("CIP-030", "L2", "Airline new route"),
    ("CIP-032", "L3", "Battery materials entry — conflicting margins"),
    ("CIP-033", "L2", "Insurance pet adjacency"),
    ("CIP-034", "L2", "E-commerce 3P marketplace"),
    ("CIP-038", "L3", "Ag co-op DTC beef"),
    ("CIP-040", "L2", "CPG M&A organic brand"),
    ("CIP-041", "L2", "Hospital ASC acquisition"),
    ("CIP-043", "L2", "SaaS acqui-hire vs build"),
    ("CIP-044", "L3", "Retail distressed-store four-wall"),
    ("CIP-050", "L3", "Pharma rare-disease biotech EV"),
    ("CIP-052", "L3", "Airline bag-fee increase"),
    ("CIP-053", "L2", "SaaS pricing model"),
    ("CIP-054", "L1", "RestInn weekend dynamic pricing"),
    ("CIP-055", "L3", "Pharma co-pay assistance paths"),
    ("CIP-057", "L2", "Telecom unlimited repricing"),
    ("CIP-059", "L2", "Logistics dim-weight"),
    ("CIP-062", "L3", "Municipal water rates"),
    ("CIP-063", "L1", "Crunchora CPG distribution white space"),
    ("CIP-064", "L2", "Airline loyalty growth"),
    ("CIP-066", "L3", "SaaS NDR — CS vs Finance conflict"),
    ("CIP-067", "L2", "Grocery fresh growth"),
    ("CIP-070", "L3", "Media ad-tier growth"),
    ("CIP-075", "L1", "GreenPouch compostable bag go/no-go"),
    ("CIP-076", "L2", "Auto subscription feature"),
    ("CIP-077", "L2", "Bank BNPL feature"),
    ("CIP-079", "L3", "Pharma diagnostic kit"),
    ("CIP-084", "L2", "Industrial IoT spin"),
    ("CIP-085", "L2", "Retail media network"),
    ("CIP-087", "L3", "Energy community solar"),
    ("CIP-089", "L1", "HeroCo private-label response"),
    ("CIP-090", "L2", "Airline competitive response"),
    ("CIP-091", "L2", "SaaS freemium response"),
    ("CIP-093", "L3", "Retail e-comm price transparency"),
    ("CIP-096", "L3", "Airline cost turnaround"),
    ("CIP-097", "L2", "Retail store closures"),
    ("CIP-098", "L1", "CloudSaaS path to profitability"),
    ("CIP-099", "L3", "Hospital service-line turnaround"),
    ("CIP-100", "L2", "Nonprofit turnaround"),
]

# DeepSeek hardened-v1 token volume is the cost baseline for the other four.
BASELINE_IN = 1_077_282
BASELINE_OUT = 562_730
MODAL_USD_PER_PASS = 1.0

MODELS = [
    {
        "id": "deepseek-v4.1-flash",
        "display": "DeepSeek V4.1 Flash",
        "lab": "DeepSeek",
        "openrouter": "openrouter/deepseek/deepseek-v4.1-flash",
        "results_file": "hardened-v1-deepseek-v4.1-flash-concurrent-results.json",
        "job_name": "hardened-v1-deepseek-v4.1-flash-concurrent",
        "price_in_per_m": 0.15,
        "price_out_per_m": 0.60,
        "role": "cheap-model baseline",
    },
    {
        "id": "gpt-5.4",
        "display": "GPT-5.4",
        "lab": "OpenAI",
        "openrouter": "openrouter/openai/gpt-5.4",
        "results_file": "hardened-v1-gpt-5.4-concurrent-results.json",
        "job_name": "hardened-v1-gpt-5.4-concurrent",
        "price_in_per_m": 2.50,
        "price_out_per_m": 15.00,
        "role": "flagship",
    },
    {
        "id": "claude-haiku-4.5",
        "display": "Claude Haiku 4.5",
        "lab": "Anthropic",
        "openrouter": "openrouter/anthropic/claude-haiku-4.5",
        "results_file": "hardened-v1-claude-haiku-4.5-concurrent-results.json",
        "job_name": "hardened-v1-claude-haiku-4.5-concurrent",
        "price_in_per_m": 1.00,
        "price_out_per_m": 5.00,
        "role": "flagship",
    },
    {
        "id": "gemini-3.1-pro",
        "display": "Gemini 3.1 Pro",
        "lab": "Google",
        "openrouter": "openrouter/google/gemini-3.1-pro-preview",
        "results_file": "hardened-v1-gemini-3.1-pro-concurrent-results.json",
        "job_name": "hardened-v1-gemini-3.1-pro-concurrent",
        "price_in_per_m": 2.00,
        "price_out_per_m": 12.00,
        "role": "flagship",
    },
    {
        "id": "grok-4.6",
        "display": "Grok 4.6",
        "lab": "xAI",
        "openrouter": "openrouter/x-ai/grok-4.6",
        "results_file": "hardened-v1-grok-4.6-concurrent-results.json",
        "job_name": "hardened-v1-grok-4.6-concurrent",
        "price_in_per_m": 2.00,
        "price_out_per_m": 6.00,
        "role": "flagship",
    },
]


def llm_estimate(price_in: float, price_out: float, scale: float = 1.0) -> float:
    return (BASELINE_IN / 1e6) * price_in + (BASELINE_OUT / 1e6) * price_out * scale


def by_level(trials: list[dict]) -> dict:
    out: dict[str, dict] = {}
    for level in ("L1", "L2", "L3"):
        rows = [t for t in trials if t.get("level") == level]
        n = len(rows)
        n_pass = sum(1 for t in rows if t.get("reward") == 1.0)
        out[level] = {
            "n": n,
            "n_pass": n_pass,
            "mean": (n_pass / n) if n else None,
        }
    return out


def load_results(name: str) -> dict | None:
    path = EVALS / name
    if not path.exists():
        return None
    return json.loads(path.read_text())


def build() -> dict:
    models = []
    for spec in MODELS:
        results = load_results(spec["results_file"])
        est_1x = llm_estimate(spec["price_in_per_m"], spec["price_out_per_m"], 1.0)
        est_2x = llm_estimate(spec["price_in_per_m"], spec["price_out_per_m"], 2.0)
        entry = {
            "id": spec["id"],
            "display": spec["display"],
            "lab": spec["lab"],
            "openrouter": spec["openrouter"],
            "role": spec["role"],
            "job_name": spec["job_name"],
            "list_price_usd_per_m": {
                "input": spec["price_in_per_m"],
                "output": spec["price_out_per_m"],
            },
            "estimated_llm_usd": round(est_1x, 2),
            "estimated_llm_usd_2x_output": round(est_2x, 2),
            "status": "pending",
        }
        if results:
            trials = results.get("trials") or []
            entry.update(
                {
                    "status": "complete",
                    "n_trials": results.get("n_trials"),
                    "n_pass": results.get("n_pass"),
                    "n_fail": results.get("n_fail"),
                    "n_errors": results.get("n_errors"),
                    "mean_reward": results.get("mean_reward"),
                    "cost_usd": results.get("cost_usd"),
                    "n_input_tokens": results.get("n_input_tokens"),
                    "n_output_tokens": results.get("n_output_tokens"),
                    "total_runtime_sec": results.get("total_runtime_sec"),
                    "finished_at": results.get("finished_at"),
                    "failed_tasks": results.get("failed_tasks") or [],
                    "passed_tasks": results.get("passed_tasks")
                    or [t["task"] for t in trials if t.get("reward") == 1.0],
                    "by_level": by_level(trials) if trials else None,
                    "trials": [
                        {
                            "task": t.get("task"),
                            "level": t.get("level"),
                            "reward": t.get("reward"),
                            "exception": t.get("exception"),
                        }
                        for t in trials
                    ],
                }
            )
        models.append(entry)

    flagships = [m for m in MODELS if m["role"] == "flagship"]
    expected = sum(
        llm_estimate(m["price_in_per_m"], m["price_out_per_m"]) + MODAL_USD_PER_PASS
        for m in flagships
    )
    upper = sum(
        llm_estimate(m["price_in_per_m"], m["price_out_per_m"], 2.0) + MODAL_USD_PER_PASS
        for m in flagships
    )

    task_matrix = []
    for task_id, level, topic in TASK_CATALOG:
        row = {"id": task_id, "level": level, "topic": topic, "results": {}}
        for model in models:
            if model["status"] != "complete":
                row["results"][model["id"]] = None
                continue
            passed = set(model.get("passed_tasks") or [])
            failed = set(model.get("failed_tasks") or [])
            if task_id in passed:
                row["results"][model["id"]] = 1
            elif task_id in failed:
                row["results"][model["id"]] = 0
            else:
                row["results"][model["id"]] = None
        task_matrix.append(row)

    return {
        "bench": "Partner-50",
        "set": "hardened-v1",
        "n_tasks": 50,
        "mix": {"L1": 5, "L2": 25, "L3": 20},
        "environment": "modal",
        "agent": "terminus-2",
        "n_concurrent_trials": 20,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "cost_estimate": {
            "method": "Scale DeepSeek V4.1 Flash hardened-v1 token volume to OpenRouter list prices, plus ~$1 Modal per 50-task pass.",
            "baseline_job": "hardened-v1-deepseek-v4.1-flash-concurrent",
            "baseline_tokens": {"input": BASELINE_IN, "output": BASELINE_OUT},
            "modal_usd_per_pass": MODAL_USD_PER_PASS,
            "four_flagships_expected_usd": round(expected, 0),
            "four_flagships_upper_usd": round(upper, 0),
            "notes": (
                "Expected band is about $35–45 if token volume stays near the DeepSeek "
                "baseline. Upper band is about $70 if thinking models emit ~2× output tokens."
            ),
        },
        "models": models,
        "tasks": task_matrix,
    }


def main() -> None:
    WEBSITE.mkdir(parents=True, exist_ok=True)
    payload = build()
    (WEBSITE / "leaderboard.json").write_text(json.dumps(payload, indent=2) + "\n")
    (WEBSITE / "data.js").write_text(
        "window.LEADERBOARD = " + json.dumps(payload, indent=2) + ";\n"
    )
    complete = sum(1 for m in payload["models"] if m["status"] == "complete")
    print(f"wrote website/leaderboard.json  {complete}/{len(payload['models'])} models complete")


if __name__ == "__main__":
    main()
