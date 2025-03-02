#function to remove blank rows from a dataframe
def remove_blanks(df, columns):
    return df[df[columns].notna().all(axis=1)]


#check if a column has unique values
def unique_values(df,column_name):
    return df[column_name].is_unique

#function to check if there are any neagtive values in a column when there should not be
def negative_values(df, column_name):
    return df[df[column_name] < 0]


