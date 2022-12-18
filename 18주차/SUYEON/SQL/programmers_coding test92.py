# 직사각형 넓이 구하기
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

def solution(dots):
    answer = 0
    for i in range(1, len(dots)):
        if dots[i][1] == dots[0][1]:
            width = abs(dots[i][0] - dots[0][0])
        if dots[i][0] == dots[0][0]:
            height = abs(dots[i][1] - dots[0][1])
    answer = width * height
    return answer

def solution(dots):
    x, y = [], []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    return (max(x) - min(x)) * (max(y) - min(y))