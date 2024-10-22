import itertools
from gendiff.formatters.str_lower import str_lower


def get_type_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        value = f"'{value}'"
    return str_lower(value)


def get_plain_tree(diff):
    def func(diff, path):
        line = []
        for child in diff.get('childs'):
            if child['type'] == 'nested':
                res = func(child, path + child['name'] + '.')
                text = f"{res}"
                line.append(text)
            elif child['type'] == 'added':
                text = f"Property \'{path + child['name']}\' was added with value: {get_type_value(child['value'])}"
                line.append(text)
            elif child['type'] == 'deleted':
                text = f"Property \'{path + child['name']} \'was removed"
                line.append(text)
            elif child['type'] == 'changed':
                val = child['value']
                text = f"Property \'{path + child['name']}\' was updated. From {get_type_value(val['old'])} to {get_type_value(val['new'])}"
                line.append((text))
            elif child['type'] == 'unchanged':
                continue
        return '\n'.join(line)
    return func(diff, '')