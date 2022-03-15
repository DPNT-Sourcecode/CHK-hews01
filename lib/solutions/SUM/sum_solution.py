# noinspection PyShadowingBuiltins,PyUnusedLocal
from errors.SUM_R1_errors import NotAnInteger, OutOfRange


def compute(int_1, int_2):

    int_list = [int_1, int_2]
    lower_limit = 1
    upper_limit = 100

    for integer in int_list:
        if not isinstance(integer, int):
            raise Exception
        if not lower_limit <= integer <= upper_limit:
            raise Exception

    int_sum = int_1 + int_2
    return int_sum


