import os
import platform

def path_join(*args):
    path = ""

    for elem in args:
        path = os.path.join(path, elem)

    return path

def dir_res_list(directory):
    return os.listdir(directory)

def is_path_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def makedirs(path, override=False):
    os.makedirs(path, exist_ok=override)

def copy_file(res_path, copy_name):
    os_env = platform.system()

    res_path_splitted = res_path.split(os.path.sep)

    if os_env == "Windows":
        copy_path = f"{res_path_splitted[0][0:2]}{os.path.sep}{res_path_splitted[0][2:]}{os.path.sep}{res_path_splitted[1]}"
    else:
        copy_path = f"{res_path_splitted[0]}{os.path.sep}{res_path_splitted[1]}"

    for x in range(2, len(res_path_splitted)- 1):
        copy_path = path_join(copy_path, res_path_splitted[x])
    
    copy_path = path_join(copy_path, copy_name)

    with open(res_path) as original:
        with open(copy_path, 'w') as copy:
            copied = original.readline()

            while copied != "":
                copy.write(copied)

                copied = original.readline()
    
    return copy_path

def remove_file(path):
    os.remove(path)

def remove_dir(path):
    os.rmdir(path)

def get_ressource_path_name(path):
    os_env = platform.system()

    if os_env == 'Windows':
        splitted_path = path.split('\\')
    elif os_env == 'Linux':
        splitted_path = path.split('/')
    
    return splitted_path[len(splitted_path) - 1]

def get_path_seperator():
    return os.path.sep