import services.pipelines.Task as task

import services.os.Operations as os

import numpy as np

import math

class AppleDataEvaluateTask(task.Task):
    def exec(self, task_input, task_output):
        evaluation_set = self._load_data(task_input["apple_data_loc"], task_input["log"])
        labels = self._load_labels_data(task_input["apple_labels_loc"], task_input["log"])

        model = task_output["model"]

        eva = model.evaluate(evaluation_set, labels)

        with open(task_input["apple_evaluation"], 'w') as evaluation_file:
            for elem in eva:
                evaluation_file.write(f"{elem}\n")
    
    def reverse(self, task_input, task_output):
        pass

    def _load_labels_data(self, path, log):
        data_sets = []
        res_name = os.get_ressource_path_name(path)

        data = self._load(path)

        percent = 0

        index = 0

        for index, data_set in enumerate(data):
            index += 1

            if len(data_set) > 0:
                self._prep_labels_data_set(data_set, data_sets)

            if log:
                percent, _ = self._log_process(len(data), index, res_name, percent)

        return np.array(data_sets)
    
    def _prep_labels_data_set(self, data_set, sets):
        result = []
        
        splitted_data = data_set.split(',')
        
        for split_elem in splitted_data:
            result.append(int(split_elem))
        
        if len(splitted_data) == 1:
            result.append(0)
        
        sets.append(np.array([result]))

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
    
    def _load(self, path):
        with open(path) as training:
            _ = training.readline() #To ignore headers

            data = training.read()
        
        return data.split('\n') # Return individual data set as a list
    
    def _prep_data_set(self, data_set, sets):
        result = []
        
        splitted_data = data_set.split(',')

        for split_elem in splitted_data:
            result.append(float(split_elem))
        
        sets.append(np.array([result]))
    
    def _log_process(self, elements, index, name, old_percent):
        percent_loaded = math.floor((index / elements) * 100)

        _to_log = f"Loaded {name}: {math.floor(percent_loaded)} %"

        if percent_loaded - old_percent == 1 or percent_loaded > old_percent:
            print(_to_log)
        
        return percent_loaded, _to_log