import random

import services.pipelines.Task as task
import services.modifiers.Loader as loader
import services.modifiers.Writer as writer
import services.os.Operations as os

class SplitTestTask(task.Task):
    def __init__(self, split_rate_train, split_rate_test):
        self.split_rate_train = split_rate_train
        self.split_rate_test = split_rate_test

    def exec(self, task_input, task_output):
        max_index = self._sample_indexes(task_output["training_loc"])

        test_samples = self._calc_test_samples(max_index)

        training_indexes = self._random_test_indexes(test_samples, max_index)

        training_indexes.sort()

        path = task_output["training_loc"][:-4]
        
        training_test_set_path = f"{path}_test.csv"

        self._save_test_samples(task_output["training_loc"], training_test_set_path, task_output["readings"], training_indexes)

        self._save_training_samples(task_output["training_loc"], training_indexes)

        task_output["training_test_loc"] = training_test_set_path
    
    def reverse(self, task_input, task_output):
        return super().reverse(task_input, task_output)
    
    def _sample_indexes(self, path):
        with open(path) as file:
            read_line = file.readline()

            indexes = -1

            while read_line != "":
                indexes += 1

                read_line = file.readline()
            
            return indexes

    def _calc_test_samples(self, datasets):
        return datasets * self.split_rate_test
    
    def _random_test_indexes(self, sample_numbers, datasets):
        test_indexes = []

        while len(test_indexes) < sample_numbers:
            temp_index = random.randrange(0, datasets)

            if temp_index not in test_indexes:
                test_indexes.append(temp_index) 

        return test_indexes  

    def _save_test_samples(self, training_path, test_path, readings, indexes):
        with open(training_path) as training_file:
            with open(test_path, 'w') as test_file:
                for x in range(0, readings):
                    test_file.write(f"x_{x}")
                    if x < readings - 1:
                        test_file.write(',')

                test_file.write("\n")

                read_line = training_file.readline()
                index_at = 0
                for index in indexes:
                    for _ in range(index_at, index + 1):
                        read_line = training_file.readline()
                    
                        index_at += 1

                    test_file.write(read_line)
    
    def _save_training_samples(self, rec_loc, indexes):
        print(rec_loc)
        copied_file = os.copy_file(rec_loc, "temp.bak")

        index = 0

        with open(copied_file) as training_copy:
            with open(rec_loc, 'w') as training:
                training.write(training_copy.readline())

                for elem in indexes:
                    for _ in range(index, elem):
                        index += 1

                        training.write(training_copy.readline())
                    
                    training_copy.readline()
                    index += 1
        
        os.remove_file(copied_file)