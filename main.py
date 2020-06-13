import Physionet.DataProcessor as pdp
import Physionet.TrainingConcatPipeline as tcp

import os

if __name__ == "__main__":
    #path = "G:\\Praktik Vinter-Forår 2020\\resources\\apple_watch\\eksport\\apple_health_export\\electrocardiograms"
    #path = "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf"
    path = "c:\\tmp"

    res_dir = os.listdir(path)
    
    min = float(999999999)
    max = float(-999999999)
    
    for elem in res_dir:
        print(elem)
        temp = os.path.join(path, elem)

        with open(temp) as file:
            file.readline()

            reading = file.readline()

            while reading != "":
                reading = reading.split(',')[-1]

                try:
                    if float(reading) < min:
                        min = float(reading)
                    if float(reading) > max:
                        max = float(reading)
                except Exception as e:
                    pass

                reading = file.readline()

        print(min)
        print(max)

    """
    pipeline = pdp.setup_pipeline(7500, 0.8, 0.2)

    pre_processers = []

    to_process = {
        "comp_res_loc": "/data/machinelearning/data/ltafdb.tar",
        "ext_loc": "/data/machinelearning/data/ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "name":"LTAF",
        "target_label": 1,
        "sampled_frequency":128,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "/data/machinelearning/data/nsrdb.tar",
        "ext_loc": "/data/machinelearning/data/nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True,
        "name":"NSR",
        "target_label": 0,
        "sampled_frequency":128,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "/data/machinelearning/data/fantasia.tar",
        "ext_loc":"/data/machinelearning/data/fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
        "name":"Fantasia",
        "target_label": 0,
        "sampled_frequency":250,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    for pre_proces_elem in pre_processers:
        pre_proces_elem.join()
        """