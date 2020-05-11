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

                worker = DataPreparerWorker(res_path, backup_name)

                worker.start()

                workers.append(worker)

        for worker in workers:
            worker.join()
        
        task_output["res_loc"] = path
        
    def reverse(self, task_input, task_output):
        pass

class DataPreparerWorker(threading.Thread):
    def __init__(self, path, backup_name):
        threading.Thread.__init__(self)

        self.res_path = path
        self.backup_name = backup_name
    
    def run(self):
        backup_path = os.copy_file(self.res_path, self.backup_name)

        with open(self.res_path, 'w') as data_file:
            with open(backup_path) as backup:
                data = backup.read()

            splitted_data = data.split("\n")

            data_file.write("readings\n")

            index = 0

            for elem in splitted_data:
                try:
                    reading = self.get_reading_value(elem)

                    if reading != None:
                        data_file.write(f"{reading}\n")
                        index += 1
                except:
                    pass

            print(f"\n{len(splitted_data)} - index: {index}\n")
        
        os.remove_file(backup_path)
    
    def get_reading_value(self, element):
        try:
            return float(element)
        except:
            pass
        
        splitted_elem = element.split(',')

        if len(splitted_elem) == 2:
            try:
                integer_split = int(splitted_elem[0])
                floating_points_split = int(splitted_elem[1])

                integer_value = float(f"{integer_split}.{floating_points_split}")
            except Exception as e:
                raise Exception(e)
        
            return integer_value
        
        return None