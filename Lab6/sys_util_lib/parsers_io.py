import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_csv(message):
    try:
        return pd.read_csv(message)
    except IOError:
        sys.exit("IO csv file error")


def read_csv_io(Message=None):
    if Message is None:
        Message = "Enter link to csv file\n"
    else:
        Message += "\n"
    try:
        return read_csv(input(Message))
    except EOFError:
        sys.exit("End of file exception found!")


def read_int(message):
    try:
        return int(message)
    except ValueError:
        sys.exit("Only integers are allowed")


def read_int_io(Message=None):
    if Message is None:
        Message = ""
    else:
        Message += "\n"
    try:
        return read_int(input(Message))
    except EOFError:
        sys.exit("End of file exception found!")


def read_float(message):
    try:
        return float(message.replace(",", "."))
    except ValueError:
        sys.exit("Only floats are allowed")


def read_float_io(Message=None):
    if Message is None:
        Message = ""
    else:
        Message += "\n"
    try:
        return read_float(input(Message))
    except EOFError:
        sys.exit("End of file exception found!")


def read_float_array(message):
    message = message.split(" ")
    array = []
    for value in message:
        array.append(read_float(value))
    return array


def read_float_array_io(Message=None):
    if Message is None:
        Message = ""
    else:
        Message += "\n"
    try:
        return read_float_array(input(Message))
    except EOFError:
        sys.exit("End of file exception found!")


def read_int_array(message):
    message = message.split(" ")
    array = []
    for value in message:
        array.append(read_int(value))
    return array


def read_int_array_io(Message=None):
    if Message is None:
        Message = ""
    else:
        Message += "\n"
    try:
        return read_int_array(input(Message))
    except EOFError:
        sys.exit("End of file exception found!")


def draw_graph_one_dot_one_function(f, X, Y):
    delta = 0
    for count, value in enumerate(X):
        if abs(f(value, f(value, value, 0), 0) - Y[count]) > delta:
            delta = abs(f(value, f(value, value, 0), 0) - Y[count])

    x = np.linspace(min(X), max(X), 1000)
    plt.plot(X, Y, "ro")
    Y0 = [f(xi, f(xi, xi, 0), 0) for xi in x]
    Y1 = [f(xi, f(xi, xi, 1), 1) for xi in x]
    Y2 = [f(xi, f(xi, xi, -1), -1) for xi in x]
    Y3 = [f(xi, f(xi, xi, delta), delta) for xi in x]
    Y4 = [f(xi, f(xi, xi, -delta), -delta) for xi in x]

    plt.plot(x, Y0, color="orange")
    plt.plot(x, Y1, color="orange")
    plt.plot(x, Y2, color="orange")
    plt.plot(x, Y3, color="orange")
    plt.plot(x, Y4, color="orange")
    plt.show()

    plt.cla()
    plt.plot(x, Y1, color="orange")
    plt.plot(X, Y, "ro")
    plt.show()


def end_of_work():
    print("Program finished! Thank you for your time")
    sys.exit(0)
