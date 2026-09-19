# Task format

Every Consulting Bench task is a Harbor task. The layout matches
[Terminal-Bench](https://www.harborframework.com/docs/tasks):

```
tasks/<kebab-slug>/
├── task.toml               # Harbor metadata and timeouts
├── instruction.md          # Partner email + deliverable contract
├── environment/
│   ├── Dockerfile          # Python sandbox; copies matter/ into /app/matter/
│   └── matter/             # Build-context exhibits (required for Modal/Docker)
├── matter/                 # Same exhibits (local oracle verify convenience)
├── tests/
│   ├── test.sh             # Writes /logs/verifier/reward.txt (1 on pass)
│   └── verify.py           # Programmatic all-pass checks
└── solution/
    └── solve.sh            # Oracle that produces a passing memo + JSON
```

## Deliverables

Agents always write:

1. `/app/output/memo.md` — one-page memo with the recommendation in the first paragraph
2. `/app/output/answer.json` — checkable core (decision, key number, method)

## Verifiers

Verifiers are programmatic (no LLM judge). Typical all-pass checks:

- Lede recommendation **and** key number
- A tight numeric band on the JSON sidecar
- Method language in the memo
- A concrete next step (not generic “monitor risks”)
- Rejection of common trap values

Matter packs do **not** precompute the answer. Lede parsing skips `#` / `##`
headings, To/From/Date/Subject lines, and horizontal rules.

## Difficulty

| Level | Meaning |
|-------|---------|
| L1 | Single-exhibit arithmetic with a clear recommendation |
| L2 | Multi-exhibit math with one distractor number |
| L3 | Conflicting exhibits, arithmetic traps, or unit/timing issues |

Target cheap-model pass rate is about 40–50% (DeepSeek V4.1 Flash).
