from gendiff.constants import (
    TYPE_REMOVED, TYPE_ADDED, TYPE_CHANGED, TYPE_NESTED
)


def format_value(value, mode="plain"):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'" if mode == "plain" else f"'{value}'"
    return value


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = f"{path}{node['key']}"
        node_type = node["type"]

        if node_type == TYPE_REMOVED:
            lines.append(f"Property '{key}' was removed")
        elif node_type == TYPE_ADDED:
            value = format_value(node["value"], mode="plain")
            lines.append(f"Property '{key}' was added with value: {value}")
        elif node_type == TYPE_CHANGED:
            old_value = format_value(node["old_value"], mode="plain")
            new_value = format_value(node["new_value"], mode="plain")
            lines.append(
                f"Property '{key}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif node_type == TYPE_NESTED:
            lines.append(format_plain(node["children"], f"{key}."))

    return "\n".join(lines)
