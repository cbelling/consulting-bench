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
