
# 📊 Telco Customer Churn Analysis

**Author:** Angel Pelaez  
**Project Type:** Data Cleaning · Exploratory Data Analysis · SQL Database Integration

---

## 📌 Project Overview

This project analyzes customer churn behavior for a fictional telecom company.  
The goal is to identify factors that contribute to churn and to build a pipeline that:
- Cleans raw customer data
- Generates key visual insights
- Stores the clean dataset in a PostgreSQL database for future analysis

---

## 📁 Project Structure

├── data/
│ └── telco_churn_cleaned.csv # Final cleaned dataset
├── notebooks/
│ ├── 1_data_cleaning.ipynb # Data cleaning & export CSV
│ ├── 2_eda_visuals.ipynb # EDA plots & insights
├── sql/
│ └── create_tables.sql # SQL schema (optional, not needed if using Python loader)
├── scripts/
│ └── load_to_postgres.py # Python script to load data to PostgreSQL
├── .env # Database credentials (not tracked in Git)
├── .gitignore # Ignores .env & other junk files
├── requirements.txt # Project dependencies
├── README.md # This file


---

## 🚀 How to Run This Project

1️⃣ **Clone the repository**

git clone https://github.com/yourusername/telco-churn-analysis.git
cd telco-churn-analysis


2️⃣ **Create & activate a virtual environment**

conda create -n flask_env python=3.11
conda activate flask_env


3️⃣ **Install all required packages**

pip install -r requirements.txt


4️⃣ **Run the Jupyter notebooks in order**

notebooks/1_data_cleaning.ipynb
👉 Loads raw data, cleans it, saves telco_churn_cleaned.csv to data/.

notebooks/2_eda_visuals.ipynb
👉 Loads the cleaned CSV, generates visualizations, and summarizes insights.


5️⃣ **Load the cleaned data to PostgreSQL**

When your local PostgreSQL server is ready:

Create a .env file in the root directory with your database credentials:

POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_database_name

Then run:
python scripts/load_to_postgres.py

This will automatically create (or replace) the telco_churn table and load the cleaned data.

## ✅ Recommended way

1️⃣ Run `sql/create_tables.sql` once to define the table with the proper schema and constraints.

2️⃣ Then run `python scripts/load_to_postgres.py`  
   👉 This will append new rows without dropping the table.

---
## 🔑 Key Insights

✅ Month-to-month contract customers have the highest churn rate

✅ Customers with shorter tenure are more likely to churn

✅ Higher monthly charges slightly increase churn risk

✅ Senior citizens churn slightly more than non-seniors

---

## 🗂️ Dependencies

All dependencies are listed in requirements.txt:

pandas

seaborn

matplotlib

SQLAlchemy

python-dotenv

and others used in notebooks

---

## 🔒 Notes on Security

⚠️ .env is used to keep database credentials private.

This file is ignored by .gitignore and should never be pushed to GitHub.

---

