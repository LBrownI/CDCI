from rut import validate

def test_valid_rut():
    assert validate("21.063.252-2") is True  # Valid RUT

def test_invalid_rut():
    assert validate("12345678-0") is False  # Wrong digit
    assert validate ("123456789") is False   # Missing dash
    assert validate("invalid") is False     # Non-numeric