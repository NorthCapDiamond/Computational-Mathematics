def euler(f, x0, y0, h, xn):
    X = []
    Y = []
    X.append(x0)
    Y.append(y0)
    while x0 < xn:
        y0 = y0 + h * f(x0, y0)
        x0 += h
        X.append(x0)
        Y.append(y0)
    return X, Y
