"""Hardened L3 stub replacements: conflicting exhibits, no precomputed answers."""

from __future__ import annotations

from harden_common import add, case, email

add(
    case(
        task_id="CIP-038",
        level="l3",
        category="go-to-market",
        description="Ag co-op DTC beef — hanging yield then retail yield, not live weight",
        instruction=email(
            sender="Maria Santos",
            practice="Agriculture",
            subject="Prairie Co-op — DTC beef incremental vs wholesale",
            date="Monday, 10:05 AM",
            body="""
Prairie Co-op is debating a DTC beef box. Two exhibits disagree on whether the 70% retail yield applies to **live weight** or **hanging weight**. Use hanging first (62% of live), then 70% retail of hanging.

Launch DTC if incremental contribution vs wholesale ≥ **$1.5M**.
""",
            schema="""
{
  "decision": "<launch|stay_wholesale>",
  "retail_lb": <float>,
  "dtc_contribution_millions": <float>,
  "wholesale_contribution_millions": <float>,
  "method": "<live × hang × retail; DTC net price vs wholesale>"
}
""",
            method_hint="Retail lb = live × 62% × 70%. DTC net = price × (1 − 4% returns) − $1.90 fulfillment. Wholesale = retail lb × $4.10. Do not use live pounds as sellable.",
        ),
        matter={
            "kill_sheet.txt": """
Annual live weight available: 2.2 million lb
Dressing / hanging yield: 62% of live
""",
            "exhibit_a_dtc.txt": """
DTC Exhibit A (marketing):
Applies 70% "retail yield" to LIVE weight → 1.54M sellable lb.
DTC list $8.40/lb, fulfillment $1.90/lb, returns 4%.
This overstates sellable pounds. 70% is of hanging, not live.
""",
            "exhibit_b_plant.txt": """
Plant Exhibit B:
Retail / boxed yield is 70% of HANGING weight.
Wholesale alternative: $4.10 / retail lb, no fulfillment, no returns.
""",
            "scratch.txt": """
A summer intern multiplied 2.2M live × ($8.40 − $1.90) and called it DTC contribution.
""",
        },
        oracle={
            "decision": "launch",
            "retail_lb": 954800.0,
            "dtc_contribution_millions": 5.885,
            "wholesale_contribution_millions": 3.915,
            "method": "live × hang × retail; DTC net price vs wholesale",
        },
        memo="""
We recommend launch. Sellable retail pounds are 954,800. DTC contribution is $5.89M versus wholesale $3.92M — incremental $1.97M, above $1.5M. Exhibit A's 1.54M live-based pounds are wrong.

## Build
- Hanging: 2.2M × 62% = 1.364M lb
- Retail: 1.364M × 70% = **954,800 lb**
- DTC net $/lb: $8.40 × 0.96 − $1.90 = **$6.164**
- DTC: 954,800 × 6.164 = **$5.885M**
- Wholesale: 954,800 × $4.10 = **$3.915M**

## Next step
Pilot 8,000 boxes through the existing locker network this quarter and lock the $8.40 list.
""",
        lede_any=["954,800", "954800", "5.89", "5.885"],
        lede_all=["launch"],
        decision="launch",
        bands=[
            ("retail_lb", 950000.0, 960000.0),
            ("dtc_contribution_millions", 5.75, 6.00),
            ("wholesale_contribution_millions", 3.85, 3.98),
        ],
        method_all=["hanging", "retail"],
        method_any=["live", "exhibit"],
        next_any=["pilot", "locker", "boxes", "list"],
        reject_values=[("retail_lb", 1540000.0), ("retail_lb", 2200000.0)],
    )
)

add(
    case(
        task_id="CIP-062",
        level="l3",
        category="pricing",
        description="Municipal water rate — elasticity plus treatment save vs $4.5M plant",
        instruction=email(
            sender="Thomas Wright",
            practice="Government",
            subject="Cedar Falls — $5.10/kgal vs $4.5M plant need",
            date="Tuesday, 8:15 AM",
            body="""
Cedar Falls proposed $5.10/kgal (from $4.20) on 82,000 accounts. Finance ignored elasticity. Public works ignored treatment-cost savings on lower volume.

Approve the rate if incremental revenue **plus** treatment save ≥ **$4.5M**. Otherwise delay the plant.
""",
            schema="""
{
  "decision": "<approve|delay>",
  "incremental_revenue_millions": <float>,
  "treatment_save_millions": <float>,
  "total_vs_plant_millions": <float>,
  "method": "<accounts × months × kgal × rate with ε=−0.15>"
}
""",
            method_hint="kgal/account/month now = 5.4. New volume = 5.4 × (1 + ε × %ΔP). Treatment save uses $1.10/kgal on the volume decline.",
        ),
        matter={
            "tariff.txt": """
Accounts: 82,000
Current use: 5,400 gallons / account / month (= 5.4 kgal)
Current rate: $4.20 / kgal
Proposed rate: $5.10 / kgal
Price elasticity: −0.15 (volume vs rate)
Treatment variable cost: $1.10 / kgal
Plant funding need: $4.5M / year
""",
            "finance_exhibit.txt": """
Finance (no elasticity): 82,000 × 12 × 5.4 × $5.10 = $27.10M proposed revenue
vs current 82,000 × 12 × 5.4 × $4.20 = $22.32M → +$4.79M. Overstates.
""",
            "public_works.txt": """
Public works modeled elasticity but forgot the $1.10/kgal treatment save on lost gallons.
""",
        },
        oracle={
            "decision": "delay",
            "incremental_revenue_millions": 3.911,
            "treatment_save_millions": 0.188,
            "total_vs_plant_millions": 4.099,
            "method": "accounts × months × kgal × rate with elasticity −0.15",
        },
        memo="""
We recommend delay. Incremental revenue is $3.91M and treatment save is $0.19M, totaling $4.10M — short of the $4.5M plant need. Finance's $4.79M ignores elasticity.

## Build
- %ΔP: (5.10 − 4.20) / 4.20 = 21.429%
- New kgal: 5.4 × (1 − 0.15 × 0.21429) = **5.2264**
- New revenue: 82k × 12 × 5.2264 × 5.10 = **$26.228M**
- Current: 82k × 12 × 5.4 × 4.20 = **$22.317M**
- Incremental revenue **$3.911M**; treatment save 82k × 12 × 0.1736 × 1.10 = **$0.188M**
- Total **$4.099M** < $4.5M

## Next step
Delay the plant vote and bring a $5.25/kgal or phased-construction option to next month's council.
""",
        lede_any=["4.10", "4.099", "3.91"],
        lede_all=["delay"],
        decision="delay",
        bands=[
            ("incremental_revenue_millions", 3.80, 4.05),
            ("treatment_save_millions", 0.17, 0.21),
            ("total_vs_plant_millions", 3.95, 4.20),
        ],
        method_all=["elastic", "treatment"],
        method_any=["kgal", "4.5"],
        next_any=["council", "delay", "5.25", "phased"],
    )
)

add(
    case(
        task_id="CIP-070",
        level="l3",
        category="growth",
        description="Streaming ad-lite tier — price mix plus ads minus ad-lite churn",
        instruction=email(
            sender="Priya Nair",
            practice="Media",
            subject="Streamhouse — ad-lite net vs $25M hurdle",
            date="Monday, 1:00 PM",
            body="""
Streamhouse wants a $12.99 ad-lite tier (35% take; rest stay at $15.99). Finance's exhibit ignores ad-lite churn. Product's exhibit ignores ad ARPU.

Launch only if net revenue vs base ≥ **$25M**.
""",
            schema="""
{
  "decision": "<launch|hold>",
  "net_vs_base_millions": <float>,
  "ad_revenue_millions": <float>,
  "method": "<mix of prices + ad ARPU − 4% ad-lite churn>"
}
""",
            method_hint="Base = 4.2M × $15.99 × 12. New = ad-lite subs × ($12.99+$4.80) × 12 × (1−4% churn) + stay × $15.99 × 12.",
        ),
        matter={
            "subs.txt": """
Subs: 4.2 million
Current price: $15.99 / month
Ad-lite price: $12.99 / month
Expected take: 35%
Ad ARPU on ad-lite: $4.80 / month
Ad-lite churn from ads: 4% of ad-lite subs (lose their $12.99 and $4.80)
""",
            "finance_exhibit.txt": """
Finance: 1.47M × $12.99 × 12 + 2.73M × $15.99 × 12 + 1.47M × $4.80 × 12
= $837.6M vs $805.9M base → +$31.8M. Ignores 4% ad-lite churn.
""",
            "product_exhibit.txt": """
Product: models the $3 price cut and 4% churn, **drops ad ARPU entirely**.
""",
        },
        oracle={
            "decision": "hold",
            "net_vs_base_millions": 19.199,
            "ad_revenue_millions": 81.285,
            "method": "mix of prices + ad ARPU − 4% ad-lite churn",
        },
        memo="""
We recommend hold. Net vs base is $19.2M after 4% ad-lite churn, below the $25M hurdle. Finance's +$31.8M skips churn; product skips $81.3M of remaining ad revenue.

## Build
- Base: 4.2M × $15.99 × 12 = **$805.896M**
- Ad-lite after churn: 1.47M × 96% = 1.4112M
- Ad-lite sub+ad: 1.4112M × ($12.99+$4.80) × 12 = **$301.263M**
- Stay: 2.73M × $15.99 × 12 = **$523.832M**
- New total $825.095M; net vs base **$19.199M**
- Remaining ad revenue: 1.4112M × $4.80 × 12 = **$81.285M**

## Next step
Hold the ad-lite launch and test a $13.99 price with a 2% churn cap in one region.
""",
        lede_any=["19.2", "19.19"],
        lede_all=["hold"],
        decision="hold",
        bands=[
            ("net_vs_base_millions", 18.8, 19.7),
            ("ad_revenue_millions", 80.5, 82.0),
        ],
        method_all=["churn", "ad"],
        method_any=["15.99", "12.99"],
        next_any=["hold", "13.99", "region", "test"],
    )
)

add(
    case(
        task_id="CIP-079",
        level="l3",
        category="investment-decision",
        description="Pharma diagnostic kit — field false-positive cost, not analytical",
        instruction=email(
            sender="Priya Nair",
            practice="Healthcare & Life Sciences",
            subject="HelixDx kit — field FP cost vs $2M hurdle",
            date="Wednesday, 11:20 AM",
            body="""
HelixDx wants to launch a kit (220k tests). Lab quotes a 0.8% **analytical** false-positive rate. Field follow-up runs at **3.2%**. Each FP follow-up costs $210.

Launch only if contribution after FP, launch opex, and cannibal ≥ **$2.0M**.
""",
            schema="""
{
  "decision": "<launch|no-go>",
  "unit_contribution_millions": <float>,
  "fp_cost_millions": <float>,
  "net_millions": <float>,
  "method": "<(ASP−COGS)×tests − field FP − opex − cannibal>"
}
""",
            method_hint="Use 3.2% field FP, not 0.8% analytical. Cannibal $1.2M. Launch opex $3.8M.",
        ),
        matter={
            "kit.txt": """
Year-1 tests: 220,000
ASP: $48
COGS: $17
Launch opex: $3.8M
Cannibal of existing panel: $1.2M
Field false-positive rate: 3.2%
Follow-up cost per FP: $210
""",
            "lab_exhibit.txt": """
Lab analytical FP: 0.8%. Using 0.8% understates follow-up cost by 4×.
""",
            "medaffairs.txt": """
Medical affairs: field discordant / confirmatory rate is 3.2% in the three-site study.
That is the number payers will experience.
""",
        },
        oracle={
            "decision": "no-go",
            "unit_contribution_millions": 6.82,
            "fp_cost_millions": 1.478,
            "net_millions": 0.342,
            "method": "(ASP−COGS)×tests − field FP − opex − cannibal",
        },
        memo="""
We recommend no-go. Unit contribution is $6.82M but field FP cost is $1.48M; after $3.8M opex and $1.2M cannibal, net is $0.34M — below $2.0M. The 0.8% analytical FP is the wrong rate.

## Build
- Unit: 220k × ($48 − $17) = **$6.82M**
- FP: 220k × 3.2% × $210 = **$1.478M**
- Net: 6.82 − 1.478 − 3.8 − 1.2 = **$0.342M**

## Next step
Pause the launch and rerun the field study powered for a ≤1.5% confirmatory rate before SteCo.
""",
        lede_any=["0.34", "0.342", "1.48"],
        lede_all=["no-go"],
        decision="no-go",
        bands=[
            ("unit_contribution_millions", 6.7, 6.95),
            ("fp_cost_millions", 1.40, 1.55),
            ("net_millions", 0.28, 0.40),
        ],
        method_all=["field", "cannibal"],
        method_any=["0.8", "analytical", "3.2"],
        next_any=["pause", "field", "steco", "study"],
    )
)

add(
    case(
        task_id="CIP-087",
        level="l3",
        category="investment-decision",
        description="Community solar — temperate yield and 88% offtake vs 9% hurdle",
        instruction=email(
            sender="James Park",
            practice="Energy",
            subject="HelioCo-op 18MW — temperate yield, not desert",
            date="Monday, 9:25 AM",
            body="""
18 MW community solar. Developer deck uses 1,800 kWh/kW-year (desert) and 100% offtake. Site is temperate: **1,450 kWh/kW-year** and **88% offtake**.

Build if EBITDA / capex ≥ **9%**. Capex is $21.6M.
""",
            schema="""
{
  "decision": "<build|no-go>",
  "ebitda_millions": <float>,
  "ebitda_over_capex_pct": <float>,
  "method": "<MW × kWh/kW × price × offtake − O&M − lease − interconnection>"
}
""",
            method_hint="Revenue = 18,000 kW × 1,450 × $0.11 × 88%. Subtract O&M $0.28M, lease $0.45M, interconnection $0.22M.",
        ),
        matter={
            "site.txt": """
DC capacity: 18 MW (= 18,000 kW)
Temperate yield: 1,450 kWh / kW-year
PPA price: $0.11 / kWh
Subscription / offtake: 88%
O&M: $0.28M
Land lease: $0.45M
Interconnection / schedule 9: $0.22M
Capex: $21.6M
""",
            "developer_deck.txt": """
Developer: 18,000 × 1,800 × $0.11 × 100% = $3.564M revenue (desert, full offtake).
Do not use 1,800 or 100%.
""",
            "utility_note.txt": """
Utility confirmed 88% subscribed. Unsubscribed generation is spilled at $0.
""",
        },
        oracle={
            "decision": "no-go",
            "ebitda_millions": 1.576,
            "ebitda_over_capex_pct": 7.3,
            "method": "MW × kWh/kW × price × offtake − O&M − lease − interconnection",
        },
        memo="""
We recommend no-go. EBITDA is $1.58M (7.3% of $21.6M capex), below the 9% hurdle. The developer's $3.56M revenue uses desert yield and 100% offtake.

## Build
- Revenue: 18,000 × 1,450 × $0.11 × 0.88 = **$2.526M**
- Costs: 0.28 + 0.45 + 0.22 = **$0.95M**
- EBITDA: **$1.576M**
- 1.576 / 21.6 = **7.3%** < 9%

## Next step
Send the developer a no-bid and reopen only if capex is ≤ $17.5M or offtake is contracted at 98%.
""",
        lede_any=["1.58", "1.576", "7.3"],
        lede_all=["no-go"],
        decision="no-go",
        bands=[("ebitda_millions", 1.52, 1.64), ("ebitda_over_capex_pct", 7.0, 7.6)],
        method_all=["offtake", "yield"],
        method_any=["desert", "1450", "1,450"],
        next_any=["no-bid", "capex", "17.5", "reopen"],
    )
)

add(
    case(
        task_id="CIP-096",
        level="l3",
        category="turnaround",
        description="Airline cost turnaround — strip hedge loss, add labor contract",
        instruction=email(
            sender="Marcus Williams",
            practice="Travel & Transportation",
            subject="NorthAir — run-rate margin vs $500M board ask",
            date="Tuesday, 5:40 PM",
            body="""
NorthAir reports $8.308B cost on 62B ASMs. The $180M fuel-hedge loss is **one-time**. Labor steps up **4.0%** next year on the labor share.

Board wants **$500M** run-rate operating profit. Say whether run-rate gets there.
""",
            schema="""
{
  "decision": "<enough|more_cuts>",
  "runrate_cost_billions": <float>,
  "runrate_profit_millions": <float>,
  "gap_to_500_millions": <float>,
  "method": "<reported cost − hedge + labor step; vs revenue>"
}
""",
            method_hint="Labor = 31% of reported cost. Run-rate cost = reported − $0.180B hedge + 4% of labor. Revenue = $8.550B.",
        ),
        matter={
            "casm.txt": """
ASMs: 62 billion
Reported cost: $8.308B (CASM 13.4¢)
Revenue: $8.550B
Fuel share of reported cost: 28%
Labor share: 31%
Other: 41%
""",
            "fuel_exhibit.txt": """
Fuel exhibit: $180M hedge loss sits inside reported fuel. Treasury: one-time, strip it.
A consultant kept it in run-rate "to be conservative."
""",
            "labor_exhibit.txt": """
CBA: +4.0% on the labor dollar next year. Do not apply 4% to total cost.
HR draft applied 4% to $8.308B.
""",
        },
        oracle={
            "decision": "more_cuts",
            "runrate_cost_billions": 8.231,
            "runrate_profit_millions": 319.0,
            "gap_to_500_millions": 181.0,
            "method": "reported cost − hedge + labor step; vs revenue",
        },
        memo="""
We recommend more_cuts. Run-rate profit is $319M, $181M short of the $500M board ask. Strip the $180M hedge loss and add 4% only on the 31% labor share.

## Build
- Labor base: 0.31 × 8.308 = **$2.575B**; +4% = **+$0.103B**
- Run-rate cost: 8.308 − 0.180 + 0.103 = **$8.231B**
- Profit: 8.550 − 8.231 = **$0.319B ($319M)**
- Gap to $500M: **$181M**

## Next step
Bring a $180M non-labor CASM program to Friday SteCo; do not claim the hedge roll-off closes the gap.
""",
        lede_any=["319", "181"],
        lede_all=["more_cuts"],
        decision="more_cuts",
        bands=[
            ("runrate_cost_billions", 8.21, 8.25),
            ("runrate_profit_millions", 310.0, 330.0),
            ("gap_to_500_millions", 170.0, 190.0),
        ],
        method_all=["hedge", "labor"],
        method_any=["one-time", "31%"],
        next_any=["steco", "casm", "180", "friday"],
    )
)
