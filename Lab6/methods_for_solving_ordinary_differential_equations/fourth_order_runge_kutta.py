def fourth_order_runge_kutta(f, x0, y0, h, xn):
    X, Y = [], []
    X.append(x0)
    Y.append(y0)
    while x0 < xn:
        k1 = h*f(x0, y0)
        k2 = h*f(x0+h/2, y0+k1/2)
        k3 = h*f(x0+h/2, y0+k2/2)
        k4 = h*f(x0+h, y0+k3)
        x0 += h
        y0 = y0 + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        X.append(x0)
        Y.append(y0)
    return X, Y
