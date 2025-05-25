from pathlib import Path
import json
import os
import yaml


def get_file_extension(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()

    if ext == ".json":
        return "json"
    if ext in (".yml", ".yaml"):
        return "yaml"
    raise ValueError(f"Неизвестное расширение файла: {filepath}")


def parse_content(content: str, filetype: str):
    if filetype == "json":
        return json.loads(content)
    elif filetype == "yaml":
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {filetype}")


def parse_file(filepath: str):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл '{filepath}' не найден.")

    filetype = get_file_extension(filepath)

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    return parse_content(content, filetype)
