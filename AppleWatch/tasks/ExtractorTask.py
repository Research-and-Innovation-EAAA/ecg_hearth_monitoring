import services.pipelines.Task as task

import services.modifiers.Extractor as ext
import services.os.Operations as os

class ExtractorTask(task.Task):
    def exec(self, task_input, task_output):
        compressed_ressource_loc = task_input["comp_loc"]

        target_extract_loc = self.extract_loc(compressed_ressource_loc)

        try:
            ext.extract(compressed_ressource_loc, target_extract_loc, True)
        except Exception as e:
            print(e)
            raise Exception(e)

        task_output["res_loc"] = target_extract_loc

    def reverse(self, task_input, task_output):
        pass

    def extract_loc(self, compressed_resource):
        splitted_path = compressed_resource.split(os.get_path_seperator())

        index = 0

        path = ""

        while index < (len(splitted_path) - 1):
            path = os.path_join(path, splitted_path[index])

            index += 1
        
        splitted_resource_name = splitted_path[len(splitted_path) - 1].split('.')

        return os.path_join(path, splitted_resource_name[0])