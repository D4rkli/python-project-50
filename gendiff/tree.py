from gendiff.constants import (
    TYPE_REMOVED,
    TYPE_ADDED,
    TYPE_NESTED,
    TYPE_UNCHANGED,
    TYPE_CHANGED,
    KEY,
    TYPE,
    VALUE,
    OLD_VALUE,
    NEW_VALUE,
    CHILDREN,
)


def build_diff(data1, data2):
    """Построение дерева различий между двумя структурами данных."""
    if not isinstance(data1, dict) or not isinstance(data2, dict):
        return []

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data2:
            diff.append({KEY: key, TYPE: TYPE_REMOVED, VALUE: data1[key]})
        elif key not in data1:
            diff.append({KEY: key, TYPE: TYPE_ADDED, VALUE: data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append(
                {
                    KEY: key,
                    TYPE: TYPE_NESTED,
                    CHILDREN: build_diff(data1[key], data2[key]),
                }
            )
        elif data1[key] == data2[key]:
            diff.append({KEY: key, TYPE: TYPE_UNCHANGED, VALUE: data1[key]})
        else:
            diff.append(
                {
                    KEY: key,
                    TYPE: TYPE_CHANGED,
                    OLD_VALUE: data1[key],
                    NEW_VALUE: data2[key],
                }
            )

    return diff
