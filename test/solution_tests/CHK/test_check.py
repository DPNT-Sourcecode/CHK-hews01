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
        ('D', 15),
        ('E', 40),
        ('AA', 100),
        ('ABCD', 115),
        ('AAA', 130),
        ('BB', 45),
        ('AAAAA', 200),
        ('AAAAAA', 250),
        ('s', -1),
        (34234, -1),
    ]
)
def test_checkout_solution(input_value, expected_value):
    assert checkout(input_value) == expected_value


"""@pytest.mark.parametrize(
    'input_value, expected_error, expected_error_message',
    [
        (123, pytest.raises(NotAString), "123 is not a string."),
        (['grace'], pytest.raises(NotAString), "['grace'] is not a string."),
        ({'a': 5}, pytest.raises(NotAString), "{'a': 5} is not a string."),
    ]
)
def test_checkout_only_accepts_strings(input_value, expected_error, expected_error_message):
    with expected_error as exc_info:
        checkout(input_value)
    if exc_info or expected_error_message:
        assert exc_info.value.message == expected_error_message


@pytest.mark.parametrize(
    'input_value, expected_error, expected_error_message',
    [
        ("F", pytest.raises(NotInPriceTable), "F is not an SKU in the price table."),
        ("j75", pytest.raises(NotInPriceTable), "j75 is not an SKU in the price table."),
    ]
)
def test_checkout_only_accepts_known_skus(input_value, expected_error, expected_error_message):
    with expected_error as exc_info:
        checkout(input_value)
    if exc_info or expected_error_message:
        assert exc_info.value.message == expected_error_message
"""

