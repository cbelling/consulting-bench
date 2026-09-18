**From:** Priya Nair, Partner — Consumer Products
**To:** Associate case team
**Subject:** GreenPouch compostable bag — launch decision for Friday SteCo
**Date:** Wednesday, 2:30 PM

Team,

Our snack client is weighing a compostable bag (GreenPouch). Year-2 volume, premium, variable cost, cannibalization of the hero SKU, and launch opex are in `/app/matter/greenpouch_economics.txt`.

Hurdle: **Year-2 incremental operating profit ≥ $2M**. Build the incremental P&L explicitly.

Deliverables for **Friday SteCo**:
1. `/app/output/memo.md` — one-page memo with the launch/no-go call in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "incremental_profit_millions_y2": <float>,
  "method": "<incremental contribution formula>"
}
```

Use an incremental contribution formula (premium − incremental VC − cannibalization − launch opex). End with a concrete next action.

Priya
