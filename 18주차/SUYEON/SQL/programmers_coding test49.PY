# 두 수의 합
def solution(num1, num2):
    return num1+num2

# 나머지 구하기
def solution(num1, num2):
    answer = num1%num2
    return answer

# 나이 출력
def solution(age):
    answer = 2022 - (age-1)
    return answer

# 각도기
def solution(angle):
    if 0 < angle < 90 :
            answer = 1
    elif angle == 90 :
            answer = 2
    elif 90 < angle < 180 :
            answer = 3
    elif angle == 180 :
            answer = 4
    return answer