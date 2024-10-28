import argparse
from gendiff.gendiff import generate_diff
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='output format (stylish (default), plain, json'
                        )
    args = parser.parse_args()
    result = generate_diff(Path(args.first_file),
                           Path(args.second_file), args.format)
    print(result)


if __name__ == "__main__":
    main()
