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
├── pipeline/                  # Isolated pipeline module with dependencies
│   ├── pyproject.toml        # Pipeline-specific dependencies
│   ├── uv.lock               # Pipeline lock file
│   ├── .python-version       # Python version specification
│   ├── Dockerfile            # Pipeline container definition
│   ├── pipeline.py           # Main pipeline orchestration
│   └── ingest_data.py        # Data ingestion logic
├── main.py                   # Entry point
├── pyproject.toml            # Root project metadata
└── README.md                 # This file
```

## Module 1: Docker & Terraform
* **Objective:** Setting up the infrastructure (PostgreSQL database) and ingestion scripts.
* **Key Learnings:** Container management, network bridging in Docker, and Infrastructure as Code basics.
