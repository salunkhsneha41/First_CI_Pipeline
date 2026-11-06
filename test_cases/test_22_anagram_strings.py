import importlib.util
from pathlib import Path

p = Path(__file__).parent.parent / "codes" / "22_anagram_strings.py"
spec = importlib.util.spec_from_file_location("program", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_anagram():
    assert m.is_anagram("listen", "silent") == True


def test_not_anagram():
    assert m.is_anagram("hello", "world") == False


def test_uppercase():
    assert m.is_anagram("Listen", "Silent") == True


def test_spaces():
    assert m.is_anagram("dormitory", "dirty room") == True


def test_empty():
    assert m.is_anagram("", "") == True