import os
import zipfile

def extract(com_res_path=None, ext_loc=None, override=False):
    #TODO Guard against missing or invalid arguments

    if zipfile.is_zipfile(com_res_path):
        __zip_extract(com_res_path, ext_loc, override)
    else:
        raise Exception(f"Currently {com_res_path[-4,]} compressions are not supported!")

def __zip_extract(com_res_path, ext_loc, override):
    split_path = com_res_path.split('\\')
 
    if ext_loc is None:
        __prepare_ext_loc()
        ext_loc = os.path.join('.', 'resources', split_path[-1][:-4])
    
    if not override and os.path.exists(f"{ext_loc}"):
        raise Exception("Extract location already contains a resource with given name")

    with zipfile.ZipFile(com_res_path) as com_file:
        com_file.extractall(ext_loc)

def __prepare_ext_loc():
    path = os.path.join('.', 'resources')

    os.makedirs(path, exist_ok=True)