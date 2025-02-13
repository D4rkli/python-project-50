from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parser import parse_file
from gendiff.tree import build_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    """Генерирует разницу между двумя конфигурационными файлами."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }

    if format_name not in formatters:
        raise ValueError(f"Unsupported format: {format_name}")

    result = formatters[format_name](diff)
    return result + "\n"
