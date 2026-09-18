#!/usr/bin/env bash
# Verify partner-50 oracle solutions: all 35 NEW partner tasks.
# Existing 15 (COD-55 + hard-10) tracked in separate scripts.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# NEW 35 tasks (10 L3 + 25 L2) for partner-50 milestone
NEW_35_TASKS="
CIP-003 CIP-005 CIP-006 CIP-010 CIP-012
CIP-016 CIP-018 CIP-019 CIP-025 CIP-030
CIP-032 CIP-033 CIP-034 CIP-038 CIP-040
CIP-041 CIP-043 CIP-053 CIP-057 CIP-059
CIP-062 CIP-064 CIP-067 CIP-070 CIP-076
CIP-077 CIP-079 CIP-084 CIP-085 CIP-087
CIP-090 CIP-091 CIP-096 CIP-097 CIP-100
"

exec bash "$ROOT/scripts/verify_oracles_local.sh" $NEW_35_TASKS
