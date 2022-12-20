# 삼각형의 완성조건 (2)
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1


def solution(sides):
    return 2 * min(sides) - 1