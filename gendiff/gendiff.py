import json


def parser_files(pathfile1, pathfile2):
    file1, file2 = json.load(open(pathfile1)), json.load(open(pathfile2))
    return file1, file2


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


def generate_diff(dic1, dic2):
    dic1, dic2 = parser_files(dic1, dic2)
    sort_keys = sorted(set(dic1.keys()) | set(dic2.keys()))
    diff_dic = {}
    for key in sort_keys:
        diff_dic[key] = {'old': dic1.setdefault(key, None),
                         'new': dic2.setdefault(key, None),
                         }
    result = formater_dic(diff_dic)
    return result
