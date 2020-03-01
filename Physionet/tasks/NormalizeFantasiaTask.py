import services.modifiers.Loader as loader
import services.pipelines.Task as task
import services.os.Operations as os

class NormalizeFantasiaTask(task.Task):
    def exec(self, task_input, task_output):
        ressources = os.dir_res_list(task_output["res_loc"])

        for res in ressources:
            if "f2" in res:
                continue
                
            data = loader.load_data(os.path_join(task_output["res_loc"], res))

            with open(task_output["res_loc"]) as dfile:
                for elem in data.values:
                    off_value = 0

                    if elem < 16000:
                        off_value = 15000
                    elif elem < 17000:
                        off_value = 16000
                    elif elem < 18000:
                        off_value = 17000
                    elif elem < 19000:
                        off_value = 18000
                    else:
                        off_value = 19000

                    temp_d_elem = elem - off_value

                    dfile.write(temp_d_elem)
    
    def reverse(self, task_input, task_output):
        return super().reverse(task_input, task_output)