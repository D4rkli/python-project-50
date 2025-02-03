import json
import yaml


def parse_file(filepath):
    """Определяет формат файла и парсит его в словарь."""
    if filepath.endswith((".yml", ".yaml")):
        with open(filepath, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    elif filepath.endswith(".json"):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")
