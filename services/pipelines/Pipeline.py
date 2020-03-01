import threading

class Pipeline:
    def __init__(self, tasks):
        self.tasks = tasks

    def execute(self, to_process):
        _pipeline = _Pipeline(self.tasks, to_process)

        _pipeline.start()

class _Pipeline(threading.Thread):
    def __init__(self, tasks, to_process):
        threading.Thread.__init__(self)

        self.tasks = tasks
        self.to_process = to_process

    def run(self):
        tasks_performed = []

        output = {
            "res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr",
            "readings": 7500,
            "training_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\nsr_training.csv"
        }

        try:
            for task in self.tasks:
                task.exec(self.to_process, output)

                #tasks_performed.push(task)
        except Exception as e:
            print(e)
            self._unravel_(tasks_performed, output)
        
    def _unravel_(self, tasks, output):
        print("Does nothing")