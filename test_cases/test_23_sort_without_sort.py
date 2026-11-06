import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "23_sort_without_sort.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.bubble_sort([5, 2, 8, 1]) == [1, 2, 5, 8]

def test_already_sorted():
    assert m.bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert m.bubble_sort([3, 2, 1]) == [1, 2, 3]

def test_empty():
    assert m.bubble_sort([]) == []

def test_duplicates():
    assert m.bubble_sort([4, 2, 4, 1]) == [1, 2, 4, 4]