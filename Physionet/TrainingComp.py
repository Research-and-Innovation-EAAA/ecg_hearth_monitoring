import os
import threading

import services.modifiers.Loader as loader

class TrainingData(threading.Thread):
    def __init__(self, training_loc, data_folder, ml_inputs):
        threading.Thread.__init__(self)
        
        self.training_data = training_loc

        self.ressource_folders = data_folder

        self.ml_inputs = ml_inputs

    def run(self):
        ressources = os.listdir(self.ressource_folders)

        with open(self.training_data, 'w') as training:
            self.__apply_headders(training, 7501)

            for split_folder in ressources:
                temp_res_path = os.path.join(self.ressource_folders, split_folder) 

                if os.path.isfile(temp_res_path) and not os.path.isdir(temp_res_path):
                    continue
                
                print(split_folder)

                self.append_training_set(training, temp_res_path)

    def __apply_headders(self, file, headders):
        for elem in range(0, headders):
            file.write(f"x_{elem}")

            if elem < (headders + 1):
                file.write(',')

    def append_training_set(self, file, path):
        ressources = os.listdir(path)

        for res_elem in ressources:
            if not res_elem.find('ecg'):
                continue

            res_path = os.path.join(path, res_elem)

            temp_data = loader.load_data(res_path)

            if len(temp_data.values) < self.ml_inputs:
                continue

            index = 1

            file.write("\n")

            for res_elem in temp_data.values:
                file.write(f"{res_elem[0]}")

                if index < len(temp_data.values):
                    file.write(',')
                
                index += 1