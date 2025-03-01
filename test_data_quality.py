import pandas as pd
from data_quality_functions import remove_blanks, unique_values


def test_blanks():
    data = {
        'name': [None, 'Bob', 'Charlie', 'David', 'Emma'],
        'age': [25, 30, 35, 40, 45]}

    df = pd.DataFrame(data)

    expected_output = {
        'name': ['Bob', 'Charlie', 'David', 'Emma'],
        'age': [30, 35, 40, 45]
    }

    df_expected_output = pd.DataFrame(expected_output)

    blank_removal = remove_blanks(df,['name'])
    blank_removal = blank_removal.reset_index(drop=True)

    assert blank_removal.equals(df_expected_output)


def test_unique():
    data = {
        'name': ['Bob', 'Bob', 'Charlie', 'David', 'Emma'],
        'age': [25, 30, 35, 40, 45]}

    df = pd.DataFrame(data)

    expected_output = False

    unique = unique_values(df,'name')

    assert unique == expected_output

