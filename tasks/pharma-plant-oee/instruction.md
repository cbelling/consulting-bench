**From:** Priya Nair, Partner — Healthcare & Life Sciences
**To:** Associate case team
**Subject:** HelixForm — Saturday shift go/no-go on true OEE
**Date:** Monday, 4:20 PM

Team,

HelixForm wants a Saturday shift at Plant B. Use **true OEE** (availability × performance × quality) on the constrained granulation line, then contribution on incremental saleable kg.

Add the Saturday shift only if incremental weekly contribution ≥ **$42k**. A maintenance log parks changeover in "quality"; do not double-count it.

Exhibits in `/app/matter/`.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<add_shift|no_shift>",
  "true_oee_pct": <float>,
  "incremental_weekly_contribution_k": <float>,
  "method": "<OEE × hours × rate × yield × margin − Saturday labor>"
}
```

True OEE = availability × performance × quality. Incremental saleable kg = Saturday hours × nameplate × true OEE. Subtract Saturday crew cost.
End with a concrete client next step—not generic risk monitoring.

Priya
