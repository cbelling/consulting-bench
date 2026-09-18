#!/usr/bin/env python3
"""Tighten the 19 already-checkable Partner-50 graders and strip spoiler notes."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "tasks"


def rewrite(rel: str, text: str) -> None:
    for base in (TASKS,):
        p = base / rel
        if p.exists():
            p.write_text(text.strip() + "\n")
    # Keep environment/matter in sync when patching matter files.
    if "/matter/" in rel:
        env = TASKS / rel.replace("/matter/", "/environment/matter/")
        env.parent.mkdir(parents=True, exist_ok=True)
        env.write_text(text.strip() + "\n")


def patch_verify(task_id: str, old: str, new: str) -> None:
    path = TASKS / task_id / "tests" / "verify.py"
    text = path.read_text()
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"{task_id}: patch anchor not found:\n{old}")
    path.write_text(text.replace(old, new, 1))


# --- Spoilers out of matter packs ------------------------------------------------

rewrite(
    "CIP-054/matter/modeling_note.txt",
    """
RestInn Weekend Pricing — Modeling Note (synthetic)
===================================================
Property: 100 rooms, single-night weekend focus.
Contribution per occupied room = ADR − variable cost ($25/occupied night).

Weekend contribution profit = rooms × occupancy × (ADR − $25).

A junior file already computed the three scenarios and circled +10% as "basically the same
as +20%." Recalculate all three; do not trust that circle.
""",
)

rewrite(
    "CIP-075/matter/greenpouch_economics.txt",
    """
GreenPouch Compostable Bag — Incremental Economics (synthetic)
================================================================
Year-2 volume: 20M units
Price premium vs. hero bag: $0.20 per unit
Incremental variable cost: +$0.12 per unit

Cannibalization: 40% of GreenPouch volume pulls from hero SKU
Hero SKU unit margin: $0.50

Launch opex (Year 2): $4.0M
Hurdle: Year-2 incremental operating profit ≥ $2.0M

A packaging slide reports "+$1.6M contribution" and stops before cannibalization and opex.
""",
)

rewrite(
    "CIP-015/matter/modeling_scratch.txt",
    """
Meridian — Cash EBITDA Bridge (WORKING — incomplete)
====================================================
Starting reported EBITDA: $40.0M

Resolve the $12M vs $4M accrual conflict using the audit-committee settlement.
Then apply uncollected receivables (8% of revenue) on base and on incremental C-scenario
revenue. Do not stop at the CFO-only or OR-only view.
""",
)

rewrite(
    "CIP-032/matter/analyst_scratch.txt",
    """
Chemora entry — working notes (incomplete)
==========================================
Reconcile consultant TAM/share/margin vs engineering margin.
Apply the policy incentive only where the exhibit says it is incremental.
Compare both cases to the $150M annual EBITDA hurdle on $900M CapEx.
Do not treat the consultant's 18% margin as engineering-achievable.
""",
)

rewrite(
    "CIP-050/matter/raredx_valuation.txt",
    """
RareDx — valuation facts (synthetic)
====================================
Bull and bear DCFs are in the accompanying exhibits.
Subtract the $80M overhead the buyer cannot avoid.
The $1.2B ask is not a valuation. Compute bull and bear EV yourself.
""",
)

# --- Tighter verifiers -----------------------------------------------------------

patch_verify(
    "CIP-054",
    '''    lede_ok = ("20" in para or "twenty" in para) and any(
        w in para for w in ("recommend", "premium", "optimal", "choose", "select")
    )
    profit = float(ans["weekend_contribution_profit_dollars"])
    band_ok = 6600.0 <= profit <= 7100.0 and ans.get("decision") == "premium_20"''',
    '''    lede_ok = ("6840" in para.replace(",", "") or "6,840" in para) and (
        "20" in para or "twenty" in para
    )
    profit = float(ans["weekend_contribution_profit_dollars"])
    band_ok = (
        6820.0 <= profit <= 6860.0
        and ans.get("decision") == "premium_20"
        and int(ans.get("optimal_premium_pct", 0)) == 20
    )''',
)

patch_verify(
    "CIP-063",
    '''    band_ok = 45.0 <= inc <= 51.0 and ans.get("decision") == "distribution_first"''',
    '''    lede_ok = lede_ok and ("48" in para)
    band_ok = 47.5 <= inc <= 48.5 and ans.get("decision") == "distribution_first"''',
)

patch_verify(
    "CIP-075",
    '''    band_ok = -7.0 <= profit <= -5.8 and ans.get("decision") == "no-go"''',
    '''    lede_ok = lede_ok and ("6.4" in para or "6.40" in para)
    band_ok = -6.50 <= profit <= -6.30 and ans.get("decision") == "no-go"''',
)

patch_verify(
    "CIP-089",
    '''    band_ok = 38.0 <= profit <= 41.0 and ans.get("decision") == "innovate"''',
    '''    lede_ok = lede_ok and ("39.5" in para or "39.50" in para)
    band_ok = 39.2 <= profit <= 39.8 and ans.get("decision") == "innovate"''',
)

patch_verify(
    "CIP-098",
    '''    band_ok = -0.5 <= q4 <= 1.0 and ans.get("decision") in ("sm_cut", "s_m_cut")''',
    '''    lede_ok = lede_ok and ("0.02" in para or "breakeven" in para or "break-even" in para)
    band_ok = -0.08 <= q4 <= 0.08 and ans.get("decision") in ("sm_cut", "s_m_cut")''',
)

patch_verify(
    "CIP-010",
    '''    lede_ok = any(w in para for w in ("9", "million", "tuning"))
    total = float(ans["annual_us_piano_tunings_millions"])
    home = float(ans["home_tunings_millions"])
    inst = float(ans["institutional_tunings_millions"])
    
    band_ok = (
        7.0 <= total <= 12.0
        and 4.0 <= home <= 5.5
        and 3.5 <= inst <= 5.0
    )''',
    '''    lede_ok = ("9.3" in para or "9.30" in para) and any(
        w in para for w in ("million", "tuning")
    )
    total = float(ans["annual_us_piano_tunings_millions"])
    home = float(ans["home_tunings_millions"])
    inst = float(ans["institutional_tunings_millions"])
    
    band_ok = (
        9.1 <= total <= 9.5
        and 4.6 <= home <= 5.0
        and 4.3 <= inst <= 4.7
    )''',
)

patch_verify(
    "CIP-012",
    '''    lede_ok = any(w in para for w in ("million", "ball", "800", "900", "1.0", "billion"))
    total = float(ans["golf_balls_lost_annually_millions"])
    course = float(ans["course_loss_millions"])
    range_c = float(ans["range_consumption_millions"])
    
    band_ok = (
        800 <= total <= 1100
        and 200 <= course <= 550
        and 500 <= range_c <= 600
    )''',
    '''    lede_ok = any(w in para for w in ("920", "900")) and any(
        w in para for w in ("million", "ball")
    )
    total = float(ans["golf_balls_lost_annually_millions"])
    course = float(ans["course_loss_millions"])
    range_c = float(ans["range_consumption_millions"])
    
    band_ok = (
        900 <= total <= 940
        and 340 <= course <= 380
        and 540 <= range_c <= 580
    )''',
)

patch_verify(
    "CIP-015",
    '''    band_ok = (
        6.5 <= low <= 8.5
        and 7.0 <= high <= 9.0
        and ans.get("decision") == "no-go"
    )''',
    '''    lede_ok = lede_ok and ("7.5" in para or "7.8" in para)
    band_ok = (
        7.3 <= low <= 7.7
        and 7.6 <= high <= 8.0
        and ans.get("decision") == "no-go"
    )''',
)

patch_verify(
    "CIP-021",
    '''    band_ok = 1.2 <= contrib <= 1.6 and ans.get("decision") == "exit_zone_c"''',
    '''    lede_ok = lede_ok and ("1.4" in para)
    band_ok = 1.35 <= contrib <= 1.45 and ans.get("decision") == "exit_zone_c"''',
)

patch_verify(
    "CIP-025",
    '''    band_ok = (
        2.8 <= var_contrib <= 3.2
        and -3.0 <= full_loaded <= -2.5
    )''',
    '''    lede_ok = lede_ok and ("2.70" in para or "2.7" in para or "$3" in para)
    band_ok = (
        2.95 <= var_contrib <= 3.05
        and -2.80 <= full_loaded <= -2.60
    )''',
)

patch_verify(
    "CIP-028",
    '''    band_ok = (
        5.0 <= at5 <= 6.5
        and 1.0 <= at15 <= 2.5
        and 5.0 <= breakeven <= 7.0
        and ans.get("decision") == "no-go"
    )''',
    '''    band_ok = (
        5.3 <= at5 <= 5.9
        and 1.4 <= at15 <= 2.0
        and 5.7 <= breakeven <= 6.3
        and ans.get("decision") == "no-go"
    )'''
)

patch_verify(
    "CIP-032",
    '''    lede_ok = any(w in para for w in ("no-go", "no go", "reject", "decline", "partner", "miss"))
    base = float(ans["base_case_annual_ebitda_millions"])
    incentive = float(ans["with_incentive_annual_ebitda_millions"])
    
    band_ok = (
        20 <= base <= 30
        and 30 <= incentive <= 45
        and ans.get("decision") == "no-go"
    )''',
    '''    lede_ok = any(w in para for w in ("no-go", "no go", "reject", "decline")) and (
        "24" in para or "32" in para or "150" in para
    )
    base = float(ans["base_case_annual_ebitda_millions"])
    incentive = float(ans["with_incentive_annual_ebitda_millions"])
    
    band_ok = (
        23.0 <= base <= 25.0
        and 31.0 <= incentive <= 33.0
        and ans.get("decision") == "no-go"
        and float(ans.get("hurdle_annual_ebitda_millions", 0)) == 150.0
    )''',
)

patch_verify(
    "CIP-044",
    '''    band_ok = -60.0 <= margin <= -50.0 and ans.get("decision") in (''',
    '''    lede_ok = lede_ok and ("56" in para)
    band_ok = -57.0 <= margin <= -55.0 and ans.get("decision") in (''',
)

patch_verify(
    "CIP-050",
    '''    band_ok = (
        1.2 <= bull <= 1.5
        and 0.25 <= bear <= 0.35
        and ans.get("decision") in ("cvr_or_no-go", "no-go", "cvr")
    )''',
    '''    lede_ok = lede_ok and ("1.37" in para or "0.31" in para)
    band_ok = (
        1.32 <= bull <= 1.42
        and 0.28 <= bear <= 0.34
        and ans.get("decision") in ("cvr_or_no-go", "no-go", "cvr")
    )''',
)

patch_verify(
    "CIP-052",
    '''    band_ok = (
        35.0 <= opt <= 45.0
        and -25.0 <= pess <= -15.0
        and ans.get("decision") == "raise"
    )''',
    '''    lede_ok = lede_ok and ("39.6" in para or "39" in para)
    band_ok = (
        38.5 <= opt <= 40.7
        and -21.5 <= pess <= -19.3
        and ans.get("decision") == "raise"
    )'''
)

patch_verify(
    "CIP-055",
    '''    band_ok = 465.0 <= rev <= 480.0 and ans.get("decision") == "path_b"''',
    '''    lede_ok = lede_ok and ("473" in para)
    band_ok = 470.0 <= rev <= 476.0 and ans.get("decision") == "path_b"''',
)

patch_verify(
    "CIP-066",
    '''    band_ok = (
        110.0 <= cs <= 115.0
        and 102.0 <= fin <= 106.0
        and ans.get("decision") == "fail_fix_retention"
    )''',
    '''    lede_ok = lede_ok and ("112" in para or "103.8" in para or "104" in para)
    band_ok = (
        111.5 <= cs <= 113.0
        and 103.3 <= fin <= 104.3
        and ans.get("decision") == "fail_fix_retention"
    )'''
)

patch_verify(
    "CIP-093",
    '''    band_ok = 440.0 <= gm <= 450.0 and ans.get("decision") == "selective_match"''',
    '''    lede_ok = lede_ok and ("445" in para)
    band_ok = 443.0 <= gm <= 447.0 and ans.get("decision") == "selective_match"''',
)

patch_verify(
    "CIP-099",
    '''    band_ok = (
        13.0 <= cardio <= 17.0
        and -10.0 <= ortho <= -6.0
        and ans.get("decision") == "keep_cardio_close_ortho_expand"
    )''',
    '''    lede_ok = lede_ok and ("15" in para)
    band_ok = (
        14.5 <= cardio <= 15.5
        and -8.5 <= ortho <= -7.5
        and ans.get("decision") == "keep_cardio_close_ortho_expand"
    )'''
)


def main() -> None:
    print("tightened existing 19 checkable graders and stripped spoiler notes")


if __name__ == "__main__":
    main()
