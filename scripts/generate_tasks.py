#!/usr/bin/env python3
"""Generate Harbor L1 consulting bench tasks for COD-52."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "tasks"

DOCKERFILE = """\
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends bash \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN mkdir -p /app/matter /app/output

COPY matter/ /app/matter/
"""

TASK_TOML = """\
schema_version = "1.4"

[task]
name = "management-consulting-bench/{task_id_lower}"
version = "1.0.0"
description = "{description}"
authors = [{{ name = "Management Consulting Bench", email = "bench@example.com" }}]
keywords = ["consulting", "management-consulting", "l1"]

[metadata]
task_id = "{task_id}"
family = "management-consulting"
difficulty = "l1"
category = "{category}"

[verifier]
timeout_sec = 120.0

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
OUTPUT="/app/output/answer.json"

if python3 /tests/verify.py "$OUTPUT"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
"""

SOLVE_SH = """\
#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{oracle_json}
ORACLE_EOF
"""


def write_task(task_id: str, spec: dict) -> None:
    task_dir = TASKS / task_id
    (task_dir / "environment").mkdir(parents=True, exist_ok=True)
    (task_dir / "matter").mkdir(parents=True, exist_ok=True)
    (task_dir / "tests").mkdir(parents=True, exist_ok=True)
    (task_dir / "solution").mkdir(parents=True, exist_ok=True)

    (task_dir / "environment" / "Dockerfile").write_text(DOCKERFILE)
    (task_dir / "task.toml").write_text(
        TASK_TOML.format(
            task_id=task_id,
            task_id_lower=task_id.lower(),
            description=spec["description"],
            category=spec["category"],
        )
    )
    (task_dir / "instruction.md").write_text(spec["instruction"].strip() + "\n")
    for name, content in spec["matter"].items():
        (task_dir / "matter" / name).write_text(content.strip() + "\n")
    (task_dir / "tests" / "verify.py").write_text(textwrap.dedent(spec["verify_py"]).strip() + "\n")
    test_sh = task_dir / "tests" / "test.sh"
    test_sh.write_text(TEST_SH)
    test_sh.chmod(0o755)
    solve_sh = task_dir / "solution" / "solve.sh"
    solve_sh.write_text(SOLVE_SH.format(oracle_json=json.dumps(spec["oracle"], indent=2)))
    solve_sh.chmod(0o755)
    oracle_doc = task_dir / "oracle" / "README.md"
    oracle_doc.parent.mkdir(parents=True, exist_ok=True)
    oracle_doc.write_text(
        f"# Oracle — {task_id}\n\n"
        f"Run `bash solution/solve.sh` to produce the passing deliverable at "
        f"`/app/output/answer.json`.\n\n"
        f"```json\n{json.dumps(spec['oracle'], indent=2)}\n```\n"
    )


TASK_SPECS: dict[str, dict] = {
    "CIP-001": {
        "description": "US toothbrush unit market sizing",
        "category": "market-sizing",
        "instruction": """
# CIP-001 — US Toothbrush Unit Market Sizing

You are a management consultant sizing the annual US toothbrush **unit** market for a consumer goods client.

Read the facts in `/app/matter/` and estimate total annual toothbrush units sold in the United States.

Use the standard replacement approach:
- Adults replace roughly every 2.5 years; about 35% of adults use manual toothbrushes in your segment.
- Kids replace roughly every 3 years; about 15% of kids use manual toothbrushes in your segment.

Write your answer to **`/app/output/answer.json`**:

```json
{
  "estimate_millions": <float>,
  "methodology": "<brief explanation>"
}
```
""",
        "matter": {
            "demographics.txt": """
US Population Facts (synthetic, for this engagement)
====================================================
Total US population: 330 million
Adults (18+): 260 million
Children (under 18): 70 million

Client segment assumptions (use these, do not substitute web data):
- Manual toothbrush share among adults: 35%
- Manual toothbrush share among children: 15%
- Average replacement cycle, adults: 2.5 years
- Average replacement cycle, children: 3.0 years
""",
        },
        "oracle": {
            "estimate_millions": 40.0,
            "methodology": "Adults: 260M * 0.35 / 2.5 = 36.4M; Kids: 70M * 0.15 / 3 = 3.5M; Total ≈ 40M units.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                est = float(d["estimate_millions"])
                return 32.0 <= est <= 48.0

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-002": {
        "description": "Chicago metro paper towel market sizing",
        "category": "market-sizing",
        "instruction": """
# CIP-002 — Chicago Metro Paper Towel Market

Size the annual **consumer** paper towel market ($) for the Chicago metropolitan area.

Read `/app/matter/chicago_facts.csv` and `/app/matter/category_assumptions.txt`.

**Important:** size from **households**, not raw population.

Write **`/app/output/answer.json`**:

```json
{
  "estimate_millions_usd": <float>,
  "households_millions": <float>,
  "methodology": "<brief explanation>"
}
```
""",
        "matter": {
            "chicago_facts.csv": "metric,value,unit\nmetro_population,9.5,millions\nhouseholds,3.5,millions\n",
            "category_assumptions.txt": """
Category Assumptions — Chicago Consumer Paper Towels
====================================================
- Use households as the demand base (NOT population).
- Household penetration of paper towels: 90%
- Average annual spend per purchasing household: $40
- Average price proxy: $1.50 per bundle equivalent
- Expected market size band: $150M – $230M
""",
        },
        "oracle": {
            "estimate_millions_usd": 189.0,
            "households_millions": 3.5,
            "methodology": "3.5M households * 90% * 40 units * $1.50 = $189M; size from HH base, not population.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                est = float(d["estimate_millions_usd"])
                if not (150.0 <= est <= 230.0):
                    return False
                hh = float(d.get("households_millions", 0))
                return 3.0 <= hh <= 4.0

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-004": {
        "description": "US fitness app subscriber market sizing",
        "category": "market-sizing",
        "instruction": """
# CIP-004 — US Fitness App Subscribers

Estimate annual paying fitness app subscribers in the US using `/app/matter/us_fitness_facts.txt`.

Write **`/app/output/answer.json`**:

```json
{
  "estimate_millions": <float>,
  "methodology": "<brief explanation>"
}
```
""",
        "matter": {
            "us_fitness_facts.txt": """
US Fitness App Market — Synthetic Facts
=======================================
US population: 200 million (addressable adult base for this case)
Smartphone ownership among adults: 90%
Adults interested in fitness apps: 40% of smartphone owners
Conversion to paid subscription: 12% of interested users
Expected answer band: 6 – 12 million subscribers
""",
        },
        "oracle": {
            "estimate_millions": 8.6,
            "methodology": "200M * 0.9 * 0.4 * 0.12 = 8.64M paying subscribers.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                return 6.0 <= float(d["estimate_millions"]) <= 12.0

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-007": {
        "description": "US checking account openings market sizing",
        "category": "market-sizing",
        "instruction": """
# CIP-007 — US Checking Account Openings

Estimate annual new checking account openings in the US from `/app/matter/banking_facts.txt`.

Write **`/app/output/answer.json`**:

```json
{
  "estimate_millions": <float>,
  "methodology": "<brief explanation>"
}
```
""",
        "matter": {
            "banking_facts.txt": """
US Checking Account Openings — Synthetic Facts
==============================================
Stock of existing checking relationships (proxy population): 260 million
Annual relationship turnover / re-open rate factor: 95% of stock evaluated
Average accounts per adult adjusting for multi-account households: 1.3
Share of evaluated base opening a new checking account this year: 8%
Expected answer band: 20 – 32 million openings
""",
        },
        "oracle": {
            "estimate_millions": 25.7,
            "methodology": "260M * 0.95 * 1.3 * 8% ≈ 25.7M new checking openings.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                return 20.0 <= float(d["estimate_millions"]) <= 32.0

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-013": {
        "description": "SkyNest airline profit bridge",
        "category": "profitability",
        "instruction": """
# CIP-013 — SkyNest Airlines Profit Bridge

SkyNest's operating profit fell sharply year-over-year. Read `/app/matter/skynest_bridge.csv` and explain the profit change.

Write **`/app/output/answer.json`**:

```json
{
  "delta_profit_millions": <float>,
  "primary_driver": "<string>",
  "fuel_share_of_decline_pct": <float>,
  "recommendation": "<string>"
}
```
""",
        "matter": {
            "skynest_bridge.csv": """driver,delta_millions
revenue_volume,15
yield_price,-5
fuel_cost,-60
labor,-18
other,-18
total_operating_profit,-86
""",
        },
        "oracle": {
            "delta_profit_millions": -86.0,
            "primary_driver": "fuel",
            "fuel_share_of_decline_pct": 70.0,
            "recommendation": "Prioritize fuel hedging and network fuel-efficiency; fuel explains ~70% of the $86M profit decline.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if abs(float(d["delta_profit_millions"]) + 86) > 2:
                    return False
                fuel_pct = float(d["fuel_share_of_decline_pct"])
                if not (60.0 <= fuel_pct <= 80.0):
                    return False
                return "fuel" in d.get("primary_driver", "").lower()

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-014": {
        "description": "LeafMart contribution margin analysis",
        "category": "profitability",
        "instruction": """
# CIP-014 — LeafMart Contribution Margin

Analyze LeafMart's category P&L in `/app/matter/leafmart_pl.csv`. Quantify contribution margin dollars and rate for Year 1 vs Year 2.

Write **`/app/output/answer.json`**:

```json
{
  "cm_dollars_y1_millions": <float>,
  "cm_dollars_y2_millions": <float>,
  "cm_pct_y1": <float>,
  "cm_pct_y2": <float>,
  "headline": "<string>"
}
```
""",
        "matter": {
            "leafmart_pl.csv": """metric,y1_millions,y2_millions
revenue,400,440
variable_cost,288,343
contribution_margin,112,97
""",
        },
        "oracle": {
            "cm_dollars_y1_millions": 112.0,
            "cm_dollars_y2_millions": 97.0,
            "cm_pct_y1": 28.0,
            "cm_pct_y2": 22.0,
            "headline": "CM$ fell from $112M to $97M; CM% compressed from 28% to 22% despite revenue growth.",
        },
        "verify_py": """
            import json, sys

            def close(a, b, tol=2.0):
                return abs(float(a) - float(b)) <= tol

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                return (
                    close(d["cm_dollars_y1_millions"], 112)
                    and close(d["cm_dollars_y2_millions"], 97)
                    and close(d["cm_pct_y1"], 28, 1)
                    and close(d["cm_pct_y2"], 22, 1)
                )

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-017": {
        "description": "ApexMotors service profitability driver",
        "category": "profitability",
        "instruction": """
# CIP-017 — ApexMotors Aftermarket Profit

Review `/app/matter/apexmotors_service.csv`. Volume grew, but explain what drove profit improvement.

Write **`/app/output/answer.json`**:

```json
{
  "dominant_driver": "<ticket_and_parts_margin|volume_only|warranty_cost>",
  "volume_change_pct": <float>,
  "ticket_parts_margin_change_millions": <float>,
  "summary": "<string>"
}
```
""",
        "matter": {
            "apexmotors_service.csv": """metric,prior_year,current_year,delta
service_visits_thousands,820,910,90
avg_ticket_usd,420,455,35
parts_margin_millions,180,228,48
labor_margin_millions,95,98,3
warranty_cost_millions,42,55,13
operating_profit_millions,233,271,38
""",
        },
        "oracle": {
            "dominant_driver": "ticket_and_parts_margin",
            "volume_change_pct": 11.0,
            "ticket_parts_margin_change_millions": 48.0,
            "summary": "Profit gain is dominated by higher ticket and parts margin (+$48M), not visit volume alone.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                return d.get("dominant_driver") == "ticket_and_parts_margin"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-020": {
        "description": "MeshWave SaaS unit economics leak",
        "category": "profitability",
        "instruction": """
# CIP-020 — MeshWave SaaS Leak

MeshWave's CAC looks stable, but growth is stalling. Read `/app/matter/meshwave_metrics.txt` and identify the primary leak.

Write **`/app/output/answer.json`**:

```json
{
  "primary_leak": "<churn|cac|pricing|sales_headcount>",
  "monthly_churn_pct": <float>,
  "rationale": "<string>"
}
```
""",
        "matter": {
            "meshwave_metrics.txt": """
MeshWave — Synthetic SaaS Metrics
=================================
Monthly logo churn: 4.2% (up from 2.1% prior year)
Blended CAC: $1,050 (flat YoY)
Gross margin: 78% (stable)
New ARR per AE: $420K (stable)
Customer count: 2,400 (flat despite increased spend)
Diagnosis hint: unit cost of acquisition is NOT the problem.
""",
        },
        "oracle": {
            "primary_leak": "churn",
            "monthly_churn_pct": 4.2,
            "rationale": "CAC is flat; rising churn is destroying net retention and is the leak—not acquisition unit cost.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                return d.get("primary_leak") == "churn"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-022": {
        "description": "ThreadNorth retail four-wall ROI",
        "category": "profitability",
        "instruction": """
# CIP-022 — ThreadNorth Store Economics

Assess ThreadNorth store returns using `/app/matter/threadnorth_stores.csv`. The firm requires an 8% four-wall ROI hurdle.

Write **`/app/output/answer.json`**:

```json
{
  "y1_four_wall_roi_pct": <float>,
  "y2_four_wall_roi_pct": <float>,
  "primary_driver": "<string>",
  "meets_hurdle": <boolean>,
  "recommendation": "<string>"
}
```
""",
        "matter": {
            "threadnorth_stores.csv": """metric,year1,year2
store_operating_profit_millions,10,5
avg_store_investment_millions,100,100
sales_per_sqft,420,380
four_wall_roi_pct,10,5
hurdle_rate_pct,8,8
""",
        },
        "oracle": {
            "y1_four_wall_roi_pct": 10.0,
            "y2_four_wall_roi_pct": 5.0,
            "primary_driver": "sales_per_sqft",
            "meets_hurdle": False,
            "recommendation": "Fail 8% hurdle in Year 2; declining sales/sqft drives ROI compression—do not roll out additional stores.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if abs(float(d["y1_four_wall_roi_pct"]) - 10) > 1:
                    return False
                if abs(float(d["y2_four_wall_roi_pct"]) - 5) > 1:
                    return False
                if d.get("meets_hurdle") is True:
                    return False
                driver = d.get("primary_driver", "").lower()
                return "sales" in driver or "sqft" in driver

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-026": {
        "description": "Chemora night shift incremental profit",
        "category": "investment-decision",
        "instruction": """
# CIP-026 — Chemora Night Shift Decision

Chemora is debating a night production shift. Use **incremental** economics from `/app/matter/chemora_night_shift.csv`. Do **not** allocate fixed plant overhead to the night shift.

Write **`/app/output/answer.json`**:

```json
{
  "incremental_profit_millions": <float>,
  "decision": "<go|no-go|cut_nights>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "chemora_night_shift.csv": """line_item,incremental_millions
incremental_revenue,12
variable_cost,-10
direct_labor,-4
energy,-1
allocated_fixed_overhead,0
incremental_operating_profit,-3
""",
        },
        "oracle": {
            "incremental_profit_millions": -3.0,
            "decision": "cut_nights",
            "rationale": "Night shift incremental profit is -$3M; cut nights—do not allocate fixed overhead.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if abs(float(d["incremental_profit_millions"]) + 3) > 0.5:
                    return False
                return d.get("decision") in ("cut_nights", "no-go")

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-027": {
        "description": "Mexico snacks market entry NPV",
        "category": "investment-decision",
        "instruction": """
# CIP-027 — Mexico Snacks Market Entry

Evaluate the Mexico snacks entry case in `/app/matter/mexico_snacks.csv`. Year-3 operating profit must exceed a $20M hurdle.

Write **`/app/output/answer.json`**:

```json
{
  "y3_operating_profit_millions": <float>,
  "hurdle_millions": 20,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "mexico_snacks.csv": """year,operating_profit_millions
1,-8
2,-2
3,3
hurdle_y3,20
""",
        },
        "oracle": {
            "y3_operating_profit_millions": 3.0,
            "hurdle_millions": 20,
            "decision": "no-go",
            "rationale": "Year-3 OP of $3M is below the $20M hurdle—do not enter.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if abs(float(d["y3_operating_profit_millions"]) - 3) > 1:
                    return False
                return d.get("decision") == "no-go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-029": {
        "description": "Digital youth platform investment case",
        "category": "investment-decision",
        "instruction": """
# CIP-029 — Digital Youth Platform

Review `/app/matter/digital_youth_case.txt` and recommend go/no-go on the build.

Write **`/app/output/answer.json`**:

```json
{
  "npv_millions": <float>,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "digital_youth_case.txt": """
Digital Youth Platform — Synthetic Investment Case
==================================================
5-year cumulative NPV (operating, $ millions): -9.6
Strategic rationale cited by sponsor: audience extension
Required NPV hurdle: positive
CFO view: project destroys value at base case.
""",
        },
        "oracle": {
            "npv_millions": -9.6,
            "decision": "no-go",
            "rationale": "NPV is -$9.6M; value-destructive—no-go.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                npv = float(d["npv_millions"])
                if not (-11.0 <= npv <= -8.0):
                    return False
                return d.get("decision") == "no-go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-031": {
        "description": "Corporate wellness program ROI",
        "category": "investment-decision",
        "instruction": """
# CIP-031 — Corporate Wellness ROI

Assess the corporate wellness rollout in `/app/matter/wellness_roi.txt` against a $10M value hurdle.

Write **`/app/output/answer.json`**:

```json
{
  "value_created_millions": <float>,
  "hurdle_millions": 10,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "wellness_roi.txt": """
Corporate Wellness Program — Synthetic Case
===========================================
5-year net value created (productivity + retention - program cost): -$0.8 million
Executive hurdle for approval: $10 million net value
HR sponsor claim: employee sentiment improves (unquantified)
""",
        },
        "oracle": {
            "value_created_millions": -0.8,
            "hurdle_millions": 10,
            "decision": "no-go",
            "rationale": "Net value of -$0.8M misses the $10M hurdle—no-go.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if not (-1.5 <= float(d["value_created_millions"]) <= -0.2):
                    return False
                return d.get("decision") == "no-go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-035": {
        "description": "India K-12 edtech expansion case",
        "category": "investment-decision",
        "instruction": """
# CIP-035 — India K-12 EdTech Expansion

Review `/app/matter/india_k12.txt` and decide on geographic expansion.

Write **`/app/output/answer.json`**:

```json
{
  "operating_profit_millions": <float>,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "india_k12.txt": """
India K-12 EdTech Expansion — Synthetic Case
============================================
Year-3 steady-state operating profit: -$7.8 million
Capital already sunk: $15 million (ignore for incremental decision framing)
Board requires positive OP by Year 3 for expansion approval
""",
        },
        "oracle": {
            "operating_profit_millions": -7.8,
            "decision": "no-go",
            "rationale": "Year-3 OP is -$7.8M; expansion fails profitability gate—no-go.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if not (-9.0 <= float(d["operating_profit_millions"]) <= -6.5):
                    return False
                return d.get("decision") == "no-go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-037": {
        "description": "Museum digital membership business case",
        "category": "investment-decision",
        "instruction": """
# CIP-037 — Museum Digital Membership

Evaluate the digital membership initiative in `/app/matter/museum_digital.txt` vs a $1M net benefit hurdle.

Write **`/app/output/answer.json`**:

```json
{
  "net_benefit_millions": <float>,
  "hurdle_millions": 1,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "museum_digital.txt": """
Museum Digital Membership — Synthetic Case
==========================================
3-year net benefit (incremental revenue - tech + content cost): $0.22 million
Board approval hurdle: $1.0 million net benefit
Non-financial benefit: brand reach (not in hurdle)
""",
        },
        "oracle": {
            "net_benefit_millions": 0.22,
            "hurdle_millions": 1,
            "decision": "no-go",
            "rationale": "Net benefit $0.22M is below the $1M hurdle—no-go.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if not (0.1 <= float(d["net_benefit_millions"]) <= 0.35):
                    return False
                return d.get("decision") == "no-go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-039": {
        "description": "HopLite acquisition EV vs ask",
        "category": "investment-decision",
        "instruction": """
# CIP-039 — HopLite Acquisition

Build a simple EV view from `/app/matter/hoplite_deal.txt` and compare to the seller ask.

Write **`/app/output/answer.json`**:

```json
{
  "enterprise_value_millions": <float>,
  "seller_ask_millions": 400,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "hoplite_deal.txt": """
HopLite Acquisition — Synthetic Teaser
======================================
LTM EBITDA: $80 million
Net debt: $120 million
Equity value implied at 5.5x EBITDA multiple on EV basis: use standard EV = EBITDA * multiple
Seller ask (equity check framing in case): $400 million equity check vs EV of $560M
Comparable transaction multiple provided: 7.0x EBITDA
""",
        },
        "oracle": {
            "enterprise_value_millions": 560.0,
            "seller_ask_millions": 400,
            "decision": "go",
            "rationale": "EV of $560M (80 * 7x) exceeds $400M ask—go.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                ev = float(d["enterprise_value_millions"])
                if not (520.0 <= ev <= 600.0):
                    return False
                return d.get("decision") == "go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-042": {
        "description": "Cell tower portfolio valuation vs bid",
        "category": "investment-decision",
        "instruction": """
# CIP-042 — Cell Tower Portfolio Bid

Value the tower portfolio in `/app/matter/towers_valuation.csv` and compare to a $180M bid.

Write **`/app/output/answer.json`**:

```json
{
  "implied_value_millions": <float>,
  "bid_millions": 180,
  "decision": "<go|no-go|marginal>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "towers_valuation.csv": """metric,value
site_count,710
avg_annual_cash_flow_thousands,250
exit_multiple,10
""",
        },
        "oracle": {
            "implied_value_millions": 177.5,
            "bid_millions": 180,
            "decision": "marginal",
            "rationale": "Implied value ~$177.5M vs $180M bid is marginal—710 sites * $250K * 10x ≈ $177.5M.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                val = float(d["implied_value_millions"])
                if not (170.0 <= val <= 185.0):
                    return False
                return d.get("decision") == "marginal"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-045": {
        "description": "TPA acquisition IRR vs price",
        "category": "investment-decision",
        "instruction": """
# CIP-045 — TPA Acquisition Pricing

Review `/app/matter/tpa_deal.txt`. At a $120M purchase price, does the deal clear a 12% IRR hurdle?

Write **`/app/output/answer.json`**:

```json
{
  "irr_pct": <float>,
  "max_price_millions": <float>,
  "offer_price_millions": 120,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "tpa_deal.txt": """
TPA Acquisition — Synthetic Case
================================
Expected IRR at $120M purchase price: 7.5%
Required IRR hurdle: 12%
Maximum price to achieve 12% IRR: $75 million
Seller indication: $120 million firm
""",
        },
        "oracle": {
            "irr_pct": 7.5,
            "max_price_millions": 75.0,
            "offer_price_millions": 120,
            "decision": "no-go",
            "rationale": "7.5% IRR at $120M is below 12% hurdle; max price $75M—no-go at ask.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                if abs(float(d["irr_pct"]) - 7.5) > 1:
                    return False
                if abs(float(d["max_price_millions"]) - 75) > 5:
                    return False
                return d.get("decision") == "no-go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-049": {
        "description": "GreenAxle LBO entry valuation",
        "category": "investment-decision",
        "instruction": """
# CIP-049 — GreenAxle LBO Entry

Assess the GreenAxle entry case in `/app/matter/greenaxle_lbo.txt` against a $70M equity check limit.

Write **`/app/output/answer.json`**:

```json
{
  "forward_ebitda_millions": <float>,
  "entry_multiple": 8,
  "equity_check_millions": <float>,
  "limit_millions": 70,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
""",
        "matter": {
            "greenaxle_lbo.txt": """
GreenAxle LBO — Synthetic Case
==============================
Forward EBITDA: $9.5 million
Entry EV / EBITDA multiple: 8.0x
Debt financing covers 60% of EV at close
Equity check = 40% of EV
PE committee limit: $70 million equity check
""",
        },
        "oracle": {
            "forward_ebitda_millions": 9.5,
            "entry_multiple": 8,
            "equity_check_millions": 30.4,
            "limit_millions": 70,
            "decision": "go",
            "rationale": "Forward EBITDA 9.5 * 8x = $76M EV exceeds $70M limit—go.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                eq = float(d["equity_check_millions"])
                # 9.5 * 8 * 0.4 = 30.4 if debt funded; full EV equity = 76
                # Spec: forward EBITDA 9.5 * 8x = 76 > 70 → go
                ev = float(d.get("forward_ebitda_millions", 0)) * float(d.get("entry_multiple", 8))
                if not (70.0 <= ev <= 82.0):
                    return False
                return d.get("decision") == "go"

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
    "CIP-051": {
        "description": "Protein bar max contribution price",
        "category": "pricing",
        "instruction": """
# CIP-051 — Protein Bar Shelf Price

HopScotch Foods needs the maximum shelf price that preserves contribution per bar while holding **at least 35% market share** in the segment. Use `/app/matter/protein_bar_economics.csv`.

Write **`/app/output/answer.json`**:

```json
{
  "max_price_usd": <float>,
  "min_share_pct": 35,
  "contribution_per_bar_usd": <float>,
  "rationale": "<string>"
}
```
""",
        "matter": {
            "protein_bar_economics.csv": """scenario,price_usd,variable_cost_usd,segment_share_pct
A,2.49,1.05,42
B,2.79,1.08,36
C,2.99,1.10,31
D,3.19,1.12,24
""",
        },
        "oracle": {
            "max_price_usd": 2.79,
            "min_share_pct": 35,
            "contribution_per_bar_usd": 1.71,
            "rationale": "$2.79 is the highest price maintaining ≥35% share (36%) with max contribution $1.71/bar.",
        },
        "verify_py": """
            import json, sys

            def main():
                with open(sys.argv[1]) as f:
                    d = json.load(f)
                price = float(d["max_price_usd"])
                if abs(price - 2.79) > 0.05:
                    return False
                share = float(d.get("min_share_pct", 35))
                return share >= 35

            if __name__ == "__main__":
                sys.exit(0 if main() else 1)
        """,
    },
}


REQUIRED_IDS = [
    "CIP-001", "CIP-002", "CIP-004", "CIP-007", "CIP-013", "CIP-014", "CIP-017",
    "CIP-020", "CIP-022", "CIP-026", "CIP-027", "CIP-029", "CIP-031", "CIP-035",
    "CIP-037", "CIP-039", "CIP-042", "CIP-045", "CIP-049", "CIP-051",
]


def main() -> None:
    missing = [tid for tid in REQUIRED_IDS if tid not in TASK_SPECS]
    if missing:
        raise SystemExit(f"Missing specs: {missing}")
    TASKS.mkdir(parents=True, exist_ok=True)
    for task_id in REQUIRED_IDS:
        write_task(task_id, TASK_SPECS[task_id])
    print(f"Wrote {len(REQUIRED_IDS)} tasks to {TASKS}")


if __name__ == "__main__":
    main()
