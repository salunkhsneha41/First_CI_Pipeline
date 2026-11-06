import importlib.util
from pathlib import Path
import pytest

p = Path(__file__).parent.parent / "codes" / "30_decimal_to_binary.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.decimal_to_binary(10) == "1010"

def test_zero():
    assert m.decimal_to_binary(0) == "0"

def test_one():
    assert m.decimal_to_binary(1) == "1"

def test_eight():
    assert m.decimal_to_binary(8) == "1000"

def test_negative():
    with pytest.raises(ValueError):
        m.decimal_to_binary(-5)