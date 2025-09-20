# PostgreSQL Setup (Docker)

## Run Postgres Container
```bash
docker run -d \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v $(pwd)/01-docker-terraform/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5433:5432 \
  --name ny_taxi_pg \
  postgres:13
```

### Details

* **User:** `root`
* **Password:** `root`
* **Database:** `ny_taxi`
* **Host port:** `5433` → mapped to container port `5432`
* **Volume:** `ny_taxi_postgres_data/` → keeps DB state persistent inside this module folder

### Verifying Container

Check container is running:

```bash
docker ps
```

Expected output should show something like:

```
CONTAINER ID   IMAGE         COMMAND                  STATUS         PORTS                    NAMES
abcd1234efgh   postgres:13   "docker-entrypoint.s…"   Up X minutes   0.0.0.0:5433->5432/tcp   ny_taxi_pg
```

Logs can be followed with:

```bash
docker logs -f ny_taxi_pg
```

---

## Running Postgres in Docker ensures:

* **Reproducibility** → anyone can recreate the same DB environment.
* **Isolation** → no need to install Postgres locally.
* **Persistence** → DB files are stored in `ny_taxi_postgres_data/` on your local machine.

---



