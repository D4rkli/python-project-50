import json
import os
import yaml


def read_file(filepath):
    """Определяет формат файла и парсит его."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл '{filepath}' не найден.")

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def parse_content(content:str, filepath: str):
    if filepath.endswith((".json", ".JSON")):
        return json.loads(content)
    elif filepath.endswith((".yml", ".yaml", ".YML", ".YAML")):
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {filepath}")


def parse_file(filepath):
    content = read_file(filepath)
    return parse_content(content, filepath)