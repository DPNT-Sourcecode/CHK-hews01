from solutions.SUM import sum_solution
import pytest


def test_sum_solution_adds_values():
    assert sum_solution(1, 2) == 3


def test_sum_solution_accepts_0_to_100():
    assert sum_solution(-1, 10)


