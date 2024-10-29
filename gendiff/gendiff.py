import json
import yaml
import os
from gendiff.formatters.format_stylish import get_stylish
from gendiff.formatters.format_plain import get_plain_tree
from gendiff.formatters.format_json import get_format_json
from gendiff.tree_diff import get_diff_tree


def get_file_to_generate_diff(path_f):
    _, ext = os.path.splitext(path_f)
    with open(path_f) as f:
        dic = f.read()
    return dic, ext


def get_dic(pathfile):
    dic, ext = get_file_to_generate_diff(pathfile)
    if ext == '.yml' or ext == '.yaml':
        dic = yaml.safe_load(dic)
    elif ext == '.json':
        dic = json.loads(dic)
    else:
        dic = (f'ERROR! {pathfile}: invalid file format. '
               f'Valid file format: json, yaml, yml')
        print(dic)
    return dic


def get_format(diff, format):
    if format == 'stylish':
        return get_stylish(diff)
    if format == 'plain':
        return get_plain_tree(diff)
    if format == 'json':
        return get_format_json(diff)


def generate_diff(pathfile1, pathfile2, format_name='stylish'):
    dic1 = get_dic(pathfile1)
    dic2 = get_dic(pathfile2)
    diff = get_diff_tree(dic1, dic2)
    result = get_format(diff, format_name)

    return result
