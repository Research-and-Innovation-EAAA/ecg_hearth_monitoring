import threading

import services.pipelines.Task as task

import services.os.Operations as os

class DataPrepTask(task.Task):
    def exec(self, task_input, task_output):
        path = task_output["res_loc"]

        path = os.path_join(path, "apple_health_export", "electrocardiograms")

        resources = os.dir_res_list(path)

        workers = []

        for elem in resources:
            res_path = os.path_join(path, elem)

            if os.is_path_file(res_path):
                splitted_elem = elem.split('.')
                
                backup_name = f"{splitted_elem[0]}.bak"
                backup_path = os.path_join(path, backup_name)

                worker = DataPreparerWorker(res_path, backup_name, backup_path)

                worker.start()

                workers.append(worker)

        for worker in workers:
            worker.join()
        
        task_output["res_loc"]

    def reverse(self, task_input, task_output):
        pass

class DataPreparerWorker(threading.Thread):
    def __init__(self, path, backup_name, backup_path):
        threading.Thread.__init__(self)

        self.res_path = path
        self.backup_name = backup_name
        self.backup_path = backup_path
    
    def run(self):
        os.copy_file(self.res_path, self.backup_name)

        with open(self.res_path, 'w') as data_file:
            with open(self.backup_path) as backup:
                data = backup.read()

            splitted_data = data.split("\n")

            data_file.write("readings\n")

            for elem in splitted_data:
                try:
                    reading = int(elem)

                    data_file.write(f"{reading}\n")
                except Exception as e:
                    print(e)