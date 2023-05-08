import sys


def parse_int(a):
    alpha = "1234567890"
    for i in range(len(a)):
        if a[i] not in alpha:
            sys.exit("Only Integer is allowed")
    return int(a)


def parse_float(a):
    alpha = "1234567890.-"
    a = str(a).replace(',', ".")
    if a.count(".") > 1 or len(a) == 0:
        sys.exit("Only float is allowed")
    for i in range(len(a)):
        if a[i] not in alpha or (a[i] == "." and i == len(a) - 1):
            sys.exit("Only float is allowed")
    return float(a)


def parse_float_array(a):
    a = str(a).strip().split(" ")
    answer = [0.0] * len(a)
    for i in range(len(a)):
        answer[i] = parse_float(a[i])
    return answer
