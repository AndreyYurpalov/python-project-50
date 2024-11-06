import itertools
from gendiff.formatters.str_lower import str_lower
from gendiff.tree_diff import ADDED, DELETED, UNCHANGED, CHANGED, NESTED


# MARK, INDENT, REPLACE, MARK_SIZE formatting options
# for functions get_diff_value, get_stylish
MARK = {ADDED: '+ ', DELETED: '- ', UNCHANGED: '  ', NESTED: '  '}
INDENT = 4
REPLACE = ' '
MARK_SIZE = 2


def get_diff_value(diff, level):
    if isinstance(diff, dict):
        line = []
        indent_size = INDENT * level
        currient_indent = (indent_size - MARK_SIZE) * REPLACE
        for key, val in diff.items():
            line.append(f"{currient_indent}{MARK[NESTED]}{key}: "
                        f"{get_diff_value(val, level + 1)}")
        currient_indent = INDENT * (level - 1) * REPLACE
        result = itertools.chain('{', line, [currient_indent + '}'])
        return '\n'.join(result)
    return str_lower(diff)


def get_stylish(diff):

    def inner(diff, level):
        line = []
        indent_size = INDENT * level
        line_indent = (indent_size - MARK_SIZE) * REPLACE
        for child in diff.get('childs'):
            type = str(child['type'])
            if type == NESTED:
                line.append(f"{line_indent}{MARK[type]}{child['name']}: "
                            f"{inner(child, level + 1)}")
            elif type == UNCHANGED:
                text = (f"{line_indent}{MARK[type]}"
                        f"{child['name']}: "
                        f"{get_diff_value(child['value'], level + 1)}")
                line.append(text)
            elif type == ADDED:
                text = (f"{line_indent}{MARK[type]}{child['name']}: "
                        f"{get_diff_value(child['value'], level + 1)}")
                line.append(text)
            elif type == DELETED:
                text = (f"{line_indent}{MARK[type]}"
                        f"{child['name']}: "
                        f"{get_diff_value(child['value'], level + 1)}")
                line.append(text)
            elif type == CHANGED:
                text = (f"{line_indent}{MARK[DELETED]}"
                        f"{child['name']}: "
                        f"{get_diff_value(child['value']['old'], level + 1)}")
                line.append(text)
                text = (f"{line_indent}{MARK[ADDED]}{child['name']}: "
                        f"{get_diff_value(child['value']['new'], level + 1)}")
                line.append(text)
        line_indent = INDENT * (level - 1) * REPLACE
        result = itertools.chain('{', line, [line_indent + '}'])
        return '\n'.join(result)
    return inner(diff, 1)
