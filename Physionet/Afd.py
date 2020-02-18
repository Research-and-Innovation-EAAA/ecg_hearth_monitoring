import tensorflow as tf

def setup_model(loss, optimizer, metrics):
    model_input = tf.keras.layers.Input(shape=(15360, ))

    model_layer = tf.keras.layers.Dense(7680, activation='sigmoid')(model_input)
    model_layer = tf.keras.layers.Dense(200, activation='tanh')(model_layer)
    model_layer = tf.keras.layers.Dense(50, activation='elu')(model_layer)
    model_layer = tf.keras.layers.Dense(50, activation='tanh')(model_layer)
    model_output = tf.keras.layers.Dense(1, activation='tanh', name="Output_layer")(model_layer)

    model = tf.keras.models.Model(inputs=model_input, outputs=model_output)

    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)