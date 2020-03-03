import services.os.Operations as op
import services.pipelines.Task as task

class HeaddersTask(task.Task):
    def exec(self, task_input, task_output):
        self.headders = task_input["headders"]
        
        res_loc = task_output["res_loc"]

        folder_res = op.dir_res_list(res_loc)

        for folder_res_elem in folder_res:
            target_res = op.path_join(res_loc, folder_res_elem) 

            try:
                self._apply_headders(target_res)
            except Exception as e:
                print(e)

    def _apply_headders(self, res_path):
        with open(res_path) as file:
            data = file.read()

        with open(res_path, 'w') as write_file:
            args_index, headders = 0, ""

            for arg_elem in self.headders:
                headders = f"{headders}{arg_elem}"

                args_index += 1

                if args_index < len(self.headders):
                    headders = f"{headders},"
            
            write_file.write(f"{headders}\n")

            write_file.write(data)
    
    def reverse(self, task_input, task_output):
        print("Does nothing")