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
