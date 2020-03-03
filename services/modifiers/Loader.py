import os
import pandas as pd

def load_data(path=None):
    if not os.path.isfile(path):
        raise Exception("File-like object is not a 'file'!")

    if path[-4:]== '.csv':
        return __csv_load(path)
    else:
        raise Exception(f"Currently {path[-4,]} files are not supported!")

def __csv_load(path):
    return pd.read_csv(path)

def __load_raw_data(path=None):
    with open(path) as file:
        return file.read()