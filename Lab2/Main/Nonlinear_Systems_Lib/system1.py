import numpy as np
from matplotlib import pyplot as plt
from Linear_Systems.gauss import gauss
from System_Utils.parsers import *


def system1():
    epsilon = parse_float_array(input("Enter epsilon\n").replace(",", ".").split())[0]
    print("x*x + y*y = 4")
    print("y = 3*x*x")
    a = np.arange(-2, 2, 0.01)
    t = np.arange(0, 2 * np.pi, 0.01)
    r = 4
    plt.plot(a, 3 * a * a, r * np.sin(t), r * np.cos(t), lw=3)
    plt.axis('equal')
    plt.show()

    user_input = input("Enter x0, y0\n").replace(",", ".").split()
    x_first, y_first = parse_float_array(user_input)
    iteration_sys1(x_first, y_first, epsilon)


def generate_matrix_sys1(x, y):
    return [[2 * x, 2 * y, 4 - x * x - y * y], [-6 * x, 1, 3 * x * x - y]]


def iteration_sys1(x, y, epsilon):
    dx, dy = gauss(generate_matrix_sys1(x, y))
    xi = x + dx
    yi = y + dy

    while abs(x - xi) > epsilon or abs(y - yi) > epsilon:
        iteration_sys1(xi, yi, epsilon)
        return

    print("|x-xi|: " + str(abs(x - xi)) + " |y-yi|: " + str(abs(y - yi)))
    x = xi
    y = yi
    print("x: " + str(x) + " y: " + str(y))
    print("Check: x_i, y_i -> equations")
    print(x * x + y * y - 4)
    print(y - 3 * x * x)
    return
