# 📂 Database Setup Instructions

**Author:** Angel Pelaez  

## 1️⃣ Create the Database

Open `psql`:

"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres

---

Inside psql:

CREATE DATABASE telco_churn;
\l 

---

## 2️⃣ Define the Table

Connect directly to the new DB:

"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -d telco_churn

Run:

\i 'C:/path/to/sql/create_tables.sql'

Check:

\dt


## 3️⃣ Load Data

Edit .env with your real credentials.

Then run:

python scripts/load_to_postgres.py


This will append rows to your pre-defined table.

---

# ✅ Verify
Inside psql:

SELECT COUNT(*) FROM telco_churn;
SELECT * FROM telco_churn LIMIT 5;
