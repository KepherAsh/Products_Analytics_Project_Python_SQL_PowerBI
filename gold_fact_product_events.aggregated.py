import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE gold_fact_product_events_aggregated AS
SELECT       
    event_ts_date AS EventDate,
    event_name AS EventName,
    event_category AS EventCategory,
    account_id AS AccountId,
    

    COUNT(*) AS EventCount,
    COUNT(DISTINCT user_id) AS UniqueUsers,         
FROM silver_product_events
GROUP BY
    event_ts_date,
    event_name,
    event_category,
    account_id   
ORDER BY 
    EventDate,
    EventName,
    AccountId;
""")

print("Created gold_fact_product_events_aggregated table")   

con.close()