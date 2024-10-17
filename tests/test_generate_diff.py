from gendiff.gendiff import generate_diff
import os
import pytest


def get_abspath(file):
    file = str(file)
    return os.path.abspath(f'tests/fixtures/{file}')


date_files = [
    ('file1.json', 'file2.json', 'diff_file1_file2'),
    ('file1.json', 'file2.yml', 'diff_file1_file2'),
    ('file1.yml', 'file2.json', 'diff_file1_file2'),
    ('file1.yml', 'file2.yml', 'diff_file1_file2'),
    ('file3.json', 'file4.json', 'diff_file3_file4'),
    ('file3.json', 'file4.yml', 'diff_file3_file4'),
    ('file3.yml', 'file4.json', 'diff_file3_file4'),
    ('file3.yml', 'file4.yml', 'diff_file3_file4'),]


@pytest.mark.parametrize('file1, file2, result_file', date_files)
def test_generate_diff(file1, file2, result_file):
    result = open(get_abspath(result_file)).read()
    assert (generate_diff(get_abspath(file1), get_abspath(file2)) == result)
