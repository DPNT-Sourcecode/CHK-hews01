from lib.solutions.SUM.sum_solution import compute
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
def test_sum_solution_adds_values(value_1, value_2, expected_value):
    assert compute(value_1, value_2) == expected_value


@pytest.mark.parametrize(
    'value_1, value_2, expected_error',
    [
        (1, 2, does_not_raise()),
        ('a', 10, pytest.raises(Exception)),
        ([], 10, pytest.raises(Exception)),
        ({}, 10, pytest.raises(Exception)),
        (3, 1000.3, pytest.raises(Exception)),
        ((2, 3, 4), 1, pytest.raises(Exception)),
    ]
)
def test_sum_solution_only_accepts_integers(value_1, value_2, expected_error):
    with expected_error:
        compute(value_1, value_2)


@pytest.mark.parametrize(
    'value_1, value_2, expected_error',
    [
        (100, 1, does_not_raise()),
        (-1, 2, pytest.raises(Exception)),
        (1, 200, pytest.raises(Exception)),
        (1000, 5, pytest.raises(Exception)),
        (-1000, 9999999999999, pytest.raises(Exception)),
        (100, 0, pytest.raises(Exception)),
    ]
)
def test_sum_solution_only_accepts_value_within_range(value_1, value_2, expected_error):
    with expected_error:
        compute(value_1, value_2)





