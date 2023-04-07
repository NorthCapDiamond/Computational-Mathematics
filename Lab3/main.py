import system_util.IO
from math_util.integrate_methods.cell_method import *
from math_util.integrate_methods.second_kind_integrals.second_kind_solver import tests
from math_util.integrate_methods.simpson_method import *
from math_util.integrate_methods.trapeze_method import *


tests()
user_input = input("Enter Command or help\n")
while True:
    if user_input == "help":
        print("cell\n" + "trapeze\n" + "simpson\n" + "exit\n")
    if user_input == "cell":
        integrate_cell_method_user(system_util.IO.read_equation_stdin())
    if user_input == "trapeze":
        integrate_trapeze_method_user(system_util.IO.read_equation_stdin())
    if user_input == "simpson":
        integrate_simpson_method_user(system_util.IO.read_equation_stdin())
    if user_input == "exit":
        exit_program()
    user_input = input("Enter Command or help\n")
