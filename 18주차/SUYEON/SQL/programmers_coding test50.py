# 짝수의 합
def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2 == 0:
            answer += i
    return answer

# 배열의 평균값
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    answer = answer/len(numbers)
    return answer

# 두 수의 나눗셈
def solution(num1, num2):
    return int(num1/num2*1000)

# 양꼬치
def solution(n, k):
    price_food = n *12000
    if n >= 10 :
        price_drink = (k-n//10)*2000 # 10인분 이상
        # //연산자 : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
        # 양꼬치의 개수인 n을 10으로 나눈 몫을 음료 개수에 빼주어 가격(2000)과 곱하기
    else:
        price_drink = k*2000 # 10인분 미만
    answer = price_food + price_drink
    return answer