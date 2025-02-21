# This file contains some helpful transformations

# Selecting/Filtering a Dataframe to a Single Column
def select_a_column(df,column_name):
    if column_name not in df.columns:
        print (f"'{column_name}' is not in the dataframe")

    return df[column_name]



#Retrieve any row of data
def retrieve_row(df,column_name,id):
    if id not in select_a_column(df,column_name):
        print (f"'{id}' is not a value in the column")

    return df[[column_name] == id]