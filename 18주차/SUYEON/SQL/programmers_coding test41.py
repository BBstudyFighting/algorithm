# 등굣길
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]

#위 점화식에 맞춰 문제를 풀게 되면, 쉽게 풀 수 있습니다.
# 다만 이번 문제에서 주의할 점은, 웅덩이의 위치 puddles의 좌표가 반대로 되어있다는 점입니다.
# (사실 이 문제의 행렬의 좌표 전체가 일반적인 좌표계와 반대방향으로 구성되어있습니다.)
# 그래서, 조건을 통해 웅덩이의 위치를 파악해줄 때 i,j 좌표를 반대로 적어주어야 합니다.