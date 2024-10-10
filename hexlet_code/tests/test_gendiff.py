import json
from hexlet_code import generate_diff


def test_gendiff():
   with open('tests/fixtures/file1.json') as f1:
      file1_data = json.load(f1)
   with open('tests/fixtures/file2.json') as f2:
      file2_data = json.load(f2)

   expected_output = '''{
   - follow: false
   host: hexlet.io
   - proxy: 123.234.53.22
   - timeout: 50
   + timeout: 20
   + verbose: true
   }'''
