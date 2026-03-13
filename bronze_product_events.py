import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE bronze_product_events AS
SELECT
    event_id,
    event_name,
    user_id,
    account_id,
    deal_id,
    event_timestamp,
    ingested_at,
    event_date,
    platform,
    device_type,
    app_version,
    country_code,
    event_properties,
    is_test_event,
    source_system
FROM raw__product_events;
""")

print("Created bronze_product_events table")   

con.close()