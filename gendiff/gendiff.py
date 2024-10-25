import json
import yaml
import os
from gendiff.formatters.format_stylish import get_stylish
from gendiff.formatters.format_plain import get_plain_tree
from gendiff.formatters.format_json import get_format_json


def get_file(file):
    dic = file.read()
    return dic


def get_dic_to_generate_diff(path_f):
    with open(path_f) as f:
        return get_file(f)


def get_dic(pathfile):
    _, ext = os.path.splitext(pathfile)
    if ext == '.yml' or ext == '.yaml':
        file_yaml = get_dic_to_generate_diff(pathfile)
        dic = yaml.safe_load(file_yaml)
    elif ext == '.json':
        file_json = get_dic_to_generate_diff(pathfile)
        dic = json.loads(file_json)
    else:
        dic = 'ERROR'
    return dic


def get_diff_tree(dic1, dic2):
    def inner(name, node1, node2):
        if isinstance(node1, dict) and isinstance(node2, dict):
            childs = []
            keys = sorted(set(node1) | set(node2))
            old_keys = set(keys) - set(node2)
            new_keys = set(keys) - set(node1)
            for key in keys:
                if key in old_keys:
                    childs.append({'name': key, 'type': 'deleted',
                                   'value': node1[key]})
                elif key in new_keys:
                    childs.append({'name': key, 'type': 'added',
                                   'value': node2[key]})
                elif (isinstance(node1[key], dict)
                      and isinstance(node2[key], dict)):
                    childs.append(inner(key, node1[key], node2[key]))
                elif node1[key] == node2[key]:
                    childs.append({'name': key, 'type': 'unchanged',
                                   'value': node1[key]})
                else:
                    childs.append({'name': key, 'type': 'changed', 'value':
                                  {'old': node1[key], 'new': node2[key]}})
        return {'name': name, 'type': 'nested', 'childs': childs}
    return inner(None, dic1, dic2)


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
