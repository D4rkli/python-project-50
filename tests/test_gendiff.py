import pytest
from hexlet_code import generate_diff

def test_generate_diff():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"

expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    result = generate_diff(file1_path, file2_path)

    assert result.strip() == expected_output.strip()
