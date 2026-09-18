#!/bin/bash
set -euo pipefail
mkdir -p /app/output

cat > /app/output/memo.md << 'EOF'
Recommendation on case.

## Analysis
Detailed analysis here.

## Next step
Specific next action.
EOF

cat > /app/output/answer.json << 'EOF'
{
  "decision": "go"
}
EOF
