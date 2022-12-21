# 유한소수 판별하기
from math import gcd
def solution(a, b):
    b //= gcd(a,b) # gcd : 최대공약수
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

