def format_value(value, depth):
    """Форматирует значение с учетом вложенности."""
    if isinstance(value, dict):
        lines = []
        indent = " " * (depth * 4)
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{indent}}}"
    return str(value).lower() if isinstance(value, bool) else value


def format_stylish(diff, depth=1):
    """Форматирует различия в виде дерева (stylish)."""
    indent = " " * (depth * 4 - 2)
    lines = ["{"]

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "removed":
            lines.append(f"{indent}- {key}: {format_value(node['value'], depth)}")
        elif node_type == "added":
            lines.append(f"{indent}+ {key}: {format_value(node['value'], depth)}")
        elif node_type == "unchanged":
            lines.append(f"{indent}  {key}: {format_value(node['value'], depth)}")
        elif node_type == "changed":
            lines.append(f"{indent}- {key}: {format_value(node['old_value'], depth)}")
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'], depth)}")
        elif node_type == "nested":
            lines.append(f"{indent}  {key}: {format_stylish(node['children'], depth + 1)}")

    lines.append(" " * ((depth - 1) * 4) + "}")
    return "\n".join(lines)
