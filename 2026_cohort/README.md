# Data Engineering Zoomcamp 2026 

This directory contains my coursework and projects for the **Data Engineering Zoomcamp 2026** cohort (run by DataTalks.Club).

## Development Environment
This project is built using a **Mobile-First Cloud Development** approach.
* **Hardware:** Samsung S10 Lite (Android).
* **Environment:** GitHub Codespaces (Cloud-based VS Code environment).
* **Goal:** To demonstrate that professional Data Engineering pipelines can be built using cloud-native tools, regardless of local hardware limitations.

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

Each module is self-contained with its own dependencies:

1. Navigate to the module directory
2. Follow the module's README for setup and execution
3. Module dependencies are isolated in each pipeline's `pyproject.toml`

This structure allows:
- ✅ Clean separation of concerns
- ✅ No dependency conflicts between modules
- ✅ Easy to add new modules
- ✅ Each module can have different Python versions/dependencies

## Module 1: Docker & Terraform
* **Objective:** Setting up the infrastructure (PostgreSQL database) and ingestion scripts.
* **Key Learnings:** Container management, network bridging in Docker, and Infrastructure as Code basics.
