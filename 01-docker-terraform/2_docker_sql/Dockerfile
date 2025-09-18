# Initial practice Dockerfile (toy example with uv + pandas)
# Will be replaced by production-ready ingestion pipeline later.

FROM python:3.9

RUN pip install uv

RUN uv pip install --system pandas

WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]
