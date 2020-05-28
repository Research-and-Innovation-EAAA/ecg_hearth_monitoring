import services.pipelines.Task as task

import services.readers.JsonReaders as jReader
import services.os.Operations as os

class PrepTrainingSourcesTask(task.Task):
    def exec(self, task_input, task_output):
        labels_information_loc = task_input["labels_information_location"]
        resources_path = task_output["res_loc"]

        labels_info = jReader.parse_data(labels_information_loc)

        os.makedirs(task_input["training_loc"], True)

        resources = os.dir_res_list(resources_path)

        training_path = f"{task_input['training_loc']}{os.get_path_seperator()}training.csv"
        labels_path = f"{task_input['training_loc']}{os.get_path_seperator()}labels.csv"

        with open(training_path, 'w') as training_file:
            with open(labels_path, 'w') as labels_file: 
                labels_file.write("Sinus, AF\n")
                index = 0

                while index < task_input["readings"]:
                    training_file.write(f"x_{index}")
                    index += 1
                    if index < task_input["readings"]:
                        training_file.write(',')
                
                training_file.write("\n")

                self.prep_training_file(training_file, labels_file, labels_info, task_output["res_loc"], resources)

    def get_resource(self, resource_name, resources):
        resource = None

        index = 0

        while resource == None and index < len(resources):
            temp = resources[index]

            if resource_name == temp:
                resource = temp

            index += 1
        
        return resource

    def prep_training_file(self, training_writer, labels_writer, labels_info, resources_loc, resources):
        for label_info in labels_info["mappings"]:
            resource = self.get_resource(label_info["file_name"], resources)

            medical_condition = label_info["medical_condition"]

            if resource != None and (medical_condition == "Sinusrytme" or medical_condition == "Artrieflimren"):
                with open(os.path_join(resources_loc, resource)) as data_file:
                    data_file.readline()

                    reading = data_file.readline()

                    while reading != "":
                        splitted_reading = reading.split("\n")

                        training_writer.write(splitted_reading[0])
                    
                        reading = data_file.readline()

                        if reading != "":
                            training_writer.write(',')
                
                training_writer.write("\n")
                
                if medical_condition == "Sinusrytme":
                    labels_writer.write("1,0\n")
                elif medical_condition == "Artrieflimren":
                    labels_writer.write("0,1\n")
    
    def reverse(self, task_input, task_output):
        pass