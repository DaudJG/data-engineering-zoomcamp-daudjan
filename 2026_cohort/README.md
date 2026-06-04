# Data Engineering Zoomcamp 2026

This directory contains my active self-paced work for the DataTalksClub Data Engineering Zoomcamp 2026 materials.

The current focus is Module 1: Docker, PostgreSQL, Python ingestion, and reproducible local development using Ubuntu WSL2, VS Code, Docker Desktop, and `uv`.

## Development environment

I am currently working with:

* Ubuntu WSL2
* VS Code
* Docker Desktop with WSL integration
* Python project management with `uv`
* Git and GitHub for version control

Earlier experiments and previous attempts are kept separately in the repository archive. The active 2026 work is being rebuilt here in a cleaner structure.

## Current progress

| Module   | Topic                                     | Status      |
| :------- | :---------------------------------------- | :---------- |
| Module 1 | Docker, PostgreSQL, SQL, Terraform basics | In progress |
| Module 2 | Workflow orchestration                    | Pending     |
| Module 3 | Data warehousing                          | Pending     |
| Module 4 | Analytics engineering with dbt            | Pending     |
| Module 5 | Batch processing                          | Pending     |
| Module 6 | Streaming                                 | Pending     |

## Structure

```text
```text
2026_cohort/
├── README.md
└── module_1_docker_sql_terraform/
    ├── README.md
    └── docker_sql/
        ├── .dockerignore
        ├── Dockerfile
        ├── ingest_data.py
        ├── pipeline.py
        ├── pyproject.toml
        └── uv.lock
```

## Current Module 1 goal

The immediate goal is to build a small reproducible Week 1 pipeline:

1. Build a Python pipeline image with Docker.
2. Run PostgreSQL in Docker.
3. Ingest sample data with Python.
4. Validate the loaded data with SQL.
5. Document the setup clearly.

This directory is a work in progress and will be updated as each part becomes runnable.
