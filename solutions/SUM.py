from errors.SUM_R1_errors import NotAnInteger


def sum_solution(int_1, int_2):
    if not isinstance(int_1, int):
        raise NotAnInteger(int_1)
    if not isinstance(int_2, int):
        raise NotAnInteger(int_2)

    int_sum = int_1 + int_2
    return int_sum

