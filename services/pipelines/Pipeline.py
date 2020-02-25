class abs Pipeline():
    def __init_(self, tasks):
        self.tasks = tasks

    def execute(action):
        tasks_performed = []

        try:
            for task in self.tasks:
                task.exec(action)
        except Exception:
            __unravel__(action, tasks_performed)

    def __unravel__(action, tasks):
        pass