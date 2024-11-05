from gendiff.formatters.str_lower import str_lower


def to_str(value):
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
                text = (f"Property \'{path + child['name']}\' "
                        f"was added with value: "
                        f"{to_str(child['value'])}")
                line.append(text)
            elif child['type'] == 'deleted':
                text = f"Property \'{path + child['name']}\' was removed"
                line.append(text)
            elif child['type'] == 'changed':
                val = child['value']
                text = (f"Property \'{path + child['name']}\' "
                        f"was updated. From {to_str(val['old'])} "
                        f"to {to_str(val['new'])}")
                line.append((text))
            elif child['type'] == 'unchanged':
                continue
        return '\n'.join(line)
    return func(diff, '')
