def format_value(value):
    """Форматирует значение для вывода в plain-формате."""
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return value


def format_plain(diff, path=""):
    """Форматирует различия в plain-формате."""
    lines = []

    for node in diff:
        key = f"{path}{node['key']}"
        node_type = node["type"]

        if node_type == "removed":
            lines.append(f"Property '{key}' was removed")
        elif node_type == "added":
            value = format_plain_value(node["value"])
            lines.append(f"Property '{key}' was added with value: {value}")
        elif node_type == "changed":
            old_value = format_plain_value(node["old_value"])
            new_value = format_plain_value(node["new_value"])
            lines.append(
                f"Property '{key}' was updated. From {old_value} to {new_value}"
            )
        elif node_type == "nested":
            lines.append(format_plain(node["children"], f"{key}."))

    return "\n".join(lines)

def format_plain_value(value):
    """Форматирует значение для plain-формата."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    return value
