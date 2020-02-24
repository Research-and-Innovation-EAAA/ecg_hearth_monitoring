import os
import threading
import math
import datetime

import services.modifiers.Loader as loader
import services.modifiers.Writer as writer

class Split_data(threading.Thread):
    def __init__(self, target_resources_folder, readings,):
        threading.Thread.__init__(self)

        self.target_resources_folder = target_resources_folder
        self.readings = readings

    def run(self):
        resources = os.listdir(self.target_resources_folder)

        for elem in resources:
            print(elem)
            res_path = os.path.join(self.target_resources_folder, elem)

            if not os.path.isfile(res_path):
                continue
            
            res_data = loader.load_data(res_path)

            target_split_folder = os.path.join(self.target_resources_folder, elem[:-4])
            os.makedirs(target_split_folder, exist_ok=True)

            self.__process(res_data, self.readings, elem, target_split_folder)

    def __process(self, data, readings, res_name, target_loc):
        sample_nr, ecg, other = self.__split(data)
        split_index = 0
        readings_index = 0

        time_start = datetime.datetime.now().time()
        
        to_wait = []

        while readings_index < len(sample_nr):
            end_index = readings_index + readings + 1

            target_folder = target_loc#os.path.join(target_loc, res_name)

            #self.__save(ecg, readings_index, end_index, target_folder, split_index, "ecg")
            #self.__save(other, readings_index, end_index, target_folder, split_index, "other")
            
            t = save_split_data(ecg, readings_index, end_index, target_folder, split_index, "ecg")

            t.start()
            to_wait.append(t)
            
            t = save_split_data(other, readings_index, end_index, target_folder, split_index, "other")

            t.start()
            to_wait.append(t)
            
            split_index += 1
            readings_index += readings + 1

        for t in to_wait:
            t.join()
        
        time_end = datetime.datetime.now().time()

        print(time_start)
        print(time_end)
    
    def __split(self, data):
        try:
            sample_nr = data.drop(columns=['ECG', 'RESP'], axis=1)
            ecg = data.drop(['ECG', 'sample #'], axis=1)
            other = data.drop(['RESP', 'sample #'], axis=1)
        except Exception:
            pass

        try:
            sample_nr = data.drop(columns=['ECG 1', 'ECG 2'], axis=1)
            ecg = data.drop(['ECG 2', 'sample #'], axis=1)
            other = data.drop(['ECG 1', 'sample #'], axis=1)
        except Exception:
            pass

        return sample_nr, ecg, other

    def __save(self, data, start_index, end_index, target_folder, index, name):
        with open(f"{target_folder}\\{name}_split_{index}.csv", 'w') as first_lead:
            first_lead.write("readings\n")

            for elem in data.values[start_index: end_index]:
                first_lead.write(f"{elem[0]}\n")

    def __dir_prep(self, target_loc):
        os.makedirs(target_loc, exist_ok=True)

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
        with open(f"{self.target_folder}\\{self.name}_split_{self.index}.csv", 'w') as first_lead:
            first_lead.write("readings\n")

            for elem in self.data.values[self.start_index: self.end_index]:
                first_lead.write(f"{elem[0]}\n")