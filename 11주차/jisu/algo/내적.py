def solution(a, b):
    answer = 0
    # 길이가 같은 배열의 내적은 각 요소를 곱한 뒤 더해주면 됨
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
