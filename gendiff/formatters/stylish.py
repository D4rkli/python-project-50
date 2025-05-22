def format_stylish(diff, depth=0):
    indent = " " * (depth * 4)
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


INDENT_SIZE = 4


def to_str(value, depth):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        indent = " " * ((depth + 1) * INDENT_SIZE)
        formatted = ["{"]
        for k, v in value.items():
            formatted.append(f"{indent}{k}: {to_str(v, depth + 1)}")
        formatted.append(" " * (depth * 4) + "}")
        return "\n".join(formatted)

    return value if isinstance(value, str) else str(value)
