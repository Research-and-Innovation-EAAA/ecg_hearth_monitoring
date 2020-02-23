import os

import services.modifiers.Loader as loader

res_path = ".\\resources\\physionet"

res_folders = os.listdir(res_path)

fantasia_res = os.listdir(os.path.join(res_path, res_folders[0]))
ltaf_res = os.listdir(os.path.join(res_path, res_folders[1]))
nsr = os.listdir(os.path.join(res_path, res_folders[2]))

fantasia_lengths = []
nrs_lengths = []
ltaf_lengths = []

for res_elem in fantasia_res:
    temp = os.path.join(res_path, res_folders[0], res_elem)

    if os.path.isfile(temp):
        temp_data = loader.load_data(temp)

        fantasia_lengths.append(temp_data.count())

for res_elem in nsr:
    temp = os.path.join(res_path, res_folders[2], res_elem)

    if os.path.isfile(temp):
        temp_data = loader.load_data(temp)

        nrs_lengths.append(temp_data.count())

for res_elem in ltaf_res:
    temp = os.path.join(res_path, res_folders[1], res_elem)

    if os.path.isfile(temp):
        temp_data = loader.load_data(temp)

        ltaf_lengths.append(temp_data.count())

print("Fantasia")

for elem in fantasia_lengths:
    print(elem)

print("----------------------------------------------------------------------------")
print("Normal Sinus rythm")

for elem in nrs_lengths:
    print(elem)

print("----------------------------------------------------------------------------")
print("Long-term AF")

for elem in ltaf_lengths:
    print(elem)
