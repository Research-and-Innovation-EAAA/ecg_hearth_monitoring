import os
import numpy as np

import services.modifiers.Extractor as extract
import services.preprocessors.DataPrune as dp
import services.modifiers.Loader as loader
import services.preprocessors.TrainingPreparer as tp
import services.displayers.Graph as display

import ML.Activity_ml as aml

comp_res_path = ".\\resources\\ecg_data.zip"

try:
    extract.extract(comp_res_path)
except Exception:
    pass

base_res_location = os.path.join('.', 'resources', 'ecg_data', 'apple_health_export', 'electrocardiograms')

resource_names = os.listdir(base_res_location)

for res_name in resource_names:
    temp_res_path = os.path.join(base_res_location, res_name)

    if os.path.isfile(temp_res_path):
        dp.remove_redundant_info(temp_res_path, 'Apple Health Data')
        
prepared_dataset_path = os.path.join('.', 'resources', 'ecg_data', 'apple_ecgs')
prepped_dataset_names = os.listdir(prepared_dataset_path)

prepped_datasets = []

for prep_dataset_name in prepped_dataset_names:
    temp_prep_ds_path = f"{prepared_dataset_path}\\{prep_dataset_name}"

    if os.path.isfile(temp_prep_ds_path) and (prep_dataset_name != 'training.csv' or prep_dataset_name != 'labels.csv'):
        prepped_datasets.append(loader.load_data(temp_prep_ds_path))

tp.prep_data(prepped_datasets)

training_set = loader.load_data(f"{prepared_dataset_path}\\training.csv")

print(training_set.count())

labels_path = f"{prepared_dataset_path}\\labels.csv"

define = False

if define:
    with open(labels_path, 'w') as labels_file:
        labels_file.write("labels\n")

        for res in prepped_datasets:
            if len(res.values) >= 15360:
                display.plot_ecg_data(y_data=res)
                
                label_input = input()

                while label_input != '0' and label_input != '1':
                    label_input = input()

                    print(label_input != '0')
                    print(label_input != '1')
                
                labels_file.write(f"{label_input}\n")

label_set = loader.load_data(f"{prepared_dataset_path}\\labels.csv")

aml.setup_model(training_set, label_set)

#aml.setup_test_model(training_set, label_set)