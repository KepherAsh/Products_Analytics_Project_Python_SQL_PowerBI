import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE gold_fact_product_events AS
SELECT
    event_id AS EventId,
        
    account_id AS AccountId,
    user_id AS UserId,
    deal_id AS DealId,
    
    event_name AS EventName,
    event_category AS EventCategory,
    has_deal_context AS HasDealContext,
            
    event_timestamp AS EventTimestamp,
    event_ts_date AS EventDate,
    event_ts_month AS EventMonth,

    platform AS Platform,
    device_type AS DeviceType,
    app_version AS AppVersion,
    country_code AS CountryCode,

    source_system AS SourceSystem
            
FROM silver_product_events
ORDER BY EventId;
""")

print("Created gold_fact_product_events table")   

con.close()