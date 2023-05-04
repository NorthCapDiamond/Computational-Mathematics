from system_utils.IO import *
from systems_of_equations.gauss import *


def cube_approximation_formula():
    return "Cube", "phi(x) = a_2 * x^2 + a_1 * x + a_0"


def cube_approximation_interval_user(f):
    a, b = enter_interval()
    h = enter_float("Enter h")
    cube_approximation_function_interval(a, b, h, f)


def cube_approximation_array_user():
    X = enter_float_array("Enter float array of X")
    Y = enter_float_array("Enter float array of Y")
    if len(X) != len(Y):
        sys.exit("X and Y nust have the same length!")
    cube_approximation_function_array(X, Y)


def cube_approximation_function_interval(a, b, h, f):
    sum_xi = 0
    sum_xi2 = 0
    sum_xi3 = 0
    sum_xi4 = 0
    sum_xi5 = 0
    sum_xi6 = 0
    sum_yi = 0
    sum_xi_yi = 0
    sum_xi2_yi = 0
    sum_xi3_yi = 0

    n = (b - a) / h
    x = a
    while x <= b:
        sum_xi += x
        sum_xi2 += x ** 2
        sum_xi3 += x ** 3
        sum_xi4 += x ** 4
        sum_xi5 += x ** 5
        sum_xi6 += x ** 6

        sum_yi += f(x)
        sum_xi_yi += x * f(x)
        sum_xi2_yi += x * x * f(x)
        sum_xi3_yi += x ** 3 * f(x)
        x += h
    matrix_of_equations = [[n, sum_xi, sum_xi2, sum_xi3, sum_yi], [sum_xi, sum_xi2, sum_xi3, sum_xi4, sum_xi_yi],
                           [sum_xi2, sum_xi3, sum_xi4, sum_xi5, sum_xi2_yi],
                           [sum_xi3, sum_xi4, sum_xi5, sum_xi6, sum_xi3_yi]]
    gauss_answer = gauss(matrix_of_equations)

    a, b, c, d = gauss_answer[3], gauss_answer[2], gauss_answer[1], gauss_answer[0]

    def approx_func(X_f):
        return a * X_f * X_f * X_f + b * X_f * X_f + c * X_f + d

    return approx_func, a, b, c, d


def cube_approximation_function_array(X, Y):
    sum_xi = 0
    sum_xi2 = 0
    sum_xi3 = 0
    sum_xi4 = 0
    sum_xi5 = 0
    sum_xi6 = 0
    sum_yi = 0
    sum_xi_yi = 0
    sum_xi2_yi = 0
    sum_xi3_yi = 0

    n = len(X)
    for i in range(n):
        x = X[i]
        sum_xi += x
        sum_xi2 += x ** 2
        sum_xi3 += x ** 3
        sum_xi4 += x ** 4
        sum_xi5 += x ** 5
        sum_xi6 += x ** 6

        sum_yi += Y[i]
        sum_xi_yi += x * Y[i]
        sum_xi2_yi += x * x * Y[i]
        sum_xi3_yi += x ** 3 * Y[i]
    matrix_of_equations = [[n, sum_xi, sum_xi2, sum_xi3, sum_yi], [sum_xi, sum_xi2, sum_xi3, sum_xi4, sum_xi_yi],
                           [sum_xi2, sum_xi3, sum_xi4, sum_xi5, sum_xi2_yi],
                           [sum_xi3, sum_xi4, sum_xi5, sum_xi6, sum_xi3_yi]]
    gauss_answer = gauss(matrix_of_equations)

    a, b, c, d = gauss_answer[3], gauss_answer[2], gauss_answer[1], gauss_answer[0]

    def approx_func(X_f):
        return a * X_f * X_f * X_f + b * X_f * X_f + c * X_f + d

    return approx_func, a, b, c, d
