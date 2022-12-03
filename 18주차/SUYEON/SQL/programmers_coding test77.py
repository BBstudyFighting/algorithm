# 개미 군단
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer

# 직각삼각형 출력하기
n = int(input())
for i in range(n):
    print('*'*(i+1))
    
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print('*', end = '')
    print()