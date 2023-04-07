from math_util.function_util.function_methods import *
from math_util.integrate_methods.runge_rule import runge_rule
from system_util.IO import *


def integrate_trapeze_method_user(equation):
    a, b = enter_interval()
    n = enter_number_of_partitions()
    print(integrate_trapeze_method(equation, a, b, n))
    error(equation, a, b, n)


def integrate_trapeze_method(equation, a, b, n):
    h = (b - a) / n
    answer = (function(a, equation) + function(b, equation)) / 2
    a += h
    n -= 1

    while a < b and n >= 1:
        tmp = function(a, equation)
        answer += tmp
        a += h
        n -= 1
    answer *= h

    return answer


def error(equation, a, b, n):
    runge_rule(integrate_trapeze_method(equation, a, b, n), integrate_trapeze_method(equation, a, b, 2 * n), 2)
