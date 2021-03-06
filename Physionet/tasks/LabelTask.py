import services.pipelines.Task as task
import services.os.Operations as os

class LabelTask(task.Task):
    def exec(self, task_input, task_output):
        training_loc, training_labels_loc = self._calc_labels_loc(task_output["training_loc"])
        test_loc, test_labels_loc = self._calc_labels_loc(task_output["training_test_loc"])

        self._create_labels_file(training_labels_loc, training_loc, task_input['target_label'])

        self._create_labels_file(test_labels_loc, test_loc, task_input['target_label'])
    
    def reverse(self, task_input, task_output):
        print("Label task reverse  does nothing!")
    
    def _calc_labels_loc(self, path):
        splitted = path.split(os.get_path_seperator())

        label_path = f"{splitted[0]}{os.get_path_seperator()}{splitted[1]}"

        for path_elem in range(2, len(splitted) - 1):
            label_path = os.path_join(label_path, splitted[path_elem])

        path_name = f"{splitted[len(splitted) - 1][:-4]}_labels.csv"

        return path, os.path_join(label_path, path_name)
    
    def _create_labels_file(self, label_loc, datasets_loc, target_label):
        with open(label_loc, 'w') as labels:
            labels.write("target\n")

            with open(datasets_loc) as data_sets:
                data_sets.readline()
                data_set = data_sets.readline()

                while(data_set != ""):
                    labels.write(f"{target_label}")
                    data_set = data_sets.readline()

                    if data_set != "":
                        labels.write('\n')