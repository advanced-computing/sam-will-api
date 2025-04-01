## Instructions
***User Instructions***:  
    1. Enter "duckdb Fed_CPI2.db" into the terminal  
    2. Enter ".tables" to see the three table titles cpi_append, cpi_inc, cpi_trunc  
    3. Enter "SELECT * FROM cpi_append;" to see the append table  
    4. Enter "SELECT * FROM cpi_inc;" to see the inc table  
    5. Enter "SELECT * FROM cpi_trunc;" to see the trunc table  

***Explanation***:
    cpi_trunc, cpi_inc, and cpi_append will all look identical to PCPI25.csv because no data was dropped from PCPI24 to PCPI25, even though there was new data, and old data was revised.
