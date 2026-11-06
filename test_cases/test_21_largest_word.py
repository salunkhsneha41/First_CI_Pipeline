import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "21_largest_word.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_normal():
    assert m.largest_word("Python is very powerful") == "powerful"

def test_single_word():
    assert m.largest_word("Hello") == "Hello"

def test_empty():
    assert m.largest_word("") == ""

def test_punctuation():
    assert m.largest_word("I love programming!") == "programming"

def test_same_length():
    assert m.largest_word("cat dog") == "cat"