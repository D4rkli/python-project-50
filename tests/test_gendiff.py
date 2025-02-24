import pytest
from pathlib import Path
from gendiff.generate_diff import generate_diff


FIXTURES_DIR = Path(__file__).parent / "fixtures"

def read_fixture(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, fixture_file, format_name",
    [
        (
            FIXTURES_DIR / "file1.json",
            FIXTURES_DIR / "file2.json",
            FIXTURES_DIR / "expected_output_stylish.txt",
            "stylish",
        ),
        (
            FIXTURES_DIR / "file1.yml",
            FIXTURES_DIR / "file2.yml",
            FIXTURES_DIR / "expected_output_stylish.txt",
            "stylish",
        ),
        (
            FIXTURES_DIR / "nested_file1.json",
            FIXTURES_DIR / "nested_file2.json",
            FIXTURES_DIR / "expected_output_plain.txt",
            "plain",
        ),
        (
            FIXTURES_DIR / "nested_file1.yml",
            FIXTURES_DIR / "nested_file2.yml",
            FIXTURES_DIR / "expected_output_plain.txt",
            "plain",
        ),
        (
            FIXTURES_DIR / "nested_file1.json",
            FIXTURES_DIR / "nested_file2.json",
            FIXTURES_DIR / "expected_output_json.txt",
            "json",
        ),
        (
            FIXTURES_DIR / "nested_file1.json",
            FIXTURES_DIR / "nested_file2.json",
            FIXTURES_DIR / "expected_nested_diff.txt",
            "stylish",
        ),
    ],
)
def test_generate_diff(file1, file2, fixture_file, format_name):
    result = generate_diff(str(file1), str(file2), format_name)
    expected_output = read_fixture(fixture_file)
    assert result == expected_output