from lib.solutions.CHK.checkout_solution import checkout
import pytest
from contextlib import contextmanager


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    'input_value,expected_value',
    [
        ('A', 50),
        ('B', 30),
        ('C', 20),
        ('D', 15),
        ('E', 40),
        ('F', 10),
        ('G', 20),
        ('H', 10),
        ('I', 35),
        ('J', 60),
        ('K', 80),
        ('L', 90),
        ('M', 15),
        ('N', 40),
        ('O', 10),
        ('P', 50),
        ('Q', 30),
        ('R', 50),
        ('S', 30),
        ('T', 20),
        ('U', 40),
        ('V', 50),
        ('W', 20),
        ('X', 90),
        ('Y', 10),
        ('Z', 50),
        ('s', -1),
        (34234, -1),
    ]
)
def test_checkout_solution(input_value, expected_value):
    assert checkout(input_value) == expected_value


@pytest.mark.parametrize(
    'input_value,expected_value',
    [
        ('AA', 100),
        ('ABCD', 115),
        ('AAA', 130),
        ('BB', 45),
        ('AAAAA', 200),
        ('AAAAAA', 250),
        ('AAAAAAAAA', 380),
        ('BBBBB', 120),
        ('HHHHHHHHHHHHHHH', 125),
        ('KKK', 230),
        ('PPPPPP', 250),
        ('QQQQQQQ', 190),
        ('VVVVV', 220)
    ]
)
def test_checkout_solution_multibuy(input_value, expected_value):
    assert checkout(input_value) == expected_value


@pytest.mark.parametrize(
    'input_value,expected_value',
    [
        ('EEB', 80),
        ('EEEB', 120),
        ('EEEEBB', 160),
        ('F', 10),
        ('FF', 20),
        ('FFF', 20),
        ('FFFF', 30),
        ('FFFFFF', 40),
        ('NNNM', 120),
        ('RRRRRRQ', 300),
        ("UUU", 120),
        ("UUUU", 120)
    ]
)
def test_checkout_solution_free_item(input_value, expected_value):
    assert checkout(input_value) == expected_value


@pytest.mark.parametrize(
    'input_value,expected_value',
    [
        ('STXYZ', 45),
    ]
)
def test_checkout_solution_grouped_items(input_value, expected_value):
    assert checkout(input_value) == expected_value