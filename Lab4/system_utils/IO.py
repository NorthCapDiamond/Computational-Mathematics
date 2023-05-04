import sys
import matplotlib.pyplot as plt
from parsers import type_parser


def enter_float_array(message):
    return type_parser.parse_float_array(input(message + "\n"))


def enter_float(message):
    user_input = input(message + "\n")
    return type_parser.parse_float(user_input)


def enter_interval():
    user_input = input("Enter interval as 2 numbers like this: 'a b'\n")
    answer = type_parser.parse_float_array(user_input)
    if len(answer) != 2:
        sys.exit("2 float arguments expected!")
    if answer[0] > answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer


def draw_function_simple(a, b, h, f):
    X = []
    Y = []
    x = a
    mini = f(a)
    maxi = f(a)
    while x <= b:
        X.append(x)
        Y.append(f(x))
        maxi = max(maxi, f(x))
        mini = min(mini, f(x))
        x += h
    plt.plot(X, Y)
    plt.axis([a, b, mini, maxi])
    plt.show()


def draw_function_dots(a, b, h, f):
    X = []
    Y = []
    x = a
    maxi = f(a)
    mini = f(a)
    while x <= b:
        X.append(x)
        Y.append(f(x))
        maxi = max(maxi, f(x))
        mini = min(mini, f(x))
        x += h
    plt.plot(X, Y, "ro")
    plt.axis([a, b, mini, maxi])
    plt.show()


def draw_function_one_dot_one_simple(a, b, h, f1, f2):
    X = []
    Y = []
    Y2 = []
    x = a
    mini = min(f1(a), f2(a))
    maxi = max(f1(a), f2(a))
    while x <= b:
        X.append(x)
        Y.append(f1(x))
        Y2.append(f2(x))
        maxi = max(maxi, f1(x), f2(x))
        mini = min(mini, f1(x), f2(x))
        x += h
    plt.plot(X, Y)
    plt.plot(X, Y2, "ro")
    plt.axis([a, b, mini, maxi])
    plt.show()


def draw_function_one_dot_one_simple_from_array(X, Y, results_array):
    plt.plot(X, Y)
    plt.plot(X, results_array, "ro")
    plt.axis([min(X), max(X), min(min(Y), min(results_array)), max(max(Y), max(results_array))])
    plt.show()


def exit_program():
    print("Thank you for your time, bye!!!")
    sys.exit(0)
