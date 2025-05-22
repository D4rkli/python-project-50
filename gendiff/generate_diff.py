from gendiff.formatters import get_formatter
from gendiff.parser import parse_file
from gendiff.tree import build_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    """Генерирует разницу между двумя конфигурационными файлами."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)

    return formatter(diff)
