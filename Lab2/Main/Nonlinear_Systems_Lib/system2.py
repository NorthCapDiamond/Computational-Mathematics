import numpy as np
from matplotlib import pyplot as plt
from Linear_Systems.gauss import gauss
from System_Utils.parsers import *


def system2():
    epsilon = parse_float_array(input("Enter epsilon\n").replace(",", ".").split())[0]
    print("2x = y/(1 + y*y)")
    # 2*x + 2*x*y*y - y = 0
    print("2y = x/(1+x*x)")
    # 2*y + 2*y*x*x - x = 0
    # 100 linearly spaced numbers
    x = np.linspace(-np.pi, np.pi, 100)
    t = np.linspace(-np.pi / 1000, np.pi / 1000, 100)

    # the functions, which are y = sin(x) and z = cos(x) here
    y = 2 * x + 2 * x * t * t - t
    z = 2 * x + 2 * x * y * y - y

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the functions
    plt.plot(y)
    plt.plot(z)

    # show the plot
    plt.show()

    user_input = input("Enter x0, y0\n").replace(",", ".").split()
    x_first, y_first = parse_float_array(user_input)
    iteration_sys2(x_first, y_first, epsilon)


def iteration_sys2(x, y, epsilon):
    dx, dy = gauss(generate_matrix_sys2(x, y))
    xi = x + dx
    yi = y + dy

    while abs(x - xi) > epsilon or abs(y - yi) > epsilon:
        iteration_sys2(xi, yi, epsilon)
        return

    print("|x-xi|: " + str(abs(x - xi)) + " |y-yi|: " + str(abs(y - yi)))
    x = xi
    y = yi
    print("x: " + str(x) + " y: " + str(y))
    print("Check: x_i, y_i -> equations")
    print(-2 * x + y / (1 + y * y))
    print(-2 * y + x / (1 + x * x))
    return


def generate_matrix_sys2(x, y):
    return [[2 + 2 * y * y, 4 * x * y - 1, -2 * x - 2 * x * y * y + y],
            [4 * x * y - 1, 2 + 2 * x * x, -2 * y - 2 * y * x * x + x]]
