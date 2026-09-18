#!/usr/bin/env python3
"""Replace the 31 stub Partner-50 tasks with checkable consulting cases.

Matter packs do not precompute the answer. Each case has a trap number that
fails the numeric band if the model includes the wrong exhibit.
"""

from __future__ import annotations

from harden_common import SPECS, add, case, email, write_task


add(
    case(
        task_id="CIP-003",
        level="l2",
        category="market-sizing",
        description="AeroTread narrowbody tire replacement TAM — exclude cargo/spares",
        instruction=email(
            sender="Emily Chen",
            practice="Industrial",
            subject="AeroTread — passenger narrowbody tire TAM before Thursday bid/no-bid",
            date="Monday, 10:15 AM",
            body="""
AeroTread wants a go/no-go on bidding the US passenger **narrowbody** mainline tire contract. Size **annual replacement unit demand** and TAM at the contract ASP.

Facts are split across fleet, utilization, and a cargo/spares note in `/app/matter/`. The bid committee will only count passenger narrowbody replacements — not cargo, not spare-pool stocking.

Hurdle: bid if TAM ≥ **$20M**.
""",
            schema="""
{
  "decision": "<go|no-go>",
  "annual_replacements": <float>,
  "tam_millions": <float>,
  "method": "<fleet × tires × cycles / life>"
}
""",
            method_hint="Show the stock × frequency build (fleet × tires per ship × cycles / landing life). State which exhibits you excluded and why.",
        ),
        matter={
            "fleet_register.csv": """
segment,aircraft,tires_per_aircraft,notes
passenger_narrowbody,180,8,Mainline US passenger NB only
passenger_widebody,22,12,Out of scope — different RFP
""",
            "utilization.txt": """
AeroTread — Utilization (passenger NB)
======================================
Average cycles per NB aircraft per year: 1,200
Certified landing life per tire: 180 landings
Contract ASP (replacement): $2,400 per tire

Do not annualize calendar-time wear; replacements are cycle-driven.
""",
            "cargo_and_spares.txt": """
Affiliate cargo fleet (DO NOT include unless the RFP is all-in):
- 40 widebody freighters, 14 tires each
- 800 cycles/year, replace every 250 landings
- Implied cargo replacements: 40 × 14 × (800/250) = 1,792

Spare-pool policy: hold 0.15 spare tires per in-service tire.
In-service NB tires = 180 × 8 = 1,440 → spare stock 216.
Spares are inventory, not annual replacement demand.

A junior model in the pack used 220 aircraft (added regional jets). Ignore that.
""",
        },
        oracle={
            "decision": "go",
            "annual_replacements": 9600.0,
            "tam_millions": 23.04,
            "method": "fleet × tires × cycles / landing life",
        },
        memo="""
We recommend go on the AeroTread passenger-narrowbody bid. Annual replacement demand is 9,600 tires and TAM is $23.04M, clearing the $20M hurdle. Cargo replacements (1,792) and the 216-tire spare pool are out of scope.

## Fleet × frequency
- 180 NB aircraft × 8 tires × (1,200 cycles / 180 landing life) = **9,600** replacements
- TAM: 9,600 × $2,400 = **$23.04M**
- Excluded: cargo 1,792 tires; spare-pool stock 216; 22 passenger widebodies; regional-jet 220-aircraft count

## Next step
Submit the NB-only bid package to the Thursday committee and lock the $2,400 ASP with procurement before cargo is added to scope.
""",
        lede_any=["9,600", "9600", "23.04"],
        lede_all=["go"],
        decision="go",
        bands=[("annual_replacements", 9500.0, 9700.0), ("tam_millions", 22.7, 23.4)],
        method_all=["cycle", "landing"],
        method_any=["cargo", "spare", "exclu"],
        next_any=["bid", "committee", "procurement", "submit", "lock"],
        reject_values=[("annual_replacements", 11392.0), ("annual_replacements", 9816.0)],
    )
)

add(
    case(
        task_id="CIP-005",
        level="l2",
        category="market-sizing",
        description="US economy-hotel room revenue TAM — exclude midscale and stale STR",
        instruction=email(
            sender="Sarah Martinez",
            practice="Hospitality",
            subject="LodgeCo — economy-segment room revenue before product-TAM review",
            date="Monday, 9:40 AM",
            body="""
LodgeCo is sizing whether a $400M RevPAR tool is worth building. We need **US economy-segment annual room revenue** only.

Use current census + occupancy/ADR in `/app/matter/`. A stale STR extract and a midscale rollup are in the pack as distractors.

Proceed if economy room revenue ≥ **$10B**.
""",
            schema="""
{
  "decision": "<proceed|hold>",
  "economy_room_nights_millions": <float>,
  "economy_room_revenue_billions": <float>,
  "method": "<properties × rooms × occ × ADR>"
}
""",
            method_hint="Build properties × rooms × 365 × occupancy × ADR. Do not mix midscale or the outdated STR snapshot.",
        ),
        matter={
            "economy_census.csv": """
segment,properties,rooms_per_property
economy,8200,92
midscale,6400,118
""",
            "current_adr_occ.txt": """
Current year (use these):
- Economy occupancy: 64%
- Economy ADR: $78
- Midscale occupancy: 68%
- Midscale ADR: $124
""",
            "stale_str_extract.txt": """
STR snapshot FY2019 (DO NOT USE for the live TAM):
- Economy rooms/property: 88
- Economy occupancy: 71%
- Economy ADR: $69

A partner sticky note says "just multiply 8,200 × 92 × 365 × $78" — that skips occupancy and overstates nights.
""",
        },
        oracle={
            "decision": "proceed",
            "economy_room_nights_millions": 176.33664,
            "economy_room_revenue_billions": 13.754,
            "method": "properties × rooms × occupancy × ADR",
        },
        memo="""
We recommend proceed: US economy-segment room revenue is $13.75B (176.3M room-nights at $78 ADR), above the $10B bar for LodgeCo's $400M RevPAR tool. Midscale and the FY2019 STR snapshot are excluded.

## Build
- Room-nights: 8,200 × 92 × 365 × 64% = **176.34M**
- Revenue: 176.34M × $78 = **$13.75B**
- Trap rejected: occupancy-free 8,200 × 92 × 365 × $78; midscale mix; 2019 STR 88 rooms / 71% / $69

## Next step
Put the $400M tool through Thursday product IC with the $13.75B economy-only TAM as the addressable base.
""",
        lede_any=["13.75", "13.8", "13.7"],
        lede_all=["proceed"],
        decision="proceed",
        bands=[
            ("economy_room_nights_millions", 174.0, 179.0),
            ("economy_room_revenue_billions", 13.5, 14.0),
        ],
        method_all=["occupancy", "adr"],
        method_any=["midscale", "str", "exclu"],
        next_any=["ic", "product", "thursday", "approve", "pilot"],
    )
)

add(
    case(
        task_id="CIP-006",
        level="l2",
        category="market-sizing",
        description="India smartphone sell-out TAM — exclude feature phones and gray sell-in",
        instruction=email(
            sender="Rahul Mehta",
            practice="Technology & Telecom",
            subject="Pixelate — India smartphone annual sell-out before entry IC",
            date="Tuesday, 8:50 AM",
            body="""
Pixelate wants a go/no-go on India entry. Size **annual smartphone sell-out units** (replacements + first-time) and dollar TAM at blended ASP.

`/app/matter/` has population, replacement, and a gray-market sell-in note that double-counts. Feature phones are not smartphones.

Enter if annual smartphone units are between **160M and 200M**.
""",
            schema="""
{
  "decision": "<go|no-go>",
  "annual_units_millions": <float>,
  "tam_billions": <float>,
  "method": "<users / cycle + first-time>"
}
""",
            method_hint="Users = population × 15+ share × smartphone penetration. Annual units = users / replacement cycle + first-time buyers. Use sell-out, not sell-in.",
        ),
        matter={
            "census.txt": """
India population: 1.42 billion
Share age 15+: 68%
Smartphone penetration among 15+: 54%
Feature-phone only among 15+: 19%
""",
            "replacement.txt": """
Observed replacement cycle (smartphones): 3.1 years
First-time smartphone buyers this year: 18.0 million
Blended sell-out ASP: $168
""",
            "sell_in_warning.txt": """
Distributor sell-in last year: 220 million units.
This includes ~40M gray-market double-counts and ~34M feature phones.
Do not use 220M as smartphone sell-out.

A channel memo quotes 521M smartphone users × 1/2.5 year cycle = 208M — that cycle is tablets, not phones.
""",
        },
        oracle={
            "decision": "go",
            "annual_units_millions": 186.201,
            "tam_billions": 31.282,
            "method": "users / replacement cycle + first-time",
        },
        memo="""
We recommend go on Pixelate India entry. Annual smartphone sell-out is 186.2M units and TAM is $31.3B, inside the 160–200M unit gate. The 220M sell-in and 2.5-year tablet cycle are rejected.

## Build
- Users: 1.42B × 68% × 54% = **521.4M**
- Replacements: 521.4 / 3.1 = **168.2M**
- Plus first-time 18.0M = **186.2M** units
- TAM: 186.2M × $168 = **$31.3B**

## Next step
File the India entry IC memo with sell-out (not sell-in) as the official TAM and commission a 6-city replacement-cycle diary.
""",
        lede_any=["186", "31.3", "31.28"],
        lede_all=["go"],
        decision="go",
        bands=[("annual_units_millions", 184.0, 188.5), ("tam_billions", 30.8, 31.8)],
        method_all=["replacement", "first-time"],
        method_any=["sell-in", "gray", "feature"],
        next_any=["ic", "diary", "commission", "file"],
        reject_values=[("annual_units_millions", 220.0), ("annual_units_millions", 208.0)],
    )
)

add(
    case(
        task_id="CIP-016",
        level="l2",
        category="profitability",
        description="SaaS gross-margin compression — isolate recurring hosting drag",
        instruction=email(
            sender="Nina Patel",
            practice="Software",
            subject="Nimbus — GM compression: hosting vs one-time migration",
            date="Monday, 2:10 PM",
            body="""
Nimbus GM fell from 72% to a reported 66% on $84M revenue. The CFO wants to know **recurring** GM after stripping the one-time migration, and which recurring line to attack.

Hurdle: renegotiate hosting if hosting drag ≥ **1.5 percentage points** of revenue; otherwise attack support mix.

Exhibits in `/app/matter/`.
""",
            schema="""
{
  "decision": "<renegotiate_hosting|fix_support>",
  "recurring_gm_pct": <float>,
  "hosting_drag_pp": <float>,
  "method": "<reported COGS − one-time, then pp of revenue>"
}
""",
            method_hint="Recurring COGS = reported COGS − one-time migration. Hosting drag pp = hosting rate hike / revenue × 100.",
        ),
        matter={
            "pnl.csv": """
item,amount_millions
revenue,84.0
reported_cogs,28.56
prior_year_cogs,23.52
""",
            "cogs_bridge.txt": """
Reported COGS $28.56M includes:
- One-time cloud migration (non-recurring): $2.52M
- Hosting rate hike vs last year (recurring): $1.68M
- Support mix shift (recurring): $0.84M
- Residual volume/other: remainder after the above vs last year's $23.52M
""",
            "cfo_note.txt": """
CFO draft treats the entire 6pp drop (72% → 66%) as hosting. That is wrong.
Also do not "add back" the rate hike when computing recurring GM — the hike is recurring.
""",
        },
        oracle={
            "decision": "renegotiate_hosting",
            "recurring_gm_pct": 69.0,
            "hosting_drag_pp": 2.0,
            "method": "reported COGS minus one-time; hosting hike / revenue",
        },
        memo="""
We recommend renegotiate_hosting. Recurring GM is 69.0% after stripping the $2.52M one-time migration, and the hosting rate hike is a 2.0pp drag — above the 1.5pp trigger. Support mix is only 1.0pp.

## Bridge
- Reported GM: 1 − 28.56/84 = 66.0%
- Recurring COGS: 28.56 − 2.52 = **$26.04M** → recurring GM **69.0%**
- Hosting drag: 1.68 / 84 = **2.0pp**
- Support mix: 0.84 / 84 = 1.0pp

## Next step
Open the hosting renegotiation workstream this week and bring a 150-bps take-or-pay counter to Friday SteCo.
""",
        lede_any=["69", "2.0"],
        lede_all=["renegotiate"],
        decision="renegotiate_hosting",
        bands=[("recurring_gm_pct", 68.5, 69.5), ("hosting_drag_pp", 1.9, 2.1)],
        method_all=["one-time", "hosting"],
        method_any=["migration", "recurring"],
        next_any=["renegotiat", "steco", "workstream", "counter"],
    )
)

add(
    case(
        task_id="CIP-018",
        level="l2",
        category="profitability",
        description="Hotel F&B mix — banquet vs outlet contribution after shared kitchen",
        instruction=email(
            sender="Elena Vasquez",
            practice="Hospitality & Leisure",
            subject="Harborlight — F&B: keep banquet or cut outlets?",
            date="Tuesday, 11:05 AM",
            body="""
Harborlight's GM wants to close in-house restaurants because departmental profit is weak. Build **true contribution after shared-kitchen allocation** for banquet vs outlets.

Keep banquet and cut outlets only if banquet true contribution ≥ **$1.8M** and outlets are negative.

`/app/matter/` has departmental P&L plus a controller note on shared kitchen and banquet labor.
""",
            schema="""
{
  "decision": "<keep_banquet_cut_outlets|keep_both|cut_banquet>",
  "banquet_true_contribution_millions": <float>,
  "outlet_true_contribution_millions": <float>,
  "method": "<dept profit + add-back − shared kitchen>"
}
""",
            method_hint="True contribution = departmental profit + wrongly loaded shared kitchen − any banquet labor parked in rooms.",
        ),
        matter={
            "dept_pnl.csv": """
line,banquet_m,outlets_m
revenue,5.40,2.80
dept_profit,2.80,-0.80
""",
            "controller_note.txt": """
Shared kitchen opex $1.50M is loaded 50/50 into each department ($0.75M each) inside the dept-profit figures above.
Kitchen exists primarily for banquet; a fair split is 85% banquet / 15% outlets.

Rooms P&L hides $0.20M of banquet overtime (setup crew on rooms payroll).
Charge that overtime to banquet.

Outlet dept profit of −$0.80M already includes their $0.75M kitchen load.
""",
            "gm_draft.txt": """
GM draft: keep outlets because "they're only losing $0.80M and banquet is fine at $2.80M."
That ignores the kitchen reallocation and the hidden overtime.
""",
        },
        oracle={
            "decision": "keep_banquet_cut_outlets",
            "banquet_true_contribution_millions": 2.075,
            "outlet_true_contribution_millions": -0.275,
            "method": "dept profit + kitchen add-back − fair kitchen − hidden overtime",
        },
        memo="""
We recommend keep_banquet_cut_outlets. Banquet true contribution is $2.08M, above the $1.8M keep-bar. Outlets are −$0.28M after a fair kitchen split.

## True contribution
- Banquet: 2.80 + 0.75 kitchen add-back − 1.275 fair kitchen (85% of $1.50M) − 0.20 hidden OT = **$2.075M**
- Outlets: −0.80 + 0.75 − 0.225 fair kitchen (15%) = **−$0.275M**
- Reject the GM draft that keeps outlets on the loaded −$0.80M / $2.80M pair.

## Next step
Close the two outlets at month-end, move kitchen allocation to 85/15, and shift $0.20M setup overtime onto the banquet payroll.
""",
        lede_any=["2.08", "2.075", "-0.28", "-0.275"],
        lede_all=["keep_banquet"],
        decision="keep_banquet_cut_outlets",
        bands=[
            ("banquet_true_contribution_millions", 2.00, 2.15),
            ("outlet_true_contribution_millions", -0.32, -0.23),
        ],
        method_all=["kitchen", "overtime"],
        method_any=["85%", "0.20", "0.2"],
        next_any=["close", "month-end", "payroll", "shift"],
    )
)

# Side-effect imports register the remaining 26 cases into SPECS.
import hardened_l2c  # noqa: E402,F401
import hardened_l2d  # noqa: E402,F401
import hardened_l2e  # noqa: E402,F401
import hardened_l3_stubs  # noqa: E402,F401
import hardened_more_cases  # noqa: E402,F401


def main() -> None:
    expected = {
        "CIP-003", "CIP-005", "CIP-006", "CIP-016", "CIP-018", "CIP-019",
        "CIP-030", "CIP-033", "CIP-034", "CIP-038", "CIP-040", "CIP-041",
        "CIP-043", "CIP-053", "CIP-057", "CIP-059", "CIP-062", "CIP-064",
        "CIP-067", "CIP-070", "CIP-076", "CIP-077", "CIP-079", "CIP-084",
        "CIP-085", "CIP-087", "CIP-090", "CIP-091", "CIP-096", "CIP-097",
        "CIP-100",
    }
    missing = expected - set(SPECS)
    extra = set(SPECS) - expected
    if missing or extra:
        raise SystemExit(f"spec mismatch missing={sorted(missing)} extra={sorted(extra)}")
    for task_id in sorted(SPECS):
        write_task(task_id, SPECS[task_id])
        print(f"wrote {task_id}")
    print(f"---\n{len(SPECS)} hardened stub tasks written")


if __name__ == "__main__":
    main()
