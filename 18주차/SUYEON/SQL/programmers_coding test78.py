# 약수 구하기
def solution(n):
    answer = []

    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)

    return answer

def solution(n):
    return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]

# 7의 개수
def solution(array):
    answer = 0
    for i in array:
        for j in range(len(str(i))):
            if str(i)[j] == '7':
                answer += 1
    return answer

def solution(array):
    return ''.join(map(str, array)).count('7')