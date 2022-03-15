from errors.SUM_R1_errors import NotAnInteger, OutOfRange


def sum_solution(int_1, int_2):

    int_list = [int_1, int_2]

    for integer in int_list:
        if not isinstance(integer, int):
            raise NotAnInteger(integer)
        if not 1 >= integer >= 100:
            raise OutOfRange

    int_sum = int_1 + int_2
    return int_sum


