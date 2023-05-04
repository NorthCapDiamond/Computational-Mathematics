import math
from system_utils.IO import *
from systems_of_equations.gauss import *


def power_approximation_formula():
    return "Power", "phi(x) = ax^b"


def power_approximation_interval_user(f):
    a, b = enter_interval()
    h = enter_float("Enter h")
    power_approximation_function_interval(a, b, h, f)


def power_approximation_array_user():
    X = enter_float_array("Enter float array of X")
    Y = enter_float_array("Enter float array of Y")
    if len(X) != len(Y):
        sys.exit("X and Y nust have the same length!")
    power_approximation_function_array(X, Y)


def power_approximation_function_interval(a, b, h, f):
    # will make this linear
    # fill the parameters for creating the system pf linear equations
    x = a
    SX = 0
    SXX = 0
    SY = 0
    SXY = 0
    n = (b - a) / h

    while x < b:
        SX += math.log(x, math.e)
        SXX += math.log(x, math.e)**2
        SY += math.log(f(x), math.e)
        SXY += math.log(x, math.e) * math.log(f(x), math.e)
        x += h
    matrix_of_equations = [[SXX, SX, SXY], [SX, n, SY]]
    gauss_answer = gauss(matrix_of_equations)
    a = gauss_answer[1]
    b = gauss_answer[0]

    def approx_func(X):
        return math.e**a * X**b

    return approx_func, a, b


def power_approximation_function_array(X, Y):
    # will make this linear
    # fill the parameters for creating the system pf linear equations
    SX = 0
    SXX = 0
    SY = 0
    SXY = 0
    n = len(X)
    for i in range(n):
        x = X[i]
        SX += math.log(x, math.e)
        SXX += math.log(x, math.e)**2
        SY += math.log(Y[i], math.e)
        SXY += math.log(x, math.e) * math.log(Y[i], math.e)
    matrix_of_equations = [[SXX, SX, SXY], [SX, n, SY]]
    gauss_answer = gauss(matrix_of_equations)
    a = gauss_answer[1]
    b = gauss_answer[0]

    def approx_func(X_f):
        return math.e**a * X_f**b

    return approx_func, a, b

