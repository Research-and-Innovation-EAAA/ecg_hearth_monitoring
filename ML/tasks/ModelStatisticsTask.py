import services.pipelines.Task as task

import matplotlib.pyplot as plt

class ModelStatisticsTask(task.Task):
    def exec(self, task_input, task_output):
        model_training_history = task_output["training_history"]

        for epoch in range(0, task_input["epochs"]):
            sensitivity, specificity = [], []

            temp = model_training_history.history

            for key_elem in model_training_history.history.keys():
                if key_elem == "loss":
                    continue
                
                if key_elem.find("sensitivity_at_") >= 0:
                    sensitivity.append(temp[key_elem][epoch])
                elif("specificity_at_"):
                    specificity.append(temp[key_elem][epoch])
            
            fig, (ax1, ax2) = plt.subplots(2)
            
            ax1.plot(task_input["sass"], sensitivity)
            ax1.set(xlabel="Specificity", ylabel="Sensitivity")

            ax2.plot(task_input["sass"], specificity)
            ax2.set(xlabel="Sensitivity", ylabel="Specificity")

            fig.savefig(f"G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\plots\\{epoch}_plot.png")
        
        with open(f"G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\plots\\data.txt", 'w') as to_save:
            temp = model_training_history.history

            for key_elem in temp.keys():
                to_save.write(f"{key_elem}\n")

                for elem in temp[key_elem]:
                    to_save.write(f"\t{elem}")
                
                to_save.write("\n")
            

            to_save.write(f"Evaluation loss\n\t{task_output['eva_loss']}\n")
            to_save.write(f"Evaluation matrics\n")

            for elem in task_output["eva_metrics"]:
                to_save.write(f"{elem}\n")

    def reverse(self, task_input, task_output):
        pass