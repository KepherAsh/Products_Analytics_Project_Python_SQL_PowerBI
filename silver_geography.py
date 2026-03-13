import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE silver_geography AS
WITH base AS(
    SELECT
        UPPER(TRIM(country_code)) AS country_code,
        country_name,
        region,
        market,
        currency,
        sales_region
    FROM bronze_geography
),
deduped AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(
            PARTITION BY country_code
            ORDER BY country_name
        ) AS rn
    FROM base
)
SELECT 
    country_code,
    country_name,
    region, 
            
    -- Fill a small known gap from the raw sheet
    CASE 
        WHEN country_code = 'UK' AND market IS NULL THEN 'UKI'
        ELSE market
    END AS market,

    currency,
    sales_region
FROM deduped
WHERE rn = 1;
""")

print("Created silver_geography table")  

con.close()