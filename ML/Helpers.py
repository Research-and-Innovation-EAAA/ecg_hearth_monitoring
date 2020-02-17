import os
import tensorflow as tf
from tensorflow import keras as keras

def load_model(path = None):
    if not isinstance(path, str):
        raise Exception("Missing path to local model!")

    return keras.model.load_model(path)

def save_model(model = None, name = None):
    if model is None:
        raise Exception("Missing model!")

    path = os.path.join('.', 'resources', 'ml_models')
    
    if name is None:
        name = f"default_model_save_{__models_count(path)}"

    model.save_model(os.path.join(path, name))    

def __models_count(path = None):
    if path is None:
        path = os.path.join('.', 'resources', 'ml_models')

    counted_models = 0

    try:
        os_list = os.listdir(path)
        for element in os_list:
            if os.path.isfile(os.path.join(path, element)):
                counted_models += 1
    except FileNotFoundError:
        os.makedirs(path)
    
    return counted_models