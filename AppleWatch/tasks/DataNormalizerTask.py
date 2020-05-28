import services.pipelines.Task as task

import services.os.Operations as os

import threading

class DataNormalizerTask(task.Task):
    def exec(self, task_input, task_output):
        resources = os.dir_res_list(task_output["res_loc"])

        workers = []

        for resource in resources:
            worker = DataNormalizer(task_output["res_loc"], resource)

            worker.start()

            workers.append(worker)
        
        for worker in workers:
            worker.join()

    def reverse(self, task_input, task_output):
        pass

class DataNormalizer(threading.Thread):
    def __init__(self, path, resource):
        threading.Thread.__init__(self)

        self.path = path
        self.resource = resource

    def run(self):
        file_to_backup = os.path_join(self.path, self.resource)
        backup_name = f"{self.resource.split('.')[0]}.bak"

        backup_path = os.copy_file(file_to_backup, backup_name)

        with open(os.path_join(self.path, self.resource), 'w') as datafile:
            with open(backup_path) as data:
                datafile.write(data.readline())

                temp = datafile.readline()

                while temp != "":
                    normalized_reading = self.data_reading_normalizer(data.readline())

                    datafile.writeline(normalized_reading)

                    temp = data.readline()

    def data_reading_normalizer(self, reading):
        reading_value = float(reading.split('\n')[0])

        while reading_value > 100.0:
            reading_value = reading_value - 100

        return f"{reading_value}"