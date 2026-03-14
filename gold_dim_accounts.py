import duckdb
from config import DB_PATH  

# Connect to your database
con = duckdb.connect(DB_PATH)
print(f"Connected to: {DB_PATH}")

con.execute("""
CREATE OR REPLACE TABLE gold_dim_accounts AS
SELECT
    account_id AS AccountId,
            
    account_name AS AccountName,
    segment AS Segment,       
    industry AS Industry,      
    employee_band AS EmployeeBand,      
    acquisition_channel AS AcquisitionChannel, 

    country_code AS CountryCode,
    country_name AS CountryName,
    region AS Region,
    market AS Market, 
    sales_region AS SalesRegion,
    local_currency AS LocalCurrency,

    account_status AS AccountStatus,
    is_active_account AS IsActiveAccount,
    has_trial AS HasTrial,

    created_at AS CreatedAt,
    created_date AS CreatedDate,
    trial_start_date AS TrialStartDate,
    trial_end_date AS TrialEndDate,

    account_age_days AS AccountAgeDays,
    account_age_bracket AS AccountAgeBucket,
    trial_lenght_days AS TrialLengthDays
FROM silver_accounts
ORDER BY AccountId;
""")

print("Created gold_dim_accounts")

con.close()