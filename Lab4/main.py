import math
import pandas as pd
from approximation.linear_approximation import *
from approximation.square_approximation import *
from approximation.cube_approximation import *
from approximation.exponential_approximation import *
from approximation.power_approximation import *
from approximation.logarithm_approximation import *
from functions.lib_of_functions import *
from parsers.type_parser import *
from systems_of_equations.gauss import *
from system_utils.IO import *
from tables.generate_table import *


def f1(x):
    return math.log(x, 2)+1000


h = 0.5
a = 2
b = 5
array_of_functions = [linear_approximation_function_array, square_approximation_function_array, cube_approximation_function_array,
                      exponential_approximation_function_array, power_approximation_function_array,
                      logarithm_approximation_function_array]
array_of_names = [linear_approximation_formula, square_approximation_formula, cube_approximation_formula, exponential_approximation_formula,
                  power_approximation_formula, logarithm_approximation_formula]

df = (resulting_table_generator_functions(a, b, h, f1, array_of_functions, array_of_names))
print(df[1])
df[0].to_csv("answer.csv")
"""


array_of_names = [linear_approximation_formula, square_approximation_formula, cube_approximation_formula, exponential_approximation_formula,
                  power_approximation_formula, logarithm_approximation_formula]
df = pd.read_csv("input.csv").reset_index(drop=True)
df = resulting_table_generator_array(df["X"], df["Y"], array_of_functions, array_of_names)
print(df[1])
"""