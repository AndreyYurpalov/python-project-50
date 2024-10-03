from gendiff.gendiff import generate_diff


file1_json = "/home/ayu_263_ekb/python-project-50/tests/fixtures/file1.json"
file2_json = "/home/ayu_263_ekb/python-project-50/tests/fixtures/file2.json"
file1_yml = "/home/ayu_263_ekb/python-project-50/tests/fixtures/file1.yml"
file2_yml = "/home/ayu_263_ekb/python-project-50/tests/fixtures/file2.yml"

diff_files = "/home/ayu_263_ekb/python-project-50/tests/fixtures/diff_file1_file2"
with open(diff_files) as f:
    diff = f.read()
def test_generate_diff():
    assert generate_diff(file1_json, file2_json) == diff
    assert generate_diff(file1_yml, file2_yml) == diff
    assert generate_diff(file1_json, file2_yml) == diff
    assert generate_diff(file1_yml, file2_json) == diff
