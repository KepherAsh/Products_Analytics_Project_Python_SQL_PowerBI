import os
from dotenv import load_dotenv

# This reads your .env file and loads what's inside into your environment
load_dotenv()

# Now grab the path from the environment
DB_PATH = os.getenv("DUCKDB_PATH")

if not DB_PATH:
    raise ValueError("DUCKDB_PATH not found. Check your .env file.")