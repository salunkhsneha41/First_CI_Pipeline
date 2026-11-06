import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "28_set_intersection.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

def test_no_common():
    assert m.set_intersection({1, 2}, {3, 4}) == set()

def test_same_sets():
    assert m.set_intersection({1, 2}, {1, 2}) == {1, 2}

def test_empty():
    assert m.set_intersection(set(), {1, 2}) == set()

def test_one_common():
    assert m.set_intersection({1, 2}, {2, 3}) == {2}