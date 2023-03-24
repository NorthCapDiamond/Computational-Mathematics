import sys


def function(coefficients, x):
    answer = 0
    for i in range(len(coefficients)):
        answer += coefficients[i] * (x ** i)
    return answer


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


def check_interval(coefficients, edges):
    if function(coefficients, edges[0]) * function(coefficients, edges[1]) >= 0:
        sys.exit("Invalid interval")
