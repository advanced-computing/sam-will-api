import pandas as pd
import duckdb

def get_latest_data(pull_date):

    cpi_data = pd.read_csv("Fed_CPI.csv")

    year = pull_date[2:3]
    month = pull_date[5:6].int
    vintage = (f"PCPI{year}M{month}")

    cpi_data_vintage = cpi_data[["DATE", vintage]]
    
    return cpi_data_vintage