import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE silver_users AS
SELECT
    user_id,
    account_id,
            
    -- Core descriptors
    full_name,
    LOWER(SPLIT_PART(email, '@', 2)) AS email_domain,
    job_role,
    user_status,
            
    created_at,
    CAST(created_at AS DATE) AS created_date,
    last_seen_at,
            
    -- Tenure & recency
    CASE
        WHEN CAST(created_at AS DATE) > CURRENT_DATE THEN 0
        ELSE DATE_DIFF('day', CAST(last_seen_at AS DATE), CURRENT_DATE)
    END AS user_tenure_days,       

    CASE
        WHEN last_seen_at IS NULL THEN NULL
        ELSE DATE_DIFF('day', CAST(last_seen_at AS DATE), CURRENT_DATE)
    END AS days_since_last_seen,
            
    CASE 
        WHEN last_seen_at IS NULL THEN 'Never seen'
        WHEN DATE_DIFF('day', CAST(last_seen_at AS DATE), CURRENT_DATE) <= 7 THEN '0-7 days'
        WHEN DATE_DIFF('day', CAST(last_seen_at AS DATE), CURRENT_DATE) <= 30 THEN '8-30 days'
        WHEN DATE_DIFF('day', CAST(last_seen_at AS DATE), CURRENT_DATE) <= 90 THEN '31-90 days'
        ELSE '90+ days'
    END AS recency_bucket,
            
    -- Flags
    (user_status = 'active') AS is_active_user,
    is_admin
    
FROM bronze_users
""")

print("Created silver_users table")   

con.close()