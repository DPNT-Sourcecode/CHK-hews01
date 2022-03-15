from solutions.SUM import sum_solution
from errors.SUM_R1_errors import NotAnInteger
import pytest


def test_sum_solution_adds_values():
    assert sum_solution(1, 2) == 3


@pytest.mark.parametrize(
    'value_1, value_2, expected_error, expected_error_message',
    [
        ('a', 10, pytest.raises(NotAnInteger), 'a is not an integer.'),
        ([], 10, pytest.raises(NotAnInteger), '[] is not an integer.'),
        ({}, 10, pytest.raises(NotAnInteger), '{} is not an integer.'),
        (3, 1000.3, pytest.raises(NotAnInteger), '1000.3 is not an integer.'),
        ((2, 3, 4), 1000.3, pytest.raises(NotAnInteger), '(2, 3, 4) is not an integer.')
    ]
)
def test_sum_solution_rejects_non_integers(value_1, value_2, expected_error, expected_error_message):
    with expected_error as exc_info:
        sum_solution(value_1, value_2)
    assert exc_info.value.message == expected_error_message
