import argparse
import json


def parse_json(filepath):
    """Читает и парсит JSON-файл."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def generate_diff(file1, file2):
    """Сравнивает два JSON-файла."""
    data1 = parse_json(file1)
    data2 = parse_json(file2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = ["{"]

    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key in data2 and key not in data1:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {data1[key]}")
        else:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")

    diff_lines.append("}")
    return "\n".join(diff_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First configuration file")
    parser.add_argument("second_file", help="Second configuration file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="plain"
    )

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
