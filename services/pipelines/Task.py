import abc

class Task(abc.ABC):
    @abc.abstractmethod
    def exec(self, task_input, task_output):
        pass

    @abc.abstractmethod
    def reverse(self, task_input, task_output):
        pass