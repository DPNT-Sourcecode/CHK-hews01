from lib.solutions.CHK import checkout_solution
import pytest
from contextlib import contextmanager


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    'input, expected_value',
    [
        ('A', 50),
    ]
)
def test_checkout_solution(input, expected_value):
    assert checkout_solution(input) == expected_value



