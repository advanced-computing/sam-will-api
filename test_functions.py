import pandas as pd
import pytest
import importlib
my_api = importlib.import_module("flask-sam-will-api")
import io

def test_limit_offset():

    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'age': [25, 30, 35, 40, 45]}

    df = pd.DataFrame(data)

    expected_output = {
        'name': ['Bob', 'Charlie'],
        'age': [30, 35]
    }

    pandas_data_out = pd.DataFrame(expected_output)

    limit = 2
    offset = 1

    output = my_api.limit_offset(df, limit, offset)

    output = output.reset_index(drop=True)

    assert output.equals(pandas_data_out)

def test_column_name():
     
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'age': [25, 30, 35, 40, 45]
    }

    df = pd.DataFrame(data)   

    output =  {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
    }
    df_output = pd.DataFrame(output)  

    column_output = my_api.column_filter(df, 'name')
    column_output = column_output.reset_index(drop=True)

    assert column_output.equals(df_output)