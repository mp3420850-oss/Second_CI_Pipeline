
import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_two():
    assert module.rotate_string("Python", 2) == "thonPy"


def test_rotate_one():
    assert module.rotate_string("Hello", 1) == "elloH"


def test_rotate_zero():
    assert module.rotate_string("Python", 0) == "Python"


def test_empty_string():
    assert module.rotate_string("", 3) == ""


def test_full_rotation():
    assert module.rotate_string("abcd", 4) == "abcd"


def test_large_rotation():
    assert module.rotate_string("abcd", 6) == "cdab"
