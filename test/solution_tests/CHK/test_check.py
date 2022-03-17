from lib.solutions.CHK.checkout_solution import checkout
import pytest
from contextlib import contextmanager


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    'input_value, expected_value',
    [
        ('A', 50),
        ('B', 30),
    ]
)
def test_checkout_solution(input_value, expected_value):
    assert checkout(input_value) == expected_value




