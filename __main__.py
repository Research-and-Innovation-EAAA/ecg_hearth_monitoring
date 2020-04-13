import Physionet.DataProcessor as pdp
import Physionet.TrainingConcatPipeline as tcp

import AppleWatch.Pipeline as applePipe

#import ML.Pipeline as clad

if __name__ == '__main__':
    target_frequency = 510
    #readings = 7500
    readings = 13361
    training_split = 0.8
    test_split = 0.2

    pipeline = pdp.setup_pipeline(readings, training_split, test_split)

    pre_processers = []

    to_process = {
        "comp_res_loc": "G:\\Praktik Vinter-Forår\\resources\\ltafdb.tar",
        "ext_loc": "G:\\Praktik Vinter-Forår\\resources\\ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "name":"LTAF",
        "target_label": 1,
        "sampled_frequency":128,
        "target_frequency": target_frequency
    }

    #pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "G:\\Praktik Vinter-Forår\\resources\\nsrdb.tar",
        "ext_loc": "G:\\Praktik Vinter-Forår\\resources\\nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True,
        "name":"NSR",
        "target_label": 0,
        "sampled_frequency":128,
        "target_frequency": target_frequency
    }

    #pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "G:\\Praktik Vinter-Forår\\resources\\fantasia.tar",
        "ext_loc":"G:\\Praktik Vinter-Forår\\resources\\fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
        "name":"Fantasia",
        "target_label": 0,
        "sampled_frequency":250,
        "target_frequency": target_frequency
    }

    #pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\apple_watch\\eksport.zip",
        "training_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\apple_watch\\training",
        "name": "Apple Watch data preprocessing",
        "labels_information_location": "F:\\Praktik EAAA\\ecg_hearth_monitoring\\resources\\mappings.json",
        "readings": readings
    }

    apple_process = applePipe.setup()

    pre_processers.append(apple_process.execute(to_process))

    for pre_proces_elem in pre_processers:
        pre_proces_elem.join()
    
    to_process = {
        "name":"Load ML data",
        "training_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training.csv",
        "training_labels_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training_labels.csv",
        "test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test.csv",
        "test_labels_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test_labels.csv",
        "model_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\model",
        "log": True,
        "inputs": 7500,
        "epochs": 5,
        "sass": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99],
        "optimizer": "adam",
        "loss":"mse",
        "verbose":0
    }

    #pipeline = clad.setup()

    #t = pipeline.execute(to_process)

    #t.join()