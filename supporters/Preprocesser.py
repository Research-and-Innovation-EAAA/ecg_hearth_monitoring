import os

def base_info_removal(containing_folder=None, resource_name=None):
    if containing_folder is None or resource_name is None:
        raise Exception("Missing required parameters!")

    resource_location = os.path.join(containing_folder, f'{resource_name}.csv')

    data = load_raw_data(containing_folder, resource_name)

    with open(resource_location, 'w') as resource:
        data_list = data.split('\n')

        resource.write("readings\n")

        for element in data_list:
            try:
                element_split = element.split(",")

                if len(element_split) == 1:
                    element_split = element.split('.')

                resource.write(f"{int(element_split[0])}.{int(element_split[1])}\n")
            except Exception as e:
                pass

def load_raw_data(containing_folder = None, resource_name = None):
    if containing_folder is None or resource_name is None:
        raise Exception("Missing required parameters!")

    with open(os.path.join(containing_folder, f'{resource_name}.csv')) as resource:
        return resource.read()