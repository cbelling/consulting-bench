**From:** Emily Chen, Partner — Education & Nonprofit
**To:** Associate case team
**Subject:** MusicBridge piano technician scholarship program sizing
**Date:** Monday, 10:20 AM

Team,

MusicBridge Foundation is planning a nationwide piano technician scholarship program and needs to understand the annual demand for piano tuning services in the US to size the cohort appropriately.

The matter pack is in `/app/matter/`. I've received conflicting data on tuning frequency from our home-piano survey and institutional contacts. The development director insists we also account for concert/rental piano tunings that don't fit the base stock categories.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with your recommendation in paragraph one on the total annual US piano tunings estimate.
2. `/app/output/answer.json`:

```json
{
  "annual_us_piano_tunings_millions": <float>,
  "home_tunings_millions": <float>,
  "institutional_tunings_millions": <float>,
  "method": "<stock × frequency approach>"
}
```

Use a stock-based approach segmenting home vs institutional pianos. The band should be 7–12M total tunings annually. End with a concrete next step for validating the estimate—not generic risk monitoring.

Emily
