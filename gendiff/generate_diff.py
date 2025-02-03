from gendiff.parser import parse_file
from gendiff.tree import build_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain

def generate_diff(file_path1, file_path2, format_name="stylish"):
    """Генерирует разницу между двумя конфигурационными файлами."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
