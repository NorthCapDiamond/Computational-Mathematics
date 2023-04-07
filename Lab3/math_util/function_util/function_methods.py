def function(x, equation):
    answer = 0
    for i in range(len(equation)):
        answer += equation[i] * (x ** i)
    return answer


def derivative(equation):
    new_equation = equation.copy()
    if len(new_equation) == 1:
        return [0]
    for i in range(len(new_equation)):
        new_equation[i] *= i
    return new_equation[1:]
