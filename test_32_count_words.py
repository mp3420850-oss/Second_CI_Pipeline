
import importlib

module = importlib.import_module("32_count_words")


def test_simple_sentence():
    assert module.count_words("I love Python") == 3


def test_single_word():
    assert module.count_words("Hello") == 1


def test_empty_sentence():
    assert module.count_words("") == 0


def test_multiple_spaces():
    assert module.count_words("I   love   Python") == 3


def test_leading_trailing_spaces():
    assert module.count_words("  Hello World  ") == 2
