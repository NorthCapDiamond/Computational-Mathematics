import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms


def read_equation_systems_file(link):
    file = open(link)
    n = int(file.readline())
    matrix = []
    for i in range(n):
        user_input = file.readline()
        line = parse_float_array(user_input)
        if len(line) != n:
            sys.exit("Invalid line")
        matrix.append(line)
    return matrix


def read_equations_system_stdin():
    size = int(input("Enter the size \n"))
    matrix = []
    for i in range(size):
        user_input = input("Enter one line (size n+1) like this: 'a b c d s'")
        line = parse_float_array(user_input)
        if len(line) != size:
            sys.exit("Invalid line")
        matrix.append(line)

    return matrix


def function(coefficients, x):
    answer = 0
    for i in range(len(coefficients)):
        answer += coefficients[i] * (x ** i)
    return answer


def check_interval(coefficients, edges):
    if function(coefficients, edges[0]) * function(coefficients, edges[1]) >= 0:
        sys.exit("Invalid interval")


def parse_float_array(user_input):
    alphabet = "1234567890,.-"
    for i in range(len(user_input)):
        for j in range(len(user_input[i])):
            if user_input[i][j] not in alphabet:
                sys.exit("invalid input")
    edges = [float(x) for x in user_input]
    return sorted(edges)


def enter_interval_stdin():
    user_input = input("Enter interval as 2 numbers like this: 'a b'\n").replace(",", ".").split()
    return parse_float_array(user_input)


def read_equation_file(link):
    file = open(link)
    user_input = file.read().replace(",", ".").split()
    if len(user_input) == 0:
        sys.exit("Empty file")
    equation = parse_float_array(user_input)
    return equation[::-1]


def read_equation_stdin():
    alphabet = "1234567890.,-"
    user_input = input("Enter coefficient of your equation in one line like that: 1 2 3 5 6...\nYou should them from "
                       "in standard order (x^n x^n-1 ... x^0)\n").replace(",", ".").split()
    if len(user_input) == 0:
        sys.exit("Empty input")
    for i in range(len(user_input)):
        for j in range(len(user_input[i])):
            if user_input[i][j] not in alphabet:
                sys.exit("Invalid input")
    equation = [float(x) for x in user_input]
    return equation[::-1]


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


def exit_program():
    print("Thank you for your time, bye!!!")
    sys.exit(0)
