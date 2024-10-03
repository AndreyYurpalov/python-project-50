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


def formater_dic(diff_dic):
    result = ''
    for key in diff_dic:
        if diff_dic[key]['old'] == diff_dic[key]['new']:
            res = f"  {key}: {diff_dic[key]['old']}\n"
        elif diff_dic[key]['old'] is None:
            res = f"+ {key}: {diff_dic[key]['new']}\n"
        elif diff_dic[key]['new'] is None:
            res = f"- {key}: {diff_dic[key]['old']}\n"
        else:
            res = (f"- {key}: {diff_dic[key]['old']}\n"
                   f"+ {key}: {diff_dic[key]['new']}\n")
        result += res
    result = result.rstrip()
    return result


def generate_diff(pathfile1, pathfil2):
    dic1 = get_dic(pathfile1)
    dic2 = get_dic(pathfil2)
    sort_keys = sorted(set(dic1.keys()) | set(dic2.keys()))
    diff_dic = {}
    for key in sort_keys:
        diff_dic[key] = {'old': dic1.setdefault(key, None),
                         'new': dic2.setdefault(key, None),
                         }
    result = formater_dic(diff_dic)
    return result
