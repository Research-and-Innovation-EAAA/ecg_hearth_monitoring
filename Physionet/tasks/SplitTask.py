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

        splitter_threads = []

        for elem in resources:
            res_path = os.path_join(task_output["res_loc"], elem)

            if not os.is_path_file(res_path):
                continue

            splitter = _Splitter(elem, res_path, self.data_readings)
            splitter.start()
            splitter_threads.append(splitter)

            if len(splitter_threads) > 5:
                for thread in splitter_threads:
                    thread.join()
                
                splitter_threads = []
        
        for thread in splitter_threads:
            thread.join()
    
    def reverse(self, task_input, task_output):
        return super().reverse(task_input, task_output)

class _Splitter(threading.Thread):
    def __init__(self, res_name, res_path, readings):
        threading.Thread.__init__(self)

        self.containing_folder = res_path
        self.res_name = res_name[:-4]
        self.res_path = res_path
        self.readings = readings
    
    def run(self):
        with open(self.res_path) as file:
            self._prep_split_folder()

            headers = self._prep_headers(file)

            self._split(file, headers)
    
    def _split(self, file, headers):
        temp_reading = file.readline()

        split_index = 1

        while temp_reading != "":
            index_at = 0
            
            readings = []

            while index_at < self.readings:
                if temp_reading != "":
                    readings.append(temp_reading)

                temp_reading = file.readline()
                
                index_at += 1
            
            split_path = os.path_join(self.containing_folder[:-3], f"{self.readings}_ecg_split_{split_index}.csv")

            split_thread = _Save_split(readings, headers, split_path)

            split_thread.start()

            split_index += 1

    def _prep_split_folder(self):
        os.makedirs(self.res_path[:-4], True)
    
    def _prep_headers(self, file):
        headers = file.readline().split(',')

        headers[2] = headers[2].split("\n")[0]

        return headers

class _Save_split(threading.Thread):
    def __init__(self, data, headers, split_path):
        threading.Thread.__init__(self)

        self.data = data
        self.headers = headers
        self.path = split_path

    def run(self):
        index = self._calc_header_index()
        ecg_data = self._prep_data(index)

        with open(self.path, 'w') as file:
            file.write("readings\n")

            for reading in ecg_data:
                file.write(f"{reading}\n")

    def _calc_header_index(self):
        self.headers[2].split("\n")[0]

        index = 0

        for header_elem in self.headers:
            if header_elem[:-2] == 'ECG' or header_elem == 'ECG':
                return index
            
            index += 1

    def _prep_data(self, index):
        data_readings = []

        for data_elem in self.data:
            data_split = data_elem.split(",")

            data_readings.append(data_split[index])
        
        return data_readings