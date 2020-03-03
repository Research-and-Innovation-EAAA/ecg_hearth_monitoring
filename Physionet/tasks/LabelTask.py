import services.Pipeline as pl
import services.os.Operations as os

class LabelTask(pl.Pipeline):
    def execute(self, task_input, task_output):
        training_loc, training_labels_loc = self._calc_labels_loc(task_output["trainin_loc"])
        test_loc, test_labels_loc = self._calc_labels_loc(task_output["training_test_loc"])

        self._create_labels_file(training_labels_loc, trainin_loc)

        self._create_labels_file(test_labels_loc, test_loc)
    
    def reverse(self, task_input, task_output):
        pass
    
    def _calc_labels_loc(path):
        splitted = path.split("\\")

        path = ""

        for path_elem in range(0, len(splitted) - 1):
            os.path_join(path, path_elem)

        path_name = f"{splitted[len(splitted) - 1][:-4]}_labels.csv"

        return path, os.path_join(path, path_name)
    
    def _create_labels_file(self, label_loc, datasets_loc):
        with open(labels_loc, 'w') as labels:
            labels.write("target")

            with open(datasets_loc) as data_sets:
                data_sets.readline()
                data_set = data_sets.readline()

                while(data_set != ""):
                    labels.write(f"{task_input["target_label"]}")