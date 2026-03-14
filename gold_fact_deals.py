import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE gold_fact_deals AS
SELECT
    deal_id AS DealId,
    account_id AS AccountId,
    owner_user_id AS OwnerUserId,
            
    pipeline_id AS PipelineId,
    current_stage_id AS StageId,
            
    status AS Status,
            
    created_at AS CreatedAt,
    created_at  AS CreatedDate,
    
    closed_at AS ClosedAt,
    closed_at AS ClosedDate,
            
    last_stage_changed_at AS LastStageChangeAt,
    last_stage_changed_at AS LastStageChangeDate,
            
    amount AS DealAmount,
    currency AS Currency,
    country_code AS CountryCode,
            
    source_system AS SourceSystem,
            
    is_closed AS IsClosed,
    is_won AS IsWon,
            
    deal_cycle_days AS DealCycleDays,
    deal_age_days AS DealAgeDays
            
FROM silver_deals
ORDER BY DealId;
""")

print("Created gold_fact_deals table")   

con.close()