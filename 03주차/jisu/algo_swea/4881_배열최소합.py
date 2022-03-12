# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg)
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개


# ```python
# - NxN 배열에서 한줄에 하나씩 N개의 숫자를 골라 최소가 되도록 한다.
# - 단, 세로로 같은 줄에서 두개 이상의 숫자를 고를 수 없다.
# - 위 조건에 맞게 최소합(min_sum)을 출력하는 프로그램을 만드시오.
# ```

# ### 풀이접근


# ```python
# - 백트레킹 알고리즘 - DFS 적용하되 유망하지 않으면 부모노드로 돌아감
# - 현재 부분합(now_sum)이 min_sum 초과하면 탐색 중지 (가지치기:Pruning)
# ```

# 코드
def backtrack(row, n, now_sum, visited):
    global min_sum  # 최소합을 전역변수로 선언
    if row == n:  # i가 배열의 수와 일치하면
        # 현재 합과 (지금까지)최소합 값을 비교
        if now_sum < min_sum:
            min_sum = now_sum  # 현재합이 적으면 대체
    elif now_sum > min_sum:
        return  # 현재합이 크면 탐색 중지 (Pruning)
    else:
        for col in range(n):
            if not visited[col]:  # 방문 전인 컬럼
                visited[col] = 1  # 방문처리
                # 다음 row로 넘어가고, now_sum에 값을 더해주고, visited 갱신
                backtrack(row+1, n, now_sum+num[row][col], visited)
                visited[col] = 0  # 함수 적용 후 초기화 (재검색 할 수 있도록)


T = int(input())
for tc in range(T):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 100  # 값을 대체해주기 임의의 큰 수 대입
    visited = [0]*n

    backtrack(0, n, 0, visited)  # 함수시작
    print(f'#{tc+1} {min_sum}')
# ```

#      1
#      5
#      5 2 1 1 9
#      3 3 8 3 1
#      9 2 8 8 6
#      1 5 7 8 3
#      5 5 4 6 8

    # 1 9
