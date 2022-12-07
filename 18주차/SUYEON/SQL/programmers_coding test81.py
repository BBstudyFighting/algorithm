# 구슬을 나누는 경우의 수 
import math
def solution(balls, share):
    return math.comb(balls, share)

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# 컨트롤 제트
def solution(s):
    arr = s.split(' ')
    result =[]
    for i in arr :
        if i=='Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)

def solution(s):
    answer = 0
    stack = []
    for c in s.split():
        if c != 'Z':
            answer += int(c)
            stack.append(int(c))
        elif stack:
            answer -= stack.pop()
    return answer