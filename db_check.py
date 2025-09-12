import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

# Automatically find .env in the same folder as this script
env_path = Path(__file__).parent / ".env"
print("Looking for .env at:", env_path)
load_dotenv(dotenv_path=env_path)

# Get your connection string
db_url = os.getenv("DATABASE_URL")
print("DATABASE_URL is:", db_url)

if not db_url:
    raise RuntimeError("DATABASE_URL is not set. Check your .env location and name.")

# Connect to PostgreSQL
engine = create_engine(db_url, future=True)

with engine.connect() as conn:
    df = pd.read_sql(text("SELECT NOW() AS current_time;"), conn)

print(df)
