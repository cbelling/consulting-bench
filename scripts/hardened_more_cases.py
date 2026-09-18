"""Additional hardened L2/L3 case builders. Imported by generate_hardened_stubs.py."""

from __future__ import annotations

from harden_common import add, case, email

# CIP-019 Pharma plant utilization
add(
    case(
        task_id="CIP-019",
        level="l2",
        category="operations",
        description="Pharma plant: run extra shift only if true OEE contribution clears hurdle",
        instruction=email(
            sender="Priya Nair",
            practice="Healthcare & Life Sciences",
            subject="HelixForm — Saturday shift go/no-go on true OEE",
            date="Monday, 4:20 PM",
            body="""
HelixForm wants a Saturday shift at Plant B. Use **true OEE** (availability × performance × quality) on the constrained granulation line, then contribution on incremental saleable kg.

Add the Saturday shift only if incremental weekly contribution ≥ **$42k**. A maintenance log parks changeover in "quality"; do not double-count it.

Exhibits in `/app/matter/`.
""",
            schema="""
{
  "decision": "<add_shift|no_shift>",
  "true_oee_pct": <float>,
  "incremental_weekly_contribution_k": <float>,
  "method": "<OEE × hours × rate × yield × margin − Saturday labor>"
}
""",
            method_hint="True OEE = availability × performance × quality. Incremental saleable kg = Saturday hours × nameplate × true OEE. Subtract Saturday crew cost.",
        ),
        matter={
            "line_card.txt": """
Granulation line nameplate: 800 kg/hour theoretical
Scheduled Saturday hours: 12
Saturday crew cost: $18,000
Contribution margin on saleable kg: $12.50/kg
Weekday true OEE is not a proxy — recompute from Saturday-only logs.
""",
            "saturday_logs.csv": """
metric,value,notes
uptime_hours,9.0,12 scheduled; 3.0h changeover + micro-stops
ideal_cycle_kg_per_up_hour,800,
actual_output_kg,6480,during the 9.0 uptime hours
saleable_kg,6156,324 kg scrap (quality)
""",
            "maintenance_trap.txt": """
Maintenance tagged the 3.0h changeover as a "quality event" and restated quality at 88%.
Do not apply that 88% on top of the 6156/6480 already-saleable figure.

Ops draft used weekday OEE 71% × 12h × 800 × $12.50 − $18k = $49.2k. Wrong period.
""",
        },
        oracle={
            "decision": "add_shift",
            "true_oee_pct": 64.125,
            "incremental_weekly_contribution_k": 58.95,
            "method": "OEE × hours × rate × yield × margin − Saturday labor",
        },
        memo="""
We recommend add_shift. Saturday true OEE is 64.1% and incremental weekly contribution is $59.0k, above the $42k hurdle. The weekday 71% OEE and the double-counted 88% quality restatement are rejected.

## OEE and contribution
- Availability: 9.0 / 12 = 75.0%
- Performance: 6,480 / (9.0 × 800) = 90.0%
- Quality: 6,156 / 6,480 = 95.0%
- True OEE: 0.75 × 0.90 × 0.95 = **64.125%**
- Saleable kg: 12 × 800 × 0.64125 = **6,156**
- Contribution: 6,156 × $12.50 − $18,000 = **$58,950**

## Next step
Approve the Saturday crew roster at Wednesday ops and lock raw-material inbound for a 6-week pilot.
""",
        lede_any=["64.1", "59", "58.9"],
        lede_all=["add_shift"],
        decision="add_shift",
        bands=[("true_oee_pct", 63.5, 64.8), ("incremental_weekly_contribution_k", 57.5, 60.5)],
        method_all=["availability", "quality"],
        method_any=["performance", "oee"],
        next_any=["roster", "pilot", "approve", "ops"],
        reject_values=[("incremental_weekly_contribution_k", 49.2)],
    )
)

add(
    case(
        task_id="CIP-030",
        level="l2",
        category="investment-decision",
        description="Airline new route — contribution after airport incentives expire",
        instruction=email(
            sender="Marcus Williams",
            practice="Travel & Transportation",
            subject="NorthAir BOS–LIS — year-3 contribution after incentive cliff",
            date="Tuesday, 9:00 AM",
            body="""
NorthAir is deciding BOS–LIS. Year 1–2 look fine because of airport incentives. We need **year-3 contribution after incentives expire**, including crew premium and a diverted connecting-feed spill.

Launch only if year-3 contribution ≥ **$4.0M**.

Do not annualize the year-1 incentive as if it lasts.
""",
            schema="""
{
  "decision": "<launch|pass>",
  "year3_contribution_millions": <float>,
  "incentive_year1_millions": <float>,
  "method": "<RASM × ASMs − CASM ex-incentive − spill>"
}
""",
            method_hint="Year-3 revenue = RASM × ASMs. Subtract cash CASM (no incentive credit) × ASMs, crew premium, and connecting-feed spill.",
        ),
        matter={
            "route_card.csv": """
item,value
annual_asms_millions,420
year3_rasm_cents,11.4
cash_casm_ex_incentive_cents,10.1
crew_premium_millions,1.8
connecting_feed_spill_millions,0.9
""",
            "incentive_memo.txt": """
Airport incentive: $6.5M in year 1, $3.0M in year 2, **$0 in year 3**.
Network planning's "steady-state" deck still credits $6.5M every year. That is wrong.

A second note loads 480M ASMs (includes a phantom 4th weekly). Use 420M.
""",
            "casm_trap.txt": """
Reported CASM of 8.6¢ already nets the year-1 incentive against cost.
Do not use 8.6¢ for year 3. Use cash CASM ex-incentive 10.1¢.
""",
        },
        oracle={
            "decision": "pass",
            "year3_contribution_millions": 2.76,
            "incentive_year1_millions": 6.5,
            "method": "RASM × ASMs − cash CASM − crew premium − spill",
        },
        memo="""
We recommend pass on BOS–LIS. Year-3 contribution is $2.76M after the incentive cliff, below the $4.0M launch hurdle. Year-1 $6.5M incentive and the 8.6¢ reported CASM are not steady-state.

## Year-3 build
- Revenue: 420M ASMs × $0.114 = **$47.88M**
- Cash cost: 420M × $0.101 = **$42.42M**
- Crew premium $1.8M + spill $0.9M
- Contribution: 47.88 − 42.42 − 1.8 − 0.9 = **$2.76M**

## Next step
Decline the slot request this week and keep LIS coverage via the MAD connect instead of a BOS launch.
""",
        lede_any=["2.76", "2.8"],
        lede_all=["pass"],
        decision="pass",
        bands=[
            ("year3_contribution_millions", 2.6, 2.9),
            ("incentive_year1_millions", 6.4, 6.6),
        ],
        method_all=["incentive", "casm"],
        method_any=["spill", "year-3", "year 3"],
        next_any=["decline", "slot", "mad", "connect"],
        reject_values=[("year3_contribution_millions", 9.26)],
    )
)

add(
    case(
        task_id="CIP-033",
        level="l2",
        category="adjacency",
        description="Pet-insurance adjacency — combined ratio after adverse selection",
        instruction=email(
            sender="Olivia Grant",
            practice="Financial Services",
            subject="PawSure — launch only if combined ratio ≤ 92%",
            date="Monday, 1:15 PM",
            body="""
PawSure (homeowners carrier) is looking at pet insurance. Build the **year-2 combined ratio** after adverse selection and a 12% cannibalization of the riders already sold on HO policies.

Launch only if combined ratio ≤ **92%**.

The actuary's 81% loss ratio ignores the selection load in `/app/matter/`.
""",
            schema="""
{
  "decision": "<launch|no-go>",
  "year2_combined_ratio_pct": <float>,
  "cannibalized_rider_profit_millions": <float>,
  "method": "<(loss + lae + opex + selection) / GWP>"
}
""",
            method_hint="Combined ratio = (loss + LAE + opex + adverse-selection load) / GWP. Separately size HO-rider profit lost.",
        ),
        matter={
            "pet_plan.txt": """
Year-2 GWP: $48.0M
Base loss ratio (booked, no selection): 81%
LAE: 6% of GWP
Opex (acquisition + admin): 11% of GWP
""",
            "selection_and_riders.txt": """
Adverse selection load: +9 pp on loss ratio (claims team, not pricing).
Existing HO pet-rider profit at risk: $3.6M today.
Cannibalization: 12% of that rider profit disappears if standalone launches.

Pricing's 81% + 6% + 11% = 98% draft **forgets selection**. Another draft uses 81%+6%+11%+9% on $60M GWP (includes a cancelled vet-network deal). Use $48M.
""",
        },
        oracle={
            "decision": "no-go",
            "year2_combined_ratio_pct": 107.0,
            "cannibalized_rider_profit_millions": 0.432,
            "method": "(loss + LAE + opex + selection) / GWP",
        },
        memo="""
We recommend no-go on PawSure standalone pet. Year-2 combined ratio is 107%, above the 92% ceiling, and the launch would still shave $0.43M of HO-rider profit.

## Combined ratio
- Loss 81% + selection 9% + LAE 6% + opex 11% = **107%**
- Cannibalized rider profit: 12% × $3.6M = **$0.432M**
- Reject $60M GWP and the 98% draft that drops selection.

## Next step
Kill the standalone filing and instead reprice the HO pet rider with the 9pp selection load.
""",
        lede_any=["107"],
        lede_all=["no-go"],
        decision="no-go",
        bands=[
            ("year2_combined_ratio_pct", 106.0, 108.0),
            ("cannibalized_rider_profit_millions", 0.40, 0.47),
        ],
        method_all=["selection", "combined"],
        method_any=["rider", "cannibal"],
        next_any=["kill", "reprice", "rider", "filing"],
    )
)

add(
    case(
        task_id="CIP-034",
        level="l2",
        category="strategy",
        description="3P marketplace take-rate vs 1P margin after returns and ads",
        instruction=email(
            sender="Daniel Cho",
            practice="Consumer & Retail",
            subject="Cartly — 3P vs 1P on the home-goods category",
            date="Wednesday, 8:30 AM",
            body="""
Cartly can flip home-goods from 1P to 3P. Compare **category contribution** under 1P vs 3P after returns, ads, and fulfillment.

Flip to 3P only if 3P contribution exceeds 1P by ≥ **$8M**.

The marketplace GM quotes take-rate × GMV and stops. That is incomplete.
""",
            schema="""
{
  "decision": "<flip_3p|keep_1p>",
  "onep_contribution_millions": <float>,
  "threep_contribution_millions": <float>,
  "method": "<1P margin after returns/fulfill vs take-rate + ads − 3P costs>"
}
""",
            method_hint="1P = GMV × (gross margin − return rate × landed cost share) − fulfillment. 3P = GMV × take-rate + ads − 3P ops − referral leakage.",
        ),
        matter={
            "category.csv": """
item,value
gmv_millions,240
onep_gross_margin_pct,28
return_rate_pct,14
landed_cost_share_of_gmv_pct,55
onep_fulfillment_millions,18.0
take_rate_pct,14
ads_on_3p_millions,6.5
threep_ops_millions,4.0
referral_leakage_millions,3.2
""",
            "gm_shortcut.txt": """
Marketplace GM: 3P = 14% × $240M = $33.6M. Claims a $20M+ beat vs 1P.
This ignores ads, 3P ops, referral leakage, and the 1P return/fulfillment drag.

Do not apply the 14% return rate to 3P (sellers eat returns).
""",
        },
        oracle={
            "decision": "keep_1p",
            "onep_contribution_millions": 30.72,
            "threep_contribution_millions": 32.9,
            "method": "1P margin after returns/fulfill vs take-rate + ads − 3P costs",
        },
        memo="""
We recommend keep_1p. 3P contribution is $32.9M vs 1P $30.72M — only a $2.18M beat, below the $8M flip hurdle. The $33.6M take-rate shortcut is not contribution.

## Build
- 1P: 240 × 28% = 67.2; return drag 240 × 14% × 55% = 18.48; minus $18.0M fulfill → **$30.72M**
- 3P: 240 × 14% = 33.6; plus ads 6.5; minus ops 4.0 and leakage 3.2 → **$32.9M**
- Gap $2.18M < $8M → keep 1P

## Next step
Hold the 3P flip and run a 90-day ads-density test on 1P home-goods instead.
""",
        lede_any=["30.72", "32.9"],
        lede_all=["keep_1p"],
        decision="keep_1p",
        bands=[
            ("onep_contribution_millions", 30.0, 31.5),
            ("threep_contribution_millions", 32.3, 33.5),
        ],
        method_all=["return", "take-rate"],
        method_any=["fulfill", "leakage", "ads"],
        next_any=["hold", "90-day", "ads", "test"],
    )
)

add(
    case(
        task_id="CIP-040",
        level="l2",
        category="m-and-a",
        description="Organic CPG brand acquisition — syn-adjusted ROIC vs 13% hurdle",
        instruction=email(
            sender="Marcus Chen",
            practice="Consumer & Retail",
            subject="Harvest & Co — bid only if syn-adjusted ROIC ≥ 13%",
            date="Monday, 11:40 AM",
            body="""
We can bid $180M for Harvest & Co (organic snacks). Build **year-3 syn-adjusted ROIC** = (NOPAT + after-tax synergies − stranded HQ) / (EV + stranded integration cash).

Bid only if ROIC ≥ **13%**. Banker materials capitalize revenue synergies that ops has not diligence-confirmed.
""",
            schema="""
{
  "decision": "<bid|walk>",
  "year3_roic_pct": <float>,
  "after_tax_synergies_millions": <float>,
  "method": "<(NOPAT + syn − stranded) / (EV + integration cash)>"
}
""",
            method_hint="Use only cost synergies ops confirmed. Tax rate 25%. Do not use the banker's $22M revenue synergy.",
        ),
        matter={
            "target_pnl.txt": """
Year-3 stand-alone EBIT: $18.0M
Tax rate: 25%
Offer EV: $180M
Integration cash (stranded systems + retention): $12M
""",
            "synergies.txt": """
Ops-confirmed cost synergies (run-rate y3, pre-tax): $8.0M
Stranded HQ / TSA that stays: $1.6M pre-tax (not a synergy)
Banker book also shows $22M revenue synergy — **unconfirmed**, exclude.
A second slide taxes synergies at 0%. Use 25%.
""",
        },
        oracle={
            "decision": "walk",
            "year3_roic_pct": 10.47,
            "after_tax_synergies_millions": 6.0,
            "method": "(NOPAT + after-tax syn − stranded) / (EV + integration cash)",
        },
        memo="""
We recommend walk. Year-3 syn-adjusted ROIC is 10.5%, below the 13% bid hurdle. After-tax confirmed synergies are $6.0M; the banker's $22M revenue synergy is excluded.

## ROIC
- NOPAT: 18.0 × (1 − 0.25) = **$13.5M**
- After-tax syn: 8.0 × 0.75 = **$6.0M**
- After-tax stranded HQ: 1.6 × 0.75 = **$1.2M**
- Numerator: 13.5 + 6.0 − 1.2 = **$18.3M**
- Denominator: 180 + 12 = **$192M**
- ROIC: 18.3 / 192 = **10.47%**

## Next step
Tell the banker we will not mark a bid and reopen only if EV ≤ $145M or confirmed cost syn reach $14M pre-tax.
""",
        lede_any=["10.5", "10.47"],
        lede_all=["walk"],
        decision="walk",
        bands=[("year3_roic_pct", 10.2, 10.8), ("after_tax_synergies_millions", 5.8, 6.2)],
        method_all=["nopat", "syn"],
        method_any=["banker", "revenue"],
        next_any=["bid", "145", "banker", "reopen"],
    )
)
