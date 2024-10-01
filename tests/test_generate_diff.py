from gendiff.gendiff import generate_diff


file1 = "/home/ayu_263_ekb/python-project-50/tests/fixtures/file1.json"
file2 = "/home/ayu_263_ekb/python-project-50/tests/fixtures/file2.json"
diff_files = "/home/ayu_263_ekb/python-project-50/tests/fixtures/diff_file1_file2"
with open(diff_files) as f:
    diff = f.read()
def test_generate_diff():
    assert generate_diff(file1, file2) == diff