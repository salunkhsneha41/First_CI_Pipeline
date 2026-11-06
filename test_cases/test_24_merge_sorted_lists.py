import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "24_merge_sorted_lists.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_empty_first():
    assert m.merge_sorted_lists([], [1, 2]) == [1, 2]

def test_empty_second():
    assert m.merge_sorted_lists([1, 2], []) == [1, 2]

def test_both_empty():
    assert m.merge_sorted_lists([], []) == []

def test_duplicates():
    assert m.merge_sorted_lists([1, 2], [2, 3]) == [1, 2, 2, 3]