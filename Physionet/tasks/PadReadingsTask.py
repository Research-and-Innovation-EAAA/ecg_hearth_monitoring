import math

import services.pipelines.Task as task
import services.os.Operations as os

class PadReadingsTask(task.Task):
    def exec(self, task_input, task_output):
        sampling_frequency = task_input["sampled_frequency"]
        target_frequency = task_input["target_frequency"]

        doubling_rate = math.ceil(sampling_frequency / (((target_frequency / sampling_frequency) - 1) * sampling_frequency))

        res_elems = os.dir_res_list(task_output["res_loc"])

        for res_elem in res_elems:
            origin_path = os.path_join(task_output["res_loc"], res_elem)
            backup_path = os.copy_file(origin_path, f"{task_input['name']}_bakup.bak")

            with open(origin_path, 'w') as file:
                with open(backup_path) as backup_file:
                    temp_reading = backup_file.readline()

                    sampling_nr = 1

                    while temp_reading != "":
                        for _ in range(1, doubling_rate):
                            temp_reading = backup_file.readline()

                            if temp_reading != "":
                                splitted = temp_reading.split(',')

                                file.write(f"{sampling_nr},{splitted[1]},{splitted[2]}")

                            sampling_nr += 1
                        
                        if temp_reading != "":
                            splitted = temp_reading.split(',')
                            file.write(f"{sampling_nr},{splitted[1]},{splitted[2]}")
                            sampling_nr += 1
                            splitted = temp_reading.split(',')
                            file.write(f"{sampling_nr},{splitted[1]},{splitted[2]}")
                            sampling_nr += 1
                        
                        temp_reading = backup_file.readline()
        
            os.remove_file(backup_path)

    def reverse(self, task_input, task_output):
        return super().reverse(task_input, task_output)