import tensorflow as tf
from tensorflow import keras

def setup_model(inputs):
    power_of = 0

    model_input = keras.layers.Input(shape=(inputs, 1,), name="ECG-model-input", dtype=tf.float32)
    model_layer = keras.layers.Conv1D(filters=32*2**power_of,kernel_size=1)(model_input)
    model_layer = keras.layers.BatchNormalization()(model_layer)
    model_layer = keras.activations.relu(model_layer)

    for x in range(0, 14):
        model_layer = keras.layers.Conv1D(filters=32*2**power_of,kernel_size=1)(model_layer)
        model_layer = keras.layers.BatchNormalization()(model_layer)
        model_layer = keras.activations.relu(model_layer)
        model_layer = keras.layers.Dropout(0.2)(model_layer)
        model_layer = keras.layers.Conv1D(filters=32*2**power_of,kernel_size=1)(model_layer)

        if x % 4 == 0:
            power_of += 1

    model_layer = keras.layers.BatchNormalization()(model_layer)
    model_layer = keras.activations.relu(model_layer)
    
    
    model_layer = keras.layers.Dense(12)(model_layer)
    output = keras.layers.Softmax(name="ECG-model-output")(model_layer)

    return keras.Model(inputs=model_input, outputs=output)