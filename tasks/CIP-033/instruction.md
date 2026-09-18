**From:** Olivia Grant, Partner — Financial Services
**To:** Associate case team
**Subject:** PawSure — launch only if combined ratio ≤ 92%
**Date:** Monday, 1:15 PM

Team,

PawSure (homeowners carrier) is looking at pet insurance. Build the **year-2 combined ratio** after adverse selection and a 12% cannibalization of the riders already sold on HO policies.

Launch only if combined ratio ≤ **92%**.

The actuary's 81% loss ratio ignores the selection load in `/app/matter/`.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|no-go>",
  "year2_combined_ratio_pct": <float>,
  "cannibalized_rider_profit_millions": <float>,
  "method": "<(loss + lae + opex + selection) / GWP>"
}
```

Combined ratio = (loss + LAE + opex + adverse-selection load) / GWP. Separately size HO-rider profit lost.
End with a concrete client next step—not generic risk monitoring.

Olivia
