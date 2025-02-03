import pytest
from gendiff.generate_diff import generate_diff

@pytest.mark.parametrize("file1, file2, expected_output", [
    ("tests/test_data/file1.json", "tests/test_data/file2.json", "tests/test_data/expected_output.txt"),
    ("tests/test_data/file1.yml", "tests/test_data/file2.yml", "tests/test_data/expected_output.txt"),
])
def test_generate_diff(file1, file2, expected_output):
    with open(expected_output, "r") as expected_file:
        expected = expected_file.read().strip()

    result = generate_diff(file1, file2)
    assert result.strip() == expected
