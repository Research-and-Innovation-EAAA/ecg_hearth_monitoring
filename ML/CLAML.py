import tensorflow as tf
from tensorflow import keras as keras

def gen_model(input_shape):
    model_input, model_layer = __gen_model_input(input_shape)

    model_layer = __gen_risidual_blocks(model_layer)

    model_output = __gen_model_output(model_layer)

    return keras.Model(inputs=model_input, outputs=model_output)

def __gen_model_input(input_shape):
    model_input = keras.layers.Input(shape=(input_shape, ))

    model_layer = keras.layers.BatchNormalization()(model_input)

    model_layer = keras.activations.relu(model_layer)

    return model_input, model_layer

def __gen_risidual_blocks(model_layer):
    res_model_layer = keras.layers.Convo1d((32*2**0), 1)(model_layer)
    
    res_model_layer = keras.layers.BatchNormalization()(res_model_layer)
    
    res_model_layer = keras.activations.relu(res_model_layer)

    for filters_level in range(0, 3):
        for _ in range(0, 4):
            res_model_layer = __gen_risidual_block(res_model_layer, filters_level)
    
    return res_model_layer


def __gen_risidual_block(model_layer, filters_level):
    filters = 32*2**filters_level

    model_layer = keras.layers.Conv1d(filters, 1)(model_layer)
    
    model_layer = keras.layers.BatchNormalization()(model_layer)
    
    model_layer = keras.activations.relu(model_layer)

    model_layer = keras.layers.Dropout()(model_layer)

    model_layer = keras.layers.Conv1d(filters, 1)(model_layer)

    return model_layer

def __gen_model_output(model_layer):
    model_layer = keras.layers.BatchNormalization()(model_layer)

    model_layer = keras.layers.relu(model_layer)

    model_layer = keras.layers.Dense(12)(model_layer)

    model_layer = keras.layers.Softmax()(model_layer)

    return model_layer