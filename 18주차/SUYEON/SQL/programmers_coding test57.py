# 순서쌍의 개수
def solution(n):
    answer =0 
    for i in range(n):
        if n % (i+1) ==0:
            answer +=1
    return answer

def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            answer+=1
    return answer*2-1 if n**0.5%1==0 else answer*2

# 제곱수 판별하기
def solution(n):
    tmp = n ** (1/2)
    if round(tmp,1)==tmp:
        answer = 1
    else:
        answer=2
    return answer

def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# n의 배수 고르기
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

def solution(n, numlist):
    answer = []
    for item in numlist:
        if item%n == 0:
            answer.append(item)
    return answer

# 대문자와 소문자
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer