from gendiff.formatters import get_formatter, apply_formatter
from gendiff.parser import parse_file
from gendiff.tree import build_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    """Генерирует разницу между двумя конфигурационными файлами."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if not isinstance(diff, list):
        raise TypeError(f"build_diff() должен возвращать список,"
                        f" а не {type(diff)}")

    return apply_formatter(diff, format_name)
