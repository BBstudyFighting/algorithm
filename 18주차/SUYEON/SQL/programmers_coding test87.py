# OX퀴즈
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)
def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]    


def solution(quiz):
    answer = []
    for q in quiz:
        p, a = q.split("=")
        if eval(p) == int(a):
            answer.append("O")
        else:
            answer.append("X")
    return answer
