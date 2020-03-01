import os

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