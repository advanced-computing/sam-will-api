-- Connect to a new or existing DuckDB database file with the following

ATTACH DATABASE 'mta_data.db' AS mydb;

-- Create table in this persistent database

CREATE TABLE mydb.mta AS SELECT * FROM read_csv("MTA_data.csv");


