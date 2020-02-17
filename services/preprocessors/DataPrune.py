import os
import services.modifiers.Loader as loader 

def remove_redundant_info(path=None, data_type=None):
    #TODO Guard against wrong formatted parameters

    if data_type == 'Apple Health Data':
        __base_info_apple_ecg_data(path)

def __base_info_apple_ecg_data(path):
    """ Removes all base information from any 'Apple Watch' ECG-reading and leaves a clean CSV-data file of readings ready for processing. """

    split_path = path.split('\\')

    __prep_target_loc(".\\resources\\ecg_data\\apple_ecgs")

    core_data_location = f'.\\resources\\ecg_data\\apple_ecgs\\{split_path[-1]}'

    data = loader.__load_raw_data(path)

    with open(core_data_location, 'w') as resource:
        data_list = data.split('\n')

        resource.write("readings\n")

        for element in data_list:
            try:
                element_split = element.split(",")

                if len(element_split) == 1:
                    element_split = element.split('.')

                resource.write(f"{int(element_split[0])}.{int(element_split[1])}\n")
            except Exception:
                pass
    
def __prep_target_loc(target_dir_path):
    os.makedirs(target_dir_path, exist_ok=True)