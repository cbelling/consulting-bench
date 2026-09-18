# Management Consulting Bench

Harbor-runnable **partner-memo** tasks for management consulting workflows (market sizing, profitability, pricing, investment decisions). Each task is a partner email to an associate: read a synthetic matter pack, write a one-page memo, and emit a checkable JSON sidecar.

This slice is **50 partner-delegated tasks** (5 L1 / 25 L2 / 20 L3). There is no frozen JSON-L1 holdout set and no separate design-brief track.

## Task shape

Every task under `tasks/<TASK-ID>/` follows the Harbor layout:

```
tasks/CIP-054/
├── task.toml
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

Deliverables are always:

1. `/app/output/memo.md` — one-page memo with the recommendation in the first paragraph
2. `/app/output/answer.json` — checkable core (decision, key number, method)

Verifiers are programmatic (no LLM judge). Typical all-pass checks: lede recommendation **and key number**, a tight numeric band on the JSON sidecar, method language in the memo, a concrete next step (not generic “monitor risks”), and rejection of common trap values. Matter packs do **not** precompute the answer. Lede parsing skips `#` / `##` headings, To/From/Date/Subject lines, and horizontal rules.

## Difficulty mix

| Level | Count | IDs |
|-------|-------|-----|
| L1 | 5 | CIP-054, CIP-063, CIP-075, CIP-089, CIP-098 |
| L2 | 25 | CIP-003, CIP-005, CIP-006, CIP-016, CIP-018, CIP-019, CIP-030, CIP-033, CIP-034, CIP-040, CIP-041, CIP-043, CIP-053, CIP-057, CIP-059, CIP-064, CIP-067, CIP-076, CIP-077, CIP-084, CIP-085, CIP-090, CIP-091, CIP-097, CIP-100 |
| L3 | 20 | CIP-010, CIP-012, CIP-015, CIP-021, CIP-025, CIP-028, CIP-032, CIP-038, CIP-044, CIP-050, CIP-052, CIP-055, CIP-062, CIP-066, CIP-070, CIP-079, CIP-087, CIP-093, CIP-096, CIP-099 |

Every task is checkable (no paragraph-length stubs). L2 packs require multi-exhibit math with one distractor number. L3 packs include conflicting exhibits, arithmetic traps, or unit/timing issues. Target cheap-model pass rate is about 40–50% (DeepSeek V4.1 Flash). Hardened-v1 concurrent run: **26/50 (52%)**, $0.73, 0 errors. All 24 fails still have a passing local oracle.

## Catalog

| ID | Level | Topic |
|----|-------|-------|
| CIP-003 | L2 | AeroTread NB tire TAM (exclude cargo/spares) |
| CIP-005 | L2 | US economy-hotel room revenue (exclude midscale) |
| CIP-006 | L2 | India smartphone sell-out (exclude gray sell-in) |
| CIP-010 | L3 | Piano tunings — unusual stock × frequency |
| CIP-012 | L3 | Golf balls lost — conflicting exhibits |
| CIP-015 | L3 | Hospital outpatient surgery profit gap |
| CIP-016 | L2 | SaaS gross margin compression |
| CIP-018 | L2 | Hotel F&B profit mix |
| CIP-019 | L2 | Pharma plant utilization |
| CIP-021 | L3 | Logistics last-mile Zone C contribution |
| CIP-025 | L3 | Media streaming contribution layers |
| CIP-028 | L3 | Hospital urgent-care adjacency |
| CIP-030 | L2 | Airline new route |
| CIP-032 | L3 | Battery materials entry — conflicting margins |
| CIP-033 | L2 | Insurance pet adjacency |
| CIP-034 | L2 | E-commerce 3P marketplace |
| CIP-038 | L3 | Ag co-op DTC beef |
| CIP-040 | L2 | CPG M&A organic brand |
| CIP-041 | L2 | Hospital ASC acquisition |
| CIP-043 | L2 | SaaS acqui-hire vs build |
| CIP-044 | L3 | Retail distressed-store four-wall |
| CIP-050 | L3 | Pharma rare-disease biotech EV |
| CIP-052 | L3 | Airline bag-fee increase |
| CIP-053 | L2 | SaaS pricing model |
| CIP-054 | L1 | RestInn weekend dynamic pricing |
| CIP-055 | L3 | Pharma co-pay assistance paths |
| CIP-057 | L2 | Telecom unlimited repricing |
| CIP-059 | L2 | Logistics dim-weight |
| CIP-062 | L3 | Municipal water rates |
| CIP-063 | L1 | Crunchora CPG distribution white space |
| CIP-064 | L2 | Airline loyalty growth |
| CIP-066 | L3 | SaaS NDR — CS vs Finance conflict |
| CIP-067 | L2 | Grocery fresh growth |
| CIP-070 | L3 | Media ad-tier growth |
| CIP-075 | L1 | GreenPouch compostable bag go/no-go |
| CIP-076 | L2 | Auto subscription feature |
| CIP-077 | L2 | Bank BNPL feature |
| CIP-079 | L3 | Pharma diagnostic kit |
| CIP-084 | L2 | Industrial IoT spin |
| CIP-085 | L2 | Retail media network |
| CIP-087 | L3 | Energy community solar |
| CIP-089 | L1 | HeroCo private-label response |
| CIP-090 | L2 | Airline competitive response |
| CIP-091 | L2 | SaaS freemium response |
| CIP-093 | L3 | Retail e-comm price transparency |
| CIP-096 | L3 | Airline cost turnaround |
| CIP-097 | L2 | Retail store closures |
| CIP-098 | L1 | CloudSaaS path to profitability |
| CIP-099 | L3 | Hospital service-line turnaround |
| CIP-100 | L2 | Nonprofit turnaround |

## Run one task with Harbor

Install [Harbor](https://www.harborframework.com/docs), then from the repo root:

```bash
harbor run -p tasks/CIP-054 -a "<agent>" -m "<model>"
```

Oracle smoke test (verifier only):

```bash
harbor run -p tasks/CIP-054 -a oracle
```

## Local verification (no Harbor required)

All 50 partner-memo oracles:

```bash
bash scripts/verify_oracles_local.sh
```

A subset or a single task:

```bash
bash scripts/verify_oracles_local.sh CIP-054 CIP-015 CIP-003
```

## Regenerate original slices

These generators rewrite slices in place. After the L1/L3 generators, re-run the hardener so spoilers stay stripped and bands stay tight.

```bash
python3 scripts/generate_partner_tasks.py
python3 scripts/generate_l3_partner_tasks.py
python3 scripts/generate_hardened_stubs.py   # 31 formerly stub L2/L3 cases
python3 scripts/tighten_existing_graders.py  # strip spoilers + tighten the other 19
bash scripts/verify_oracles_local.sh
```

## Scope

- Management consulting only; all matter is synthetic
- Partner-memo Harbor tasks only (memo + JSON sidecar)

## Cheap-model dry run (Modal)

The cheapest current OpenRouter model that matches the planned DeepSeek 4.1 slot is **DeepSeek V4.1 Flash** (`openrouter/deepseek/deepseek-v4.1-flash`, about $0.15 / $0.60 per 1M tokens). Trials run on **Modal sandboxes** (`-e modal`). A 3-task slice (L1 pricing, L1 P&L, L3 cash EBITDA) lives in `evals/dry-run-deepseek-v4.1-flash.json`:

```bash
uv tool install "harbor[modal]"
export OPENROUTER_API_KEY="..."
export MODAL_TOKEN_ID="..."
export MODAL_TOKEN_SECRET="..."
bash scripts/run_dry_run.sh
```

Full 50-task run, 20 Modal sandboxes at a time:

```bash
bash scripts/run_full_bench_concurrent.sh
```

Sequential (one sandbox at a time):

```bash
bash scripts/run_full_bench_sequential.sh
```

Oracle-only Harbor smoke test on Modal (no model key):

```bash
harbor run -p tasks/CIP-054 -a oracle -e modal -y
```
