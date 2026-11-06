import importlib.util
from pathlib import Path
import pytest

p = Path(__file__).parent.parent / "codes" / "25_max_min_list.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.find_max_min([4, 1, 9, 2]) == (9, 1)

def test_single():
    assert m.find_max_min([5]) == (5, 5)

def test_negative():
    assert m.find_max_min([-2, -5, -1]) == (-1, -5)

def test_duplicates():
    assert m.find_max_min([3, 3, 3]) == (3, 3)

def test_empty():
    with pytest.raises(ValueError):
        m.find_max_min([])