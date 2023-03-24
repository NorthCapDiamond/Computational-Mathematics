from Nonlinear_Equations.function_util import *


def check_interval(coefficients, edges):
    if function(coefficients, edges[0]) * function(coefficients, edges[1]) >= 0:
        sys.exit("Invalid interval")


def parse_float_array(user_input):
    alphabet = "1234567890,.-"
    for i in range(len(user_input)):
        for j in range(len(user_input[i])):
            if user_input[i][j] not in alphabet:
                sys.exit("invalid input")
    edges = [float(x) for x in user_input]
    return edges