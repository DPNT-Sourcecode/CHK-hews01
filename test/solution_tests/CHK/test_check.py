from lib.solutions.CHK.checkout_solution import checkout
from errors.CHK_R1_errors import NotAString, NotInPriceTable
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
        ('D', 15)
    ]
)
def test_checkout_solution(input_value, expected_value):
    assert checkout(input_value) == expected_value


@pytest.mark.parametrize(
    'input_value, expected_error, expected_error_message',
    [
        (123, pytest.raises(NotAString), "123 is not a string."),
    ]
)
def test_hello_solution_only_accepts_strings(input_value, expected_error, expected_error_message):
    with expected_error as exc_info:
        checkout(input_value)
    if exc_info or expected_error_message:
        assert exc_info.value.message == expected_error_message