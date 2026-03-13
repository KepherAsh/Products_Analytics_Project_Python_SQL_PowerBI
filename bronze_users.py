import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE bronze_users AS
SELECT
    user_id,
    account_id,
    full_name,
    email,
    job_role,
    user_status,
    created_at,
    last_seen_at,
    timezone,
    locale,
    is_admin
FROM raw__users
""")

print("Created bronze_users table")   

con.close()