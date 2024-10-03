from gendiff.gendiff import generate_diff
import os

def get_abspath(file):
    file = str(file)
    return os.path.abspath(f'tests/fixtures/{file}')


file1_json = get_abspath('file1.json')
file2_json = get_abspath('file2.json')
file1_yml = get_abspath('file1.yml')
file2_yml = get_abspath('file2.yml')
diff_files = get_abspath('diff_file1_file2')
with open(diff_files) as f:
    diff = f.read()


def test_generate_diff():
    assert generate_diff(file1_json, file2_json) == diff
    assert generate_diff(file1_yml, file2_yml) == diff
    assert generate_diff(file1_json, file2_yml) == diff
    assert generate_diff(file1_yml, file2_json) == diff
