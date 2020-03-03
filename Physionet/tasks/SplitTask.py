import threading

import services.os.Operations as os
import services.pipelines.Task as Task
import services.modifiers.Loader as loader

import pandas as pd

class SplitTask(Task.Task):
    def __init__(self, readings):
        self.data_readings = readings

    def exec(self, task_input, task_output):
        task_output["readings"] = self.data_readings

        resources = os.dir_res_list(task_output["res_loc"])

        for res_elem in resources:
            res_path = os.path_join(task_output["res_loc"], res_elem)

            if not os.is_path_file(res_path):
                continue
            
            target_split_folder = os.path_join(task_output["res_loc"], res_elem[:-4])
            os.makedirs(target_split_folder, True)

            self._split_training_data(res_path, res_elem, target_split_folder)
    
    def _split_training_data(self, res_path, res_elem, target_split_folder):
        to_wait = []
            
        with open(res_path) as file:
            headders_splitted = file.readline().split(',')
            headder_three = headders_splitted[2].split('\n')[0]
            
            temp_read_line = file.readline()
            split_index = 1

            while temp_read_line != "":
                data =  {
                    headders_splitted[0]:[],
                    headders_splitted[1]:[],
                    headder_three:[]
                }

                for _ in range(0, self.data_readings):
                    temp_read_line = file.readline()
                    temp_splitted = temp_read_line.split(",")

                    if temp_read_line != "":
                        data[headders_splitted[0]].append(int(temp_splitted[0]))
                        data[headders_splitted[1]].append(int(temp_splitted[1]))
                        data[headder_three].append(int(temp_splitted[2].split("\\")[0]))

                data = pd.DataFrame(data)

                to_wait.append(self._process(data, self.data_readings, res_elem, target_split_folder, split_index))

                split_index += 1
        
        for t in to_wait:
            t.join()
        
    def _process(self, data, readings, res_name, target_loc, split_index):
        _, ecg, _ = self._split_headder_data(data)
        readings_index = 0

        end_index = readings_index + readings

        t = save_split_data(ecg, readings_index, end_index, target_loc, split_index, f"ecg_{readings}")

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