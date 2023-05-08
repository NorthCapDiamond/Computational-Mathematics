from interpolation.universal import *


def lagrange_function(x, X, Y):
    n = len(X)
    L_sum = 0
    for i in range(n):
        l_i = 1
        for j in range(n):
            if j == i:
                continue
            deltaX = X[i] - X[j]
            if deltaX == 0:
                deltaX = 0.0000000001
            l_i *= ((x - X[j]) / deltaX)
        l_i *= Y[i]
        L_sum += l_i
    return L_sum
