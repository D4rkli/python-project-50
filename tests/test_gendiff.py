import pytest
from hexlet_code import generate_diff

def test_generate_diff():
    expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    assert generate_diff("tests/test_data/file1.json", "tests/test_data/file2.json") == expected
