import os
from zipfile import ZipFile

def zip_extract(containing_resource_folder = None, resource_name=None, extract_location=''):
    if containing_resource_folder is None or resource_name is None:
        raise Exception("Missing required parameters!")

    resource = os.path.join(containing_resource_folder, f"{resource_name}.zip")

    with ZipFile(resource) as resource_zip:
        target_folder = extract_location

        if extract_location == '':
            target_folder =  os.path.join(resource_name, containing_resource_folder)

        os.makedirs(target_folder, exist_ok=True)

        resource_zip.extractall(target_folder)