import argparse
import pandas as pd
from sqlalchemy import create_engine, Integer, Float, String, DateTime

dtype_schema = {
    "VendorID": Integer(),
    "tpep_pickup_datetime": DateTime(),
    "tpep_dropoff_datetime": DateTime(),
    "passenger_count": Integer(),
    "trip_distance": Float(),
    "RatecodeID": Integer(),
    "store_and_fwd_flag": String(1),
    "PULocationID": Integer(),
    "DOLocationID": Integer(),
    "payment_type": Integer(),
    "fare_amount": Float(),
    "extra": Float(),
    "mta_tax": Float(),
    "tip_amount": Float(),
    "tolls_amount": Float(),
    "improvement_surcharge": Float(),
    "total_amount": Float(),
    "congestion_surcharge": Float(),
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres with batching and schema enforcement")

    parser.add_argument("--user", required=True, help="Postgres user name")
    parser.add_argument("--password", required=True, help="Postgres password")
    parser.add_argument("--host", required=True, help="Postgres host")
    parser.add_argument("--port", required=True, help="Postgres port")
    parser.add_argument("--db", required=True, help="Database name")
    parser.add_argument("--table_name", required=True, help="Destination table")
    parser.add_argument("--url", required=True, help="URL of the CSV file")

    args = parser.parse_args()

    print(f"Reading data in chunks from {args.url}")
    chunksize = 100_000
    df_iter = pd.read_csv(args.url, compression="gzip", chunksize=chunksize)

    engine_url = f"postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}"
    engine = create_engine(engine_url)

    first_chunk = next(df_iter)
    first_chunk.tpep_pickup_datetime = pd.to_datetime(first_chunk.tpep_pickup_datetime)
    first_chunk.tpep_dropoff_datetime = pd.to_datetime(first_chunk.tpep_dropoff_datetime)

    first_chunk.head(0).to_sql(
        name=args.table_name,
        con=engine,
        if_exists="replace",
        dtype=dtype_schema,
        index=False
    )
    print(f"Created table {args.table_name} with schema.")

    first_chunk.to_sql(name=args.table_name, con=engine, if_exists="append", index=False)
    print(f"Inserted first {len(first_chunk)} rows.")

    for i, chunk in enumerate(df_iter, start=2):
        chunk.tpep_pickup_datetime = pd.to_datetime(chunk.tpep_pickup_datetime)
        chunk.tpep_dropoff_datetime = pd.to_datetime(chunk.tpep_dropoff_datetime)

        chunk.to_sql(name=args.table_name, con=engine, if_exists="append", index=False)
        print(f"Inserted chunk {i} with {len(chunk)} rows.")

    print("Finished ingesting data into Postgres.")
