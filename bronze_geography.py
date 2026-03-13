import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE bronze_geography AS
SELECT
    country_code,
    country_name,
    region,
    market,
    currency,
    sales_region
FROM raw__geography;
""")

print("Created bronze_geography table")  

con.close()