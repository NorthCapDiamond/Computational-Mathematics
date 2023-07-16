from methods_for_solving_ordinary_differential_equations.fourth_order_runge_kutta import *


def milna(f, x, y, h, xn, eps):
    xnn = x + h*4
    X, Y = fourth_order_runge_kutta(f, x, y, h, xnn)
    F = []
    for i in range(4):
        F.append(f(X[i], Y[i]))

    # Prediction part:

    while X[-1] < xn:
        X.append(X[-1] + h)
        Y.append(Y[-4] + 4*h/3 * (2 * F[-3] - F[-2] + 2 * F[-1]))
        Fi = f(X[-1], Y[-1])
        y_correct = Y[-2] + h/3 * (F[-2] + 4*F[-1] - Fi)

        # Correction part:
        while abs(y_correct-Y[-1]) >= eps:
            Y[-1] = y_correct
            Fi = f(X[-1], y_correct)
            y_correct = Y[-2] + h/3 * (F[-2] + 4*F[-1] - Fi)
        Y[-1] = y_correct
        F[-1] = Fi
    return X, Y
