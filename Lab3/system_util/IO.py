import sys
from parsers import types_parser


def read_equation_stdin():
    user_input = input("Enter coefficient of your equation in one line like that: 1 2 3 5 6...\nYou should type them "
                       "in standard order: x^(n) x^(n-1) ... x^0\n")
    if len(user_input) == 0:
        sys.exit("Empty input")

    equation = types_parser.parse_float_array(user_input)
    return equation[::-1]


def enter_epsilon():
    user_input = input("Enter epsilon\n")
    return types_parser.parse_float(user_input)


def enter_interval():
    user_input = input("Enter interval as 2 numbers like this: 'a b'\n")
    answer = types_parser.parse_float_array(user_input)
    if len(answer) != 2:
        sys.exit("2 float arguments expected!")
    if answer[0] > answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer


def enter_number_of_partitions():
    return types_parser.parse_int(input("Enter number of partitions\n"))


def changing_number_of_partitions():
    n = 4
    a = input("Enter 'yes' if you want to change the number of partitions\n")
    if a.trim() == "yes":
        n = enter_number_of_partitions()
        if n <= 0:
            sys.exit("n must be > 0")
    return n


def enter_left_right_center():
    a = str(input("choose: 'left', 'right', 'center'\n"))
    a = a.strip()
    if a not in ["left", "right", "center"]:
        sys.exit("You have to choose between 'left', 'right', 'center'")
    return a


def starter_pack():
    a, b = enter_interval()
    return a, b, enter_epsilon(), enter_number_of_partitions()


def exit_program():
    print("Thank you for your time, bye!!!")
    sys.exit(0)
