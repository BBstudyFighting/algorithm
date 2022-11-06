# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if height < i:
            answer += 1
    return answer

def solution(array, height):
    answer = 0
    answer = sum(1 for a in array if a > height)
    return answer

# 중복된 숫자 개수
def solution(array, n):
    answer = 0
    answer = array.count(n)
    return answer

# 짝수 홀수 개수
def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for i in num_list:
        if(i%2==0):
            even += 1
        else : 
            odd += 1
    answer.insert(0,even)
    answer.insert(1,odd)
    return answer

# 피자 나눠 먹기 (1)
import math
def solution(n):
    return math.ceil(n/7)

def solution(n):
    return (n - 1) // 7 + 1

def solution(n):
    answer = 0
    if n%7 != 0:
        answer = (n//7) + 1
    else:
        answer = n//7
    return answer