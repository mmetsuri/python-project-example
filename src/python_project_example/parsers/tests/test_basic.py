from python_project_example.parsers.basic import parse_str

def test_parsing():
    assert parse_str('tuuba pasuuna') == ['tuuba', 'pasuuna']