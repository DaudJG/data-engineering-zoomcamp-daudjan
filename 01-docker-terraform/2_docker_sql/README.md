## Run Postgres Container

Start Postgres with the helper script:

```bash
bash start_postgres.sh
```

This script:

* Starts the container as `ny_taxi_pg`
* Mounts the persistent data folder (`ny_taxi_postgres_data/`)
* Mounts the `sql/` folder (for running scripts)
* Uses defaults: user `root`, password `root`, db `ny_taxi`, port `5433`

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
