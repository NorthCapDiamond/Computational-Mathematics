from System_Utils import graph_util
from System_Utils.parsers import *


def half_division(equation, interval):
    graph_util.draw_graph(equation, -5, 5)
    check_interval(equation, interval)
    epsilon = parse_float_array(input("Enter epsilon\n").replace(",", ".").split())[0]
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
    graph_util.draw_graph(equation, -5, 5)
    check_interval(equation, interval)
    epsilon = parse_float_array(input("Enter epsilon\n").replace(",", ".").split())[0]
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
    graph_util.draw_graph(equation, -5, 5)
    check_interval(equation, interval)
    epsilon = parse_float_array(input("Enter epsilon\n").replace(",", ".").split())[0]
    equation = list(equation)
    x_prev = interval[0]
    x_next = interval[1]

    while abs(x_next - x_prev) > epsilon:
        tmp = x_next
        x_next = x_next - (1 / iteration_derivative(equation, x_next, x_prev)) * function(equation, x_next)
        x_prev = tmp

    return x_next
