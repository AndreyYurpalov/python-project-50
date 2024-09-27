import json


def generate_diff(file1, file2):
    file1, file2 = json.load(open(file1)), json.load(open(file2))
    sort_keys = sorted(set(file1.keys()) | set(file2.keys()))
    diff_dic = {}
    for key in sort_keys:
        diff_dic[key] = [file1.setdefault(key, 'None'),
                         file2.setdefault(key, 'None'),
                         ]
    result = ''
    for key in diff_dic:
        if diff_dic[key][0] == diff_dic[key][1]:
            res = f'  {key}: {diff_dic[key][0]}\n'
        elif diff_dic[key][0] == 'None':
            res = f'+ {key}: {diff_dic[key][1]}\n'
        elif diff_dic[key][1] == 'None':
            res = f'- {key}: {diff_dic[key][0]}\n'
        else:
            res = f'- {key}: {diff_dic[key][0]}\n+ {key}: {diff_dic[key][1]}\n'
        result += res
    return result
