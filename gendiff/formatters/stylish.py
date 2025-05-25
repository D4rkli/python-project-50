INDENT_SIZE = 4


def make_indent(depth: int, shift: int = 0) -> str:
    return " " * ((depth + shift) * INDENT_SIZE)


def format_stylish(diff, depth=0):
    indent = make_indent(depth, shift=1)
    result = ["{"]

    for node in diff:
        key = node["key"]
        if node["type"] == "nested":
            result.append(f"{indent}    {key}: "
                          f"{format_stylish(node['children'], depth + 1)}")
        elif node["type"] == "added":
            result.append(f"{indent}  + {key}: "
                          f"{to_str(node['value'], depth + 1)}")
        elif node["type"] == "removed":
            result.append(f"{indent}  - {key}: "
                          f"{to_str(node['value'], depth + 1)}")
        elif node["type"] == "changed":
            result.append(f"{indent}  - {key}: "
                          f"{to_str(node['old_value'], depth + 1)}")
            result.append(f"{indent}  + {key}: "
                          f"{to_str(node['new_value'], depth + 1)}")
        else:
            result.append(f"{indent}    {key}: "
                          f"{to_str(node['value'], depth + 1)}")

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
