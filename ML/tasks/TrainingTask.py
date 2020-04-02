import services.pipelines.Task as task

import numpy as np

import tensorflow as tf
from tensorflow import keras

class TrainingTask(task.Task):
    def exec(self, task_input, task_output):
        model = self._setup_model(task_input["inputs"])

        self._model_compile(model, task_input["optimizer"], task_input["loss"], task_input["sass"])

        task_output["training_history"] = model.fit(task_output["training"], task_output["training_labels"], epochs=task_input["epochs"], verbose=task_input["verbose"])

        #eva_loss, eva_metrics = model.evaluate(task_output["test"], task_output["test_labels"])
        eva = model.evaluate(task_output["test"], task_output["test_labels"])

        task_output["eva_loss"] = eva[0]
        task_output["eva_metrics"] = eva[1:]

        task_output["model"] = model
    
    def reverse(self, task_input, task_output):
        pass

    def _setup_model(self, inputs, power=0):
        model_input = keras.layers.Input(shape=(1,inputs), name="ECG-model-input", dtype=tf.float32)
        model_layer = keras.layers.Conv1D(filters=32*2**power,kernel_size=1)(model_input)
        model_layer = keras.layers.BatchNormalization()(model_layer)
        model_layer = keras.activations.relu(model_layer)

        for x in range(0, 17):
            model_layer = keras.layers.Conv1D(filters=32*2**power,kernel_size=1)(model_layer)
            model_layer = keras.layers.BatchNormalization()(model_layer)
            model_layer = keras.activations.relu(model_layer)
            model_layer = keras.layers.Dropout(0.2)(model_layer)
            model_layer = keras.layers.Conv1D(filters=32*2**power,kernel_size=1)(model_layer)

            if x != 0 and x % 4 == 0:
                power += 1

        model_layer = keras.layers.BatchNormalization()(model_layer)
        model_layer = keras.activations.relu(model_layer)
        model_layer = keras.layers.Dense(2)(model_layer)
        output = keras.layers.Softmax(name="ECG-model-output")(model_layer)
        
        return keras.Model(inputs=model_input, outputs=output)
    
    def _model_compile(self,model, optimizer, loss, sass):
        metrics = []

        for value in sass:
            metrics.append(keras.metrics.SensitivityAtSpecificity(value))
            metrics.append(keras.metrics.SpecificityAtSensitivity(value))

        model.compile(optimizer=optimizer, loss=loss, metrics=metrics)