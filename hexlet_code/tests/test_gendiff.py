import json
from hexlet_code import generate_diff


def test_gendiff():
    with open('tests/test_data/file1.json') as f1:
        file1_data = json.load(f1)
    with open('tests/test_data/file2.json') as f2:
        file2_data = json.load(f2)

    expected_output = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

    result = generate_diff("tests/test_data/file1.json", "tests/test_data/file2.json")

    assert result.strip() == expected_output.strip()
