from gendiff.constants import (
    FORMAT_STYLISH, FORMAT_PLAIN, FORMAT_JSON
)
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json

__all__ = [FORMAT_JSON, FORMAT_PLAIN, FORMAT_STYLISH, 'apply_formatter']


def apply_formatter(diff, format_name):
    formatters = {
        FORMAT_STYLISH: format_stylish,
        FORMAT_PLAIN: format_plain,
        FORMAT_JSON: format_json,
    }

    if format_name not in formatters:
        raise ValueError(f"Unsupported format: {format_name}")

    return formatters[format_name](diff)
