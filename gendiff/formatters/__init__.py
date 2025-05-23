from gendiff.formatters import json, plain, stylish
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json

__all__ = ['json', 'plain', 'stylish']


def get_formatter(format_name):
    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }

    if format_name not in formatters:
        raise ValueError(f"Unsupported format: {format_name}")

    return formatters[format_name]
