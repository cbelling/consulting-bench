#!/usr/bin/env bash
# Verify hard L3 partner-delegated oracle solutions (memo.md + answer.json).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec bash "$ROOT/scripts/verify_oracles_local.sh" \
  CIP-015 CIP-021 CIP-028 CIP-044 CIP-050 CIP-052 CIP-055 CIP-066 CIP-093 CIP-099
