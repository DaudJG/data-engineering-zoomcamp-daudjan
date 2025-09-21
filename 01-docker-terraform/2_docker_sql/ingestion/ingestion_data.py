import argparse
import pandas as pd 
from sqlalchemy import create_engine


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument("--user", required=True, help="Postgres user name")
    parser.add_argument("--password", required=True, help="Postgres password")
    parser.add_argument("--host", required=True, help="Postgres host")
    parser.add_argument("--port", required=True, help="Postgres port")
    parser.add_argument("--db", required=True, help="Database name")
    parser.add_argument("--table_name", required=True, help="Destination table")
    parser.add_argument("--url", required=True, help="URL of the CSV file")

    args = parser.parse_args()

    print(f"Reading data from {args.url} ")
    df = pd.read_csv(args.url, compression="gzip")
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")

    engine_url = f"postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}"
    engine = create_engine(engine_url)
 
    df.to_sql(
    name=args.table_name,
    con=engine,
    if_exists="replace",   
    index=False)            
    print(f"Data written to Postgres table: {args.table_name}")