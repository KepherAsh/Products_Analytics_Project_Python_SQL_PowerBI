import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

# Create bronze schema
# con.execute("CREATE SCHEMA IF NOT EXISTS bronze")

# Create bronze tables - raw table no transformations yes
# raw_tables = ["raw_accounts", "raw_deals", "raw_product_events", "raw_users"]

# for table in raw_tables:
#     bronze_table = f"bronze.{table.replace('raw_', 'bronze_')}"
    
con.execute("""
CREATE OR REPLACE TABLE bronze_accounts AS
SELECT
    account_id,
    account_name,
    country_code,
    city,
    industry,
    employee_band,
    segment,
    created_at,
    trial_start_date,
    trial_end_date,
    account_status,
    acquisition_channel
FROM raw__accounts
""")

print("Created bronze_account table")   
# count = con.execute(f"SELECT COUNT(*) FROM {bronze_table}").fetchone()[0]
#     print(f"✅ Created {bronze_table} — {count} rows")
con.close()