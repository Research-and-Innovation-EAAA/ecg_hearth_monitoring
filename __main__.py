import os

import services.modifiers.Loader as loader
import services.displayers.Graph as displayer

res_path = "C:\\Users\\mabh\\Desktop\\Workspace_development\\ECG Hearth Monitoring\\resources\\physionet"

res_folders = os.listdir(res_path)

fantasia_res = os.listdir(os.path.join(res_path, res_folders[0]))
ltaf_res = os.listdir(os.path.join(res_path, res_folders[1]))
nsr = os.listdir(os.path.join(res_path, res_folders[2]))

for folder_elem in res_folders:
    temp_path = os.path.join(res_path, folder_elem)

    for res_elem in os.listdir(os.path.join(temp_path)):
        temp_res_load = loader.load_data(os.path.join(temp_path, res_elem))

        print(temp_res_load.count())

        x, y, z, = temp_res_load.split('id', '1-led', '2-led')
        
        print(x.count())
        print(y.count())
        print(z.count())

        displayer.plot_ecg_data(y_data=temp_res_load, x_scale=13000, y_scale=25000, title=f"{folder_elem}-{res_elem}")