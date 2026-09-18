#!/usr/bin/env bash
# Verify partner-delegated oracle solutions (memo.md + answer.json).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec bash "$ROOT/scripts/verify_oracles_local.sh" CIP-054 CIP-063 CIP-075 CIP-089 CIP-098
