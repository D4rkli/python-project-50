import argparse
import json


def read_json_file(file_path):
    """Чтение и парсинг JSON-файла."""
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_diff(first_data, second_data):
    """Сравнивает два словаря и возвращает разницу в виде строки."""
    result = {}

    all_keys = sorted(set(first_data.keys()).union(second_data.keys()))

    for key in all_keys:
        if key in first_data and key not in second_data:
            result[key] = f"- {key}: {first_data[key]}"
        elif key not in first_data and key in second_data:
            result[key] = f"+ {key}: {second_data[key]}"
        elif first_data[key] != second_data[key]:
            result[key] = f"- {key}: {first_data[key]}"
            result[key + "_new"] = f"+{key}: {second_data[key]}"

    return "{\n " + "\n ".join(result.values()) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')

    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='plain'
    )

    args = parser.parse_args()

    first_data = read_json_file(args.first_file)
    second_data = read_json_file(args.second_file)

    diff = generate_diff(first_data, second_data)
    print(diff)


if __name__ == '__main__':
    main()
