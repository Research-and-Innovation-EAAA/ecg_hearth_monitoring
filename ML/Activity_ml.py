import tensorflow as tf

def setup_model(training, labels):
    model_input = tf.keras.layers.Input(shape=(15360, ))

    """
    model_layer = tf.keras.layers.Dense(7680, activation='sigmoid')(model_input)
    model_layer = tf.keras.layers.Dense(3590, activation='tanh')(model_layer)
    model_layer = tf.keras.layers.Dense(1795, activation='elu')(model_layer)
    model_layer = tf.keras.layers.Dense(200, activation='tanh')(model_layer)
    """

    model_layer = tf.keras.layers.Dense(7680, activation='sigmoid')(model_input)
    model_layer = tf.keras.layers.Dense(200, activation='tanh')(model_layer)
    model_layer = tf.keras.layers.Dense(50, activation='elu')(model_layer)
    model_layer = tf.keras.layers.Dense(50, activation='tanh')(model_layer)
    model_output = tf.keras.layers.Dense(1, activation='tanh', name="Output_layer")(model_layer)

    model = tf.keras.models.Model(inputs=model_input, outputs=model_output)

    model.compile(loss='mse', optimizer="sgd", metrics=["accuracy"])

    model.fit(training.to_numpy(), labels.to_numpy(), epochs=15, batch_size=4)

