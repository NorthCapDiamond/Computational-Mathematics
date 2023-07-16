import math


def f1(x, y):
    return x ** 2 + y


def f1_ans(x, y, c):
    return c*math.e ** x - x ** 2 - 2 * x - 2


def f2(x, y):
    return x + y


def f2_ans(x, y, c):
    return c*math.e**x - x - 1


def f3(x, y):
    return math.cos(x) * y


def f3_ans(x, y, c):
    return c*math.e**(math.sin(x))


def f4(x, y):
    return x**5 + (x-1)*(x-2)*(x-3)*(x-4) + 1000*x - 10101010 + y


def f4_ans(x, y, c):
    return c*math.e**x - x**5 - 6*x**4 - 14*x**3 - 77*x**2 - 1104*x + 10099882


def f5(x, y):
    return math.sqrt(x*y)


def f5_ans(x, y, c):
    return 1/36 * (12*c*x**(3/2) + 9*c**2 + 4*x**3)
