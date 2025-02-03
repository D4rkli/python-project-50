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
    """Форматирует различия в виде плоского списка (plain)."""
    lines = []

    for node in diff:
        key_path = f"{path}.{node['key']}" if path else node["key"]
        node_type = node["type"]

        if node_type == "added":
            lines.append(f"Property '{key_path}' was added with value: {format_value(node['value'])}")
        elif node_type == "removed":
            lines.append(f"Property '{key_path}' was removed")
        elif node_type == "changed":
            lines.append(f"Property '{key_path}' was updated. From {format_value(node['old_value'])} to {format_value(node['new_value'])}")
        elif node_type == "nested":
            lines.append(format_plain(node["children"], key_path))

    return "\n".join(lines)
