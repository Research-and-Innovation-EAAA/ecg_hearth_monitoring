import threading
import datetime

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

        output = {}

        print(self.to_process["name"], "starting at", datetime.datetime.now().time())

        try:
            for task in self.tasks:
                print(task)
                task.exec(self.to_process, output)

                tasks_performed.insert(0, task)
        except Exception as e:
            print(e)
            self._unravel_(tasks_performed, output)
        
        print(self.to_process["name"], "ending at", datetime.datetime.now().time())
        
    def _unravel_(self, tasks, output):
        print("Does nothing")
        pass