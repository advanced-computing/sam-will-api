-- Connect to a new or existing DuckDB database file with the following

ATTACH DATABASE 'Fed_CPI2.db' AS mydb;

-- Create table in this persistent database

CREATE OR REPLACE TABLE mydb.cpi_append AS SELECT * FROM read_csv('PCPI24M1.csv');
CREATE OR REPLACE TABLE mydb.cpi_trunc AS SELECT * FROM read_csv('PCPI24M1.csv');
CREATE OR REPLACE TABLE mydb.cpi_inc AS SELECT * FROM read_csv('PCPI24M1.csv');