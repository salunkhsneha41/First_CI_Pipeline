import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "29_armstrong_number.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_three_digit():
    assert m.is_armstrong(153) == True

def test_single_digit():
    assert m.is_armstrong(5) == True

def test_not_armstrong():
    assert m.is_armstrong(123) == False

def test_zero():
    assert m.is_armstrong(0) == True

def test_negative():
    assert m.is_armstrong(-153) == False