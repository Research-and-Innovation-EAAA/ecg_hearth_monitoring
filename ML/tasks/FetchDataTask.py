import math
import numpy as np
import pandas as pd

import services.pipelines.Task as task
import services.os.Operations as os

class FetchDataTask(task.Task):
    def exec(self, task_input, task_output):
        try:
            training_loc = task_input["training_loc"]
            training_labels_loc = task_input["training_labels_loc"]

            test_loc = task_input["test_loc"]
            test_labels_loc = task_input["test_labels_loc"]

            task_output["training"] = self._load_data(training_loc, task_input["log"])
            task_output["training_labels"] = self._load_data(training_labels_loc, task_input["log"])

            task_output["test"] = self._load_data(test_loc, task_input["log"])
            task_output["test_labels"] = self._load_data(test_labels_loc, task_input["log"])
        except Exception as e:
            print(e)

    def reverse(self, task_input, task_output):
        raise Exception("FetchDataTask reverse does nothing!")

    def _load_data(self, path, log):
        data_sets = []
        res_name = os.get_ressource_path_name(path)

        data = self._load(path)

        percent = 0

        index = 0

        for index, data_set in enumerate(data):
            index += 1

            if len(data_set) > 0:
                self._prep_data_set(data_set, data_sets)

            if log:
                percent, _ = self._log_process(len(data), index, res_name, percent)

        return np.array(data_sets)
    
    def _prep_data_set(self, data_set, sets):
        result = []
        
        splitted_data = data_set.split(',')
        
        for split_elem in splitted_data:
            result.append(int(split_elem))
        
        sets.append(np.array([result]))
    
    def _log_process(self, elements, index, name, old_percent):
        percent_loaded = math.floor((index / elements) * 100)

        _to_log = f"Loaded {name}: {math.floor(percent_loaded)} %"

        if percent_loaded - old_percent == 1:
            print(_to_log)
        
        return percent_loaded, _to_log
    
    def _load(self, path):
        with open(path) as training:
            _ = training.readline() #To ignore headers

            data = training.read()
        
        return data.split('\n') # Return individual data set as a list