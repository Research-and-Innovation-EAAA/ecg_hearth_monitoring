import services.modifiers.Loader as loader
import services.pipelines.Task as task
import services.os.Operations as os

class NormalizeFantasiaTask(task.Task):
    def exec(self, task_input, task_output):
        res_name = task_output["res_loc"].split("\\")

        if res_name[-1] != "fantasia":
            return

        ressources = os.dir_res_list(task_output["res_loc"])

        self._normalize_elements(ressources, task_output)
    
    def _normalize_elements(self, res_elems, task_output):
        for res in res_elems:
            if "f1" not in res: #or res[:-4] != '.csv':
                continue
                
            data = loader.load_data(os.path_join(task_output["res_loc"], res))

            with open(os.path_join(task_output["res_loc"], res), 'w') as dfile:
                for elem in data.values:
                    off_value = 0

                    if elem[2] < 16000:
                        off_value = 15000
                    elif elem[2] < 17000:
                        off_value = 16000
                    elif elem[2] < 18000:
                        off_value = 17000
                    elif elem[2] < 19000:
                        off_value = 18000
                    else:
                        off_value = 19000

                    temp_d_elem = elem[2] - off_value

                    dfile.write(f"{elem[0]},{elem[1]},{temp_d_elem}\n")
    
    def reverse(self, task_input, task_output):
        return super().reverse(task_input, task_output)