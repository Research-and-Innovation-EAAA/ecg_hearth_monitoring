import services.pipelines.Task as task

import tensorflow as tf
from tensorflow import keras as keras

class LoadModelTask(task.Task):
    def exec(self, task_input, task_output):
        model_path = task_input["model_loc"]

        model = keras.models.load_model(model_path, compile=task_input["compile"])

        task_output["model"] = model

    def reverse(self, task_input, task_output):
        pass