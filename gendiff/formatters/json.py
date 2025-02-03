import json

def format_json(diff):
    """Форматирует различия в JSON-формате."""
    return json.dumps(diff, indent=2, sort_keys=True)

