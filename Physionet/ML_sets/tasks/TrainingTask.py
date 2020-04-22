import services.pipelines.Task as task

class TrainingTask(task.Task):
    def exec(self, task_input, task_output):
        sinus_rythm_count = self.instances(task_input["fantasia_loc"]) + self.instances(task_input["nsr_loc"])

        af_rythm_count = self.instances(task_input["ltaf_loc"])

        ratio = af_rythm_count // sinus_rythm_count

        with open(task_input["training_loc"], 'w') as training_file:
            training_labels = open(task_input["labels_loc"], 'w')
            training_labels.write("sinus,af\n")

            nsr = open(task_input["nsr_loc"])
            fantasia = open(task_input["fantasia_loc"])
            ltaf =open(task_input["ltaf_loc"]) 

            training_file.write(ltaf.readline())
            
            nsr.readline()
            fantasia.readline()

            nsr_read = nsr.readline()
            fantasia_read = fantasia.readline()
            ltaf_read = ltaf.readline()

            while nsr_read != "" and ltaf_read != "" and fantasia_read != "":
                index_counter = 0

                while index_counter < 2000 and fantasia_read != "":
                    training_file.write(fantasia_read)
                    training_labels.write("1,0\n")

                    fantasia_read = fantasia.readline()

                    index_counter += 1

                index_ltaf = 0

                while index_ltaf < index_counter and ltaf_read != "":
                    training_file.write(ltaf_read)
                    training_labels.write("0,1\n")

                    for _ in range(0, (ratio - 1)):
                        ltaf.readline()

                    ltaf_read = ltaf.readline()
                    index_ltaf += 1
                
                index_nsr = 0

                while index_nsr < index_ltaf and nsr_read != "":
                    training_file.write(nsr_read)
                    training_labels.write("1,0\n")

                    nsr_read = nsr.readline()

                    index_nsr += 1
                
                index_ltaf = 0

                while index_ltaf < index_counter and ltaf_read != "":
                    training_file.write(ltaf_read)
                    training_labels.write("0,1\n")

                    for _ in range(0, (ratio - 1)):
                        ltaf.readline()

                    ltaf_read = ltaf.readline()
                    index_ltaf += 1
            
            while ltaf_read != "" and nsr_read != "":
                index_nsr = 0

                while index_nsr < 2000 and nsr_read != "":
                    training_file.write(nsr_read)
                    training_labels.write("1,0\n")

                    nsr_read = nsr.readline()

                    index_nsr += 1
                
                index_ltaf = 0

                while index_ltaf < index_nsr and ltaf_read != "":
                    training_file.write(ltaf_read)
                    training_labels.write("0,1\n")

                    for _ in range(0, (ratio - 1)):
                        ltaf.readline()

                    ltaf_read = ltaf.readline()
                    index_ltaf += 1

        nsr.close()
        fantasia.close()
        ltaf.close()
        training_labels.close()

    def reverse(self, task_input, task_output):
        pass

    def instances(self, path):
        count = 0

        with open(path) as data_file:
            data_set = data_file.readline()

            while data_set != "":
                count += 1

                data_set = data_file.readline()
        
        return count