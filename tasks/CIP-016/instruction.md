**From:** Nina Patel, Partner — Software
**To:** Associate case team
**Subject:** Nimbus — GM compression: hosting vs one-time migration
**Date:** Monday, 2:10 PM

Team,

Nimbus GM fell from 72% to a reported 66% on $84M revenue. The CFO wants to know **recurring** GM after stripping the one-time migration, and which recurring line to attack.

Hurdle: renegotiate hosting if hosting drag ≥ **1.5 percentage points** of revenue; otherwise attack support mix.

Exhibits in `/app/matter/`.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<renegotiate_hosting|fix_support>",
  "recurring_gm_pct": <float>,
  "hosting_drag_pp": <float>,
  "method": "<reported COGS − one-time, then pp of revenue>"
}
```

Recurring COGS = reported COGS − one-time migration. Hosting drag pp = hosting rate hike / revenue × 100.
End with a concrete client next step—not generic risk monitoring.

Nina
