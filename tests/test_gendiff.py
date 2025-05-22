import pytest
from pathlib import Path
from gendiff.generate_diff import generate_diff


FIXTURES_DIR = Path("tests/fixtures")


def fixture_path(name: str) -> Path:
    return FIXTURES_DIR / name


def read_fixture(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, fixture_file, format_name",
    [
        (
                fixture_path("file1.json"),
                fixture_path("file2.json"),
                fixture_path("expected_output_stylish.txt"),
                "stylish",
        ),
        (
                fixture_path("file1.yml"),
                fixture_path("file2.yml"),
                fixture_path("expected_output_stylish.txt"),
                "stylish",
        ),
        (
                fixture_path("nested_file1.json"),
                fixture_path("nested_file2.json"),
                fixture_path("expected_output_plain.txt"),
                "plain",
        ),
        (
                fixture_path("nested_file1.yml"),
                fixture_path("nested_file2.yml"),
                fixture_path("expected_output_plain.txt"),
                "plain",
        ),
        (
                fixture_path("nested_file1.json"),
                fixture_path("nested_file2.json"),
                fixture_path("expected_output_json.txt"),
                "json",
        ),
        (
                fixture_path("nested_file1.json"),
                fixture_path("nested_file2.json"),
                fixture_path("expected_nested_diff.txt"),
                "stylish",
        ),
    ],
)
def test_generate_diff(file1, file2, fixture_file, format_name):
    result = generate_diff(str(file1), str(file2), format_name)
    expected_output = read_fixture(fixture_file)
    assert result == expected_output