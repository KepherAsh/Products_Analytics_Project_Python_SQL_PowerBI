import duckdb

# Connect to the example DuckDB file
con = duckdb.connect("setup_example.duckdb")

# Run a simple query to confirm the connection works
result = con.sql("SELECT COUNT(*) AS total_customers FROM raw_customers").fetchdf()

print("Connection successful!")
print(result)
con.close()
# import duckdb

# con = duckdb.connect("setup_example.duckdb")

# tables = con.execute("SHOW TABLES").fetchdf()
# print(tables)
# print(table)
