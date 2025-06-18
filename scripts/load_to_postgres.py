"""
Author: Angel Pelaez
Purpose:
  - Connect to local PostgreSQL
  - Insert only new rows (avoid duplicates using customerid)
"""

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# 1️⃣ Load .env variables
load_dotenv()

username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")

# 2️⃣ Load cleaned CSV
df = pd.read_csv("../data/telco_churn_cleaned.csv")
print(f"Loaded DataFrame shape: {df.shape}")

# ⚡ IMPORTANT: Make sure your DataFrame column matches the lowercase table column
df.columns = [col.lower() for col in df.columns]  # auto lower all columns

# 3️⃣ Create connection URL & engine
connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"
engine = create_engine(connection_url)

table_name = "telco_churn"

try:
    # 4️⃣ Fetch existing customerids (all lowercase now!)
    existing_ids = pd.read_sql(f"SELECT customerid FROM {table_name};", engine)
    print(f"Found {existing_ids.shape[0]} existing customerids in the table.")

    # 5️⃣ Remove duplicates in DataFrame
    new_rows = df[~df['customerid'].isin(existing_ids['customerid'])]
    print(f"Rows remaining after deduplication: {new_rows.shape[0]}")

    # 6️⃣ Insert only new rows
    if not new_rows.empty:
        new_rows.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"✅ Inserted {new_rows.shape[0]} new rows.")
    else:
        print("✅ No new rows to insert. Database is up to date.")

except Exception as e:
    print(f"❌ Failed to load data: {e}")
