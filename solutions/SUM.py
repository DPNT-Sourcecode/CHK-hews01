from errors.SUM_R1_errors import NotAnInteger, OutOfRange


def sum_solution(int_1, int_2):

    int_list = [int_1, int_2]
    lower_limit = 1
    upper_limit = 100

    for integer in int_list:
        if not isinstance(integer, int):
            raise NotAnInteger(integer)
        if not lower_limit <= integer <= upper_limit:
            raise OutOfRange(integer, lower_limit, upper_limit)

    int_sum = int_1 + int_2
    return int_sum



