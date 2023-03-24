from Nonlinear_Equations.methods import *
from Nonlinear_Systems_Lib.system1 import *
from Nonlinear_Systems_Lib.system2 import *
from System_Utils.io_util import *

while True:
    user_input = input("Enter Command or help\n")
    if user_input == "help":
        print("system1\n" + "system2\n" + "secant\n" + "simple\n" + "half\n" + "exit\n")
    if user_input == "system1":
        system1()
    if user_input == "system2":
        system2()
    if user_input == "secant":
        typer = input("f or in\n")
        if typer == "f":
            print(secant_method(read_equation_file(input("type the link\n")), enter_interval_stdin()))
        if typer == "in":
            print(secant_method(read_equation_stdin(), enter_interval_stdin()))
    if user_input == "simple":
        typer = input("f or in\n")
        if typer == "f":
            print(simple_iteration(read_equation_file(input("type the link\n")), enter_interval_stdin()))
        if typer == "in":
            print(simple_iteration(read_equation_stdin(), enter_interval_stdin()))
    if user_input == "half":
        typer = input("f or in\n")
        if typer == "f":
            print(half_division(read_equation_file(input("type the link\n")), enter_interval_stdin()))
        if typer == "in":
            print(half_division(read_equation_stdin(), enter_interval_stdin()))
    if user_input == "exit":
        exit_program()
