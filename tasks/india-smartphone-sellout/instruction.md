**From:** Rahul Mehta, Partner — Technology & Telecom
**To:** Associate case team
**Subject:** Pixelate — India smartphone annual sell-out before entry IC
**Date:** Tuesday, 8:50 AM

Team,

Pixelate wants a go/no-go on India entry. Size **annual smartphone sell-out units** (replacements + first-time) and dollar TAM at blended ASP.

`/app/matter/` has population, replacement, and a gray-market sell-in note that double-counts. Feature phones are not smartphones.

Enter if annual smartphone units are between **160M and 200M**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "annual_units_millions": <float>,
  "tam_billions": <float>,
  "method": "<users / cycle + first-time>"
}
```

Users = population × 15+ share × smartphone penetration. Annual units = users / replacement cycle + first-time buyers. Use sell-out, not sell-in.
End with a concrete client next step—not generic risk monitoring.

Rahul
