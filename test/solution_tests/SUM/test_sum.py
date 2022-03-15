from solutions.SUM import sum_two_integers
from errors.SUM_R1_errors import NotAnInteger, OutOfRange
import pytest
from contextlib import contextmanager


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    'value_1, value_2, expected_value',
    [
        (1, 2, 3),
        (100, 100, 200),
        (100, 1, 101),
    ]
)
def test_sum_two_integers_adds_values(value_1, value_2, expected_value):
    assert sum_two_integers(value_1, value_2) == expected_value


@pytest.mark.parametrize(
    'value_1, value_2, expected_error, expected_error_message',
    [
        (1, 2, does_not_raise(), ''),
        ('a', 10, pytest.raises(NotAnInteger), 'a is not an integer.'),
        ([], 10, pytest.raises(NotAnInteger), '[] is not an integer.'),
        ({}, 10, pytest.raises(NotAnInteger), '{} is not an integer.'),
        (3, 1000.3, pytest.raises(NotAnInteger), '1000.3 is not an integer.'),
        ((2, 3, 4), 1000.3, pytest.raises(NotAnInteger), '(2, 3, 4) is not an integer.')
    ]
)
def test_sum_two_integers_only_accepts_integers(value_1, value_2, expected_error, expected_error_message):
    with expected_error as exc_info:
        sum_two_integers(value_1, value_2)
    if exc_info or expected_error_message:
        assert exc_info.value.message == expected_error_message


@pytest.mark.parametrize(
    'value_1, value_2, expected_error, expected_error_message',
    [
        (100, 1, does_not_raise(), ''),
        (-1, 2, pytest.raises(OutOfRange), '-1 is not between 1 and 100.'),
        (1, 200, pytest.raises(OutOfRange), '200 is not between 1 and 100.'),
        (1000, 5, pytest.raises(OutOfRange), '1000 is not between 1 and 100.'),
        (-1000, 9999999999999, pytest.raises(OutOfRange), '-1000 is not between 1 and 100.'),
        (100, 0, pytest.raises(OutOfRange), '0 is not between 1 and 100.'),
    ]
)
def test_sum_two_integers_only_accepts_value_within_range(value_1, value_2, expected_error, expected_error_message):
    with expected_error as exc_info:
        sum_two_integers(value_1, value_2)
    if exc_info or expected_error_message:
        assert exc_info.value.message == expected_error_message






