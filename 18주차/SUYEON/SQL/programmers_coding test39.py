# 정수 삼각형
def solution(triangle):
    # dp 테이블 초기화
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    # 거쳐간 숫자의 최댓값 구하기
    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return max(dp[-1]) # dp 테이블의 마지막 원소들 중 최댓값 반환
################################################################3
# 젤 어이없는 정답
# 1 한 층씩 제거하며, 그 층에서 계산한 최대 이동거리 배열을 계산하여, 한 층을 제거한 traingle을 첫번째 input, 이동거리 배열을 두 번째 input으로 넣어줍니다. 
# 2. 따라서 traingle이 없으면 제거할 층이 없으므로 최종 조건입니다. 3. [0] + l, l + [0] 을 이용하여 모서리 조건을 해결해줍니다.
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
