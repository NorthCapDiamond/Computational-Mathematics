import numpy as np
from matplotlib import pyplot as plt


def draw_graph(coefficients, leftBound, rightBound):
    # 100000 linearly spaced numbers
    x = np.linspace(leftBound, rightBound, 100000)

    # the function
    y = 0
    for i in range(len(coefficients)):
        y += coefficients[i] * (x ** i)

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x, y, 'r')

    # show the plot
    plt.show()
    return