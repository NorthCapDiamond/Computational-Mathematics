from math_util.function_util.function_methods import *
from math_util.integrate_methods.runge_rule import runge_rule
from system_util.IO import *


def integrate_simpson_method_user(equation):
    a, b = enter_interval()
    n = enter_number_of_partitions()
    print(integrate_simpson_method(equation, a, b, n))
    error(equation, a, b, n)


def integrate_simpson_method(equation, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n

    answer = function(a, equation) + function(b, equation)
    a += h

    for i in range(1, n):
        if not (i % 2):
            tmp = function(a, equation)
            answer += 2 * tmp
        elif i % 2:
            tmp = function(a, equation)
            answer += 4 * tmp
        a += h
    return (answer * h) / 3


def error(equation, a, b, n):
    runge_rule(integrate_simpson_method(equation, a, b, n), integrate_simpson_method(equation, a, b, n), 4)
