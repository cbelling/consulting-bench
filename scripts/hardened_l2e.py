"""Hardened L2 cases: CIP-084 through CIP-100."""

from __future__ import annotations

from harden_common import add, case, email

add(
    case(
        task_id="CIP-084",
        level="l2",
        category="corporate-strategy",
        description="Industrial IoT spin — strip captive transfer revenue",
        instruction=email(
            sender="Emily Chen",
            practice="Industrial",
            subject="Sensoria IoT — spin EBITDA after captive transfer leakage",
            date="Monday, 11:00 AM",
            body="""
Corporate wants to spin Sensoria IoT. Build **standalone EBITDA** after losing most parent transfer revenue.

Spin only if standalone EBITDA ≥ **$4.0M**. The CIM treats $17M parent transfers as lasting third-party sales.
""",
            schema="""
{
  "decision": "<spin|no-spin>",
  "standalone_ebitda_millions": <float>,
  "kept_transfer_gm_millions": <float>,
  "method": "<external GM + surviving transfer GM − standalone opex>"
}
""",
            method_hint="Keep 40% of transfer at 18% GM (arm's length). Lose 60% of transfer entirely. External GM stays 34%. Subtract standalone opex.",
        ),
        matter={
            "cim.txt": """
External revenue: $28.0M at 34% gross margin
Parent transfer revenue: $17.0M booked at 100% margin (captive)
Standalone opex if spun: $9.5M
""",
            "tsa.txt": """
If spun, parent keeps 60% of the work in-house (transfer goes to zero).
Remaining 40% is renegotiated at 18% GM, not 100%.
CIM EBITDA of $28×34% + $17 − $9.5 = $19.02M is not standalone.
""",
        },
        oracle={
            "decision": "no-spin",
            "standalone_ebitda_millions": 1.244,
            "kept_transfer_gm_millions": 1.224,
            "method": "external GM + surviving transfer GM − standalone opex",
        },
        memo="""
We recommend no-spin. Standalone EBITDA is $1.24M after captive leakage, below the $4.0M spin hurdle. Kept transfer GM is only $1.22M. The CIM's $19M treats $17M of captive sales as external.

## Build
- External GM: 28 × 34% = **$9.52M**
- Surviving transfer GM: 17 × 40% × 18% = **$1.224M**
- Opex **$9.5M**
- EBITDA: 9.52 + 1.224 − 9.5 = **$1.244M**

## Next step
Keep Sensoria inside the parent and renegotiate the transfer price to 18% GM without a spin.
""",
        lede_any=["1.24", "1.244"],
        lede_all=["no-spin"],
        decision="no-spin",
        bands=[
            ("standalone_ebitda_millions", 1.15, 1.35),
            ("kept_transfer_gm_millions", 1.15, 1.30),
        ],
        method_all=["transfer", "opex"],
        method_any=["captive", "arm"],
        next_any=["keep", "renegotiat", "parent", "spin"],
    )
)

add(
    case(
        task_id="CIP-085",
        level="l2",
        category="new-business",
        description="Retail media network — joiners only, minus guarantees and serving",
        instruction=email(
            sender="Daniel Cho",
            practice="Consumer & Retail",
            subject="AisleMedia — RNM contribution after guarantees",
            date="Tuesday, 1:40 PM",
            body="""
AisleMedia can stand up a retail media network. Only **400 of 1,200** banners will join year 1. Build contribution after traffic cost, serving, and top-10 guarantees.

Build only if contribution ≥ **$7.0M**. Do not multiply by 1,200 banners.
""",
            schema="""
{
  "decision": "<build|hold>",
  "gross_take_millions": <float>,
  "contribution_millions": <float>,
  "method": "<joiners × ad GMV × take − traffic − serving − guarantees>"
}
""",
            method_hint="Gross take = 400 × $0.24M × 22%. Subtract $6.0M traffic, $3.1M serving, $8.0M guarantees.",
        ),
        matter={
            "network.txt": """
Banners in the sales universe: 1,200
Expected year-1 joiners: 400
Ad GMV per joiner: $0.24M
Take rate: 22%
Incremental traffic cost: $6.0M
Ad serving: $3.1M
Guaranteed payments to top-10 banners: $8.0M
""",
            "sales_trap.txt": """
Sales TAM: 1,200 × $0.24M × 22% = $63.36M. That is not year-1 joiners.
A media deck skips the $8.0M guarantee.
""",
        },
        oracle={
            "decision": "hold",
            "gross_take_millions": 21.12,
            "contribution_millions": 4.02,
            "method": "joiners × ad GMV × take − traffic − serving − guarantees",
        },
        memo="""
We recommend hold. Gross take from 400 joiners is $21.12M but contribution is $4.02M after traffic, serving, and $8.0M guarantees — below the $7.0M build bar. The $63.36M 1,200-banner TAM is not year 1.

## Build
- Gross take: 400 × $0.24M × 22% = **$21.12M**
- Minus 6.0 + 3.1 + 8.0 = **$17.1M**
- Contribution: **$4.02M**

## Next step
Renegotiate top-10 guarantees below $4M or delay the network until 700 joiners are signed.
""",
        lede_any=["4.02", "21.12"],
        lede_all=["hold"],
        decision="hold",
        bands=[("gross_take_millions", 20.8, 21.4), ("contribution_millions", 3.8, 4.3)],
        method_all=["guarantee", "take"],
        method_any=["joiner", "1200", "1,200"],
        next_any=["renegotiat", "delay", "700", "guarantee"],
    )
)

add(
    case(
        task_id="CIP-090",
        level="l2",
        category="competitive-response",
        description="Airline fare-match on overlap ASMs only — vs walk-away spill",
        instruction=email(
            sender="Marcus Williams",
            practice="Travel & Transportation",
            subject="NorthAir — match the −8% fare on overlap ASMs only",
            date="Monday, 4:55 PM",
            body="""
A competitor cut fares 8% on overlap flying. Compare **revenue change if we match** vs **if we do not**. Match only if matching saves ≥ **$100M** versus not matching.

Apply the cut only to the 8.5B overlap ASMs, not the 70B system.
""",
            schema="""
{
  "decision": "<match|no_match>",
  "match_revenue_delta_millions": <float>,
  "no_match_revenue_delta_millions": <float>,
  "savings_vs_walk_millions": <float>,
  "method": "<overlap ASMs × RASM; match volume vs walk spill>"
}
""",
            method_hint="Base overlap revenue = 8.5B × $0.12. Match: ×1.03 volume ×0.92 yield. No-match: keep yield, lose 18% passengers.",
        ),
        matter={
            "overlap.txt": """
Overlap ASMs: 8.5 billion
System ASMs (do not use): 70 billion
Overlap RASM: 12.0 cents
Competitor fare cut: −8%
If we match: volume +3% on overlap, yield −8%
If we do not match: yield unchanged, passengers −18% on overlap
""",
            "network_trap.txt": """
Network planning applied −8% to all 70B ASMs (= $672M hit). Wrong scope.
""",
        },
        oracle={
            "decision": "match",
            "match_revenue_delta_millions": -52.968,
            "no_match_revenue_delta_millions": -183.6,
            "savings_vs_walk_millions": 130.632,
            "method": "overlap ASMs × RASM; match volume vs walk spill",
        },
        memo="""
We recommend match. Matching cuts overlap yield 8% and costs $53.0M of overlap revenue versus $183.6M if we walk — a $130.6M save, above the $100M bar. Do not apply the cut to 70B system ASMs.

## Build
- Base overlap: 8.5B × $0.12 = **$1,020M**
- Match: 8.5B × 1.03 × $0.12 × 0.92 = $967.0M → **−$53.0M**
- No-match: $1,020M × 0.82 = $836.4M → **−$183.6M**
- Save vs walk: **$130.6M**

## Next step
File the matched fare in the overlap markets this weekend and hold system-wide prices.
""",
        lede_any=["130", "53"],
        lede_all=["match"],
        decision="match",
        bands=[
            ("match_revenue_delta_millions", -55.0, -50.0),
            ("no_match_revenue_delta_millions", -186.0, -180.0),
            ("savings_vs_walk_millions", 128.0, 134.0),
        ],
        method_all=["overlap", "yield"],
        method_any=["18%", "system"],
        next_any=["file", "weekend", "overlap", "hold"],
    )
)

add(
    case(
        task_id="CIP-091",
        level="l2",
        category="competitive-response",
        description="SaaS freemium match — downgrade leak vs competitor churn",
        instruction=email(
            sender="Lena Ortiz",
            practice="Software",
            subject="Nimbus — match freemium only if year-1 ARR hit ≤ $5M",
            date="Tuesday, 9:35 AM",
            body="""
A competitor launched a free tier. Compare our **year-1 ARR hit if we match** vs if we do not. Match only if the match hit is ≤ **$5.0M**.

Do not treat 210k free users as paid conversions.
""",
            schema="""
{
  "decision": "<match|hold>",
  "match_arr_hit_millions": <float>,
  "hold_arr_hit_millions": <float>,
  "method": "<free conversion − paid downgrade vs extra churn + lost logos>"
}
""",
            method_hint="Match hit = downgrade loss − free-to-paid conversion. Hold hit = extra mid-year churn + lost new logos.",
        ),
        matter={
            "book.txt": """
Paid customers: 82,000
Paid ARPU: $1,140
Starting ARR: 82,000 × $1,140
Expected free-tier users if we match: 210,000
Free-to-paid conversion: 4%
Converted ARPU: $480
Paid downgrade to free if we match: 9% of paid
""",
            "hold_case.txt": """
If we do not match:
- Monthly churn rises 0.7pp; treat extra lost logos as 82,000 × 0.7% × 12 × 0.5 year × $1,140
- New logos were 12,000/year; −30% at $1,140
""",
            "product_trap.txt": """
Product: 210,000 × $480 = $100.8M as if every free user paid. Wrong.
""",
        },
        oracle={
            "decision": "match",
            "match_arr_hit_millions": 4.381,
            "hold_arr_hit_millions": 8.030,
            "method": "free conversion − paid downgrade vs extra churn + lost logos",
        },
        memo="""
We recommend match. The year-1 ARR hit if we match is $4.38M (under the $5.0M cap) versus an $8.03M hit if we hold. 210k × $480 is not a forecast.

## Build
- Match conversion: 210k × 4% × $480 = **+$4.032M**
- Match downgrade: 82k × 9% × $1,140 = **−$8.413M**
- Match hit: **$4.381M**
- Hold extra churn: 82k × 0.7% × 12 × 0.5 × $1,140 = **$3.926M**
- Hold lost logos: 12k × 30% × $1,140 = **$4.104M**
- Hold hit: **$8.030M**

## Next step
Ship the free tier on the existing SKU tree Friday and cap conversion campaigns at the $480 ARPU pack.
""",
        lede_any=["4.38", "4.381", "8.03"],
        lede_all=["match"],
        decision="match",
        bands=[
            ("match_arr_hit_millions", 4.2, 4.6),
            ("hold_arr_hit_millions", 7.8, 8.3),
        ],
        method_all=["downgrade", "churn"],
        method_any=["conversion", "free"],
        next_any=["ship", "friday", "sku", "cap"],
    )
)

add(
    case(
        task_id="CIP-097",
        level="l2",
        category="turnaround",
        description="Retail store closures — four-wall save minus stranded leases and halo",
        instruction=email(
            sender="Marcus Chen",
            practice="Consumer & Retail",
            subject="AisleMart — close 40 boxes only if run-rate benefit ≥ $1.5M",
            date="Monday, 6:10 PM",
            body="""
Forty boxes lose $80k four-wall each. Closing them saves that loss but leaves stranded leases and a halo hit on nearby stores.

Close the set only if **run-rate** benefit ≥ **$1.5M**. Ignore one-time severance.
""",
            schema="""
{
  "decision": "<close|keep_open>",
  "four_wall_save_millions": <float>,
  "runrate_benefit_millions": <float>,
  "method": "<40 × loss save − stranded leases − halo>"
}
""",
            method_hint="Four-wall save = 40 × $80k. Subtract $2.4M stranded leases and $0.6M halo. Do not net the $2.0M severance into run-rate.",
        ),
        matter={
            "stores.txt": """
Stores in the close set: 40
Average four-wall contribution: −$80,000 (i.e., an $80k loss)
Stranded leases if closed: $2.4M / year
Halo / transfer shortfall on remaining stores: $0.6M / year
One-time severance: $2.0M (exclude from run-rate)
""",
            "re_trap.txt": """
RE committee: 40 × $80k = $3.2M "savings" and recommends close. Skips leases and halo.
A finance note subtracts severance from run-rate.
""",
        },
        oracle={
            "decision": "keep_open",
            "four_wall_save_millions": 3.2,
            "runrate_benefit_millions": 0.2,
            "method": "40 × loss save − stranded leases − halo",
        },
        memo="""
We recommend keep_open. Four-wall save is $3.2M but run-rate benefit is only $0.2M after $2.4M stranded leases and $0.6M halo — below the $1.5M close bar. Severance is one-time.

## Build
- Four-wall save: 40 × $80k = **$3.2M**
- Minus leases $2.4M and halo $0.6M → **$0.2M**
- Do not subtract $2.0M severance from run-rate.

## Next step
Keep the 40 boxes and renegotiate the 15 worst leases before any close vote.
""",
        lede_any=["0.2", "3.2"],
        lede_all=["keep_open"],
        decision="keep_open",
        bands=[("four_wall_save_millions", 3.15, 3.25), ("runrate_benefit_millions", 0.15, 0.30)],
        method_all=["lease", "halo"],
        method_any=["severance", "four-wall", "four wall"],
        next_any=["renegotiat", "lease", "vote", "keep"],
    )
)

add(
    case(
        task_id="CIP-100",
        level="l2",
        category="turnaround",
        description="Nonprofit — cut Program B using unrestricted only",
        instruction=email(
            sender="Emily Chen",
            practice="Education & Nonprofit",
            subject="Harbor House — cut Program B only if surplus ≥ $0.5M",
            date="Tuesday, 2:20 PM",
            body="""
Harbor House is $2.4M in deficit. Program B loses money. If we cut B we save its expenses but lose only the **unrestricted** B revenue. Restricted B gifts leave with the program.

Cut B if the resulting surplus ≥ **$0.5M**. Do not treat restricted gifts as remaining fuel for overhead.
""",
            schema="""
{
  "decision": "<cut_b|keep_b>",
  "surplus_if_cut_millions": <float>,
  "unrestricted_revenue_lost_millions": <float>,
  "method": "<current deficit + expense save − unrestricted revenue lost>"
}
""",
            method_hint="Improvement = B expenses − unrestricted B revenue. New surplus = −2.4 + improvement. Restricted $2.4M of B revenue goes away with B and was not funding the deficit.",
        ),
        matter={
            "ops.txt": """
Current operating deficit: $2.4M
Program B revenue: $4.0M, of which 60% is restricted
Program B expenses: $6.2M
Restricted B gifts cannot cover other programs and disappear if B is cut.
""",
            "dev_trap.txt": """
Development: "we keep the $2.4M restricted even if we cut B." Counsel says no.
A board slide adds the $2.4M restricted to the post-cut surplus.
""",
        },
        oracle={
            "decision": "cut_b",
            "surplus_if_cut_millions": 2.2,
            "unrestricted_revenue_lost_millions": 1.6,
            "method": "current deficit + expense save − unrestricted revenue lost",
        },
        memo="""
We recommend cut_b. Surplus if we cut Program B is $2.2M, above the $0.5M bar. Unrestricted revenue lost is $1.6M; the $2.4M restricted book leaves with the program and was never deficit fuel.

## Build
- Unrestricted B revenue: 40% × $4.0M = **$1.6M**
- Improvement: $6.2M expenses saved − $1.6M = **$4.6M**
- Surplus: −$2.4M + $4.6M = **+$2.2M**

## Next step
Vote the Program B wind-down at Thursday board and reassign unrestricted donors to Program A.
""",
        lede_any=["2.2"],
        lede_all=["cut_b"],
        decision="cut_b",
        bands=[
            ("surplus_if_cut_millions", 2.1, 2.3),
            ("unrestricted_revenue_lost_millions", 1.55, 1.65),
        ],
        method_all=["restricted", "unrestricted"],
        method_any=["deficit", "expense"],
        next_any=["vote", "board", "wind-down", "reassign"],
    )
)
