-- Connect to a new or existing DuckDB database file with the following

ATTACH DATABASE 'Fed_CPI.db' AS mydb;

-- Create table in this persistent database

CREATE TABLE mydb.fed AS SELECT * FROM read_csv('Fed_CPI.csv');