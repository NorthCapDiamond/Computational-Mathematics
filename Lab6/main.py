from functions.func_lib import *
from methods_for_solving_ordinary_differential_equations.euler import *
from methods_for_solving_ordinary_differential_equations.milna import *
from tables.answer_generator import *
from sys_util_lib.parsers_io import *

funcs_array = [(f1, f1_ans), (f2, f2_ans), (f3, f3_ans), (f4, f4_ans), (f5, f5_ans)]
methods = [euler, fourth_order_runge_kutta, milna]
# power of method, used for calculating of the Runge Rule
p_array = [1, 4, 4]

try:
    # Here user will choose the function for searching of the solution
    n = len(funcs_array)
    line = "choose function: from 0 to " + str(n-1)
    input_user = read_int_io(line)
    if input_user >= n or input_user < 0:
        sys.exit("Incorrect index")
    test_func = funcs_array[input_user]
    n = len(methods)

    # Here user will choose the type of the function
    type_of_function = read_int_io("'0' - Euler; '1' - Runge Kutta; '2' - Milna")
    if type_of_function >= n or type_of_function < 0:
        sys.exit("Incorrect index")
    else:
        function_t = methods[type_of_function]
    # This array contains p value for Runge Rule Method! (Check formula)
    p_i = p_array[type_of_function]

    # run main function in tables -> answer_generator
    if type_of_function == len(methods)-1:
        solution(test_func, read_float_io("Enter x0"), read_float_io("Enter y0"), read_float_io("Enter h"), read_float_io("Enter xn"), function_t, p_i, read_float_io("Enter Epsilon"))
    else:
        solution(test_func, read_float_io("Enter x0"), read_float_io("Enter y0"), read_float_io("Enter h"), read_float_io("Enter xn"), function_t, p_i)

except EOFError:
    sys.exit("End of file error detected")
