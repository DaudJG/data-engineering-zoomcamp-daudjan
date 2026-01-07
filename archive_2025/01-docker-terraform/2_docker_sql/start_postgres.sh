#!/usr/bin/env bash
set -euo pipefail

docker run -d \
  --name ny_taxi_pg \
  -e POSTGRES_USER=${POSTGRES_USER:-root} \
  -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-root} \
  -e POSTGRES_DB=${POSTGRES_DB:-ny_taxi} \
  -v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data" \
  -v "$(pwd)/sql:/sql" \
  -p ${POSTGRES_PORT:-5433}:5432 \
  postgres:13
