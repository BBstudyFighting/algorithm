# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(3,n+1) :
        temp = 1
        for j in range(1,i) :
            if i % j == 0 :
                temp += 1

        if temp > 2 :
            answer += 1
    return answer

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer

# 팩토리얼
from math import factorial 
# facorial, 계승 이라고 표현하며, 1부터 지정된 수까지 모든 수의 곱을 의미/ 수학 기호로는 '!'를 숫자뒤에 붙여 표시

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k