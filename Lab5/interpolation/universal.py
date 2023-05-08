import math


def get_results_array(X, new_function):
    Y = []
    for i in range(len(X)):
        Y.append(new_function(X[i]))
    return X, Y


def get_results_function(a, b, h, new_function):
    X = []
    Y = []
    x = a
    while x <= b:
        X.append(x)
        Y.append(new_function(x))
        x += h
    return X, Y


def ln(a):
    return math.log(a, math.e)


def function_generator(method, X, Y):
    def f(x):
        ans = (method(x, X, Y))
        return ans
    return f

