from system_util.IO import *
from math_util.function_util.function_methods import *
from math_util.integrate_methods.runge_rule import runge_rule


def integrate_cell_method_user(equation):
    a, b = enter_interval()
    n = enter_number_of_partitions()
    side = enter_left_right_center()
    print(integrate_cell_method(equation, a, b, n, side))
    error(equation, a, b, n, side)


def integrate_cell_method(equation, a, b, n, side):
    h = (b - a) / n
    answer = 0

    if side == "center":
        a += h / 2
    elif side == "right":
        a += h

    while a < b and n >= 1:
        answer += function(a, equation)
        a += h
        n -= 1
    answer *= h
    return answer


def error(equation, a, b, n, side):
    runge_rule(integrate_cell_method(equation, a, b, n, side), integrate_cell_method(equation, a, b, 2 * n, side), 2)
    return
