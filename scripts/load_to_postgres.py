# scripts/load_to_postgres.py

"""
Author: Angel Pelaez
Purpose:
  - Connect to local PostgreSQL
  - Create telco_churn table (if not exists)
  - Load cleaned CSV data into it

Run this AFTER you have PostgreSQL installed locally.
"""
# scripts/load_to_postgres.py

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

# 3️⃣ Create connection URL
connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"

engine = create_engine(connection_url)

# 4️⃣ Load DataFrame to PostgreSQL table
table_name = "telco_churn"

try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Table '{table_name}' loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")


# 5️⃣ Done!
