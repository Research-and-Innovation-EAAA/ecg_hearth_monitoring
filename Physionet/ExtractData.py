import os
import threading

import services.modifiers.Loader as loader

class speed_up:#(threading.Thread):
    def __init__(self, target_write_loc, target_read_loc, resource_name, daemon=False):
        #super().__init__(daemon=daemon)

        self.target_write_loc = target_write_loc
        self.target_read_loc = target_read_loc
        self.resource_name = resource_name
    
    def run(self):
        temp_path = os.path.join(self.target_read_loc, self.resource_name)

        if os.path.isfile(temp_path) and self.resource_name[-4:] == '.csv':
            with open(os.path.join(self.target_write_loc, self.resource_name), 'w') as write_file:
                write_file.write('id,1-led,2-lead\n')

                with open(temp_path) as file:
                    write_file.write(file.read())
                    #temp = file.readline()

                    #while temp != '':
                     #   write_file.writelines(temp)
                      #  temp = file.readline()

import os
import asyncio
from Physionet import ltafdb as ltaf


temp_res_path = "D:\\Praktik Vinter-Forår 2020\\ressourcer\\ltafdb"

temp_target_loc = 'C:\\Users\\mabh\\Desktop\\Workspace_development\\ECG Hearth Monitoring\\resources\\physionet\\ltafdb'

res_names = os.listdir(temp_res_path)

tasks = []

for res_name_elem in res_names:
    temp_task = ltaf.speed_up(target_write_loc=temp_target_loc, target_read_loc=temp_res_path, resource_name=res_name_elem)
    temp_task.run()
    tasks.append(temp_task)

temp_res_path = "D:\\Praktik Vinter-Forår 2020\\ressourcer\\nsrdb"

temp_target_loc = 'C:\\Users\\mabh\\Desktop\\Workspace_development\\ECG Hearth Monitoring\\resources\\physionet\\nsrdb'

res_names = os.listdir(temp_res_path)

tasks = []

for res_name_elem in res_names:
    temp_task = ltaf.speed_up(target_write_loc=temp_target_loc, target_read_loc=temp_res_path, resource_name=res_name_elem)
    temp_task.run()
    tasks.append(temp_task)

temp_res_path = "D:\\Praktik Vinter-Forår 2020\\ressourcer\\fantasia"

temp_target_loc = 'C:\\Users\\mabh\\Desktop\\Workspace_development\\ECG Hearth Monitoring\\resources\\physionet\\fantasia'

res_names = os.listdir(temp_res_path)

tasks = []

for res_name_elem in res_names:
    temp_task = ltaf.speed_up(target_write_loc=temp_target_loc, target_read_loc=temp_res_path, resource_name=res_name_elem)
    temp_task.run()
    tasks.append(temp_task)