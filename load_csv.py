import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"), future=True)

# Example CSV path
csv_path = r"C:\Users\<you>\Projects\christopher-analytics\data\expenses_2025_08.csv"
df = pd.read_csv(csv_path)

# Ensure column names/types match your table or transform as needed:
df.columns = ["month", "category", "amount"]
df["month"] = pd.to_datetime(df["month"]).dt.date

# Load into a staging table first (common analytics pattern)
df.to_sql("monthly_expenses_staging", con=engine, schema="sandbox", if_exists="replace", index=False)
print("Loaded to sandbox.monthly_expenses_staging")
