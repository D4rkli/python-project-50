import pytest
from hexlet_code import generate_diff

def test_generate_diff():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    file1_yaml = "tests/test_data/file1.yml"
    file2_yaml = "tests/test_data/file2.yml"

    expected_output = (
	"""{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    )

    assert generate_diff(file1_path, file2_path).strip() == expected_output.strip()
    assert generate_diff(file1_yaml, file2_yaml).strip() == expected_output.strip()
