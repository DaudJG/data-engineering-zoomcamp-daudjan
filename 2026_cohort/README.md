# Data Engineering Zoomcamp 2026 

This directory contains my coursework and projects for the **Data Engineering Zoomcamp 2026** cohort (run by DataTalks.Club).

## Development Environment
I'm building this using a **Mobile-First Cloud Development** setup - basically developing on my Samsung S10 Lite using GitHub Codespaces. 

Why? Because I wanted to challenge myself: prove that you don't need fancy local hardware to build solid data engineering pipelines. All you need is cloud tools and the right mindset. It's actually pretty cool seeing how far cloud development has come.

## Curriculum Progress

| Module | Topic | Tech Stack | Status |
| :--- | :--- | :--- | :--- |
| **Module 1** | Containerization & IaC | Docker, Docker Compose, Terraform, PostgreSQL | In Progress |
| **Module 2** | Workflow Orchestration | Kestra / Airflow | Pending |
| **Module 3** | Data Warehousing | BigQuery / Snowflake | Pending |
| **Module 4** | Analytics Engineering | dbt (Data Build Tool) | Pending |
| **Module 5** | Batch Processing | Spark | Pending |
| **Module 6** | Streaming | Kafka | Pending |

## Project Structure

```
2026_cohort/
├── README.md                       # This file
│
└── module_1_docker_sql_terraform/  # Module 1: Docker, SQL & Terraform
    ├── README.md                   # Module-specific docs
    └── pipeline/                   # Data pipeline
        ├── pyproject.toml         # Pipeline dependencies (isolated)
        ├── uv.lock                # Dependency lock file
        ├── .python-version        # Python version
        ├── Dockerfile             # Container definition
        ├── pipeline.py            # Pipeline orchestration
        └── ingest_data.py         # Data ingestion logic

# Additional modules will be added here (e.g., module_2, module_3, etc.)
```

## How to Use

Each module handles a specific part of the data engineering pipeline and manages its own dependencies independently. This keeps things organized and prevents one module from breaking another.

To work with a module:
1. Go into the module directory
2. Check its README for instructions
3. All dependencies are contained within that module - no global conflicts

I structured it this way because I want to keep things modular from the start. It's easier to scale and experiment with different tech stacks when each module is self-contained.

## Module 1: Docker & Terraform

This is where I'm learning the fundamentals - how to containerize applications and automate infrastructure setup.

**What I'm doing:** Building a PostgreSQL database in Docker, setting up data ingestion scripts, and eventually automating it all with Terraform.

**Why it matters:** Docker and IaC are essential skills for any data engineer. I want to understand them deeply, not just use them superficially.
