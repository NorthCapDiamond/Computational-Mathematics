import sys
import pandas as pd
from approximation.stats import *
from system_utils.IO import *


def resulting_table_generator_functions(a, b, h, f, array_of_functions, array_of_function_names):
    X = []
    Y = []
    while a <= b:
        X.append(a)
        Y.append(f(a))
        a += h
    return resulting_table_generator_array(X, Y, array_of_functions, array_of_function_names)


def resulting_table_generator_array(X, Y, array_of_functions, array_of_function_names):
    df = pd.DataFrame(
        columns=["Type", "Coefficients", "Results", "Ei", "Sum(ei)", "Sigma", "Correlation", "Dependency", "R2"])
    short_df = pd.DataFrame(columns=df.columns)
    array_of_bests = []
    results_memory = []
    if len(array_of_functions) != len(array_of_function_names):
        sys.exit("resulting_table_generator arrays must be the same")
    for i in range(len(array_of_functions)):

        data = array_of_functions[i](X, Y)
        fi = data[0]
        array_of_bests.append(fi)
        coefs = list(data[1:])
        for j in range(len(coefs)):
            coefs[j] = coefs[j]

        results_array = []
        for j in range(len(X)):
            results_array.append(fi(X[j]))
        results_memory.append(results_array)
        e_array = create_e_array_from_x_array(Y, results_array)[1]

        for j in range(len(e_array)):
            e_array[j] = (e_array[j])

        function_name = array_of_function_names[i]()

        sigma = standard_deviation_arrays(results_array)

        sum_e2 = 0
        for j in range(len(e_array)):
            sum_e2 += e_array[j]**2
        sum_phi2 = 0
        for j in range(len(results_array)):
            sum_phi2 += results_array[j]**2

        R2 = sum_e2/(sum_phi2 - 1/len(results_array) * sum(results_array)**2)

        new_line = [function_name, str(coefs), str(results_array), str(e_array), str(sum_e2), str(sigma),
                    (correlation_array(X, results_array)), rate_correlation_array(X, results_array), str(R2)]
        short_df_line = [function_name[0], str(coefs), str(results_array), str(e_array), str(round(sum_e2, 2)),
                         str(round(sigma, 4)), round(correlation_array(X, results_array), 4),
                         rate_correlation_array(X, results_array), str(round(R2, 2))]
        df.loc[len(df)] = new_line
        short_df.loc[len(short_df)] = short_df_line

    df = df.sort_values(by="R2", ascending=True)
    short_df = short_df.sort_values(by="R2", ascending=True)
    print(df.index.values.tolist()[0])
    draw_function_one_dot_one_simple_from_array(X, Y, results_memory[df.index.values.tolist()[0]])
    return df, short_df.drop("Results", axis=1).drop("Coefficients", axis=1).drop("Ei", axis=1)
