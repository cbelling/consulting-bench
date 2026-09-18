#!/usr/bin/env python3
"""Generate five partner-delegated Harbor tasks for COD-55."""

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
keywords = ["consulting", "management-consulting", "l1", "partner-delegated"]

[metadata]
task_id = "{task_id}"
family = "management-consulting"
difficulty = "l1"
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
        )
    )
    (task_dir / "instruction.md").write_text(spec["instruction"].strip() + "\n")
    for name, content in spec["matter"].items():
        text = content.strip() + "\n"
        (task_dir / "matter" / name).write_text(text)
        (task_dir / "environment" / "matter" / name).write_text(text)
    (task_dir / "tests" / "verify.py").write_text(textwrap.dedent(spec["verify_py"]).strip() + "\n")
    test_sh = task_dir / "tests" / "test.sh"
    test_sh.write_text(TEST_SH)
    test_sh.chmod(0o755)

    solve_sh = task_dir / "solution" / "solve.sh"
    solve_sh.write_text(spec["solve_sh"].strip() + "\n")
    solve_sh.chmod(0o755)

    oracle_doc = task_dir / "oracle" / "README.md"
    oracle_doc.write_text(
        f"# Oracle — {task_id}\n\n"
        f"Run `bash solution/solve.sh` to produce `/app/output/memo.md` and "
        f"`/app/output/answer.json`.\n\n"
        f"## answer.json\n\n```json\n{json.dumps(spec['oracle'], indent=2)}\n```\n"
    )


TASK_SPECS: dict[str, dict] = {
    "CIP-054": {
        "description": "RestInn hotel weekend dynamic pricing optimization",
        "category": "pricing",
        "instruction": """
**From:** Elena Vasquez, Partner — Hospitality & Leisure
**To:** Associate case team
**Subject:** RestInn — weekend dynamic pricing before Monday walk-in
**Date:** Thursday, 4:00 PM

Team,

RestInn (100 rooms) wants a weekend-night pricing recommendation before Monday's owner walk-in. Revenue management sent occupancy/ADR scenarios in `/app/matter/restinn_weekend.csv`.

Please read the facts, size contribution margin per occupied room (ADR minus variable cost of $25/occupied night), and compare base vs. +10% vs. +20% weekend ADR premiums with the occupancy curves provided.

Deliverables due by **Friday 5 PM**:
1. A **one-page memo** at `/app/output/memo.md` suitable for a walk-in readout (recommendation in the opening paragraph).
2. Sidecar JSON at `/app/output/answer.json`:

```json
{
  "decision": "<base|premium_10|premium_20>",
  "optimal_premium_pct": <int>,
  "weekend_contribution_profit_dollars": <float>,
  "method": "<contribution margin tree>"
}
```

Use a clear contribution-margin decision tree in the memo. End with a concrete next step for the client—not generic risk monitoring.

Thanks,
Elena
""",
        "matter": {
            "restinn_weekend.csv": """
scenario,premium_pct,adr_usd,occupancy_pct,variable_cost_per_occ_usd
base,0,100,85,25
premium_10,10,110,80,25
premium_20,20,120,72,25
""".strip(),
            "modeling_note.txt": """
RestInn Weekend Pricing — Modeling Note (synthetic)
===================================================
Property: 100 rooms, single-night weekend focus.
Contribution per occupied room = ADR − variable cost ($25/occupied night).

Weekend contribution profit = rooms × occupancy × (ADR − $25).

Recalculated scenarios (100 rooms):
- Base (0% premium): 100 × 85% × ($100 − $25) = $6,375
- +10% premium:     100 × 80% × ($110 − $25) = $6,800
- +20% premium:     100 × 72% × ($120 − $25) = $6,840  ← optimal

The +20% premium uniquely maximizes weekend contribution profit.
""".strip(),
        },
        "oracle": {
            "decision": "premium_20",
            "optimal_premium_pct": 20,
            "weekend_contribution_profit_dollars": 6840.0,
            "method": "contribution margin tree",
        },
        "verify_py": '''
import json, sys

def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\\r\\n", "\\n").strip().split("\\n\\n") if c.strip()]
    for c in chunks:
        first = c.split("\\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = ("20" in para or "twenty" in para) and any(
        w in para for w in ("recommend", "premium", "optimal", "choose", "select")
    )
    profit = float(ans["weekend_contribution_profit_dollars"])
    band_ok = 6600.0 <= profit <= 7100.0 and ans.get("decision") == "premium_20"
    method_ok = "contribution" in memo.lower() and any(
        k in memo.lower() for k in ("adr", "occupancy", "variable cost")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("pilot", "implement", "roll out", "deploy", "a/b", "test in", "schedule", "sign off")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend the +20% weekend ADR premium for RestInn. It delivers the highest weekend contribution profit ($6,840) versus base ($6,375) and +10% ($6,800) on 100 rooms.

## Contribution margin tree
- Base: 100 rooms × 85% occupancy × ($100 ADR − $25 variable cost) = **$6,375**
- +10% premium: 100 × 80% × ($110 − $25) = **$6,800**
- +20% premium: 100 × 72% × ($120 − $25) = **$6,840** ← optimal

## Next step
Schedule a 6-week A/B test on two comparable properties before portfolio roll-out; Elena to sign off on test design Friday.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "premium_20",
  "optimal_premium_pct": 20,
  "weekend_contribution_profit_dollars": 6840.0,
  "method": "contribution margin tree"
}
JSON_EOF
''',
    },
    "CIP-063": {
        "description": "Crunchora CPG distribution white-space growth options",
        "category": "market-sizing",
        "instruction": """
**From:** Marcus Chen, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** Crunchora — $50M growth bridge for Tuesday IC prep
**Date:** Monday, 9:15 AM

Team,

Crunchora ($400M revenue today) needs a credible path to **+$50M in 24 months**. The CMO left three growth levers in `/app/matter/crunchora_growth.txt`.

Please compare distribution expansion, a new SKU launch, and a list-price move. Show incremental revenue math (including cannibalization where noted) and lead with a clear sequencing recommendation for the IC.

Deliverables by **Tuesday noon**:
1. One-page memo at `/app/output/memo.md` (recommendation in paragraph one).
2. JSON sidecar at `/app/output/answer.json`:

```json
{
  "decision": "<distribution_first|new_sku_first|price_first>",
  "distribution_incremental_millions": <float>,
  "method": "<option tree label>"
}
```

Frame the work as an option tree with explicit cannibalization on the SKU path. Close with a concrete client next step.

Best,
Marcus
""",
        "matter": {
            "crunchora_growth.txt": """
Crunchora Growth Options — Synthetic Facts
==========================================
Current revenue: $400M (24-month baseline)

Option A — Distribution / ACV white space
- Expand weighted distribution +15% with same per-store velocity
- Ramp realization: 80% of full theoretical uplift in 24 months
- Incremental revenue: $400M × 15% × 80% = **+$48M**

Option B — New SKU launch
- Gross incremental revenue: +$30M
- Cannibalization: 40% of gross uplift comes from existing SKUs
- Net incremental revenue: $30M × (1 − 40%) = **+$18M**

Option C — List price +3%
- Price elasticity: −0.8
- Volume impact: −0.8 × 3% = −2.4% volume
- Net revenue impact: (1 + 3%) × (1 − 2.4%) − 1 ≈ +0.5% → **~+$2M**

Sequencing: Option A dominates on incremental revenue; pursue distribution first.
""".strip(),
        },
        "oracle": {
            "decision": "distribution_first",
            "distribution_incremental_millions": 48.0,
            "method": "growth option tree with cannibalization",
        },
        "verify_py": '''
import json, sys

def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\\r\\n", "\\n").strip().split("\\n\\n") if c.strip()]
    for c in chunks:
        first = c.split("\\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = "distribution" in para and any(
        w in para for w in ("recommend", "first", "priorit", "lead", "sequence")
    )
    inc = float(ans["distribution_incremental_millions"])
    band_ok = 45.0 <= inc <= 51.0 and ans.get("decision") == "distribution_first"
    method_ok = "option" in memo.lower() and "cannibal" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("pilot", "roll out", "retailer", "launch plan", "sign off", "workshop", "field team", "reset")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend distribution expansion first for Crunchora. It yields ~+$48M incremental revenue in 24 months, ahead of a new SKU net +$18M (after 40% cannibalization) and a price move worth only ~+$2M.

## Growth option tree
| Option | Incremental revenue | Notes |
|--------|--------------------:|-------|
| A — Distribution +15% (80% ramp) | **+$48M** | Same velocity, white-space ACV |
| B — New SKU | +$18M net | $30M gross, 40% cannibalized |
| C — Price +3% (ε=−0.8) | ~+$2M | Volume −2.4% |

## Next step
Book a retailer reset workshop with the top-4 accounts in the week of the 18th to lock distribution targets before SKU design spend.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "distribution_first",
  "distribution_incremental_millions": 48.0,
  "method": "growth option tree with cannibalization"
}
JSON_EOF
''',
    },
    "CIP-075": {
        "description": "Compostable snack bag launch/no-go decision",
        "category": "investment-decision",
        "instruction": """
**From:** Priya Nair, Partner — Consumer Products
**To:** Associate case team
**Subject:** GreenPouch compostable bag — launch decision for Friday SteCo
**Date:** Wednesday, 2:30 PM

Team,

Our snack client is weighing a compostable bag (GreenPouch). Year-2 volume, premium, variable cost, cannibalization of the hero SKU, and launch opex are in `/app/matter/greenpouch_economics.txt`.

Hurdle: **Year-2 incremental operating profit ≥ $2M**. Build the incremental P&L explicitly.

Deliverables for **Friday SteCo**:
1. `/app/output/memo.md` — one-page memo with the launch/no-go call in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "incremental_profit_millions_y2": <float>,
  "method": "<incremental contribution formula>"
}
```

Use an incremental contribution formula (premium − incremental VC − cannibalization − launch opex). End with a concrete next action.

Priya
""",
        "matter": {
            "greenpouch_economics.txt": """
GreenPouch Compostable Bag — Incremental Economics (synthetic)
================================================================
Year-2 volume: 20M units
Price premium vs. hero bag: $0.20 per unit
Incremental variable cost: +$0.12 per unit
Unit contribution (premium − incremental VC): $0.08

Cannibalization: 40% of GreenPouch volume pulls from hero SKU
Hero SKU unit margin: $0.50

Launch opex (Year 2): $4.0M
Hurdle: Year-2 incremental operating profit ≥ $2.0M

Incremental P&L (Year 2):
- Gross contribution: 20M × $0.08 = $1.6M
- Cannibalization drag: 40% × 20M × $0.50 = $4.0M
- Launch opex: $4.0M
- **Incremental profit: $1.6M − $4.0M − $4.0M = −$6.4M** → **NO-GO**
""".strip(),
        },
        "oracle": {
            "decision": "no-go",
            "incremental_profit_millions_y2": -6.4,
            "method": "incremental contribution formula",
        },
        "verify_py": '''
import json, sys

def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\\r\\n", "\\n").strip().split("\\n\\n") if c.strip()]
    for c in chunks:
        first = c.split("\\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("no-go", "no go", "do not launch", "decline", "reject"))
    profit = float(ans["incremental_profit_millions_y2"])
    band_ok = -7.0 <= profit <= -5.8 and ans.get("decision") == "no-go"
    method_ok = "contribution" in memo.lower() and "cannibal" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("deprioritize", "kill", "pause", "redirect", "reallocate", "steerco", "sign off", "halt")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on GreenPouch. Year-2 incremental operating profit is −$6.4M, well below the $2M hurdle.

## Incremental contribution formula
- Unit contribution: $0.20 premium − $0.12 incremental VC = **$0.08**
- Gross contribution: 20M × $0.08 = **$1.6M**
- Cannibalization: 40% × 20M × $0.50 hero margin = **−$4.0M**
- Launch opex: **−$4.0M**
- **Incremental profit: −$6.4M**

## Next step
Deprioritize GreenPouch at Friday SteCo and redirect packaging R&D budget to the proven hero SKU cost-down initiative.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "incremental_profit_millions_y2": -6.4,
  "method": "incremental contribution formula"
}
JSON_EOF
''',
    },
    "CIP-089": {
        "description": "Hero brand private-label attack response options",
        "category": "pricing",
        "instruction": """
**From:** David Okonkwo, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** HeroCo — private-label response before Thursday exec session
**Date:** Tuesday, 11:00 AM

Team,

HeroCo's $100M hero line faces a private-label attack. Without action they lose 20% volume. Three responses—and a do-nothing baseline—are modeled in `/app/matter/heroco_pl_scenarios.csv`.

Build the full P&L for each option and pick the **profit-maximizing** response. Exactly one option should win; show your math.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo; state the winning option in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<match_price|promo|innovate|no_response>",
  "operating_profit_millions": <float>,
  "method": "<scenario P&L comparison>"
}
```

Use an explicit scenario P&L table. Close with a concrete next step for HeroCo leadership.

David
""",
        "matter": {
            "heroco_pl_scenarios.csv": """
option,units_m,price_usd,variable_cost_per_unit_usd,one_time_spend_m,description
no_response,0.80,100,55,0,Baseline 20% volume loss
match_price,1.00,75,55,0,Match PL price -25% keep volume
promo,0.88,85,55,0,15% promo; volume loss 12%
innovate,0.95,105,55,8,5% volume loss; +5% price; $8M innovation
""".strip(),
            "pl_calculation_note.txt": """
HeroCo Private-Label Response — P&L Calculation (synthetic)
===========================================================
Base reference: 1.0M units @ $100, VC $55/unit → $100M revenue, $45M gross margin (45%).

Operating profit = (units × price) − (units × VC) − one-time spend

Recalculated options:
- No response: 0.80M × $100 − 0.80M × $55 = **$36.0M**
- Match price (−25%): 1.00M × $75 − 1.00M × $55 = **$20.0M** (worst response)
- Promo (−15%, −12% vol): 0.88M × $85 − 0.88M × $55 = **$26.4M**
- Innovate (+5% price, −5% vol, $8M spend): 0.95M × $105 − 0.95M × $55 − $8M = **$39.5M** ← unique max

Innovate uniquely maximizes operating profit.
""".strip(),
        },
        "oracle": {
            "decision": "innovate",
            "operating_profit_millions": 39.5,
            "method": "scenario P&L comparison",
        },
        "verify_py": '''
import json, sys

def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\\r\\n", "\\n").strip().split("\\n\\n") if c.strip()]
    for c in chunks:
        first = c.split("\\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = "innov" in para and any(
        w in para for w in ("recommend", "choose", "select", "maxim", "best", "win")
    )
    profit = float(ans["operating_profit_millions"])
    band_ok = 38.0 <= profit <= 41.0 and ans.get("decision") == "innovate"
    method_ok = "p&l" in memo.lower() or "profit" in memo.lower()
    method_ok = method_ok and ("private label" in memo.lower() or "private-label" in memo.lower())
    next_ok = any(
        k in memo.lower()
        for k in ("approve", "fund", "launch", "pilot", "exec session", "sign off", "allocate", "workstream")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend the innovate response to HeroCo's private-label attack. It maximizes operating profit at $39.5M, beating no-response ($36.0M), promo ($26.4M), and full price match ($20.0M).

## Scenario P&L comparison
| Option | Operating profit ($M) |
|--------|----------------------:|
| No response (−20% vol) | 36.0 |
| Match PL price (−25%) | 20.0 |
| Promo (−15% price, −12% vol) | 26.4 |
| **Innovate (+5% price, −5% vol, $8M spend)** | **39.5** |

Private-label defense math: innovate = 0.95M units × ($105 − $55) − $8M = $39.5M.

## Next step
Approve the $8M innovation workstream at Thursday's exec session and assign a GM to ship reformulation by Q3.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "innovate",
  "operating_profit_millions": 39.5,
  "method": "scenario P&L comparison"
}
JSON_EOF
''',
    },
    "CIP-098": {
        "description": "CloudSaaS path to profitability — S&M vs R&D cut",
        "category": "profitability",
        "instruction": """
**From:** Rachel Kim, Partner — Technology & Analytics
**To:** Associate case team
**Subject:** CloudSaaS — breakeven path for board prep
**Date:** Monday, 8:00 AM

Team,

CloudSaaS is burning cash. Board deck shows **$80M ARR**, **70% gross margin**, **$50M S&M**, **$30M R&D**, **$15M G&A**. FP&A flagged a duplicate corp allocation in G&A—see `/app/matter/cloudsaas_pl.txt` for the corrected run-rate and two cost-cut scenarios.

Hurdle: **operating breakeven within four quarters**. Compare (A) cut S&M 30% with growth slowing to 5% ARR over 4Q vs. (B) cut R&D 20% while holding growth at 10% ARR over 4Q.

Deliverables by **Tuesday 3 PM**:
1. `/app/output/memo.md` — recommend one path in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<sm_cut|rd_cut>",
  "q4_operating_profit_millions": <float>,
  "method": "<four-quarter breakeven P&L>"
}
```

Show a four-quarter breakeven P&L. Note the single FP&A correction in the memo body. End with a concrete board/next-step ask.

Rachel
""",
        "matter": {
            "cloudsaas_pl.txt": """
CloudSaaS — Path to Profitability Model (synthetic)
===================================================

Board deck (Q0):
- ARR: $80M  |  Gross margin: 70% (board)  |  Quarterly revenue: $20.0M
- S&M: $50M/yr  |  R&D: $30M/yr  |  G&A: $15M/yr  |  Opex: $95M/yr ($23.75M/q)

FP&A correction (ONE adjustment):
Duplicate HQ allocation inflated G&A, and COGS was overstated in the board deck.
- Correct run-rate G&A: **$9M/yr ($2.25M/q)** (was $15M)
- Correct run-rate gross margin: **88%** (was 70% pre-allocation)
- Correct Q0 quarterly GP: **$17.60M** | Correct Q0 opex: **$22.25M/q** | Q0 op loss: **−$4.65M/q**

Scenario A — Cut S&M 30% (to $35M/yr = $8.75M/q); ARR grows 5% over 4 quarters to $84M
  Q4 quarterly revenue: $84M / 4 = **$21.0M**
  Q4 quarterly GP (88% × $21.0M) = **$18.48M**
  Q4 opex = $8.75M + $7.50M + $2.25M = **$18.50M/q**
  Q4 operating profit = $18.48M − $18.50M = **−$0.02M (~breakeven)** ✓

Scenario B — Cut R&D 20% (to $24M/yr = $6.0M/q); ARR grows 10% over 4 quarters to $88M
  Q4 quarterly revenue: $88M / 4 = **$22.0M**
  Q4 quarterly GP (88% × $22.0M) = **$19.36M**
  Q4 opex = $12.50M + $6.00M + $2.25M = **$20.75M/q**
  Q4 operating profit = $19.36M − $20.75M = **−$1.39M** ✗ (misses 4Q breakeven hurdle)

Arithmetic check (must tie):
- Scenario A: $18.48M − $18.50M = −$0.02M (within breakeven band −$0.5M to +$1.0M)
- Scenario B: $19.36M − $20.75M = −$1.39M (below breakeven band)

Recommendation: Scenario A (S&M cut) uniquely meets the 4-quarter breakeven hurdle.
""".strip(),
        },
        "oracle": {
            "decision": "sm_cut",
            "q4_operating_profit_millions": -0.02,
            "method": "four-quarter breakeven P&L",
        },
        "verify_py": '''
import json, sys

def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\\r\\n", "\\n").strip().split("\\n\\n") if c.strip()]
    for c in chunks:
        first = c.split("\\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = ("s&m" in para or "sm" in para or "sales" in para) and any(
        w in para for w in ("recommend", "cut", "reduce", "choose")
    )
    q4 = float(ans["q4_operating_profit_millions"])
    band_ok = -0.5 <= q4 <= 1.0 and ans.get("decision") in ("sm_cut", "s_m_cut")
    method_ok = "breakeven" in memo.lower() or "break-even" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("quarter", "q4", "four-quarter"))
    next_ok = any(
        k in memo.lower()
        for k in ("board", "approve", "sign off", "implement", "reforecast", "headcount", "plan")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend cutting S&M by 30% at CloudSaaS. After the FP&A corrections (G&A $15M → $9M run-rate and gross margin true-up to 88%), the S&M-cut path reaches −$0.02M Q4 operating profit (~breakeven) while the R&D-cut path remains at −$1.39M.

## Four-quarter breakeven P&L (Q4 run-rate)
| Scenario | Q4 ARR | Q4 GP | Q4 Opex | Q4 Op profit |
|----------|-------:|------:|--------:|-------------:|
| A — S&M −30%, 5% growth | $84M | $18.48M | $18.50M | **−$0.02M** |
| B — R&D −20%, 10% growth | $88M | $19.36M | $20.75M | −$1.39M |

FP&A noted one correction bundle: duplicate HQ allocation removed from G&A and COGS reclassified (GM 70% → 88% run-rate).

## Next step
Ask the board Tuesday to approve the S&M reduction plan and reforecast hiring to match 5% growth.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "sm_cut",
  "q4_operating_profit_millions": -0.02,
  "method": "four-quarter breakeven P&L"
}
JSON_EOF
''',
    },
}


def main() -> None:
    for task_id, spec in TASK_SPECS.items():
        write_task(task_id, spec)
        print(f"Wrote {task_id}")


if __name__ == "__main__":
    main()
