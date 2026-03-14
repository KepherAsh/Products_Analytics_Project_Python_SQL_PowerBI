import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE gold_dim_users AS
SELECT
    user_id AS UserId,
    account_id AS AccountId,
            
    full_name AS FullName,
    email_domain AS EmailDomain,       
    job_role AS JobRole,      
    user_status AS UserStatus,  
                
    is_active_user AS IsActiveUser, 
    is_admin AS IsAdmin,
            
    created_at AS CreatedAt,
    created_date AS CreatedDate,
    last_seen_at AS lastSeenAt,

    user_tenure_days AS UserTenureDays,
    days_since_last_seen AS DaysSinceLastSeen,
    recency_bucket AS RecencyBucket,

FROM silver_users
ORDER BY UserId;
""")

print("Created gold_dim_users")

con.close()