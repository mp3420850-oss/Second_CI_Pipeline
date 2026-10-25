
import importlib

module = importlib.import_module("40_gcd")


def test_simple_gcd():
    assert module.gcd(12, 18) == 6


def test_coprime_numbers():
    assert module.gcd(7, 13) == 1


def test_same_numbers():
    assert module.gcd(10, 10) == 10


def test_first_number_zero():
    assert module.gcd(0, 5) == 5


def test_second_number_zero():
    assert module.gcd(8, 0) == 8


def test_negative_numbers():
    assert module.gcd(-12, 18) == 6


def test_both_zero():
    assert module.gcd(0, 0) == 0
