import pandas as pd
import duckdb

def get_latest_data(pull_date):

    cpi_data = pd.read_csv("Fed_CPI.csv")

    year, month, day = pull_date.split('-')

    year = year[2:]
    month = month.lstrip('0')
    # month = month.int()
    # stringmonth = month.str()

    # string_date = pull_date.dt.strftime('%YM%-m')
    # year = string_date[2:4]
    # month = string_date[5:7].astype(int)
    vintage = (f"PCPI{year}M{month}")

    cpi_data_vintage = cpi_data[["DATE", vintage]]
    
    return cpi_data_vintage
   