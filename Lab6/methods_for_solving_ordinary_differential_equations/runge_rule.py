import math
import sys
import numpy as np


def runge_rule(method, f, x0, y0, h, xn, p, eps=None):
    eps_array = []
    if eps is None:
        eps = 0.01
        X, Y1 = method(f, x0, y0, h, xn)
        Y2 = method(f, x0, y0, h/2, xn)[1]
    else:
        X, Y1 = method(f, x0, y0, h, xn, eps)
        Y2 = method(f, x0, y0, h / 2, xn, eps)[1]

    for i in range(1, int(math.ceil((xn - x0)/h))):
        res = abs(Y1[i] - Y2[i])/(2**p - 1)
        eps_array.append(res)

    if len(eps_array) == 0:
        sys.exit("Bad interval! Expected more elements")
    is_optimal = max(eps_array) < eps
    eps_array = np.array(eps_array)
    return eps_array.mean(), "h is OK" if is_optimal else "h is NOT OK"
