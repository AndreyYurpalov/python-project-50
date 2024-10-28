from gendiff.gendiff import generate_diff
import os
import pytest


def get_abspath(file):
    file = str(file)
    return os.path.abspath(f'tests/fixtures/{file}')


date_files = [
    ('file1.json', 'file2.json', 'stylish', 'diff_file1_file2.txt'),
    ('file1.json', 'file2.yml', 'stylish', 'diff_file1_file2.txt'),
    ('file1.yml', 'file2.json', 'stylish', 'diff_file1_file2.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'diff_file1_file2.txt'),
    ('file3.json', 'file4.json', 'stylish', 'diff_file3_file4.txt'),
    ('file3.json', 'file4.yml', 'stylish', 'diff_file3_file4.txt'),
    ('file3.yml', 'file4.json', 'stylish', 'diff_file3_file4.txt'),
    ('file3.yml', 'file4.yml', 'stylish', 'diff_file3_file4.txt'),
    ('file3.json', 'file4.json', 'plain', 'diff_plain.txt'),
    ('file3.json', 'file4.yml', 'plain', 'diff_plain.txt'),]


@pytest.mark.parametrize('file1, file2, format, result_file', date_files)
def test_generate_diff(file1, file2, format, result_file):
    result = open(get_abspath(result_file)).read()
    if ':\n' in result:
        result = result.replace(':\n', ': \n')
    assert (generate_diff(get_abspath(file1),
                          get_abspath(file2), format) == result)
