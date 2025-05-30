#!/usr/bin/env python3
import argparse

from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        metavar="FORMAT",
        default="stylish",
        choices=["stylish", "plain", "json"],
    )

    args = parser.parse_args()

    diff = generate_diff(
       args.first_file,
       args.second_file,
       format_name=args.format
    )
    print(diff)


if __name__ == "__main__":
    main()
