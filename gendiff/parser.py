import json
import os

import yaml

DEFAULT_PATH = "tests/test_data/"


def parse_file(filepath):
    """Определяет формат файла и парсит его."""
    if not os.path.exists(filepath):

        filepath = os.path.join(DEFAULT_PATH, filepath)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл '{filepath}' не найден.")

    if filepath.endswith((".json", ".JSON")):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    elif filepath.endswith((".yml", ".yaml", ".YML", ".YAML")):
        with open(filepath, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {filepath}")
