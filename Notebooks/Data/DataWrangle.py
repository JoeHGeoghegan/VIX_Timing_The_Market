import pandas as pd
import os

from pyparsing import col

def HelloWorld():
    return "Hello World"

def read_into_single_DF():
    # Reading all csv data from PopStocks (containing 5 popular stocks) resource folder
    DF_DataImport = pd.DataFrame()
    filepath_str = "./Data/cleandata/"
    indexCol = "timestamp"

    for filename in os.listdir(filepath_str): # Loops over ever file name in the folder
        # print(filename)
        df = pd.read_csv( # Uses Pandas csv reader
            f"{filepath_str}/{filename}", # Recreates the  direct path to the csv file
            
            # Parse and set the date index
            parse_dates=True,
            infer_datetime_format=True
            )
        df = df[[indexCol,'close']] # Remove all but useful data
        df = df.rename(columns={'close':f'close_{filename[:len(filename)-9]}'}) # name closing data

        # DF_DataImport = DF_DataImport.append(df,ignore_index=True) # Appends the dataframe to the array of dataframes
        DF_DataImport = pd.concat([DF_DataImport,df.set_index(indexCol)],axis='columns',join='outer')
    return DF_DataImport.sort_index()

def shared_date_data():
    return read_into_single_DF().dropna()

def slice_up(sources,dropNa=True):
    if dropNa:
        return read_into_single_DF()[sources].dropna()
    else:
        return read_into_single_DF()[sources]

def add_pct_change(dataframe:pd.DataFrame):
    col_headers = {}
    for col in dataframe.columns:
        col_headers[col] = col.replace('close','pct_change')
    return pd.concat([dataframe,
    dataframe.pct_change().rename(columns=col_headers)
    ],axis='columns')

def combine_DFs(list_of_DF,key_names):
    df_base = {}
    for index in range(len(key_names)):
        df_base[key_names[index]] = list_of_DF[index]
    return pd.concat(df_base.values(), keys=df_base.keys(), axis="columns")
