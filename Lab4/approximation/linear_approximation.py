from system_utils.IO import *
from systems_of_equations.gauss import *


def linear_approximation_formula():
    return "Linear", "phi(x) = ax + b"


def linear_approximation_interval_user(f):
    a, b = enter_interval()
    h = enter_float("Enter h")
    linear_approximation_function_interval(a, b, h, f)


def linear_approximation_array_user():
    X = enter_float_array("Enter float array of X")
    Y = enter_float_array("Enter float array of Y")
    if len(X) != len(Y):
        sys.exit("X and Y nust have the same length!")
    linear_approximation_function_array(X, Y)


def linear_approximation_function_interval(a, b, h, f):
    # fill the parameters for creating the system pf linear equations
    x = a
    SX = 0
    SXX = 0
    SY = 0
    SXY = 0
    n = (b - a) / h

    while x <= b:
        SX += x
        SXX += x * x
        SY += f(x)
        SXY += x * f(x)
        x += h

    matrix_of_equations = [[SXX, SX, SXY], [SX, n, SY]]
    gauss_answer = gauss(matrix_of_equations)
    a = gauss_answer[0]
    b = gauss_answer[1]

    def approx_func(X):
        return a * X + b
    return approx_func, a, b


def linear_approximation_function_array(X, Y):
    # fill the parameters for creating the system pf linear equations
    SX = 0
    SXX = 0
    SY = 0
    SXY = 0
    n = len(X)

    for i in range(n):
        x = X[i]
        SX += x
        SXX += x * x
        SY += Y[i]
        SXY += x * Y[i]

    matrix_of_equations = [[SXX, SX, SXY], [SX, n, SY]]
    gauss_answer = gauss(matrix_of_equations)
    a = gauss_answer[0]
    b = gauss_answer[1]

    def approx_func(X_ans):
        return a * X_ans + b

    return approx_func, a, b
