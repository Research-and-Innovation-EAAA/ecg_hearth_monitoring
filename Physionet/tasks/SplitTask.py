import threading

import services.os.Operations as os
import services.pipelines.Task as Task
import services.modifiers.Loader as loader

class SplitTask(Task.Task):
    def __init__(self, readings):
        self.data_readings = readings

    def exec(self, task_input, task_output):
        task_output["readings"] = self.data_readings

        resources = os.dir_res_list(task_output["res_loc"])

        for elem in resources:
            res_path = os.path_join(task_output["res_loc"], elem)

            if not os.is_path_file(res_path):
                continue
            
            res_data = loader.load_data(res_path)

            target_split_folder = os.path_join(task_output["res_loc"], elem[:-4])
            os.makedirs(target_split_folder, True)

            self._process(res_data, self.data_readings, elem, target_split_folder)
        
    def _process(self, data, readings, res_name, target_loc):
        sample_nr, ecg, other = self._split_headder_data(data)
        split_index, readings_index = 0, 0
        to_wait = []

        while readings_index < len(sample_nr):
            end_index = readings_index + readings

            to_wait.append(self._split_and_save(ecg, readings_index, end_index, target_loc, split_index, f"ecg_{readings}"))
            
            split_index += 1
            readings_index += readings + 1

        for t in to_wait:
            t.join()
    
    def _split_and_save(self, readings, readings_index, end_index, target_loc, split_index, name):
        t = save_split_data(readings, readings_index, end_index, target_loc, split_index, name)
        t.start()
        return t
    
    def _split_headder_data(self, data):
        try:
            sample_nr = data.drop(columns=['ECG', 'RESP'], axis=1)
            ecg = data.drop(['RESP', 'sample #'], axis=1)
            other = data.drop(['ECG', 'sample #'], axis=1)
        except Exception:
            sample_nr = data.drop(columns=['ECG 1', 'ECG 2'], axis=1)
            ecg = data.drop(['ECG 2', 'sample #'], axis=1)
            other = data.drop(['ECG 1', 'sample #'], axis=1)

        return sample_nr, ecg, other
    
    def reverse(self, task_input, task_output):
        print("Does nothing")

class save_split_data(threading.Thread):
    def __init__(self, data, start_index, end_index, target_folder, index, name):
        threading.Thread.__init__(self)

        self.data = data
        self.start_index = start_index
        self.end_index = end_index
        self.target_folder = target_folder
        self.index = index
        self.name = name

    def run(self):
        target_loc = os.path_join(self.target_folder, f"{self.name}_split_{self.index}.csv")
        training_sample = "readings\n"

        for elem in self.data.values[self.start_index: self.end_index]:
            training_sample = f"{training_sample}{elem[0]}\n"

        with open(target_loc, 'w') as file:
            file.write(training_sample)