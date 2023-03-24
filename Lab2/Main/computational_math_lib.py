from util_lib import *


def derivative(equation):
    new_equation = equation.copy()
    if len(new_equation) == 1:
        return [0]
    for i in range(len(new_equation)):
        new_equation[i] *= i

    return new_equation[1:]


def iteration_derivative(equation, xi, xi_prev):
    derivative_equation = (function(equation, xi) - function(equation, xi_prev)) / (xi - xi_prev)
    return derivative_equation


def half_division(equation, interval):
    check_interval(equation, interval)
    epsilon = float(input("Enter epsilon\n").replace(",", "."))
    a = interval[0]
    b = interval[1]
    x = (a + b) / 2

    current_epsilon = abs(a - b)
    while current_epsilon > epsilon:
        x = (a + b) / 2
        if function(equation, a) * function(equation, x) > 0 > function(equation, b) * function(equation, x):
            a = x
        elif function(equation, b) * function(equation, x) > 0 > function(equation, a) * function(equation, x):
            b = x
        elif function(equation, x) == 0:
            return x
        else:
            sys.exit("Needs a debug in computational_math_lib -> half_division -> while loop")
        current_epsilon = abs(a - b)

    return x


def simple_iteration(equation, interval):
    check_interval(equation, interval)
    epsilon = float(input("Enter epsilon\n").replace(",", "."))
    equation = list(equation)
    a = interval[0]
    b = interval[1]
    derivative_eq = derivative(equation)
    if (function(derivative_eq, a)) > function(derivative_eq, b):
        max_derivative = function(derivative_eq, a)
        xi = a
    else:
        max_derivative = function(derivative_eq, b)
        xi = b
    lambda_var = - 1 / max_derivative
    phi = equation[:]
    for i in range(len(equation)):
        phi[i] *= lambda_var
    if len(phi) < 2:
        phi.append(1)
    else:
        phi[1] += 1

    while abs(function(phi, xi) - xi) > epsilon:
        xi = function(phi, xi)

    return function(phi, xi)


def secant_method(equation, interval):
    check_interval(equation, interval)
    epsilon = float(input("Enter epsilon\n").replace(",", "."))
    equation = list(equation)
    x_prev = interval[0]
    x_next = interval[1]

    while abs(x_next - x_prev) > epsilon:
        tmp = x_next
        x_next = x_next - (1 / iteration_derivative(equation, x_next, x_prev)) * function(equation, x_next)
        x_prev = tmp

    return x_next


def gauss(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(len(matrix)):
                if matrix[j][i] != 0:
                    for k in range(len(matrix) + 1):
                        matrix[i][k] += matrix[j][k]
                    break

    if matrix[len(matrix) - 1][len(matrix) - 1] == 0:
        for i in range(len(matrix)):
            if matrix[i][len(matrix) - 1] != 0:
                for j in range(len(matrix) + 1):
                    matrix[len(matrix)][j] += matrix[i][j]
                break

    # forward stroke

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            c = matrix[j][i] / matrix[i][i]
            for k in range(len(matrix), i - 1, -1):
                matrix[j][k] -= c * matrix[i][k]

    # creating diagonals of ones

    for i in range(len(matrix)):
        tmp = matrix[i][i]
        for j in range(len(matrix) + 1):
            matrix[i][j] /= tmp

    # reverse stroke

    all_x = [0] * len(matrix)
    all_x[len(matrix) - 1] = matrix[len(matrix) - 1][len(matrix)]

    for i in range(len(matrix) - 2, -1, -1):
        all_x[i] = matrix[i][len(matrix)]
        for j in range(i + 1, len(matrix)):
            all_x[i] -= matrix[i][j] * all_x[j]

    return all_x
