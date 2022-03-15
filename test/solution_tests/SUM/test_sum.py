from solutions.SUM import sum_solution
from errors.SUM_R1_errors import NotAnInteger
import pytest


def test_sum_solution_adds_values():
    assert sum_solution(1, 2) == 3


def test_sum_solution_rejects_non_integers():
    with pytest.raises(NotAnInteger) as exc_info:
        sum_solution('a', 10)
