# Module 1: Docker, SQL & Terraform

This module covers containerization, database management, and infrastructure as code.

## Objective
Setting up the infrastructure (PostgreSQL database) and ingestion scripts using Docker, Docker Compose, and Terraform.

## Key Learnings
- Container management and networking
- Docker Compose orchestration
- Infrastructure as Code (IaC) with Terraform
- Data ingestion patterns

## Structure

```
module_1_docker_sql_terraform/
└── pipeline/                  # Data pipeline module
    ├── pyproject.toml        # Pipeline dependencies
    ├── uv.lock               # Dependency lock file
    ├── .python-version       # Python version
    ├── Dockerfile            # Container definition
    ├── pipeline.py           # Pipeline orchestration
    └── ingest_data.py        # Data ingestion logic
```

## Running the Pipeline

See the main [2026_cohort README](../README.md) for instructions on running modules.
