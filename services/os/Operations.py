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

def copy_file(res_path, copy_name):
    res_path_splitted = res_path.split("\\")

    copy_path = ""

    for x in range(0, len(res_path_splitted)- 1):
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