#!/usr/bin/env python3


from gendiff.gendiff import generate_diff
from gendiff.argparse import get_args
from pathlib import Path


def main():
    args = get_args()
    result = generate_diff(Path(args.first_file),
                           Path(args.second_file), args.format)
    print(result)


if __name__ == "__main__":
    main()
