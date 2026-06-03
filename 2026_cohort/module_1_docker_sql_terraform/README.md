# Module 1: Docker, SQL & Terraform

This module contains my active work for Week 1 of the Data Engineering Zoomcamp.

The current focus is on building the foundation step by step: Docker, PostgreSQL, Python ingestion, SQL validation, and later Terraform.

## Current status

In progress.

The current implemented work is inside the `pipeline/` folder. It contains a small Python project managed with `uv` and a Dockerfile for containerizing the pipeline code.

## Current structure

```text
module_1_docker_sql_terraform/
├── README.md
└── pipeline/
    ├── .dockerignore
    ├── Dockerfile
    ├── ingest_data.py
    ├── pipeline.py
    ├── pyproject.toml
    └── uv.lock
```

## Current focus

The immediate goal is to make a small runnable Week 1 pipeline:

1. Build and run the Python pipeline container.
2. Start a PostgreSQL database with Docker.
3. Ingest sample data into PostgreSQL.
4. Run SQL checks to verify the loaded data.
5. Add Docker Compose once the individual pieces work.

## Notes

Terraform is part of the Module 1 scope, but it has not been added to this active 2026 module yet. The current priority is to get the local Docker and PostgreSQL workflow working cleanly first.
