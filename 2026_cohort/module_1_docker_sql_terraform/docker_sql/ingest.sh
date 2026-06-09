#!/usr/bin/env bash
set -euo pipefail

uv run python ingest_data.py \
  --user weather_user \
  --password weather_pass \
  --host localhost \
  --port 5432 \
  --db weather
