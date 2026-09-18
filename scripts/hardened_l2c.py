"""Hardened L2 cases: CIP-041 through CIP-077."""

from __future__ import annotations

from harden_common import add, case, email

add(
    case(
        task_id="CIP-041",
        level="l2",
        category="m-and-a",
        description="Hospital ASC acquisition — cash EBITDA after physician leakage",
        instruction=email(
            sender="Amara Osei",
            practice="Healthcare Services",
            subject="Riverside Health — ASC bid after physician leakage",
            date="Tuesday, 3:05 PM",
            body="""
Riverside can buy MetroASC for $42M. Build **year-2 cash EBITDA** after physician-owner leakage and a billing under-code add-back that compliance will not let us keep.

Bid only if year-2 cash EBITDA / EV ≥ **18%**.

The CIM's $11.2M EBITDA is reported, not cash, and assumes all five surgeon-owners stay.
""",
            schema="""
{
  "decision": "<bid|walk>",
  "year2_cash_ebitda_millions": <float>,
  "cash_ebitda_over_ev_pct": <float>,
  "method": "<reported EBITDA − leakage − disallowed coding + rent-norm>"
}
""",
            method_hint="Start from reported EBITDA. Subtract departing-surgeon contribution. Remove the coding add-back compliance disallows. Normalize related-party rent.",
        ),
        matter={
            "cim_snip.txt": """
Reported EBITDA: $11.2M
Purchase EV: $42.0M
Related-party rent vs market: target pays $0.8M below market (add cost)
""",
            "physician_notes.txt": """
Five surgeon-owners produce 70% of EBITDA equally.
Two of five have declined employment term sheets → expect them to leave.
Departing share of reported EBITDA: 2/5 × 70% = 28%.

Coding "opportunity" in the CIM: +$1.4M. Compliance has already said no — exclude it
(the $11.2M does NOT include this $1.4M; a banker upside case adds it).
""",
            "qoe_trap.txt": """
QoE restates EBITDA to $13.1M by adding back $1.9M "one-time COVID staffing."
Those costs recur. Do not add them back.
""",
        },
        oracle={
            "decision": "walk",
            "year2_cash_ebitda_millions": 7.264,
            "cash_ebitda_over_ev_pct": 17.3,
            "method": "reported EBITDA − leakage − rent-norm; no coding/QoE add-back",
        },
        memo="""
We recommend walk. Year-2 cash EBITDA is $7.26M (17.3% of $42M EV), just under the 18% bid hurdle, after two surgeon-owners leave and rent is normalized. The $13.1M QoE and $1.4M coding upside are rejected.

## Cash EBITDA
- Leakage: 28% × 11.2 = **$3.136M**
- Rent normalize: **$0.8M**
- Cash EBITDA: 11.2 − 3.136 − 0.8 = **$7.264M**
- 7.264 / 42 = **17.3%** < 18%

## Next step
Walk from $42M and reopen only at EV ≤ $38M with signed employment for at least four of five owners.
""",
        lede_any=["7.26", "17.3"],
        lede_all=["walk"],
        decision="walk",
        bands=[
            ("year2_cash_ebitda_millions", 7.1, 7.45),
            ("cash_ebitda_over_ev_pct", 16.9, 17.7),
        ],
        method_all=["leakage", "rent"],
        method_any=["surgeon", "coding", "qoe"],
        next_any=["38", "walk", "employment", "reopen"],
    )
)

add(
    case(
        task_id="CIP-043",
        level="l2",
        category="make-vs-buy",
        description="SaaS acqui-hire vs build — 24-month cash including dead-time",
        instruction=email(
            sender="Nina Patel",
            practice="Software",
            subject="Nimbus — acqui-hire Helio vs 14-person build",
            date="Monday, 5:10 PM",
            body="""
Nimbus needs an observability module in 24 months. Compare **24-month cash out** of acqui-hiring Helio vs building 14 engineers, including dead-time before the build team is productive.

Choose the cheaper 24-month cash path. A board slide treats Helio equity as free.

Exhibits in `/app/matter/`.
""",
            schema="""
{
  "decision": "<acqui_hire|build>",
  "acqui_hire_cash_24m_millions": <float>,
  "build_cash_24m_millions": <float>,
  "method": "<cash + retention + dead-time loaded build cost>"
}
""",
            method_hint="Acqui-hire cash = close cash + 24-month retention + integration. Build = loaded cost × 14 × 24 months, plus 4 months of unproductive dead-time at the same burn.",
        ),
        matter={
            "helio_term.txt": """
Close cash: $9.0M
Retention (24 months, guaranteed): $4.8M
Integration / tooling: $1.1M
Helio unvested option rollover face: $6.0M — **not cash**, exclude from cash-out.
""",
            "build_card.txt": """
Fully loaded engineer cost: $220k / year
Headcount: 14
Calendar: 24 months
Ramp: first 4 months the team is hired but unproductive — you still pay them.
So cash is 24 months of burn, not 20.
Do not capitalize "internal labor" to make build look cheaper.
""",
            "board_slide.txt": """
Board slide: build = 14 × $220k × 20/12 = $5.13M (skips dead-time and treats year as 20 months of work).
Acqui-hire slide: $9.0M only.
""",
        },
        oracle={
            "decision": "build",
            "acqui_hire_cash_24m_millions": 14.9,
            "build_cash_24m_millions": 6.16,
            "method": "close cash + retention + integration vs loaded 24-month build burn",
        },
        memo="""
We recommend build. 24-month cash is $6.16M for the 14-person team including the 4-month dead-time payroll, versus $14.9M cash for the Helio acqui-hire. Option rollover is not cash.

## Cash-out
- Acqui-hire: 9.0 + 4.8 + 1.1 = **$14.9M** (exclude $6.0M equity face)
- Build: 14 × $0.220M × 2.0 years = **$6.16M** (pay through dead-time)
- Board $5.13M skips 4 months; $9.0M Helio skip ignores retention.

## Next step
Stand up the 14-person requisition this Friday and withdraw the Helio LOI.
""",
        lede_any=["6.16", "14.9"],
        lede_all=["build"],
        decision="build",
        bands=[
            ("acqui_hire_cash_24m_millions", 14.7, 15.1),
            ("build_cash_24m_millions", 6.0, 6.4),
        ],
        method_all=["retention", "dead-time"],
        method_any=["equity", "option", "loi"],
        next_any=["requisition", "withdraw", "loi", "friday"],
    )
)

add(
    case(
        task_id="CIP-053",
        level="l2",
        category="pricing",
        description="SaaS seat-to-usage price move — net ARR after elasticity and grandfathering",
        instruction=email(
            sender="Lena Ortiz",
            practice="Software",
            subject="Nimbus — usage pricing: net ARR after elasticity + grandfather",
            date="Tuesday, 10:25 AM",
            body="""
Nimbus wants to move from $80/seat to usage. Build **year-1 net ARR** after elasticity, a 40% grandfather, and overage leakage.

Switch only if year-1 net ARR ≥ current $36.0M.

The pricing deck multiplies usage list × all seats and skips grandfathering.
""",
            schema="""
{
  "decision": "<switch|keep_seats>",
  "year1_net_arr_millions": <float>,
  "grandfathered_arr_millions": <float>,
  "method": "<grandfather ARR + converted usage × elasticity − leakage>"
}
""",
            method_hint="Current ARR = seats × $80. 40% of seats stay on $80. Converted 60% pay usage list × (1+elasticity). Subtract overage leakage.",
        ),
        matter={
            "current.txt": """
Paid seats: 450,000
Seat price: $80 / year
Current ARR: seats × $80
""",
            "usage_card.txt": """
Usage list equivalent: $96 / seat-year on the converted book
Price elasticity on converted seats: −0.35 on the 20% list lift
  Volume factor = 1 + (−0.35 × 0.20) = 0.93
Grandfather: 40% of seats remain on $80 for year 1
Overage leakage (unbilled): $1.8M
""",
            "deck_trap.txt": """
Deck: 450k × $96 = $43.2M. Ignores grandfather, elasticity, leakage.
A second model applies elasticity to the grandfathered 40% as well. Do not.
""",
        },
        oracle={
            "decision": "switch",
            "year1_net_arr_millions": 36.706,
            "grandfathered_arr_millions": 14.4,
            "method": "grandfather ARR + converted usage × elasticity − leakage",
        },
        memo="""
We recommend switch. Year-1 net ARR under usage is $36.71M, just above the $36.0M current book. Grandfathered ARR is $14.4M; the $43.2M deck is not a forecast.

## Build
- Current ARR: 450k × $80 = **$36.0M**
- Grandfather 40%: 0.40 × 36.0 = **$14.4M**
- Converted 60% at $96 with 0.93 volume: 270k × $96 × 0.93 = **$24.11M**
- Minus leakage $1.8M → year-1 net **$36.71M**
- Reject applying elasticity to the grandfathered 40%.

## Next step
Pilot usage on the newest 15% cohort, keep the 40% grandfather, and announce the switch after the first billed month.
""",
        lede_any=["36.7", "36.71", "14.4"],
        lede_all=["switch"],
        decision="switch",
        bands=[
            ("year1_net_arr_millions", 36.4, 37.0),
            ("grandfathered_arr_millions", 14.2, 14.6),
        ],
        method_all=["grandfather", "elastic"],
        method_any=["leakage", "usage"],
        next_any=["pilot", "grandfather", "announce", "cohort"],
    )
)
