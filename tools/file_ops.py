import sys
import json
import os
import re
import csv
import pandas as pd
from tools.convert import MyCoolDict
import plotly.io as io


def pretty_print(data):
    if type(data) == str:
        data = load_json(data)
    print(json.dumps(data, indent=2, sort_keys=True))


def load_csv(path):
    with open(path, 'r') as f:
        return list(csv.DictReader(f, skipinitialspace=True))
        # return [
        #     {k: int(v) for k, v in row.items()}
        #     for row in csv.DictReader(f, skipinitialspace=True)
        # ]

def write_csv(data, path):
    if isinstance(data, pd.DataFrame):
        data.to_csv(path)
    elif isinstance(data, list) and isinstance(data[0], dict):
        keys = data[0].keys()
        with open(path, 'w+') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

def load_json(path, output_format = 'json'):
    assert re.search("^str|figure|json$", output_format)
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
    elif isinstance(path, str):
        data = json.loads(path)
    if output_format == "json":
        return data
    elif output_format == "str":
        return json.dumps(data)
    elif output_format == "figure":
        return io.from_json(json.dumps(data), output_type="Figure", engine = None)

def load_jsons(path, output_format = 'json'):
    assert re.search("^str|figure|json$", output_format)
    walk_dir = os.walk(path)
    jsons = {}
    for dirpath, _, filenames in walk_dir:
        for filename in filenames:
            if filename.endswith(".json"):
                try:
                    jsons[filename.split(".")[0]] = load_json(
                        os.path.join(dirpath, filename),
                        output_format=output_format
                    )
                except Exception as error:
                    if output_format == 'figure':
                        print("Can't load figure, skipping")
                    else:
                        raise Exception(error)
    return jsons

def write_json(data, path):
    if isinstance(data, str):
        data = load_json(data)
    with open(path, "w+") as f:
        json.dump(data, f, indent=2)

def get_all_instances_of_nested_keys(data, key):
    """
    Returns a list of all values that have a given key.

    Args:
        data (dict): The dictionary to search for the key.
        key (str): The key to search for in the dictionary.

    Yields:
        Any: The values that have the given key.

    """
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                yield v
            if isinstance(v, (dict, list)):
                yield from get_all_instances_of_nested_keys(v, key)
    elif isinstance(data, list):
        for d in data:
            yield from get_all_instances_of_nested_keys(d, key)

def get_nested_path(element, data, path="data", all_paths=[]):
    """
    Prints the nested path of the given element key in the data dictionary.

    Args:
        element (str): The key to search for in the data dictionary.
        data (dict): The dictionary to search for the key.
        path (str, optional): The current nested path. Defaults to "data".
        all_paths (list, optional): The list to store all the nested paths. Defaults to [].

    """
    if isinstance(data, str):
        data = load_json(data)
    if element in data:
        current_path = f"{path}.{element} = {data[element]}"
        print(current_path)
        all_paths.append(current_path)
    if isinstance(data, dict):
        for key in data.keys():
            if isinstance(data[key], (dict, list)):
                get_nested_path(element, data[key], f"{path}.{key}", all_paths)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            get_nested_path(element, item, f"{path}[{i}]", all_paths)


if __name__ == "__main__":
    locals().get( sys.argv[1])(*sys.argv[2:])
    # data = load_json(os.path.join(os.path.dirname(__file__), "..", "tests", "data", "random.json"))
    # data = MyCoolDict(data)
    # print(list(get_all_instances_of_nested_keys(data, "heythere")))
    # get_nested_path("heythere", data)
    # data.nestedlist[0].heythere
    # pretty_print(data)