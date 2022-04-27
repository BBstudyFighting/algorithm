# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg&&#)
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개


# ```python
# -  N x N 크기 미로가 있다. 출발지(2) 목적지(3) 벽(1) 통로(0)가 주어질 때,
#    지나가야하는 최소한의 칸 수를 계산하는 프로그램을 작성하시오
# 예)
# 13101
# 10101
# 10101
# 10101
# 10021
# - 목적지(3)까지 5개의 칸을 지나 도착할 수 있다.
# ```

# ### 풀이접근


# ```python
# 1. 큐를 활용한 너비우선탐색(BFS) 활용
#     - 인접 정점을 모두 방문한 후 방문했던 정점을 시작접으로 다시 인접 정점을 방문
#     - 앞서 방문한 정점에 다시 BFS 해야하므로 선입선출의 큐를 활용
# ```

# ### 코드


# ```python
# 상하좌우 이동표시
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():  # 너비우선탐색 함수
    global queue
    count = 0
    # temp가 빈리스트면 queue도 빈리스트, return 0으로 이동
    while queue:
        # 지나온 길을 표시할 temp
        temp = []
        while queue:
            # 출발지점 가로(x),세로(y) 좌표를 꺼내서
            y, x = queue.pop()
            # 상하좌우로 이동
            for i, j in move:
                dy = y+i
                dx = x+j
                # 맵을 벗어나지 않는다면
                if 0 <= dy < N and 0 <= dx < N:
                    if not map_list[dy][dx]:
                        # 경로의 값이 0이면 방문처리하고
                        map_list[dy][dx] = 1
                        # 좌표를 second_queue에 추가
                        temp.append((dy, dx))
                    # 도착지에 도착하면 현재 카운트 리턴
                    if map_list[dy][dx] == 3:
                        return count
        # 큐가 비면서 한칸 이동하면 카운트 증가
        count += 1
        queue = temp  # 세컨큐를 기본큐에 대입
    return 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            # 2를 찾는다면 큐에 넣고 브레이크
            if map_list[i][j] == 2:
                queue.append((i, j))
                break
        # esle는 브레이크에 걸리지 않았을때만 동작한다.
        # 못찾았다면 위로 올린다.
        else:
            continue
        # 2를 찾았다면 더이상의 반복문은 필요가 없으므로 정지
        break
    # 결과값을 출력한다.
    print(f'#{tc} {bfs()}')

# ```

#      1
#      5
#      13101
#      10101
#      10101
#      10101
#      10021


#     #1 5
