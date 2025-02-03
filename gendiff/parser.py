import json
import yaml

def parse_file(filepath):
    """Определяет формат файла и парсит его."""
    if filepath.endswith((".json", ".JSON")):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    elif filepath.endswith((".yml", ".yaml", ".YML", ".YAML")):
        with open(filepath, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")
