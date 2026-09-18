"""Hardened L2 cases: CIP-057 through CIP-100."""

from __future__ import annotations

from harden_common import add, case, email

add(
    case(
        task_id="CIP-057",
        level="l2",
        category="pricing",
        description="Telecom unlimited — net after heavy-user cannibal and network opex",
        instruction=email(
            sender="Thomas Wright",
            practice="Technology & Telecom",
            subject="Relay Mobile — unlimited plan net vs $2M hurdle",
            date="Monday, 3:30 PM",
            body="""
Relay wants an unlimited SKU at $75. Heavy users who switch currently spend more than $75. Build **year-1 net contribution** after cannibalization, new joiners, and network opex.

Launch only if net ≥ **$2.0M**. Marketing's $75 × switchers is not incremental.
""",
            schema="""
{
  "decision": "<launch|no-go>",
  "year1_net_millions": <float>,
  "cannibal_millions": <float>,
  "method": "<new joiners − ARPU step-down − network opex>"
}
""",
            method_hint="Cannibal = switcher count × (current heavy ARPU − $75). Add new-joiner revenue. Subtract network opex. Do not count switcher $75 as new revenue.",
        ),
        matter={
            "base.csv": """
item,value
subs_millions,2.4
current_blended_arpu,62
heavy_user_share,0.28
heavy_user_arpu,81
unlimited_price,75
new_joiners,90000
network_opex_millions,3.1
""",
            "marketing_trap.txt": """
Marketing: 0.28 × 2.4M × $75 = $50.4M "new" unlimited revenue.
Those subscribers already pay $81. Switching is an ARPU step-down, not new revenue.

Do not apply the $62 blended ARPU to switchers.
""",
        },
        oracle={
            "decision": "no-go",
            "year1_net_millions": -0.382,
            "cannibal_millions": 4.032,
            "method": "new joiners − ARPU step-down − network opex",
        },
        memo="""
We recommend no-go. Year-1 net is −$0.38M after a $4.03M heavy-user step-down and $3.1M network opex, below the $2.0M hurdle. The $50.4M marketing figure is not incremental.

## Build
- Switchers: 0.28 × 2.4M = 672k; cannibal 672k × ($81 − $75) = **$4.032M**
- New joiners: 90k × $75 = **$6.75M**
- Network opex **$3.1M**
- Net: 6.75 − 4.032 − 3.1 = **−$0.382M**

## Next step
Kill the unlimited SKU and instead cap high-usage overage at a $70 safety-valve plan for a 90-day test.
""",
        lede_any=["-0.38", "-0.382", "4.03"],
        lede_all=["no-go"],
        decision="no-go",
        bands=[("year1_net_millions", -0.45, -0.30), ("cannibal_millions", 3.9, 4.2)],
        method_all=["cannibal", "opex"],
        method_any=["heavy", "step-down", "arpu"],
        next_any=["kill", "safety-valve", "90-day", "overage"],
    )
)

add(
    case(
        task_id="CIP-059",
        level="l2",
        category="pricing",
        description="Logistics dim-weight — incremental billable pounds minus churn",
        instruction=email(
            sender="James Park",
            practice="Logistics",
            subject="Parceline — dim-weight net after small-shipper churn",
            date="Tuesday, 7:50 AM",
            body="""
Parceline can switch from actual-weight billing to dim-weight (bill the max of actual vs dim). Build **year-1 net** = incremental billed pounds × rate − small-shipper churn.

Implement if net ≥ **$8M**. Do not bill dim pounds on top of actual — only the increment. Ignore the oversized-subset average in the ops footnote.
""",
            schema="""
{
  "decision": "<implement|hold>",
  "year1_net_millions": <float>,
  "incremental_lb_billions": <float>,
  "method": "<parcels × (dim − actual) × rate − churn>"
}
""",
            method_hint="Incremental pounds = parcels × (average dim − average actual). Multiply by $/lb. Subtract churn on small-shipper revenue.",
        ),
        matter={
            "weights.csv": """
item,value
parcels,12000000
avg_actual_lb,4.2
avg_dim_lb,6.8
rate_per_lb,0.42
small_shipper_revenue_millions,48.0
expected_churn_pct,3.5
""",
            "ops_footnote.txt": """
Oversized subset (8% of parcels) averages 8.1 lb dim. Do not substitute 8.1 for the 6.8 network average.

A pricing draft billed 12M × 6.8 × $0.42 as if actual weight were zero.
""",
        },
        oracle={
            "decision": "implement",
            "year1_net_millions": 11.424,
            "incremental_lb_billions": 0.0312,
            "method": "parcels × (dim − actual) × rate − churn",
        },
        memo="""
We recommend implement. Year-1 net is $11.42M after $1.68M small-shipper churn, above the $8M bar. Incremental billed pounds are 31.2M (2.6 lb × 12M), not 81.6M.

## Build
- Increment: 12M × (6.8 − 4.2) = **31.2M lb**
- Revenue: 31.2M × $0.42 = **$13.104M**
- Churn: 3.5% × $48M = **$1.68M**
- Net: **$11.424M**

## Next step
File the dim-weight tariff for the 1st-of-month cycle and stand up a small-shipper rebate desk before go-live.
""",
        lede_any=["11.42", "11.4"],
        lede_all=["implement"],
        decision="implement",
        bands=[("year1_net_millions", 11.1, 11.8), ("incremental_lb_billions", 0.030, 0.033)],
        method_all=["dim", "churn"],
        method_any=["actual", "increment"],
        next_any=["tariff", "rebate", "go-live", "file"],
    )
)

add(
    case(
        task_id="CIP-064",
        level="l2",
        category="growth",
        description="Airline loyalty status-match — true new members only",
        instruction=email(
            sender="Marcus Williams",
            practice="Travel & Transportation",
            subject="NorthAir — status-match: true-new ancillary vs $4M hurdle",
            date="Monday, 8:20 AM",
            body="""
Loyalty wants a status-match campaign. Marketing quotes 0.9M "new" members. 40% are already on the file. Year-1 new members fly fewer trips than the base.

Approve only if incremental ancillary − campaign cost ≥ **$4.0M**.
""",
            schema="""
{
  "decision": "<approve|reject>",
  "true_new_members_millions": <float>,
  "net_ancillary_millions": <float>,
  "method": "<true-new × y1 trips × miles × ancillary − cost>"
}
""",
            method_hint="True new = campaign members × (1 − already-member share). Use year-1 trip rate, not the base 1.4.",
        ),
        matter={
            "loyalty.txt": """
Base members: 8.2M (context only)
Campaign sign-ups: 0.90M
Already members (status-match duplicates): 40%
Year-1 trips per true-new member: 0.8
Base-member trips (do not use for new): 1.4
Avg miles / trip: 1,150
Ancillary per mile: $0.018
Campaign cost: $6.2M
""",
            "marketing_trap.txt": """
Marketing: 0.90M × 1.4 × 1,150 × $0.018 = $20.8M gross. Ignores duplicates and the 0.8 year-1 trip rate.
""",
        },
        oracle={
            "decision": "reject",
            "true_new_members_millions": 0.54,
            "net_ancillary_millions": 2.742,
            "method": "true-new × y1 trips × miles × ancillary − cost",
        },
        memo="""
We recommend reject. True-new members are 0.54M and net ancillary is $2.74M after the $6.2M campaign cost, below the $4.0M hurdle. The $20.8M marketing gross uses duplicates and the base trip rate.

## Build
- True new: 0.90M × 60% = **0.54M**
- Gross ancillary: 0.54M × 0.8 × 1,150 × $0.018 = **$8.942M**
- Net: 8.942 − 6.2 = **$2.742M**

## Next step
Cancel the mass status-match and run a 50k-member controlled match with proof-of-non-member filters.
""",
        lede_any=["2.74", "0.54"],
        lede_all=["reject"],
        decision="reject",
        bands=[("true_new_members_millions", 0.53, 0.55), ("net_ancillary_millions", 2.6, 2.9)],
        method_all=["true", "trip"],
        method_any=["duplicate", "already", "0.8"],
        next_any=["cancel", "50k", "controlled", "filter"],
    )
)

add(
    case(
        task_id="CIP-067",
        level="l2",
        category="growth",
        description="Grocery fresh vendor deal — GM bps vs extra shrink on SKU subset",
        instruction=email(
            sender="Marcus Chen",
            practice="Consumer & Retail",
            subject="GreenBasket — vendor 80bps vs shrink on the $80M subset",
            date="Wednesday, 9:15 AM",
            body="""
A produce vendor offers +80 bps category GM on $420M fresh sales if we take a SKU reset. The reset adds **2.0pp shrink on an $80M SKU subset** (full retail, we already bought the goods).

Accept only if net ≥ **$2.5M**. Do not apply shrink to the whole $420M.
""",
            schema="""
{
  "decision": "<accept|reject>",
  "gm_uplift_millions": <float>,
  "shrink_hit_millions": <float>,
  "net_millions": <float>,
  "method": "<category sales × bps − subset sales × extra shrink>"
}
""",
            method_hint="GM uplift = $420M × 0.80%. Shrink hit = $80M × 2.0% (full retail). Net = uplift − shrink.",
        ),
        matter={
            "fresh.txt": """
Fresh category sales: $420M
Offered GM uplift: +80 bps on the full category
SKU-reset subset sales: $80M
Extra shrink on subset: +2.0 percentage points of subset sales
Category reported GM 22% is context; extra shrink is a full-retail hit.
""",
            "buyer_trap.txt": """
Buyer model: 80 bps × $420M = $3.36M and stops.
A second model applies 2.0pp shrink to all $420M (= $8.4M) — wrong scope.
""",
        },
        oracle={
            "decision": "reject",
            "gm_uplift_millions": 3.36,
            "shrink_hit_millions": 1.60,
            "net_millions": 1.76,
            "method": "category sales × bps − subset sales × extra shrink",
        },
        memo="""
We recommend reject. Net is $1.76M after a $1.60M shrink hit on the $80M subset, below the $2.5M accept bar. The $3.36M buyer model ignores shrink; the $8.4M model over-scopes it.

## Build
- GM uplift: $420M × 0.80% = **$3.36M**
- Shrink hit: $80M × 2.0% = **$1.60M**
- Net: **$1.76M**

## Next step
Counter the vendor for 80bps plus shrink-sharing on the $80M subset, or walk.
""",
        lede_any=["1.76"],
        lede_all=["reject"],
        decision="reject",
        bands=[
            ("gm_uplift_millions", 3.3, 3.42),
            ("shrink_hit_millions", 1.55, 1.65),
            ("net_millions", 1.70, 1.82),
        ],
        method_all=["shrink", "bps"],
        method_any=["subset", "80"],
        next_any=["counter", "walk", "vendor", "sharing"],
    )
)

add(
    case(
        task_id="CIP-076",
        level="l2",
        category="product",
        description="Auto connected-feature subscription after cellular COGS and trim churn",
        instruction=email(
            sender="Daniel Cho",
            practice="Automotive",
            subject="Motorly — connected-feature net vs $3.5M hurdle",
            date="Monday, 2:45 PM",
            body="""
Motorly can sell a $18/mo connected feature. Build **year-1 net** after cellular COGS and premium-trim churn.

Launch only if net ≥ **$3.5M**. Product finance forgot cellular; sales forgot trim churn.
""",
            schema="""
{
  "decision": "<launch|no-go>",
  "gross_sub_millions": <float>,
  "year1_net_millions": <float>,
  "method": "<attach × price − cellular − trim churn>"
}
""",
            method_hint="Gross = vehicles × attach × $18 × 12. Cellular = attached vehicles × $4.50 × 12. Trim churn = premium buyers × 1.5pp × $4,200.",
        ),
        matter={
            "feature.txt": """
Vehicles in-scope: 120,000
Attach rate: 22%
Subscription: $18 / month
Cellular COGS: $4.50 / month per attached vehicle
Premium-trim buyers: 28,000
Expected extra trim churn if feature is paid: 1.5 percentage points
Gross profit per lost premium vehicle: $4,200
""",
            "traps.txt": """
Product: 120k × 22% × $18 × 12 = $5.70M and stops (no cellular, no churn).
Sales: applies 1.5pp churn to all 120k vehicles at $4,200.
""",
        },
        oracle={
            "decision": "no-go",
            "gross_sub_millions": 5.702,
            "year1_net_millions": 2.513,
            "method": "attach × price − cellular − trim churn",
        },
        memo="""
We recommend no-go. Year-1 net is $2.51M after $1.43M cellular and $1.76M premium-trim churn, below the $3.5M hurdle. Gross subscriptions are $5.70M.

## Build
- Gross: 120k × 22% × $18 × 12 = **$5.702M**
- Cellular: 26,400 × $4.50 × 12 = **$1.426M**
- Trim churn: 28,000 × 1.5% × $4,200 = **$1.764M**
- Net: 5.702 − 1.426 − 1.764 = **$2.513M**

## Next step
Bundle the feature into premium trim instead of a stand-alone $18 SKU and re-forecast attach.
""",
        lede_any=["2.51", "2.513", "5.70"],
        lede_all=["no-go"],
        decision="no-go",
        bands=[("gross_sub_millions", 5.6, 5.8), ("year1_net_millions", 2.40, 2.65)],
        method_all=["cellular", "churn"],
        method_any=["trim", "attach"],
        next_any=["bundle", "premium", "re-forecast", "sku"],
    )
)

add(
    case(
        task_id="CIP-077",
        level="l2",
        category="product",
        description="Bank BNPL — take-rate minus losses, opex, and revolving NII cannibal",
        instruction=email(
            sender="Olivia Grant",
            practice="Financial Services",
            subject="ClearBank — BNPL net vs $8M hurdle",
            date="Tuesday, 4:00 PM",
            body="""
ClearBank can put BNPL on checkout. Build **year-1 net** = GMV × (take-rate − loss − opex) − revolving-NII cannibal.

Launch only if net ≥ **$8M**. Do not report take-rate × GMV as profit.
""",
            schema="""
{
  "decision": "<launch|no-go>",
  "bnpl_contribution_millions": <float>,
  "year1_net_millions": <float>,
  "method": "<GMV × spread − revolving cannibal>"
}
""",
            method_hint="Spread = take-rate − loss rate − opex rate. Cannibal = 18% of $40M revolving NII.",
        ),
        matter={
            "bnpl.txt": """
Eligible checkout GMV: $1.8B
Merchant take-rate: 3.4% of GMV
Credit loss rate: 2.1% of GMV
Ops/fraud opex: 0.6% of GMV
Revolving card NII at risk: $40M
Expected NII cannibal: 18%
""",
            "pmt_trap.txt": """
Payments deck: 3.4% × $1.8B = $61.2M "revenue" as if it were profit.
Risk draft uses a 0.9% analog-card loss rate, not the 2.1% BNPL field loss.
""",
        },
        oracle={
            "decision": "no-go",
            "bnpl_contribution_millions": 12.6,
            "year1_net_millions": 5.4,
            "method": "GMV × spread − revolving cannibal",
        },
        memo="""
We recommend no-go. BNPL contribution is $12.6M but year-1 net is $5.4M after credit loss, opex, and $7.2M revolving NII cannibal, below the $8M hurdle. The $61.2M take-rate slide is not profit.

## Build
- Spread: 3.4% − 2.1% − 0.6% = **0.7%**
- Contribution: $1.8B × 0.7% = **$12.6M**
- Cannibal: 18% × $40M = **$7.2M**
- Net: **$5.4M**

## Next step
Hold BNPL and instead raise revolving interchange-plus APR on the same checkout cohort.
""",
        lede_any=["5.4", "12.6"],
        lede_all=["no-go"],
        decision="no-go",
        bands=[("bnpl_contribution_millions", 12.3, 12.9), ("year1_net_millions", 5.2, 5.6)],
        method_all=["cannibal", "loss"],
        method_any=["take-rate", "spread", "nii"],
        next_any=["hold", "revolving", "apr", "checkout"],
    )
)
