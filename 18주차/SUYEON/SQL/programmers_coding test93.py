# 다항식 구하기
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d # a/= b의 뜻은 a=a/b
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
