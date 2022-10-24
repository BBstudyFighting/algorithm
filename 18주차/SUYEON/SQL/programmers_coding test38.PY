# N으로 표현
def solution(N, number):
    dp = [set() for i in range(9)] # 사용횟수에 따라 가능한 숫자를 담을 리스트
    for i in range(1, 9): # 1~8
        dp[i].add(int(str(N)*i)) # 단순히 이어붙인 숫자
        for j in range(i//2 + 1):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    if second != 0 :
                        dp[i].add(first // second)
                    if first != 0 :
                        dp[i].add(second // first)
                    
        if number in dp[i]:
            return i
    return -1
# 연산 횟수에 따른 가능한 숫자를 담을 리스트 dp를 만들었다. 각 경우의 수는 set을 이용해서 중복없이 담았다. set을 사용한 이유는 중복뿐만 아니라 in 탐색에 있어서도 효율이 높기 때문이다.
# 경우의 수는 먼저 횟수만큼 숫자가 이어 붙여진 값을 담는다. 그리고 다른 경우의 수는 많은 연산을 필요로한다. 예를 들어 5의 경우, 1번의 연산으로 만들어진 숫자들(first)과 4번의 연산으로 만들어진 숫자들(second) 을 사칙연산한 숫자들로 구성된다. 즉 합으로 5를 만들 수 있는 자연수인 (1,4) (2,3) 을 모두 사칙연산해야한다.
# 이 때 나눗셈에 유의하여야한다. 나누기는 순서가 바뀌면 답이 달라질 뿐만아니라 0으로 나누면 오류와 함께 종료될 수 있다.
# 하나의 작업이 끝날때마다 number가 있는지 확인하고 있다면 i (연산횟수)를 반환한다.
# 다행히 연산이 8보다 커지면 멈추고 -1을 출력하기 때문에 4중 for문이 무사히 돌아간다. 