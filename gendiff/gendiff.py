import json
import yaml
import os
from gendiff.tree_diff import get_diff_tree
from gendiff.formatters.format_diff import get_format


def get_dict_to_generate_diff(path_f):
    _, ext = os.path.splitext(path_f)
    with open(path_f) as f:
        opened_file = f.read()
    return parse(opened_file, ext)


def parse(file, ext):
    if ext == '.yml' or ext == '.yaml':
        dictionary = yaml.safe_load(file)
    elif ext == '.json':
        dictionary = json.loads(file)
    return dictionary


def generate_diff(path_file1, path_file2, format_name='stylish'):
    dict1 = get_dict_to_generate_diff(path_file1)
    print(dict1)
    dict2 = get_dict_to_generate_diff(path_file2)
    print(dict2)
    diff = get_diff_tree(dict1, dict2)
    result = get_format(diff, format_name)
    return result
