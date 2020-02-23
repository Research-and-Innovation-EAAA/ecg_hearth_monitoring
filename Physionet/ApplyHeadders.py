import os
import threading

class Apply_headders(threading.Thread):
    def __init__(self, ressource_path, *args, daemon=False):
        super().__init__(daemon=daemon)

        self.res_path = ressource_path
        self.args = args
    
    def run(self):
        folder_res = os.listdir(self.res_path)

        for folder_res_elem in folder_res:
            target_res = f"{self.res_path}\\{folder_res_elem}"

            try:
                self.__apply_headders(target_res)
            except Exception:
                pass       

    def __apply_headders(self, res_path):
        if not (os.path.isfile(res_path) and res_path[-4:] == '.csv'): 
            raise Exception()

        with open(res_path) as file:
            self.data = file.read()

        with open(res_path, 'w') as write_file:
            args_index = 0

            for arg_elem in self.args:
                write_file.write(arg_elem)

                args_index += 1

                if args_index < len(self.args):
                    write_file.write(',')
            
            write_file.write("\n")

            write_file.write(self.data)