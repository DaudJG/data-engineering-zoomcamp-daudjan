import argparse
import pandas as pd
from datetime import datetime, timezone
from sqlalchemy import create_engine, inspect, text

SMHI_URL = (
    "https://opendata-download-metobs.smhi.se"
    "/api/version/1.0/parameter/1/station-set/all/period/latest-hour/data.csv"
)
TABLE_NAME = "smhi_air_temperature_latest_hour"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest SMHI air temperature data to Postgres")

    parser.add_argument("--user", required=True, help="Postgres user name")
    parser.add_argument("--password", required=True, help="Postgres password")
    parser.add_argument("--host", required=True, help="Postgres host")
    parser.add_argument("--port", required=True, help="Postgres port")
    parser.add_argument("--db", required=True, help="Database name")

    args = parser.parse_args()

    print(f"Fetching data from {SMHI_URL}")
    df = pd.read_csv(SMHI_URL, sep=";", skiprows=3, encoding="utf-8-sig")
    df = df.iloc[:, :7]

    # col 5 name is the observation timestamp, e.g. "2026-06-09 11:00:00"
    obs_time = df.columns[5]

    df.columns = ["station_id", "station_name", "latitude", "longitude", "height_m", "temperature_c", "quality_code"]
    df["observation_time"] = pd.to_datetime(obs_time)
    df["ingested_at"] = datetime.now(timezone.utc)
    df["source_url"] = SMHI_URL

    df = df.dropna(subset=["temperature_c"])
    df["temperature_c"] = pd.to_numeric(df["temperature_c"], errors="coerce")
    df["latitude"]      = pd.to_numeric(df["latitude"],      errors="coerce")
    df["longitude"]     = pd.to_numeric(df["longitude"],     errors="coerce")
    df["height_m"]      = pd.to_numeric(df["height_m"],      errors="coerce")

    print(f"Loaded {len(df)} rows, observation time: {obs_time}")

    engine_url = f"postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}"
    engine = create_engine(engine_url)

    with engine.connect() as conn:
        table_exists = inspect(engine).has_table(TABLE_NAME)
        if table_exists:
            result = conn.execute(
                text(f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE observation_time = :t"),
                {"t": str(obs_time)}
            )
            already_loaded = result.scalar() > 0
        else:
            already_loaded = False

    if already_loaded:
        print(f"observation_time {obs_time} already in table, skipping.")
    else:
        df.to_sql(name=TABLE_NAME, con=engine, if_exists="append", index=False)
        print(f"Data written to Postgres table: {TABLE_NAME}")
