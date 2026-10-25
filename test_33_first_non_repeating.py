
import importlib

module = importlib.import_module("33_first_non_repeating")


def test_simple_string():
    assert module.first_non_repeating("programming") == "p"


def test_repeating_characters():
    assert module.first_non_repeating("aabbc") == "c"


def test_all_repeating():
    assert module.first_non_repeating("aabb") is None


def test_single_character():
    assert module.first_non_repeating("x") == "x"


def test_empty_string():
    assert module.first_non_repeating("") is None
