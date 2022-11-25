# 다음에 올 숫자
def solution(common: list) -> int:
    if common[1] - common[0] == common[2] - common[1]:  # 등차
        return common[-1] + (common[1] - common[0])
    else:  # 등비
        return common[-1] * (common[1] // common[0])
    

# 분수의 덧셈
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd] # gcd: 최대공약수 함수