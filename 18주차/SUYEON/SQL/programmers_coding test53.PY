# 점의 위치 구하기
def solution(dot):
    x = dot[0]
    y = dot[1]
    if x > 0 and y > 0 :
        answer = 1
    elif x > 0 and y < 0 :
        answer = 4
    elif x < 0 and y > 0 :
        answer = 2
    elif x < 0 and y < 0 :
        answer = 3
    return answer

# 최댓값 만들기(1)
def solution(numbers):
    numbers.sort() #오름차순 정렬
    return numbers[-1]*numbers[-2]

# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(1,n+1,2):
        answer.append(i)
    return answer

def solution(n):
    return [x for x in range(n + 1) if x % 2]

# 특정 문자 제거하기
def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer += my_string[i]
    return answer