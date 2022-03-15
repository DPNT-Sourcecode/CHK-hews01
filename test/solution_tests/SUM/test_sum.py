from solutions.SUM import sum_solution
from errors.SUM_R1_errors import NotAnInteger
import pytest


def test_sum_solution_adds_values():
    assert sum_solution(1, 2) == 3


@pytest.mark.parametrize(
    'value_1, value_2, expected_error',
    [
        pytest.param('a', 10, pytest.raises(NotAnInteger), id="string and integer")
    ]
)
def test_sum_solution_rejects_non_integers(value_1, value_2, expected_error):
    with expected_error:
        sum_solution(value_1, value_2)


