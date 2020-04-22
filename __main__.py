import Physionet.DataProcessor as pdp
import Physionet.TrainingConcatPipeline as tcp

import AppleWatch.Pipeline as applePipe

import Physionet.ML_sets.Pipeline as training_pipeline

import ML.Pipeline as clad

if __name__ == '__main__':
    target_frequency = 510
    #readings = 7500
    readings = 13361
    training_split = 0.8
    test_split = 0.2

    pipeline = pdp.setup_pipeline(readings, training_split, test_split)

    pre_processers = []

    to_process = {
        "comp_res_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltafdb.tar",
        "ext_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "name":"LTAF",
        "target_label": 1,
        "sampled_frequency":128,
        "target_frequency": target_frequency
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsrdb.tar",
        "ext_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True,
        "name":"NSR",
        "target_label": 0,
        "sampled_frequency":128,
        "target_frequency": target_frequency
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia.tar",
        "ext_loc":"G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
        "name":"Fantasia",
        "target_label": 0,
        "sampled_frequency":250,
        "target_frequency": target_frequency
    }

    pre_processers.append(pipeline.execute(to_process))

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


    training_pipe = training_pipeline.setup()

    to_process = {
        "nsr_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\nsr.csv",
        "fantasia_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\fantasia.csv",
        "ltaf_loc":"G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\ltaf.csv",
        "name": "Physionet training sets preparations",
        "training_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training.csv",
        "labels_loc":"G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training_labels.csv",
        "fantasia_test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\fantasia_test.csv",
        "nsr_test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\nsr_test.csv",
        "ltaf_test_loc":"G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\ltaf_test.csv",
        "labels_test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test_labels.csv",
        "test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test.csv"
    }

    worker = training_pipe.execute(to_process)

    worker.join()
    
    to_process = {
        "name":"Load ML data",
        "training_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training.csv",
        "training_labels_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training_labels.csv",
        "test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test.csv",
        "test_labels_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test_labels.csv",
        "model_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\model.hdf5",
        "log": True,
        "inputs": 13361,
        "epochs": 5,
        "sass": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99],
        "optimizer": "adam",
        "loss":"mse",
        "verbose":1,
        "model_override": False
    }

    pipeline = clad.setup()

    t = pipeline.execute(to_process)

    t.join()