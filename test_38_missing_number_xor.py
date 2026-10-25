
import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_middle():
    assert module.missing_number([1, 2, 4, 5], 5) == 3


def test_missing_first():
    assert module.missing_number([2, 3, 4, 5], 5) == 1


def test_missing_last():
    assert module.missing_number([1, 2, 3, 4], 5) == 5


def test_single_number():
    assert module.missing_number([], 1) == 1


def test_unsorted_list():
    assert module.missing_number([4, 1, 5, 2], 5) == 3


def test_large_sequence():
    assert module.missing_number(
        [1, 2, 3, 4, 6, 7, 8, 9, 10], 10
    ) == 5
