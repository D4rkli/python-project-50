from gendiff.constants import (
    INDENT_SIZE,
    TYPE, TYPE_ADDED, TYPE_CHANGED, TYPE_NESTED, TYPE_REMOVED,
    KEY, VALUE, OLD_VALUE, NEW_VALUE, CHILDREN
)


def make_indent(depth: int, shift: int = 0) -> str:
    return " " * ((depth + shift) * INDENT_SIZE)


def format_stylish(diff, depth=0):
    indent = make_indent(depth)
    result = ["{"]

    for node in diff:
        key = node[KEY]
        if node[TYPE] == TYPE_NESTED:
            result.append(f"{indent}    {key}: "
                          f"{format_stylish(node[CHILDREN], depth + 1)}")
        elif node[TYPE] == TYPE_ADDED:
            result.append(f"{indent}  + {key}: "
                          f"{to_str(node[VALUE], depth + 1)}")
        elif node[TYPE] == TYPE_REMOVED:
            result.append(f"{indent}  - {key}: "
                          f"{to_str(node[VALUE], depth + 1)}")
        elif node[TYPE] == TYPE_CHANGED:
            result.append(f"{indent}  - {key}: "
                          f"{to_str(node[OLD_VALUE], depth + 1)}")
            result.append(f"{indent}  + {key}: "
                          f"{to_str(node[NEW_VALUE], depth + 1)}")
        else:
            result.append(f"{indent}    {key}: "
                          f"{to_str(node[VALUE], depth + 1)}")

    result.append(indent + "}")
    return "\n".join(result)


def to_str(value, depth):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        indent = make_indent(depth, shift=1)
        formatted = ["{"]
        for k, v in value.items():
            formatted.append(f"{indent}{k}: {to_str(v, depth + 1)}")
        formatted.append(make_indent(depth) + "}")
        return "\n".join(formatted)

    return value if isinstance(value, str) else str(value)
