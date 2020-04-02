import services.pipelines.Task as task
import services.os.Operations as os

import tensorflow as tf
from tensorflow import keras

class ModelSaveTask(task.Task):
    def exec(self, task_input, task_output):
        self._prep_dir(task_input["model_loc"])

        model_path = os.path_join(task_input["model_loc"], f'model-{task_input["inputs"]}')

        if not task_input["model_override"] and os.is_dir(model_path):
            #TODO implement a dynamic "path increment" model-name save functionality
            pass

        task_output["model"].save(model_path)

    def reverse(self, task_input, task_output):
        pass

    def _prep_dir(self, path):
        pass