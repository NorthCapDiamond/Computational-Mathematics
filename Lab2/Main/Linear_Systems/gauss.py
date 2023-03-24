def gauss(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(len(matrix)):
                if matrix[j][i] != 0:
                    for k in range(len(matrix) + 1):
                        matrix[i][k] += matrix[j][k]
                    break

    if matrix[len(matrix) - 1][len(matrix) - 1] == 0:
        for i in range(len(matrix)):
            if matrix[i][len(matrix) - 1] != 0:
                for j in range(len(matrix) + 1):
                    matrix[len(matrix)][j] += matrix[i][j]
                break

    # forward stroke

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            c = matrix[j][i] / matrix[i][i]
            for k in range(len(matrix), i - 1, -1):
                matrix[j][k] -= c * matrix[i][k]

    # creating diagonals of ones

    for i in range(len(matrix)):
        tmp = matrix[i][i]
        for j in range(len(matrix) + 1):
            matrix[i][j] /= tmp

    # reverse stroke

    all_x = [0] * len(matrix)
    all_x[len(matrix) - 1] = matrix[len(matrix) - 1][len(matrix)]

    for i in range(len(matrix) - 2, -1, -1):
        all_x[i] = matrix[i][len(matrix)]
        for j in range(i + 1, len(matrix)):
            all_x[i] -= matrix[i][j] * all_x[j]

    return all_x
