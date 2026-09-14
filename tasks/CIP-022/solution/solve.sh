#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "y1_four_wall_roi_pct": 10.0,
  "y2_four_wall_roi_pct": 5.0,
  "primary_driver": "sales_per_sqft",
  "meets_hurdle": false,
  "recommendation": "Fail 8% hurdle in Year 2; declining sales/sqft drives ROI compression\u2014do not roll out additional stores."
}
ORACLE_EOF
