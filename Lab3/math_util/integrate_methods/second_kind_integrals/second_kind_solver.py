import sys
import numpy as np
from sympy import *

from system_util.IO import enter_number_of_partitions

infy = np.inf
n = 1000


def simply_calculate_limit(f, a, b):
    f = sympify(f)
    x = symbols('x')
    return integrate(abs(f), (x, a, b))


def simply_calculate_integral(f, a, b):
    f = sympify(f)
    x = symbols('x')
    return integrate(f, (x, a, b))


def check_integral(f, a, b):
    if simply_calculate_integral(f, a, b) is None:
        return False
    return True


def check_limit(f, a, b):
    if simply_calculate_limit(f, a, b) == infy:
        return False
    return True


def check_integral_for_convergence(f, a, b):
    f = sympify(f)
    if check_integral(f, a, b) and check_limit(f, a, b):
        return
    sys.exit("!!!integral contains convergences!!!")


def merge_calculator(f, a, b):
    check_integral_for_convergence(f, a, b)
    f = lambdify("x", sympify(f))

    def merger(f, a, b):
        # we will divide intervals:
        middle = (a + b) / 2
        if a > b:
            a, b = b, a
        h = (b - a) / (n - 2)
        x = np.linspace(a, b, n)[1:-1]
        y = f(x)

        iterator = zip(x, y)

        if not np.isfinite(y).all():
            i_answer = 0
            for (i, j) in iterator:
                if not np.isfinite(j):
                    i_answer += merger(f, a, x)
                    a = x
            i_answer += merger(f, a, b)
            return i_answer

        left_part = np.sum(y[:len(x) // 2])
        right_part = np.sum(y[len(x) // 2:])

        i_answer = left_part + right_part
        i_answer *= h

        return i_answer

    with np.errstate(divide='ignore'):
        return merger(f, a, b)


def tests():
    print("enter amount of intervals")
    n = enter_number_of_partitions()

    equation0 = "1/x"
    equation4 = "1/(x-1)"
    equation1 = "1/sqrt(x**5)"
    equation2 = "1/sqrt(x)"
    equation3 = "log(x)"

    print(equation0)
    print(merge_calculator(equation0, -5, 5))
    print(equation4)
    print(merge_calculator(equation4, -2, 4))
    print(equation2)
    print(merge_calculator(equation2, 0, 1))
    print(equation3)
    print(merge_calculator(equation3, 0, 1))
    print(equation1)
    print(merge_calculator(equation1, 0, 1))
