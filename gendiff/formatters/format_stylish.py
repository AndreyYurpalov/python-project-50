import itertools
from gendiff.formatters.str_lower import str_lower


# MARK, INDENT, REPLACE, MARK_SIZE formatting options
# for functions get_diff_value, get_stylish
MARK = {'added': '+ ', 'deleted': '- ', 'unchanged': '  ', 'nested': '  '}
INDENT = 4
REPLACE = ' '
MARK_SIZE = 2


def get_diff_value(diff, level):
    if isinstance(diff, dict):
        line = []
        indent_size = INDENT * level
        line_indent = (indent_size - MARK_SIZE) * REPLACE
        for key, val in diff.items():
            text_value = (f"{line_indent}{MARK['nested']}{key}: "
                          f"{get_diff_value(val, level + 1)}")
            line.append(text_value)
        line_indent = INDENT * (level - 1) * REPLACE
        result = itertools.chain('{', line, [line_indent + '}'])
        return '\n'.join(result)
    return str_lower(diff)


def get_stylish(diff):
    def inner(diff, level):
        line = []
        indent_size = INDENT * level
        line_indent = (indent_size - MARK_SIZE) * REPLACE
        for child in diff.get('childs'):
            type = str(child['type'])
            if type == 'nested':
                line.append(f"{line_indent}{MARK[type]}{child['name']}: "
                            f"{inner(child, level + 1)}")
            elif type == 'changed':
                text = (f"{line_indent}{MARK['deleted']}"
                        f"{child['name']}: "
                        f"{get_diff_value(child['value']['old'], level + 1)}")
                line.append(text)
                text = (f"{line_indent}{MARK['added']}{child['name']}: "
                        f"{get_diff_value(child['value']['new'], level + 1)}")
                line.append(text)
            else:
                line.append(f"{line_indent}{MARK[type]}{child['name']}: "
                            f"{get_diff_value(child['value'], level + 1)}")
        line_indent = INDENT * (level - 1) * REPLACE
        result = itertools.chain('{', line, [line_indent + '}'])
        return '\n'.join(result)
    return inner(diff, 1)
