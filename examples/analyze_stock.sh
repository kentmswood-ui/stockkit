#!/usr/bin/env bash
set -euo pipefail

SYMBOL="${1:-NVDA}"

curl -sS -X POST "https://stockkit.net/api/analyze" \
  -H "Content-Type: application/json" \
  -d "{\"symbol\":\"${SYMBOL}\"}"
