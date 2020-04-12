import services.pipelines.Task as task

import services.os.Operations as os

import services.readers.JsonReaders as jReader

class PrepLabelsTask(task.Task):
    def exec(self, task_input, task_output):
        target_labels_loc = task_input["labels_loc"]

        #TODO - make sure folder exists
        os.makedirs(target_labels_loc, True)
        #TODO - join taining folder with name of label file
        target_labels_loc = os.path_join(target_labels_loc, "labels.csv")

        data_labels_mappings = jReader.parse_data(task_input["data_labels_mappings"])

        self.create_labels_file(target_labels_loc, data_labels_mappings)

    def reverse(self, task_input, task_output):
        pass

    def create_labels_file(self, target_resource_location, mappings):
        with open(target_resource_location, 'w') as labels:
            labels.write("sinus,af\n")

            for mapping_elem in mappings["mappings"]:
                to_write = ""

                medical_condition = mapping_elem["medical_condition"]

                if medical_condition == "Sinusrytme":
                    to_write = "1,0"
                elif medical_condition == "Artrieflimren":
                    to_write = "0,1"

                to_write = f"{to_write}\n"

                labels.write(to_write)