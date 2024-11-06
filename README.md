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
gendiff file1 file2 #out put format stylish (default)
gendiff -f plain file1 file2 #out put format plain
gendiff -f json file1 file2 #out put format json
```

### compare files in format STYLISH
[![Diff files format:stylish](https://asciinema.org/a/Q8KyhrHR07o40OO9bXJ6KC64R.svg)](https://asciinema.org/a/Q8KyhrHR07o40OO9bXJ6KC64R)

### compare files in format PLAIN
[![Diff files format:plain](https://asciinema.org/a/eH3oVtSeZBB2roomV2p0kdOsy.svg)](https://asciinema.org/a/eH3oVtSeZBB2roomV2p0kdOsy)

### compare files in format JSON
[![Diff files format:json](https://asciinema.org/a/P8X2ThUMcKtPD8RzRA7cB1IDS.svg)](https://asciinema.org/a/P8X2ThUMcKtPD8RzRA7cB1IDS)