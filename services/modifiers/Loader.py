import os
import pandas as pd

def load_data(path=None):
    #TODO Add a guard for non-existing or missing parameters

    if not os.path.isfile(path):
        raise Exception("File-like object is not a 'file'!")

    if path[-4:]== '.csv':
        return __csv_load(path)
    else:
        raise Exception(f"Currently {path[-4,]} files are not supported!")

def __csv_load(path):
    if not os.path.isfile(path):
        raise Exception("Path for a non-file like object")

    return pd.read_csv(path)

def __load_raw_data(path=None):
    if path == None:
        raise Exception("Missing path")

    with open(path) as file:
        return file.read()