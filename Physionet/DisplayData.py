import os

import services.modifiers.Loader as loader
import services.displayers.Graph as displayer

res_path = ".\\resources\\physionet"

res_folders = os.listdir(res_path)

for folder_elem in res_folders:
    temp_path = os.path.join(res_path, folder_elem)

    for res_elem in os.listdir(os.path.join(temp_path)):
        temp_res_load = loader.load_data(os.path.join(temp_path, res_elem))

        print(temp_res_load.count())

        x, y, z, = temp_res_load.split('id', '1-led', '2-led')

        displayer.plot_ecg_data(y_data=temp_res_load, x_scale=13000, y_scale=25000, title=f"{folder_elem}-{res_elem}")