import os.path
import sys

from System_Utils.parsers import *


def read_equation_systems_file(link):
    if not (os.path.exists(link)):
        sys.exit("No such file exists")
    if not(os.path.isfile(link)):
        sys.exit("No such file")

    file = open(link)
    n = int(file.readline())
    matrix = []
    for i in range(n):
        user_input = file.readline()
        line = parse_float_array(user_input)
        if len(line) != n:
            sys.exit("Invalid line")
        matrix.append(line)
    return matrix


def read_equations_system_stdin():
    size = int(input("Enter the size \n"))
    matrix = []
    for i in range(size):
        user_input = input("Enter one line (size n+1) like this: 'a b c d s'")
        line = parse_float_array(user_input)
        if len(line) != size:
            sys.exit("Invalid line")
        matrix.append(line)

    return matrix


def enter_interval_stdin():
    user_input = input("Enter interval as 2 numbers like this: 'a b'\n").replace(",", ".").split()
    return parse_float_array(user_input)


def read_equation_file(link):
    if not (os.path.exists(link)):
        sys.exit("No such file exists")
    if not(os.path.isfile(link)):
        sys.exit("No such file")
    file = open(link)
    user_input = file.read().replace(",", ".").split()
    if len(user_input) == 0:
        sys.exit("Empty file")
    equation = parse_float_array(user_input)
    return equation[::-1]


def read_equation_stdin():
    alphabet = "1234567890.,-"
    user_input = input("Enter coefficient of your equation in one line like that: 1 2 3 5 6...\nYou should them from "
                       "in standard order (x^n x^n-1 ... x^0)\n").replace(",", ".").split()
    if len(user_input) == 0:
        sys.exit("Empty input")
    for i in range(len(user_input)):
        for j in range(len(user_input[i])):
            if user_input[i][j] not in alphabet:
                sys.exit("Invalid input")
    equation = [float(x) for x in user_input]
    return equation[::-1]


def exit_program():
    print("Thank you for your time, bye!!!")
    sys.exit(0)
