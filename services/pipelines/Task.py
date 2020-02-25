from abc import ABCMeta

class Task(ABCMeta):
    @classmethod
    def exec(self, action):
        pass

    @classmethod
    def revese(self, action):
        pass