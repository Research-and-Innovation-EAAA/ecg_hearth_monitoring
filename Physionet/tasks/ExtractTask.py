import services.pipelines.Task as Task
import services.modifiers.Extractor as extractor

class ExtractTask(Task.Task):
    def exec(self, task_input, task_output):
        compressed_res_loc = task_input["comp_res_loc"]
        extract_loc = task_input["ext_loc"]
        override_policy = task_input["override_policy"]

        task_output["res_loc"] = extract_loc

        extractor.extract(compressed_res_loc, extract_loc, override_policy)

    def reverse(self, task_input, task_output):
        print("Does nothing")