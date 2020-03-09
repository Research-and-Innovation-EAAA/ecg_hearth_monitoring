import math
import threading

import services.pipelines.Task as task
import services.os.Operations as os

class ConcatTrainTask(task.Task):
    def exec(self, task_input, task_output):
        threads = []

        #TODO - need to refactor to use runtime inputs instead of hardcoded values
        threads.append(self._spawn_worker(task_input, "training.csv", "fantasia.csv", "nsr.csv", "ltaf.csv"))
        threads.append(self._spawn_worker(task_input, "training_labels.csv", "fantasia_labels.csv", "nsr_labels.csv", "ltaf_labels.csv"))
        threads.append(self._spawn_worker(task_input, "test.csv", "fantasia_test.csv", "nsr_test.csv", "ltaf_test.csv"))
        threads.append(self._spawn_worker(task_input, "test_labels.csv", "fantasia_test_labels.csv", "nsr_test_labels.csv", "ltaf_test_labels.csv"))

        for td in threads:
            td.join()
    
    def _spawn_worker(self, task_input, name, *args):
        concat_train_path = os.path_join(task_input["training"], name)
        
        t = _Concatter(fantasia=args[0], nsr=args[1], ltaf=args[2], 
                        training=task_input["training"], 
                        path=concat_train_path, 
                        concat_rate=task_input["concat_rate"])
        
        t.start()
        
        return t

    def reverse(self, task_input, task_output):
        return super().reverse(task_input, task_output)

class _Concatter(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)

        self.fantasia = os.path_join(kwargs["training"], kwargs["fantasia"])
        self.nsr = os.path_join(kwargs["training"], kwargs["nsr"])
        self.ltaf = os.path_join(kwargs["training"], kwargs["ltaf"])

        self.path = kwargs["path"]
        self.concat_rate = kwargs["concat_rate"]

    def _count(self, path):
        counter = 0

        with open(path) as path_file:
            temp = path_file.readline()

            while temp != "":
                temp = path_file.readline()

                if temp != "":
                    counter += 1
        
        return counter
    
    def run(self):
        fantasia_counter = self._count(self.fantasia)
        nsr_counter = self._count(self.nsr)
        ltaf_counter = self._count(self.ltaf)
        
        with open(self.path, 'w') as res_file:
            fantasia = open(self.fantasia)
            nsr = open(self.nsr)
            ltaf = open(self.ltaf)

            fantasia_temp = fantasia.readline()
            nsr_temp = nsr.readline()
            ltaf_temp = ltaf.readline()

            res_file.write(fantasia_temp)

            ltaf_read_rate = (ltaf_counter // (fantasia_counter + nsr_counter)) - 1
            ltaf_counter = fantasia_counter + nsr_counter

            while fantasia_temp != "" and nsr_temp != "" and ltaf_temp != "":
                fantasia_temp = self._write_data(res_file, fantasia, fantasia_counter, self.concat_rate, False)
                nsr_temp = self._write_data(res_file, nsr, nsr_counter, self.concat_rate, False)
                ltaf_temp = self._write_data(res_file, ltaf, ltaf_counter, self.concat_rate, True, ltaf_read_rate)

            while fantasia_temp != "" and ltaf_temp != "":
                fantasia_temp = self._write_data(res_file, fantasia, fantasia_counter, self.concat_rate, False)
                ltaf_temp = self._write_data(res_file, ltaf, ltaf_counter, self.concat_rate, True, ltaf_read_rate)
            
            while nsr_temp != "" and ltaf_temp != "":
                nsr_temp = self._write_data(res_file, nsr, nsr_counter, self.concat_rate, False)
                ltaf_temp = self._write_data(res_file, ltaf, ltaf_counter, self.concat_rate, True, ltaf_read_rate)
            
            fantasia.close()
            nsr.close()
            ltaf.close()

            os.remove_file(self.fantasia)
            os.remove_file(self.nsr)
            os.remove_file(self.ltaf)
    
    def _write_data(self, write_file, read_file, counter, concat_rate, scale, read_rate = 0):
        for _ in range(0, math.floor(counter * concat_rate)):
            read_temp = read_file.readline()
            if read_temp != "":
                write_file.write(read_temp)

                if scale:
                    for _ in range(0, read_rate):
                        read_temp = read_file.readline()
        
        return read_temp