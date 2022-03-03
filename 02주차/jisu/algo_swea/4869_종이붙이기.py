# 문제소개

# 20x10(a) / 20x20(b) 의 직사각형 종이를 맘껏 쓸수 있다고 할때,
# 20 x n(입력값)의 직사각형을 만드는 경우의 수(num)를 구하시오.

# 법칙구하기 : 앞, 뒤, 위, 아래
# 예시 - 20x20 : a2x2, b1 -> 3
#        20x30 : a3, (a1,b1), (b1,a1), (a2,a1), (a1,a2) -> 5
#        20x40 : a4x2, (a2,b1)x2, (b1,a2)x2, b2x2 ... -> 11

# --> DP(동적계획법) 활용

def count(n):  # 경우의 수 count 함수
    if n % 10 == 0:
        if n == 10:  # n = 10 이면 경우의 수는 1
            return 1
        elif n == 20:  # n = 20 이면 경우의 수 = 3
            return 3
        else:  # n이 30이면 5, 40이면 8, 50이면 13
            return count(n-10)+(2*count(n-20))
    else:
        print("10의 배수만 입력할 수 있어요.")


T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    num = count(n)
    print(f'#{tc} {num}')
