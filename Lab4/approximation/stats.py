import math


def mean(X):
    return sum(X) / len(X)


def deviation_measure_functions(a, b, h, f1, f2):
    S = 0
    while a <= b:
        S += (f1(a) - f2(a)) ** 2
        a += h
    return S


def deviation_measure_arrays(F, Y):
    S = 0
    for i in range(len(F)):
        S += (F[i] - Y[i]) ** 2
    return S


def create_e_array_functions(a, b, h, f1, f2):
    e = []
    while a <= b:
        e.append(f2(a) - f1(a))
        a += h
    return [f2, e]


def create_e_array_from_x_array(Y1, Y2):
    e = []
    for i in range(len(Y1)):
        e.append(Y2[i] - Y1[i] )
    return [Y2, e]


def variance_arrays(Y):
    variance = 0
    y_mean = mean(Y)

    for i in range(len(Y)):
        variance += (Y[i] - y_mean) ** 2

    return variance / len(Y)


def variance_function(a, b, h, f):
    Y = []
    while a <= b:
        Y.append(f(a))
        a += h
    return variance_arrays(Y)


def standard_deviation_arrays(Y):
    return (variance_arrays(Y)) ** 0.5


def standard_deviation_function(a, b, h, f):
    return (variance_function(a, b, h, f)) ** 0.5


def correlation_array(X, Y):
    x_mean = mean(X)
    y_mean = mean(Y)

    sum_multiply_dx_dy = 0
    sum_dx2 = 0
    sum_dy2 = 0

    for i in range(len(X)):
        sum_multiply_dx_dy += ((X[i] - x_mean) * (Y[i] - y_mean))

        sum_dx2 += (X[i] - x_mean) ** 2
        sum_dy2 += (Y[i] - y_mean) ** 2

    return sum_multiply_dx_dy / math.sqrt(sum_dx2 * sum_dy2)


def correlation_function(a, b, h, f1, f2):
    Y1 = []
    Y2 = []
    while a <= b:
        Y1.append(f1(a))
        Y2.append(f2(a))
        a += h
    return correlation_array(Y1, Y2)


def rate_correlation(r):
    if r < 0.3:
        return "connection is weak"
    if 0.3 <= r < 0.5:
        return "connection is moderate"
    if 0.5 <= r < 0.7:
        return "conspicuous connection"
    if 0.7 <= r < 0.9:
        return "connection is strong"
    if 0.9 <= r < 0.99:
        return "connection is very strong"
    if 1.1 > r >= 0.99:
        return "almost identical"
    else:
        return "WHATTT THE FUCKKKK"


def rate_correlation_array(X, Y):
    return rate_correlation(correlation_array(X, Y))


def rate_correlation_function(a, b, h, f1, f2):
    return rate_correlation(correlation_function(a, b, h, f1, f2))


