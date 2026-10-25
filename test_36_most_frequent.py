
import importlib

module = importlib.import_module("36_most_frequent")


def test_simple_list():
    assert module.most_frequent([1, 2, 2, 3]) == 2


def test_all_same():
    assert module.most_frequent([5, 5, 5]) == 5


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None


def test_negative_numbers():
    assert module.most_frequent([-1, -1, 2, 3]) == -1


def test_tie_returns_first():
    assert module.most_frequent([1, 2, 1, 2]) == 1
