import json
import os


def read_from_json(file_name):
    with open(resolve_file_path(file_name)) as f:
        data = json.load(f)
        return data


def resolve_file_path(file_name):
    return os.path.join(project_root, file_name)


project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
endpoints = read_from_json('src/json/endpoints.json')
pets_data = read_from_json('src/json/petsData.json')
