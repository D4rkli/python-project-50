import pytest
from gendiff.generate_diff import generate_diff

def read_expected_result(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read().strip()

@pytest.mark.parametrize("file1, file2, expected_output, format_name", [
    ("tests/test_data/file1.json", "tests/test_data/file2.json", "tests/test_data/expected_output_stylish.txt", "stylish"),
    ("tests/test_data/file1.yml", "tests/test_data/file2.yml", "tests/test_data/expected_output_stylish.txt", "stylish"),
    ("tests/test_data/nested_file1.json", "tests/test_data/nested_file2.json", "tests/test_data/expected_output_plain.txt", "plain"),
    ("tests/test_data/nested_file1.yml", "tests/test_data/nested_file2.yml", "tests/test_data/expected_output_plain.txt", "plain"),
])
def test_generate_diff(file1, file2, expected_output, format_name):
    with open(expected_output, "r") as expected_file:
        expected = expected_file.read().strip()

    result = generate_diff(file1, file2, format_name)
    assert result.strip() == expected
