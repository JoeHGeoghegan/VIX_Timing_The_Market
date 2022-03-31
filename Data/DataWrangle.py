import pandas as pd
import os

def HelloWorld():
    return "Hello World"

def create_data():
    # Reading all csv data from PopStocks (containing 5 popular stocks) resource folder
    DF_DataImport = []
    filepath_str = "./cleandata/"
    indexCol = "timestamp"

    for filename in os.listdir(filepath_str): # Loops over ever file name in the folder
        df = pd.read_csv( # Uses Pandas csv reader
            f"{filepath_str}/{filename}", # Recreates the  direct path to the csv file
            
            # Parse and set the date index
            parse_dates=True,
            infer_datetime_format=True,
            index_col=indexCol
            )
        DF_DataImport.append(df) # Appends the dataframe to the array of dataframes