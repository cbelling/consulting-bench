# Management Consulting Bench

Harbor-runnable evaluation tasks for **management consulting** workflows (market sizing, profitability bridges, investment decisions, pricing). This repository ships an L1 slice of 20 synthetic consulting cases.

> **Design docs:** Full bench architecture lives in [`DESIGN.md`](DESIGN.md) when present on `main`. As of this scaffold, design is still in the COD-53 PR ([`cursor/cod-53-design-brief-apex-harvey-consulting-bench-0246`](https://github.com/cbelling/management-consulting-bench/tree/cursor/cod-53-design-brief-apex-harvey-consulting-bench-0246)).

## Repository layout

Each task under `tasks/<TASK-ID>/` follows the Harbor task format:

```
tasks/CIP-001/
├── task.toml
├── instruction.md          # Engagement brief + deliverable path
├── environment/
│   └── Dockerfile          # Python sandbox; copies matter/ into /app/matter/
├── matter/                 # Synthetic consulting facts (txt/csv)
├── tests/
│   ├── test.sh             # Writes /logs/verifier/reward.txt (1 on pass)
│   └── verify.py           # Programmatic checkable core
├── solution/
│   └── solve.sh            # Oracle that produces a passing answer.json
└── oracle/
    └── README.md           # Documented oracle answer
```

## L1 task set (20)

| ID | Topic | Checkable core |
|----|-------|----------------|
| CIP-001 | Toothbrush units | ~35–45M units (±20%) |
| CIP-002 | Chicago paper towels | $150–230M; HH base |
| CIP-004 | Fitness apps | 6–12M subscribers |
| CIP-007 | Checking opens | 20–32M openings |
| CIP-013 | SkyNest profit bridge | Δprofit −$86M; fuel ~70% |
| CIP-014 | LeafMart CM | CM$ 112→97; CM% 28→22% |
| CIP-017 | ApexMotors service | Ticket+parts margin driver |
| CIP-020 | MeshWave SaaS | Churn is the leak |
| CIP-022 | ThreadNorth retail | Y1 10% vs Y2 5% ROI; fail hurdle |
| CIP-026 | Chemora night shift | Incremental −$3M → cut |
| CIP-027 | Mexico snacks | Y3 OP $3M < $20M → no-go |
| CIP-029 | Digital youth | NPV −$9.6M → no-go |
| CIP-031 | Corporate wellness | −$0.8M vs $10M → no-go |
| CIP-035 | India K-12 | OP −$7.8M → no-go |
| CIP-037 | Museum digital | Net $0.22M < $1M → no-go |
| CIP-039 | HopLite M&A | EV $560M > $400M ask → go |
| CIP-042 | Cell towers | ~$177.5M vs $180M bid → marginal |
| CIP-045 | TPA deal | 7.5% IRR; max $75M → no-go at $120M |
| CIP-049 | GreenAxle LBO | 9.5×8=$76M > $70M → go |
| CIP-051 | Protein bar price | $2.79 max with ≥35% share |

## Run one task with Harbor

Install [Harbor](https://www.harborframework.com/docs), then from the repo root:

```bash
harbor run -p tasks/CIP-001 -a "<agent>" -m "<model>"
```

Example with the oracle solution (verifier-only smoke test):

```bash
harbor run -p tasks/CIP-001 --solution solution/solve.sh
```

The agent (or oracle) must write **`/app/output/answer.json`** as specified in each task's `instruction.md`. The verifier runs `tests/test.sh`, which executes `tests/verify.py` and writes `1` to `/logs/verifier/reward.txt` on pass.

## Local verification (no Harbor required)

Verify all 20 oracle solutions locally:

```bash
bash scripts/verify_oracles_local.sh
```

With Docker available, build the task environment image and run the same check:

```bash
bash scripts/verify_oracles.sh
```

Or verify a single task:

```bash
bash scripts/verify_oracles_local.sh CIP-001
```

## Regenerate tasks

Task files are generated from `scripts/generate_tasks.py`:

```bash
python3 scripts/generate_tasks.py
```

## Scope

- Management consulting only (synthetic cases; not Cosentino/Cheng published text)
- Docs + tasks only in this PR
- 20 L1 tasks — not the full 100-task bench
