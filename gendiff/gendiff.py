import itertools
import json
import yaml
import os


def get_file(file):
    dic = file.read()
    return dic


def get_dic_to_generate_diff(path_f):
    with open(path_f) as f:
        return get_file(f)


def get_dic(pathfile):
    _, ext = os.path.splitext(pathfile)
    if ext == '.yml' or ext == '.yaml':
        fy = get_dic_to_generate_diff(pathfile)
        dic = yaml.load(fy, Loader=yaml.FullLoader)
    elif ext == '.json':
        fj = get_dic_to_generate_diff(pathfile)
        dic = json.loads(fj)
    else:
        dic = 'ERROR'
    return dic


def str_lower(word):
    if isinstance(word, bool):
        return str(word).lower()
    if word is None:
        return 'null'
    return word


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


def get_stylish(diff, replase=' ', indent=4):
    mark = {'added': '+ ', 'deleted': '- ', 'unchanged': '  ', 'nested': '  '}

    def get_ch_diff(diff, level):
        if isinstance(diff, dict):
            line = []
            mark_size = 2
            indent_size = indent * level
            currient_indent = (indent_size - mark_size) * replase
            for key, val in diff.items():
                line.append(f"{currient_indent}{mark['nested']}{key}: "
                            f"{get_ch_diff(val, level + 1)}")
            currient_indent = indent * (level - 1) * replase
            result = itertools.chain('{', line, [currient_indent + '}'])
            return '\n'.join(result)
        return str_lower(diff)

    def inner(diff, level):
        line = []
        mark_size = 2
        indent_size = indent * level
        line_indent = (indent_size - mark_size) * replase
        for child in diff.get('childs'):
            type = str(child['type'])
            if type == 'nested':
                line.append(f"{line_indent}{mark[type]}{child['name']}: "
                            f"{inner(child, level + 1)}")
            elif type == 'changed':
                line.append(f"{line_indent}{mark['deleted']}{child['name']}: "
                            f"{get_ch_diff(child['value']['old'], level + 1)}")

                line.append(f"{line_indent}{mark['added']}{child['name']}: "
                            f"{get_ch_diff(child['value']['new'], level + 1)}")
            else:
                line.append(f"{line_indent}{mark[type]}{child['name']}: "
                            f"{get_ch_diff(child['value'], level + 1)}")

        line_indent = indent * (level - 1) * replase
        result = itertools.chain('{', line, [line_indent + '}'])
        return '\n'.join(result)

    return inner(diff, 1)


def get_format(diff, format):
    if format == 'stylish':
        return get_stylish(diff)


def generate_diff(pathfile1, pathfil2, format_name='stylish'):
    dic1 = get_dic(pathfile1)
    dic2 = get_dic(pathfil2)
    diff = get_diff_tree(dic1, dic2)
    result = get_format(diff, format_name)

    return result
