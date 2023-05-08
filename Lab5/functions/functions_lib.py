import math


def f_from_variant(x):
    return (4 * x) / (x ** 4 + 3)


def f_linear(x):
    return x + 12


def f_2nd(x):
    return x * x + 2 * x + 1


def f_3rd(x):
    return x ** 3 + x - 10


def f_exp(x):
    return math.e ** (x ** 2 - x + 1)


def f_log(x):
    if x <= 0:
        return 0
    else:
        return math.log(x, 2) + math.log(x, 3)


def f_power(x):
    return x ** 5 + x ** 2 - x + 10000
