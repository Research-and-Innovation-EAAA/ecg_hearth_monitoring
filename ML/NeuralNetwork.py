import tensorflow as tf
from tensorflow import keras

import supporters.Loaders as loader

__epochs = 10
__save_path = "C:\\Users\\mabh\\Desktop\\Workspace_development\\ECG Hearth Monitoring\\resources\\ML-models"

def model_5l_pred_norm_hbeat():
    model_1 = keras.Sequential([
        keras.layers.Dense(513, activation='tanh'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(32, activation='tanh'),
        keras.layers.Dense(10, activation='tanh'),
        keras.layers.Dense(1)
    ])

    model_1.compile(loss="mse", optimizer="sgd", metrics=['accuracy'])

def model_4l_model():
    model_2 = keras.Sequential([
        keras.layers.Dense(513, activation='tanh'),
        keras.layers.Dense(128, activation='tanh'),
        keras.layers.Dense(10, activation='tanh'),
        keras.layers.Dense(1)
    ])

    model_2.compile(loss=tf.keras.losses.MeanAbsoluteError(), optimizer="adam", metrics=['accuracy'])
    
def model_3l_jump_model():
    model_3 = keras.Sequential([
        keras.layers.Dense(513, activation='tanh'),
        keras.layers.Dense(10, activation='relu'),
        keras.layers.Dense(1)
    ])

    model_3.compile(loss=tf.keras.losses.LogCosh(), optimizer="adam", metrics=['accuracy'])

