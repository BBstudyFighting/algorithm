# 세균 증식
def solution(n, t):
    answer = 0
    for i in range(t):
        n = n*2
    return n

# 배열 두 배 만들기
def solution(numbers):
    return [num*2 for num in numbers]

def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

# 문자 반복 출력하기
def solution(my_string, n):
    answer = []
    for i in range(len(my_string)):
        for j in range(n):
            answer.append(my_string[i])
    return "".join(answer)

# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer