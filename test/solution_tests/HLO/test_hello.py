from lib.solutions.HLO.hello_solution import hello
from errors.HLO_R1_errors import NotAString
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


@pytest.mark.parametrize(
    'input, expected_error, expected_error_message',
    [
        (["Grace"], pytest.raises(NotAString), '["Grace"] is not a string.'),
    ]
)
def test_hello_solution(input, expected_error, expected_error_message):
    with expected_error as exc_info:
        hello(input)
    if exc_info or expected_error_message:
        assert exc_info.value.message == expected_error_message






