**From:** Marcus Williams, Partner — Travel & Transportation
**To:** Associate case team
**Subject:** NorthAir BOS–LIS — year-3 contribution after incentive cliff
**Date:** Tuesday, 9:00 AM

Team,

NorthAir is deciding BOS–LIS. Year 1–2 look fine because of airport incentives. We need **year-3 contribution after incentives expire**, including crew premium and a diverted connecting-feed spill.

Launch only if year-3 contribution ≥ **$4.0M**.

Do not annualize the year-1 incentive as if it lasts.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|pass>",
  "year3_contribution_millions": <float>,
  "incentive_year1_millions": <float>,
  "method": "<RASM × ASMs − CASM ex-incentive − spill>"
}
```

Year-3 revenue = RASM × ASMs. Subtract cash CASM (no incentive credit) × ASMs, crew premium, and connecting-feed spill.
End with a concrete client next step—not generic risk monitoring.

Marcus
