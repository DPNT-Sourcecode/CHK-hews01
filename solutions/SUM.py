from errors.SUM_R1_errors import NotAnInteger


def sum_solution(int_1, int_2):
    if isinstance(int_1, int) and isinstance(int_2, int):
        int_sum = int_1 + int_2
        return int_sum
    raise NotAnInteger
