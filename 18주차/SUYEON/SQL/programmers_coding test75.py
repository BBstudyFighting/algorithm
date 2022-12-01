# 피자 나눠 먹기 (3)
def solution(slice, n):
    return ((n - 1) // slice) + 1

def solution(slice, n):
    answer = 0

    if n%slice != 0:
        answer = (n // slice) + 1
    else:
        answer = n // slice

    return answer

# 삼각형의 완성조건 (1)
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

