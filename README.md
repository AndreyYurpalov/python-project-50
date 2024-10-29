### Hexlet tests and linter status:
[![Actions Status](https://github.com/AndreyYurpalov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AndreyYurpalov/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/59c04c73291342ba04b3/maintainability)](https://codeclimate.com/github/AndreyYurpalov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/59c04c73291342ba04b3/test_coverage)](https://codeclimate.com/github/AndreyYurpalov/python-project-50/test_coverage)

# "Сompare file differences"

### The Project uses: Language Python, Library Poetry, Library Pyyaml, Library Pytest, 

### This programme can find different between two files format json, yaml, yml.


### The output of the result can be obtained in the format:
+  **stylish** *(using default)*
+  **plain** 
+  **json**

## Install
```python3
git clone https://github.com/AndreyYurpalov/python-project-50.git
cd gendiff
make install
```

## Сommand line usage
```python3
gendiff -h #help output
gendiff file1 file2 #out put format(stylish)
gendiff -f plain file1 file2 #out put format plain
gendiff -f json file1 file2 #out put format json
```

### Diff all files
[![Diff all files](https://asciinema.org/a/fQFG65UXngHA3lf5mDAHR9rTJ.svg)](https://asciinema.org/a/fQFG65UXngHA3lf5mDAHR9rTJ)
