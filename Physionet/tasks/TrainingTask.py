import services.os.Operations as os
import services.pipelines.Task as Task
import services.modifiers.Loader as loader

class TrainingTask(Task.Task):
    def _setup(self, task_output):
        self.training_readings = task_output["readings"]
        
        ressources = os.dir_res_list(task_output["res_loc"])
        training_data = self._training_loc(task_output["res_loc"])

        task_output["training_loc"] = training_data

        backup = self._bakup_saved(training_data)

        return ressources, training_data, backup

    def exec(self, task_input, task_output):
        ressources, training_data, backup = self._setup(task_output)

        with open(training_data, 'w') as training:
            if os.is_path_file(backup):
                self._merge_training(training, backup)
            else:
                headders = self._get_headders(task_output["readings"])
                training.write(headders)

            for split_folder in ressources:
                split_dir = os.path_join(task_output["res_loc"], split_folder) 

                if os.is_path_file(split_dir) and not os.is_dir(split_dir):
                    continue
                
                self.append_training_set(training, split_dir, os.dir_res_list(split_dir))

                os.remove_dir(split_dir)
    
    def _merge_training(self, training, backup):
        with open(backup) as backup_training:
            temp = backup_training.readline()

            while temp != "":
                training.write(temp)
                temp = backup_training.readline()
        
        os.remove_file(backup)

    def _get_headders(self, readings):
        headders = ""

        for elem in range(1, readings):
            headders = f"{headders}x_{elem}"

            if elem < (readings):
                headders = f"{headders},"
        
        return f"{headders}\n"

    def append_training_set(self, file, path, ressources):
        for res_elem in ressources:
            training_data = ""
            
            if not self._is_ecg(res_elem):
                continue

            res_path = os.path_join(path, res_elem)

            temp_data = loader.load_data(res_path)

            if self._is_missing_inputs(len(temp_data.values)):
                os.remove_file(res_path)
                continue

            training_data = self._append_data_set(training_data, temp_data)
            file.write(training_data)

            os.remove_file(res_path)
    
    def _is_ecg(self, path):
        return path.find('ecg') >= 0
    
    def _is_missing_inputs(self, data_readings):
        return data_readings != self.training_readings
    
    def _append_data_set(self, data_string, data):
        index = 1

        for res_elem in data.values:
            data_string = f"{data_string}{res_elem[0]}"

            if index < len(data.values):
                data_string = f"{data_string},"
            
            index += 1
        
        return f"{data_string}\n"
    
    def reverse(self, task_input, task_output):
        print("Does nothing")
    
    def _training_loc(self, res_loc):
        path_split = res_loc.split("\\")

        training_path = f"{path_split[0]}\\{path_split[1]}"

        for x in range(2, len(path_split) - 1):
            training_path = os.path_join(training_path, path_split[x])

        training_path = os.path_join(training_path, "training")
        
        return os.path_join(training_path, f"{path_split[len(path_split) - 1]}.csv")

    def _bakup_saved(self, training_loc):
        if not os.is_path_file(training_loc):
            return
        
        return os.copy_file(training_loc, "temp.bak")