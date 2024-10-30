from gendiff.formatters.format_stylish import get_stylish
from gendiff.formatters.format_plain import get_plain_tree
from gendiff.formatters.format_json import get_format_json


def get_format(diff, format):
    if format == 'stylish':
        return get_stylish(diff)
    if format == 'plain':
        return get_plain_tree(diff)
    if format == 'json':
        return get_format_json(diff)
