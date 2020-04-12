import json

def parse_data(path):
    with open(path) as data_file:
        return json.loads(data_file.read())