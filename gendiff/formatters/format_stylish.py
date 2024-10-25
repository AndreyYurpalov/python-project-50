import itertools
from gendiff.formatters.str_lower import str_lower


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
                text = (f"{line_indent}{mark['deleted']}"
                        f"{child['name']}: "
                        f"{get_ch_diff(child['value']['old'], level + 1)}")
                line.append(text)

                line.append(f"{line_indent}{mark['added']}{child['name']}: "
                            f"{get_ch_diff(child['value']['new'], level + 1)}")
            else:
                line.append(f"{line_indent}{mark[type]}{child['name']}: "
                            f"{get_ch_diff(child['value'], level + 1)}")

        line_indent = indent * (level - 1) * replase
        result = itertools.chain('{', line, [line_indent + '}'])
        return '\n'.join(result)

    return inner(diff, 1)
