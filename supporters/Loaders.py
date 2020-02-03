import os
import pandas as pd

def load_csv(resource_folder=None, resource_name=None):
    if resource_folder is None or resource_name is None:
        raise Exception("Required parameters is missing!")

    resource = os.path.join(resource_folder, f'{resource_name}.csv')

    return pd.read_csv(resource)