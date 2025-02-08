def format_value(value, depth=1):
    """Форматирует значение для корректного отображения в stylish-формате."""
    indent = " " * (depth * 4)

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        formatted_dict = "\n".join(
            f"{indent}{key}: {format_value(val, depth + 1)}"
            for key, val in value.items()
        )
        return f"{{\n{formatted_dict}\n{indent}}}"
    return str(value)


def format_stylish(diff, depth=1):
    """Форматирует различия в виде дерева (stylish)."""
    indent = " " * (depth * 4 - 2)
    closing_indent = " " * ((depth - 1) * 4)
    lines = ["{"]

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "removed":
            lines.append(
                f"{indent}- {key}: {format_value(node['value'], depth)}"
            )
        elif node_type == "added":
            lines.append(
                f"{indent}+ {key}: {format_value(node['value'], depth)}"
            )
        elif node_type == "unchanged":
            lines.append(
                 f"{indent}  {key}: {format_value(node['value'], depth)}"
            )
        elif node_type == "changed":
            lines.append(
                f"{indent}- {key}: {format_value(node['old_value'], depth)}"
            )
            lines.append(
                f"{indent}+ {key}: {format_value(node['new_value'], depth)}"
            )
        elif node_type == "nested":
            lines.append(
                f"{indent}  {key}:"
                f"{format_stylish(node['children'], depth + 1)}"
            )

    lines.append(closing_indent + "}")
    return "\n".join(lines)
