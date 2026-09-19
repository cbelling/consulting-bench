#!/usr/bin/env python3
"""Generate ten hard L3 partner-delegated Harbor tasks for COD-57."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

from task_slugs import folder_slug, harbor_name, legacy_cip

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
name = "{harbor_name}"
version = "1.0.0"
description = "{description}"
authors = [{{ name = "Management Consulting Bench", email = "bench@example.com" }}]
keywords = ["consulting", "management-consulting", "l3", "partner-delegated", "frontier-probe"]

[metadata]
task_id = "{task_id}"
legacy_id = "{legacy_id}"
family = "management-consulting"
difficulty = "l3"
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

FIRST_PARAGRAPH_HELPER = '''
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
'''


def write_task(task_id: str, spec: dict) -> None:
    slug = folder_slug(task_id)
    task_dir = TASKS / slug
    (task_dir / "environment" / "matter").mkdir(parents=True, exist_ok=True)
    (task_dir / "matter").mkdir(parents=True, exist_ok=True)
    (task_dir / "tests").mkdir(parents=True, exist_ok=True)
    (task_dir / "solution").mkdir(parents=True, exist_ok=True)
    (task_dir / "oracle").mkdir(parents=True, exist_ok=True)

    (task_dir / "environment" / "Dockerfile").write_text(DOCKERFILE)
    (task_dir / "task.toml").write_text(
        TASK_TOML.format(
            harbor_name=harbor_name(task_id),
            task_id=slug,
            legacy_id=legacy_cip(task_id),
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
        f"# Oracle — {slug}\n\n"
        f"Run `bash solution/solve.sh` to produce `/app/output/memo.md` and "
        f"`/app/output/answer.json`.\n\n"
        f"## answer.json\n\n```json\n{json.dumps(spec['oracle'], indent=2)}\n```\n"
    )


TASK_SPECS: dict[str, dict] = {
    "CIP-015": {
        "description": "Hospital outpatient surgery profit gap — cash EBITDA hurdle",
        "category": "profitability",
        "instruction": """
**From:** Dr. Amara Osei, Partner — Healthcare Services
**To:** Associate case team
**Subject:** Meridian ASC — outpatient surgery profit gap before Thursday board
**Date:** Tuesday, 3:45 PM

Team,

Meridian's outpatient surgery center reports **$200M revenue** and **$40M EBITDA** (20% margin). The CFO and the OR materials team sent conflicting implant under-accrual exhibits in `/app/matter/`. FP&A also flagged **8% uncollected receivables** on outpatient revenue.

Two capacity scenarios (C-Low and C-High) are in `/app/matter/meridian_asc_scenarios.csv`. Hurdle from the board: **≥15% cash EBITDA margin** on revenue after resolving the accrual conflict and uncollected adjustment.

Reconcile the exhibits, show **both** C scenarios against the hurdle, and lead with a go/no-go on further outpatient expansion.

Deliverables by **Wednesday 6 PM**:
1. `/app/output/memo.md` — one-page memo (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<no-go|go>",
  "scenario_c_low_cash_ebitda_margin_pct": <float>,
  "scenario_c_high_cash_ebitda_margin_pct": <float>,
  "method": "<cash EBITDA bridge>"
}
```

Use an explicit cash EBITDA bridge. End with a concrete diligence next step—not generic risk monitoring.

Amara
""",
        "matter": {
            "cfo_implant_accrual_memo.txt": """
Meridian ASC — CFO Implant Under-Accrual Memo (Exhibit A)
=========================================================
Reported outpatient EBITDA: $40.0M on $200.0M revenue (20.0%)

Implant vendor accrual understatement identified in Q3 audit:
- Under-accrual adjustment required: **$12.0M**
- Cash EBITDA after adjustment: $40.0M − $12.0M = **$28.0M** (14.0% margin)

Note: Does NOT yet reflect uncollected receivables.
""".strip(),
            "or_materials_review.txt": """
Meridian ASC — OR Materials Team Review (Exhibit B)
===================================================
Implant under-accrual review (independent count):
- Under-accrual adjustment: **$4.0M** (OR believes CFO double-counted consignment)
- Cash EBITDA after adjustment: $40.0M − $4.0M = **$36.0M** (18.0% margin)

⚠️ OR spreadsheet total on page 3 shows $8.0M — **arithmetic error**; use $4.0M line items.
""".strip(),
            "fpa_collections_note.txt": """
FP&A Collections Note
=====================
Outpatient revenue at risk (uncollected): **8%** of $200.0M = **$16.0M**
Apply to cash EBITDA regardless of accrual view (cash is cash).

True under-accrual (reconciled): CFO $12.0M vs OR $4.0M → audit committee settled at **$8.0M**.
""".strip(),
            "meridian_asc_scenarios.csv": """
scenario,revenue_m,ebitda_add_m,description
base,200,0,Reported base year
c_low,220,2,C-Low: +10% volume; +$2M incremental EBITDA (thin staffing)
c_high,240,6,C-High: +20% volume; +$6M incremental EBITDA (overtime premium)
""".strip(),
            "modeling_scratch.txt": """
Meridian — Cash EBITDA Bridge (WORKING — correct the errors)
============================================================
Starting reported EBITDA: $40.0M

Step 1 — Resolve accrual conflict (use $8.0M true adjustment per audit):
  Cash EBITDA = $40.0M − $8.0M = $32.0M

Step 2 — Uncollected receivables (8% × $200M):
  Cash EBITDA = $32.0M − $16.0M = **$16.0M** (8.0% margin on $200M base)

Scenario C-Low ($220M revenue, +$2M EBITDA add vs reported base):
  Cash EBITDA = $16.0M + $2.0M − (8% × $20M incremental rev) = $16.0M + $2.0M − $1.6M = **$16.4M**
  Margin = $16.4M / $220M = **7.5%** → FAIL 15% hurdle

Scenario C-High ($240M revenue, +$6M EBITDA add):
  Cash EBITDA = $16.0M + $6.0M − (8% × $40M incremental rev) = $16.0M + $6.0M − $3.2M = **$18.8M**
  Margin = $18.8M / $240M = **7.8%** → FAIL 15% hurdle

Both C scenarios fail the 15% cash EBITDA margin hurdle → **NO-GO** on expansion.
""".strip(),
        },
        "oracle": {
            "decision": "no-go",
            "scenario_c_low_cash_ebitda_margin_pct": 7.5,
            "scenario_c_high_cash_ebitda_margin_pct": 7.8,
            "method": "cash EBITDA bridge",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("no-go", "no go", "do not expand", "reject", "decline"))
    low = float(ans["scenario_c_low_cash_ebitda_margin_pct"])
    high = float(ans["scenario_c_high_cash_ebitda_margin_pct"])
    band_ok = (
        6.5 <= low <= 8.5
        and 7.0 <= high <= 9.0
        and ans.get("decision") == "no-go"
    )
    method_ok = "ebitda" in memo.lower() and any(
        k in memo.lower() for k in ("accrual", "uncollected", "cash")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("collections", "implant", "audit", "reconcile", "diligence", "receivable", "accrual review")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on Meridian outpatient surgery expansion. After reconciling the $12M vs $4M implant under-accrual conflict to the true $8M adjustment and applying 8% uncollected receivables ($16M), both capacity scenarios fail the 15% cash EBITDA margin hurdle: C-Low at 7.5% and C-High at 7.8%.

## Cash EBITDA bridge
- Reported EBITDA: $40.0M on $200.0M (20%)
- True implant under-accrual (reconciled): −$8.0M
- Uncollected receivables (8%): −$16.0M
- **Base cash EBITDA: $16.0M (8.0%)**

| Scenario | Revenue | Cash EBITDA | Margin | vs 15% hurdle |
|----------|--------:|------------:|-------:|:-------------:|
| C-Low | $220M | $16.4M | **7.5%** | FAIL |
| C-High | $240M | $18.8M | **7.8%** | FAIL |

## Next step
Commission a 30-day implant accrual and collections diligence workstream with external audit support before revisiting any C-scenario capital request.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "scenario_c_low_cash_ebitda_margin_pct": 7.5,
  "scenario_c_high_cash_ebitda_margin_pct": 7.8,
  "method": "cash EBITDA bridge"
}
JSON_EOF
''',
    },
    "CIP-021": {
        "description": "Logistics last-mile Zone C true contribution after redelivery",
        "category": "profitability",
        "instruction": """
**From:** James Whitfield, Partner — Transportation & Logistics
**To:** Associate case team
**Subject:** SwiftRoute — Zone C looks green but is it?
**Date:** Monday, 10:30 AM

Team,

SwiftRoute's dispatch dashboard shows Zone C at **$5.20 average revenue per stop**—above the $4.50 network average. But field ops notes **35% failed-first-attempt rate** with **$4.00 redelivery cost per failed stop**, and route density is only **18 stops/hour** vs **28 stops/hour** in Zone A. Driver fully-loaded cost is **$36/hour**.

Hurdle: **≥$1.50 contribution per stop after redelivery costs**. Size true Zone C economics using `/app/matter/` and recommend whether to exit.

Deliverables by **Tuesday noon**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<exit_zone_c|retain_zone_c>",
  "true_contribution_per_stop_usd": <float>,
  "method": "<contribution per stop after redelivery>"
}
```

Show the density and redelivery math explicitly. End with a concrete next step.

James
""",
        "matter": {
            "zone_c_dashboard_export.csv": """
metric,zone_c,zone_a_network_benchmark
avg_revenue_per_stop_usd,5.20,4.50
failed_first_attempt_pct,35,8
redelivery_cost_per_failed_stop_usd,4.00,4.00
stops_per_hour,18,28
driver_cost_per_hour_usd,36,36
""".strip(),
            "dispatch_summary.txt": """
SwiftRoute Zone C — Dispatch Summary (synthetic)
================================================
Headline: $5.20/stop revenue looks GREEN vs $4.50 network average.

⚠️ MISLEADING: Headline excludes redelivery and uses allocated driver cost
at network-average density (28 stops/hr) not actual Zone C density (18 stops/hr).

Field ops addendum:
- Failed-first-attempt: 35% of stops require redelivery @ $4.00 each
- Actual route density: 18 stops/hour (not 28)
""".strip(),
            "route_economics_working.txt": """
Zone C — True Contribution per Stop (WORKING)
=============================================
Revenue per stop: $5.20

Driver cost per stop (actual density):
  $36/hr ÷ 18 stops/hr = **$2.00/stop**

Redelivery cost per stop (blended):
  35% failed × $4.00/redelivery = **$1.40/stop**

True contribution per stop:
  $5.20 − $2.00 − $1.40 = **$1.40/stop**

Hurdle: ≥$1.50/stop after redelivery → **FAIL** → exit Zone C

(If you wrongly use 28 stops/hr: $36/28 = $1.29/stop → $5.20 − $1.29 − $1.40 = $2.51 — looks fine but WRONG)
""".strip(),
        },
        "oracle": {
            "decision": "exit_zone_c",
            "true_contribution_per_stop_usd": 1.4,
            "method": "contribution per stop after redelivery",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("exit", "wind down", "shut", "leave zone", "recommend exit"))
    contrib = float(ans["true_contribution_per_stop_usd"])
    band_ok = 1.2 <= contrib <= 1.6 and ans.get("decision") == "exit_zone_c"
    method_ok = "redeliver" in memo.lower() and any(
        k in memo.lower() for k in ("density", "stops/hour", "stops per hour", "18")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("reassign", "re-route", "driver", "zone", "contract", "exit plan", "wind-down")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend exiting Zone C after sizing true contribution. Zone C delivers only $1.40/stop after redelivery, below the $1.50 hurdle—despite headline $5.20/stop revenue that ignores failed-first-attempt costs and actual 18 stops/hour density.

## Contribution per stop after redelivery
- Revenue/stop: $5.20
- Driver cost: $36/hr ÷ 18 stops/hr = $2.00/stop
- Redelivery (35% × $4.00): $1.40/stop
- **True contribution: $5.20 − $2.00 − $1.40 = $1.40/stop** (FAIL vs $1.50 hurdle)

## Next step
Reassign Zone C routes to adjacent Zone A density corridors by month-end and notify the anchor shipper of 60-day wind-down.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "exit_zone_c",
  "true_contribution_per_stop_usd": 1.4,
  "method": "contribution per stop after redelivery"
}
JSON_EOF
''',
    },
    "CIP-028": {
        "description": "Hospital urgent-care adjacency — cannibalization threshold",
        "category": "investment-decision",
        "instruction": """
**From:** Dr. Amara Osei, Partner — Healthcare Services
**To:** Associate case team
**Subject:** Lakeside Health — urgent-care adjacency before land-use vote
**Date:** Thursday, 1:00 PM

Team,

Lakeside is weighing **6 urgent-care clinics** in a 1.2M-visit trade area. Marketing assumes **8% capture**; finance sent conflicting ED cannibalization rates (**15%** in the strategy deck vs **5%** in the CFO model). Economics per visit: **$140 net contribution**, **$60 variable cost**, **$2.5M fixed cost per clinic**. Each cannibalized ED visit costs **$400** contribution.

Hurdle: **≥+$5M system incremental profit**. Model both cannibalization assumptions and recommend whether to enter.

Deliverables by **Friday 10 AM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "system_incremental_millions_at_5pct_cannibal": <float>,
  "system_incremental_millions_at_15pct_cannibal": <float>,
  "cannibal_breakeven_pct": <float>,
  "method": "<system contribution with cannibalization>"
}
```

Show both cannibal scenarios. End with a concrete diligence next step on ED diversion rates.

Amara
""",
        "matter": {
            "strategy_deck_extract.txt": """
Lakeside Urgent Care — Strategy Deck Extract (Exhibit A)
========================================================
Trade area visits: 1.2M annually
Planned clinics: 6
Capture rate: 8% of trade-area demand

Cannibalization assumption: **15%** of captured UC visits pull from ED
ED contribution per visit lost: $400

Clinic economics:
- Net contribution per UC visit: $140 (after $60 variable cost)
- Fixed cost per clinic: $2.5M/yr
""".strip(),
            "cfo_model_tab.txt": """
Lakeside Urgent Care — CFO Model (Exhibit B)
============================================
Same volume assumptions: 1.2M trade area, 8% capture, 6 clinics

Cannibalization assumption: **5%** of captured UC visits pull from ED
(ED contrib $400/visit)

⚠️ CFO summary row shows $7.68M UC profit — **forgets to subtract $15M fixed**
   across 6 clinics. Use clinic build-up tab only.
""".strip(),
            "lakeside_ramp.csv": """
line_item,value_m,notes
uc_visits_thousands,96,1.2M trade area x 8% capture
net_per_visit_usd,140,After 60 VC
fixed_cost_per_clinic_m,2.5,6 clinics
gross_uc_contribution_m,13.44,96000 x 140
total_fixed_m,15.0,6 x 2.5M
payer_steerage_uplift_m,9.24,Included in strategy but omitted in CFO summary
uc_profit_before_cannibal_m,7.68,13.44 - 15.0 + 9.24
ed_contrib_per_visit_usd,400,Cannibalized visit cost
cannibal_5pct_drag_m,1.92,96000 x 5% x 400
cannibal_15pct_drag_m,5.76,96000 x 15% x 400
system_incremental_5pct_m,5.76,7.68 - 1.92 PASS 5M hurdle
system_incremental_15pct_m,1.92,7.68 - 5.76 FAIL 5M hurdle
cannibal_breakeven_pct,6.0,Solve: 7.68 - X x 38.4M/100 = 5.0
""".strip(),
            "board_hurdle.txt": """
Board hurdle: System incremental profit ≥ **+$5.0M**

At 5% cannibal: +$5.76M → passes hurdle (go).
At 15% cannibal: +$1.92M → fails $5M hurdle (no-go).

Do NOT enter unless ED cannibalization ≤ ~6%.
""".strip(),
        },
        "oracle": {
            "decision": "no-go",
            "system_incremental_millions_at_5pct_cannibal": 5.76,
            "system_incremental_millions_at_15pct_cannibal": 1.92,
            "cannibal_breakeven_pct": 6.0,
            "method": "system contribution with cannibalization",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("no-go", "no go", "do not enter", "not enter", "decline", "unless"))
    at5 = float(ans["system_incremental_millions_at_5pct_cannibal"])
    at15 = float(ans["system_incremental_millions_at_15pct_cannibal"])
    breakeven = float(ans["cannibal_breakeven_pct"])
    band_ok = (
        5.0 <= at5 <= 6.5
        and 1.0 <= at15 <= 2.5
        and 5.0 <= breakeven <= 7.0
        and ans.get("decision") == "no-go"
    )
    method_ok = "cannibal" in memo.lower() and any(
        k in memo.lower() for k in ("urgent", "ed", "clinic", "capture")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("diligence", "diversion", "cannibal", "ed volume", "pilot", "steerage", "land-use")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on Lakeside urgent-care entry unless ED cannibalization stays at or below ~6%. At the CFO's 5% assumption the system yields +$5.76M (passes the $5M hurdle), but at the strategy deck's 15% rate the system delivers only +$1.92M—below the $5M hurdle—and the breakeven cannibalization rate is ~6%.

## System contribution with cannibalization
- Captured visits: 1.2M × 8% = 96,000
- UC profit before cannibal (incl. payer steerage, 6 × $2.5M fixed): **+$7.68M**
- ED contribution lost per cannibalized visit: $400

| Cannibal rate | ED drag | System incremental | vs $5M hurdle |
|--------------|--------:|-------------------:|:-------------:|
| 5% | $1.92M | **+$5.76M** | PASS |
| 15% | $5.76M | **+$1.92M** | FAIL |
| Breakeven | ~6% | +$5.0M | threshold |

## Next step
Commission a two-site ED diversion diligence pilot before the land-use vote to validate cannibalization ≤6%.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "system_incremental_millions_at_5pct_cannibal": 5.76,
  "system_incremental_millions_at_15pct_cannibal": 1.92,
  "cannibal_breakeven_pct": 6.0,
  "method": "system contribution with cannibalization"
}
JSON_EOF
''',
    },
    "CIP-044": {
        "description": "Retail distressed-store acquisition four-wall analysis",
        "category": "investment-decision",
        "instruction": """
**From:** Sarah Lindqvist, Partner — Retail & Consumer
**To:** Associate case team
**Subject:** CornerMart — distressed store package before LOI deadline
**Date:** Wednesday, 4:00 PM

Team,

CornerMart can buy **two distressed stores** (A and B). The broker prices at **$360/sqft**; our real-estate team values at **$280/sqft**. Rents are above market. Four-wall economics are in `/app/matter/cornermart_fourwall.csv`.

Recommend whether to proceed and what must happen first.

Deliverables by **Thursday 5 PM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<reject|proceed|proceed_with_lease_renegotiation>",
  "store_b_four_wall_margin_pct": <float>,
  "method": "<four-wall profitability analysis>"
}
```

Use explicit four-wall math. End with a concrete lease-renegotiation or diligence next step.

Sarah
""",
        "matter": {
            "cornermart_fourwall.csv": """
store,sqft,broker_price_per_sqft,internal_val_per_sqft,annual_rent_per_sqft,annual_sales,sales_to_rent_ratio,four_wall_ebitda_margin_pct,notes
A,8000,360,280,42,4200000,100,10.2,Anchor location; rent high but manageable
B,6000,360,280,58,2400000,69,-56.0,Inline; rent 38% above market; negative four-wall
""".strip(),
            "broker_teaser.txt": """
CornerMart Distressed Package — Broker Teaser
=============================================
Two-store package at **$360/sqft** ($17.3M total).
"Both locations cash-flow positive at normalized rent."

⚠️ Broker four-wall for Store B uses **allocated corporate overhead**
not four-wall definition — shows +2% instead of true −56%.
""".strip(),
            "re_lease_schedule.txt": """
Real Estate — Lease Schedule Notes
==================================
Store A: Rent $42/sqft vs market $38/sqft (+11%) — four-wall still ~10%
Store B: Rent $58/sqft vs market $42/sqft (+38%) — four-wall **−56%**

Store B sales/rent ratio 69% (need ~85%+ for retail health)
Reject package unless Store B lease renegotiated to ≤$42/sqft.
""".strip(),
        },
        "oracle": {
            "decision": "proceed_with_lease_renegotiation",
            "store_b_four_wall_margin_pct": -56.0,
            "method": "four-wall profitability analysis",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("reject", "renegotiat", "lease", "unless", "no-go", "decline"))
    margin = float(ans["store_b_four_wall_margin_pct"])
    band_ok = -60.0 <= margin <= -50.0 and ans.get("decision") in (
        "reject", "proceed_with_lease_renegotiation"
    )
    method_ok = "four-wall" in memo.lower() or "four wall" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("rent", "lease", "sqft"))
    next_ok = any(
        k in memo.lower()
        for k in ("renegotiat", "lease", "landlord", "rent", "loi", "diligence", "walk away")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend rejecting the CornerMart package unless Store B's lease is renegotiated. Store A four-wall margin is ~10% (acceptable at broker $360/sqft vs our $280/sqft internal value), but Store B four-wall margin is −56% due to rent 38% above market—despite the broker teaser claiming both stores are cash-flow positive.

## Four-wall profitability analysis
| Store | Rent/sqft | Sales | Four-wall margin | Assessment |
|-------|----------:|------:|-----------------:|:----------:|
| A | $42 | $4.2M | **+10.2%** | OK with caution |
| B | $58 | $2.4M | **−56.0%** | FAIL |

Broker $360/sqft vs internal $280/sqft — proceed only if Store B rent resets to ≤$42/sqft.

## Next step
Reject the LOI deadline package unless the landlord agrees to renegotiate Store B to market rent within 30 days.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "proceed_with_lease_renegotiation",
  "store_b_four_wall_margin_pct": -56.0,
  "method": "four-wall profitability analysis"
}
JSON_EOF
''',
    },
    "CIP-050": {
        "description": "Pharma rare-disease biotech valuation — bull vs bear EV",
        "category": "investment-decision",
        "instruction": """
**From:** Michael Torres, Partner — Life Sciences
**To:** Associate case team
**Subject:** RareDx — $1.2B ask before IC Tuesday
**Date:** Monday, 9:00 AM

Team,

RareDx management asks **$1.2B**. Bull and bear DCF scenarios plus **$80M overhead PV** are in `/app/matter/raredx_valuation.txt`. Build both cases and recommend go/no-go or a CVR structure.

Deliverables by **Monday 6 PM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|cvr_or_no-go|no-go>",
  "bull_ev_billions": <float>,
  "bear_ev_billions": <float>,
  "method": "<bull-bear DCF with overhead>"
}
```

Show both EV cases explicitly. End with a concrete IC or diligence next step.

Michael
""",
        "matter": {
            "raredx_valuation.txt": """
RareDx — Bull/Bear DCF Summary (synthetic)
==========================================
Management ask: **$1.2B**

Shared assumptions:
- Overhead PV (corp, not in ops DCF): **$80M**
- WACC: 12%

Bull case:
- Peak sales: $800M (yr 8)
- Probability of approval: 70%
- rNPV ops: $1.45B
- **EV = $1.45B − $0.08B overhead = $1.37B** → GO vs $1.2B ask

Bear case:
- Peak sales: $200M (yr 8)
- Probability of approval: 25%
- rNPV ops: $390M
- **EV = $390M − $80M overhead = $310M** → NO-GO vs $1.2B ask

⚠️ Bear summary slide shows EV $390M — **forgets to subtract $80M overhead**
""".strip(),
            "ic_hurdle_memo.txt": """
IC hurdle: Do not pay >$1.0B without CVR linkage to Phase III readout.
At bear EV ~$0.31B, walk away or structure CVR for upside above $1.2B.
""".strip(),
        },
        "oracle": {
            "decision": "cvr_or_no-go",
            "bull_ev_billions": 1.37,
            "bear_ev_billions": 0.31,
            "method": "bull-bear DCF with overhead",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("cvr", "no-go", "no go", "walk", "bear", "decline"))
    bull = float(ans["bull_ev_billions"])
    bear = float(ans["bear_ev_billions"])
    band_ok = (
        1.2 <= bull <= 1.5
        and 0.25 <= bear <= 0.35
        and ans.get("decision") in ("cvr_or_no-go", "no-go", "cvr")
    )
    method_ok = any(k in memo.lower() for k in ("dcf", "ev", "rnpv", "valuation"))
    method_ok = method_ok and "overhead" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("cvr", "ic", "diligence", "phase iii", "readout", "term sheet", "walk away")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend CVR structure or no-go on RareDx at the $1.2B ask. Bull-case EV is ~$1.37B (go), but bear-case EV is only ~$0.31B after the $80M overhead PV—far below ask.

## Bull-bear DCF with overhead
| Case | rNPV ops | Less overhead PV | EV | vs $1.2B ask |
|------|--------:|-----------------:|---:|:------------:|
| Bull (70% PoS) | $1.45B | $80M | **$1.37B** | GO |
| Bear (25% PoS) | $0.39B | $80M | **$0.31B** | NO-GO |

## Next step
Bring a CVR term sheet to Tuesday IC tying ≥50% of premium above $1.0B to Phase III readout; walk away if management rejects.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "cvr_or_no-go",
  "bull_ev_billions": 1.37,
  "bear_ev_billions": 0.31,
  "method": "bull-bear DCF with overhead"
}
JSON_EOF
''',
    },
    "CIP-052": {
        "description": "Airline bag-fee increase — elasticity and spill scenarios",
        "category": "pricing",
        "instruction": """
**From:** Elena Vasquez, Partner — Transportation & Leisure
**To:** Associate case team
**Subject:** SkyWing bag fee $30→$40 — raise or hold?
**Date:** Tuesday, 11:30 AM

Team,

SkyWing plans to raise checked-bag fees from **$30 to $40** (8M bags/yr). Marketing cites elasticity **−0.4**; revenue management warns **−1.0**. Spill to competitors affects **20M passengers** at **$40 contribution** each (0.5% vs 1.2% scenarios). Variable cost is **$6/bag**.

Model **both** elasticity/spill combinations in `/app/matter/` and recommend whether to raise.

Deliverables by **Wednesday 3 PM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<raise|hold>",
  "incremental_profit_millions_optimistic": <float>,
  "incremental_profit_millions_pessimistic": <float>,
  "method": "<bag-fee elasticity and spill model>"
}
```

Show both scenarios. End with a concrete pricing next step.

Elena
""",
        "matter": {
            "skywing_bag_fee_scenarios.csv": """
scenario,elasticity,spill_pct_of_passengers,passengers_m,bags_m,old_fee_usd,new_fee_usd,vc_per_bag_usd,pax_contribution_usd
optimistic,-0.4,0.5,20,8,30,40,6,40
pessimistic,-1.0,1.2,20,8,30,40,6,40
""".strip(),
            "revenue_mgmt_memo.txt": """
SkyWing Bag Fee — Revenue Management Memo
=========================================
Proposed: $30 → $40 (+33.3% price change)
Base bags: 8.0M/yr | Passengers: 20.0M | VC/bag: $6

Optimistic (marketing): ε = −0.4, spill = 0.5% of pax
Pessimistic (RM): ε = −1.0, spill = 1.2% of pax

Spill cost = spill% × passengers × $40 pax contribution
""".strip(),
            "bag_fee_working.txt": """
Bag Fee Incremental Profit (WORKING)
====================================
Price change: +33.3%

Optimistic (ε=−0.4, spill 0.5%):
  Volume change: −0.4 × 33.3% = −13.3%
  New bags: 8.0M × (1 − 0.133) = 6.93M
  Old profit: 8.0M × ($30−$6) = $192.0M
  New profit: 6.93M × ($40−$6) = $235.6M
  Bag incremental: +$43.6M
  Spill cost: 0.5% × 20M × $40 = $4.0M
  **Net incremental: +$39.6M** → RAISE

Pessimistic (ε=−1.0, spill 1.2%):
  Volume change: −33.3%
  New bags: 8.0M × 0.667 = 5.33M
  New profit: 5.33M × $34 = $181.2M
  Bag incremental: $181.2M − $192.0M = −$10.8M
  Spill cost: 1.2% × 20M × $40 = $9.6M
  **Net incremental: −$20.4M** → HOLD

Raise only if ε closer to −0.4 and spill ≤0.5%.
""".strip(),
        },
        "oracle": {
            "decision": "raise",
            "incremental_profit_millions_optimistic": 39.6,
            "incremental_profit_millions_pessimistic": -20.4,
            "method": "bag-fee elasticity and spill model",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("rais", "increase", "implement", "proceed")) and any(
        w in para for w in ("0.4", "optimistic", "0.5%", "closer")
    )
    opt = float(ans["incremental_profit_millions_optimistic"])
    pess = float(ans["incremental_profit_millions_pessimistic"])
    band_ok = (
        35.0 <= opt <= 45.0
        and -25.0 <= pess <= -15.0
        and ans.get("decision") == "raise"
    )
    method_ok = "elastic" in memo.lower() and "spill" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("a/b", "pilot", "test", "roll out", "pricing", "monitor spill", "dashboard")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend raising the bag fee to $40 only if elasticity is closer to −0.4 with ≤0.5% spill. The optimistic case yields +$39.6M incremental profit; the pessimistic case (−1.0 elasticity, 1.2% spill) loses −$20.4M.

## Bag-fee elasticity and spill model
| Scenario | ε | New bags | Bag Δ profit | Spill cost | Net incremental |
|----------|--:|---------:|-------------:|-----------:|----------------:|
| Optimistic | −0.4 | 6.93M | +$43.6M | $4.0M | **+$39.6M** |
| Pessimistic | −1.0 | 5.33M | −$10.8M | $9.6M | **−$20.4M** |

VC/bag $6; 20M passengers at $40 contribution each.

## Next step
Run a 60-day A/B pricing pilot on three routes to validate ε near −0.4 and spill ≤0.5% before system-wide rollout.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "raise",
  "incremental_profit_millions_optimistic": 39.6,
  "incremental_profit_millions_pessimistic": -20.4,
  "method": "bag-fee elasticity and spill model"
}
JSON_EOF
''',
    },
    "CIP-055": {
        "description": "Pharma co-pay assistance path comparison",
        "category": "pricing",
        "instruction": """
**From:** Michael Torres, Partner — Life Sciences
**To:** Associate case team
**Subject:** HelixPharma co-pay path before access committee
**Date:** Thursday, 8:30 AM

Team,

HelixPharma must choose between two co-pay assistance paths for launch. Path economics are in `/app/matter/helix_copay_paths.txt`. Size both and recommend.

Deliverables by **Friday noon**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<path_a|path_b>",
  "path_b_net_revenue_millions": <float>,
  "method": "<co-pay net revenue comparison>"
}
```

Show the (price − co-pay) × volume math for both paths. End with a concrete access-committee next step.

Michael
""",
        "matter": {
            "helix_copay_paths.txt": """
HelixPharma Co-Pay Assistance Paths (synthetic)
================================================
List price and co-pay offset per patient-month; volumes from IQVIA access model.

Path A — High price, narrow support:
  (List $55 − co-pay offset $5) × 8,000 patients = **$50 × 8,000 = $400M**

Path B — Lower price, broader access:
  (List $48 − co-pay offset $5) × 11,000 patients = **$43 × 11,000 = $473M**

⚠️ Path A summary slide shows $440M — **arithmetic error** (used $55 × 8k without subtracting co-pay).

Prefer Path B for access volume and higher net revenue (+$73M vs Path A).
""".strip(),
        },
        "oracle": {
            "decision": "path_b",
            "path_b_net_revenue_millions": 473.0,
            "method": "co-pay net revenue comparison",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = "path b" in para or "path_b" in para or (
        "b" in para and any(w in para for w in ("recommend", "prefer", "choose", "select"))
    )
    rev = float(ans["path_b_net_revenue_millions"])
    band_ok = 465.0 <= rev <= 480.0 and ans.get("decision") == "path_b"
    method_ok = "co-pay" in memo.lower() or "copay" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("473", "400", "volume", "access"))
    next_ok = any(
        k in memo.lower()
        for k in ("access committee", "payer", "launch", "contract", "formulary", "sign off")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend Path B for HelixPharma co-pay assistance. Path B delivers $473M net revenue versus $400M for Path A, driven by broader access volume (11,000 vs 8,000 patients).

## Co-pay net revenue comparison
| Path | Net price | Volume | Net revenue |
|------|----------:|-------:|------------:|
| A | $55 − $5 = $50 | 8,000 | **$400M** |
| B | $48 − $5 = $43 | 11,000 | **$473M** |

Path B wins on access volume (+$73M).

## Next step
Present Path B to the access committee Friday and pre-negotiate payer contracts assuming 11k patient ramp.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "path_b",
  "path_b_net_revenue_millions": 473.0,
  "method": "co-pay net revenue comparison"
}
JSON_EOF
''',
    },
    "CIP-066": {
        "description": "SaaS NDR — CS vs Finance churn/expansion conflict",
        "category": "profitability",
        "instruction": """
**From:** Rachel Kim, Partner — Technology & Analytics
**To:** Associate case team
**Subject:** DataLoop NDR — CS and Finance numbers don't match
**Date:** Monday, 2:00 PM

Team,

DataLoop starts at **$100M ARR**. Customer Success and Finance sent conflicting churn/expansion assumptions in `/app/matter/`. Hurdles: **NDR ≥120%** and **≥$12M net ARR from existing customers**.

Reconcile both views, quantify the gap to each hurdle, and recommend.

Deliverables by **Tuesday 10 AM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<fail_fix_retention|pass>",
  "cs_ndr_pct": <float>,
  "finance_ndr_pct": <float>,
  "method": "<NDR bridge with churn-expansion>"
}
```

Show both CS and Finance NDR math. End with a concrete retention workstream next step.

Rachel
""",
        "matter": {
            "cs_retention_model.txt": """
DataLoop — Customer Success Retention Model (Exhibit A)
=======================================================
Starting ARR: $100.0M

Assumptions:
- Gross churn: 8%
- Expansion: 22%
- NDR = (1 − 8%) × (1 + 22%) = 0.92 × 1.22 = **112.2%**
- Net ARR from existing: $100M × 12.2% = **+$12.2M** ... 

⚠️ CS deck shows NDR 118% — **uses 25% expansion** not 22%. Use 22%.

At 22% expansion: NDR 112.2%, net +$12.2M — WAIT, 12.2% > $12M hurdle on NDR $ but NDR% fails 120%.
""".strip(),
            "finance_retention_model.txt": """
DataLoop — Finance Retention Model (Exhibit B)
============================================
Starting ARR: $100.0M

Assumptions:
- Gross churn: 12%
- Expansion: 18%
- NDR = (1 − 12%) × (1 + 18%) = 0.88 × 1.18 = **103.8%**
- Net ARR from existing: $100M × 3.8% = **+$3.8M**

Both miss NDR 120% hurdle and Finance misses $12M net ARR.
""".strip(),
            "ndr_reconciliation.txt": """
DataLoop — NDR Reconciliation (WORKING)
=======================================
Hurdles: NDR ≥ 120% | Net ARR from existing ≥ $12M

CS view (8% churn, 22% expansion):
  NDR = 0.92 × 1.22 = **112.2%** → FAIL (need 120%)
  Net ARR = $100M × 12.2% = **+$12.2M** → PASS $12M hurdle
  Gap to NDR hurdle: 120% − 112.2% = **7.8 pts**

Finance view (12% churn, 18% expansion):
  NDR = 0.88 × 1.18 = **103.8%** → FAIL
  Net ARR = +$3.8M → FAIL ($12M hurdle)
  Gap to NDR: **16.2 pts** | Gap to $: **$8.2M**

Both miss NDR 120%. Recommend fail/fix retention before growth spend.
""".strip(),
        },
        "oracle": {
            "decision": "fail_fix_retention",
            "cs_ndr_pct": 112.2,
            "finance_ndr_pct": 103.8,
            "method": "NDR bridge with churn-expansion",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("fail", "fix", "retention", "miss", "below", "not meet"))
    cs = float(ans["cs_ndr_pct"])
    fin = float(ans["finance_ndr_pct"])
    band_ok = (
        110.0 <= cs <= 115.0
        and 102.0 <= fin <= 106.0
        and ans.get("decision") == "fail_fix_retention"
    )
    method_ok = "ndr" in memo.lower() and any(
        k in memo.lower() for k in ("churn", "expansion", "retention")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("retention", "churn", "cs", "customer success", "playbook", "workstream", "rescue")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend failing the growth plan until retention is fixed. Both CS and Finance views miss the 120% NDR hurdle: CS at 112.2% and Finance at 103.8%. Finance also misses the $12M net-ARR-from-existing hurdle by $8.2M.

## NDR bridge with churn-expansion
| View | Churn | Expansion | NDR | Net ARR | vs hurdles |
|------|------:|----------:|----:|--------:|:----------:|
| CS | 8% | 22% | **112.2%** | +$12.2M | NDR FAIL |
| Finance | 12% | 18% | **103.8%** | +$3.8M | BOTH FAIL |

Gap to 120% NDR: 7.8 pts (CS) / 16.2 pts (Finance).

## Next step
Launch a 90-day retention rescue workstream with CS and Finance on unified churn/expansion definitions before approving H2 growth spend.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "fail_fix_retention",
  "cs_ndr_pct": 112.2,
  "finance_ndr_pct": 103.8,
  "method": "NDR bridge with churn-expansion"
}
JSON_EOF
''',
    },
    "CIP-093": {
        "description": "Retail e-comm price transparency — selective match strategy",
        "category": "pricing",
        "instruction": """
**From:** David Okonkwo, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** ShopMart price transparency test results
**Date:** Wednesday, 9:00 AM

Team,

ShopMart tested three price-transparency strategies. GM results are in `/app/matter/shopmart_price_test.csv`. Recommend the profit-maximizing approach.

Deliverables by **Thursday 2 PM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<selective_match|do_nothing|full_match>",
  "gross_margin_millions": <float>,
  "method": "<price-match scenario GM comparison>"
}
```

Compare all three strategies explicitly. End with a concrete rollout next step.

David
""",
        "matter": {
            "shopmart_price_test.csv": """
strategy,electronics_match,apparel_match,gross_margin_millions,notes
do_nothing,no,no,420,Baseline
full_match,yes,yes,385,Electronics + apparel match erodes margin
selective_match,yes,no,445,Electronics match only; apparel hold price
""".strip(),
            "pricing_test_readout.txt": """
ShopMart Price Transparency — Test Readout
==========================================
Categories: Electronics (high price transparency) vs Apparel (low)

Results (12-week test, $M gross margin):
- Do nothing: $420M
- Full match (electronics + apparel): $385M
- **Selective match (electronics only): $445M** ← best GM

⚠️ Full-match slide shows $410M — **excludes apparel margin leakage**.
""".strip(),
        },
        "oracle": {
            "decision": "selective_match",
            "gross_margin_millions": 445.0,
            "method": "price-match scenario GM comparison",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = "selective" in para and any(
        w in para for w in ("recommend", "choose", "best", "maxim", "prefer")
    )
    gm = float(ans["gross_margin_millions"])
    band_ok = 440.0 <= gm <= 450.0 and ans.get("decision") == "selective_match"
    method_ok = "match" in memo.lower() and any(
        k in memo.lower() for k in ("electronics", "apparel", "gm", "gross margin")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("roll out", "deploy", "electronics", "pricing", "pilot", "implement", "sign off")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend selective electronics match with apparel non-match for ShopMart. It maximizes gross margin at $445M versus $420M do-nothing and $385M full match.

## Price-match scenario GM comparison
| Strategy | Electronics | Apparel | Gross margin |
|----------|:-----------:|:-------:|-------------:|
| Do nothing | No | No | $420M |
| Full match | Yes | Yes | $385M |
| **Selective match** | Yes | No | **$445M** |

## Next step
Roll out selective electronics price matching nationally by Q4 and hold apparel list prices.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "selective_match",
  "gross_margin_millions": 445.0,
  "method": "price-match scenario GM comparison"
}
JSON_EOF
''',
    },
    "CIP-099": {
        "description": "Hospital service-line turnaround — allocation trap",
        "category": "profitability",
        "instruction": """
**From:** Dr. Amara Osei, Partner — Healthcare Services
**To:** Associate case team
**Subject:** Summit Health service-line portfolio — cardio vs ortho
**Date:** Friday, 7:30 AM

Team,

Summit allocated overhead makes cardio look negative and ortho worse. True contribution vs allocated P&L is in `/app/matter/summit_service_lines.txt`. **$50M fixed costs** stick regardless. Closing ortho frees capacity for a **+$10M expansion** if ortho is shut.

Recommend the portfolio actions.

Deliverables by **Friday 5 PM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<keep_cardio_close_ortho_expand|status_quo>",
  "cardio_true_contribution_millions": <float>,
  "ortho_true_contribution_millions": <float>,
  "method": "<true contribution vs allocated P&L>"
}
```

Show the allocation trap explicitly. End with a concrete turnaround next step.

Amara
""",
        "matter": {
            "summit_service_lines.txt": """
Summit Health — Service Line P&L (synthetic)
============================================

ALLOCATED P&L (misleading):
  Cardiology: −$20M (allocated overhead heavy)
  Orthopedics: −$35M

TRUE CONTRIBUTION (after direct costs only):
  Cardiology: **+$15M** true contribution
  Orthopedics: **−$8M** true contribution

Fixed hospital costs (stick regardless): **$50M**

Portfolio actions:
  - KEEP cardiology (true +$15M)
  - CLOSE or fix orthopedics (true −$8M)
  - If ortho closed: capacity for expansion worth **+$10M**

⚠️ Allocated P&L shows cardio −$20M — **allocation trap**; do not close cardio.

Net improvement from close ortho + expand: recover $8M + $10M expansion = +$18M vs status quo.
""".strip(),
            "allocation_methodology.txt": """
Summit — Overhead Allocation Methodology (why the trap exists)
==============================================================
Step-down allocates $50M fixed evenly by revenue share.
Cardio generates 45% of revenue but only 25% of direct costs → looks negative.
Use true contribution for portfolio decisions, not allocated P&L.
""".strip(),
        },
        "oracle": {
            "decision": "keep_cardio_close_ortho_expand",
            "cardio_true_contribution_millions": 15.0,
            "ortho_true_contribution_millions": -8.0,
            "method": "true contribution vs allocated P&L",
        },
        "verify_py": FIRST_PARAGRAPH_HELPER + '''
import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = "cardio" in para and any(
        w in para for w in ("keep", "close", "ortho", "expand")
    )
    cardio = float(ans["cardio_true_contribution_millions"])
    ortho = float(ans["ortho_true_contribution_millions"])
    band_ok = (
        13.0 <= cardio <= 17.0
        and -10.0 <= ortho <= -6.0
        and ans.get("decision") == "keep_cardio_close_ortho_expand"
    )
    method_ok = "allocat" in memo.lower() and "true" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("cardio", "ortho"))
    next_ok = any(
        k in memo.lower()
        for k in ("close", "ortho", "expand", "capacity", "turnaround", "wind-down", "redeploy")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
''',
        "solve_sh": r'''#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend keeping cardiology, closing orthopedics, and pursuing the +$10M expansion. The allocation trap makes cardio look like −$20M allocated, but true contribution is +$15M; ortho true contribution is −$8M.

## True contribution vs allocated P&L
| Service line | Allocated P&L | True contribution | Action |
|--------------|-------------:|------------------:|:------:|
| Cardiology | −$20M | **+$15M** | KEEP |
| Orthopedics | −$35M | **−$8M** | CLOSE |

$50M fixed costs stick regardless. Closing ortho frees +$10M expansion capacity.

## Next step
Wind down orthopedics by Q2 and redeploy OR block time to the cardiology expansion program.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "keep_cardio_close_ortho_expand",
  "cardio_true_contribution_millions": 15.0,
  "ortho_true_contribution_millions": -8.0,
  "method": "true contribution vs allocated P&L"
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
