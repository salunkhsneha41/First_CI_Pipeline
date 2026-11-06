import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "26_sum_of_list.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.sum_of_list([1, 2, 3, 4]) == 10

def test_empty():
    assert m.sum_of_list([]) == 0

def test_single():
    assert m.sum_of_list([5]) == 5

def test_negative():
    assert m.sum_of_list([-1, -2, 3]) == 0

def test_zero():
    assert m.sum_of_list([0, 0, 0]) == 0