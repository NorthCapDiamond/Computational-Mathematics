def newton_f_k(X, Y, mem=None):
    if len(X) == 1:
        return Y[0]
    else:
        f_left = newton_f_k(X[1:].copy(), Y[1:].copy())
        f_right = newton_f_k(X[:-1].copy(), Y[:-1].copy())
        x_left = X[-1]
        x_right = X[0]
        return (f_left - f_right)/(x_left - x_right)


def newton_function(x, X, Y, n=None):
    if n is None:
        n = len(X)
    X = list(X)
    Y = list(Y)
    Nn = 0
    for i in range(1, n):
        sum_fi = (newton_f_k(X[:i].copy(), Y[:i].copy()))
        for j in range(i-1):
            sum_fi *= (x - (X[j]))
        Nn += sum_fi
    return Nn
