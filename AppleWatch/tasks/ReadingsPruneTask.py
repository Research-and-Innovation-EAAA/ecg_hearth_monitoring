import threading

import services.pipelines.Task as task

import services.os.Operations as os

class ReadingsPruneTask(task.Task):
    def exec(self, task_input, task_output):
        min_readings = self.get_min_readings(task_output["res_loc"])

        index = 0

        resources = os.dir_res_list(task_output["res_loc"])

        workers = []

        for elem in resources:
            path = os.path_join(task_output["res_loc"], elem)

            worker = NormalizeReadingsCountWorker(path, min_readings, index)

            worker.start()

            workers.append(worker)

            index += 1

        for worker in workers:
            worker.join()

    def reverse(self, task_input, task_output):
        pass

    def get_min_readings(self, path):
        resources = os.dir_res_list(path)

        readings = []

        for elem in resources:
            readings.append(self.count(os.path_join(resources, elem)))
        
        min_reading = readings[0]

        for elem in readings:
            if elem < min_reading:
                min_reading = elem

        return min_reading

    def count(self, path):
        count = 0

        with open(path) as data_file:
            data = data_file.read()

            splitted = data.split('\n')

            count = len(splitted) - 1
        
        return count
    
class NormalizeReadingsCountWorker(threading.Thread):
    def __init__(self, path, readings, backup_name_index):
        threading.Thread(self)

        self.readings = readings
        self.path = path
        self.backup_name_index = backup_name_index

    def run(self):
        path_split = self.path.split(os.get_path_seperator())

        backup_name = path_split[len(path_split) - 1]

        backup_name = backup_name.split('.')[0]

        backup = os.copy_file(self.path, f"{backup_name}{self.backup_name_index}.bak")

        with open(self.path, 'w') as data_file:
            with open(backup) as backup_file:
                data_file.write(backup_file.readline())

                data_reading = backup_file.readline()

                index = 0

                while index < self.readings and data_reading != "":
                    data_file.write(data_reading)

                    data_reading = backup_file.readline()

                    index += 1
        
        os.remove_file(backup)