#!/usr/bin/env bash
set -euo pipefail

URL=$1
TABLE_NAME=$2
shift 2

python ingestion/ingestion_data_v2.py \
  --user postgres \
  --password postgres \
  --host localhost \
  --port 5433 \
  --db ny_taxi \
  --table_name "$TABLE_NAME" \
  --url "$URL" \
  "$@"
