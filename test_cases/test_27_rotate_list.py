import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "27_rotate_list.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_zero():
    assert m.rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_full_rotation():
    assert m.rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_empty():
    assert m.rotate_list([], 2) == []

def test_single():
    assert m.rotate_list([5], 2) == [5]