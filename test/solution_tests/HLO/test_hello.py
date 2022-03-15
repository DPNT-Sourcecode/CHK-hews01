from lib.solutions.HLO.hello_solution import hello
import pytest
from contextlib import contextmanager


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    'input, expected_output',
    [
        ("Grace", "Hello Grace"),
        ("Tom", "Hello Tom"),
    ]
)
def test_hello_solution(input, expected_output):
    assert hello(input) == expected_output







