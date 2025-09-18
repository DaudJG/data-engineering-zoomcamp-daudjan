# Week 1 – Docker & SQL (Toy Example → Postgres Pipeline)

## 📌 What I’ve Done So Far
- Set up a **toy pipeline** in Docker:
  - `Dockerfile` (Python 3.9 + `uv` + `pandas`)
  - `pipeline.py` (prints args + sanity check)
- Built and ran container successfully with:
  ```bash
  docker build -t my-uv-pipeline .
  docker run my-uv-pipeline 2025-09-18
