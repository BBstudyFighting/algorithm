# 1. 깊이우선탐색(DFS) 개념 (+ 스택)
# 활용
# - 지름길, 미로찾기 등에선 모든 경로를 검색해야함
# - 이 때 자주 쓰이는 알고리즘이 DFS(깊이우선탐색)
# 개념
# - 갈 수 있는 곳까지 아래로 내려가며 깊이 탐색
# - 더 갈 곳이 없으면 마지막 갈림길 간선으로 돌아온 뒤,
#   다른 방향의 탐색을 반복해 결국 모든 노드을 방문
# -> 마지막 갈림길 간선으로 돌아올 때
#    후입선출 구조인 스택을 활용

# 2. 문제소개
# - V개 노드, E개의 간선으로 연결한 그래프가 주어짐
# - 시작노드(S), 도착노드(G)가 입력될 때,
#   길이 연결되어 있으면 1, 없으면 0 을 출력
# - 1 에서 6 은 가는 길이 있으므로 1출력

### 3 .입력값 + 접근
# - 테스트 갯수 T, 다음 V(노드)와 E(간선)
# 	-> visit 리스트에 노드갯수만큼 False(방문 전)
#     -> 방문한 노드는 visit[node] = True
#     -> 모든 요소 값이 0인 VxV 2차원 배열 graph 정의
# - 다음 줄부터 E개 줄만큼 간선의 정보
# 	-> graph에 입력된 간선 연결을 1로 정의
# - 마지막 줄엔 출발노드 S, 도착노드 G 입력
# 	-> dfs 함수에 S, G 대입

# 4. 깊이우선탐색 함수
# DFS - 아래로 내려가며 방문안한 노드 반복탐색
def dfs(start, end):  # 출발노드, 도착노드
    stack = []  # 스택초기화
    # 노드 수만큼 False 만들기 (인덱스 0 부터 시작하니 +1)
    visit = [False] * (V+1)  # False는 방문 전 의미
    stack.append(start)  # 출발노드를 스택에 추가

    # 모든 노드 반복할 때(stack이 빌 때)까지 반복
    while stack:
        # 최근 스택의 값을 now에 할당
        now = stack.pop()
        # now 노드는 방문(True) 처리
        visit[now] = True
        # next는 now 다음 노드값
        for next in range(1, V+1):
            # 아직 next 노드가 방문 전이고,
            # 2차원 배열 graph 값이 1(연결)이라면
            if not visit[next] and graph[now][next]:
                stack.append(next)  # 스택에 next 값 추가

    # while문이 끝났을 때,
    if visit[end]:  # end 노드가 1(방문)이라면?
        return 1
    else:
        return 0


# 5. 함수적용
T = int(input())
for tc in range(1, 1+T):
    # V(노드) E(간선)
    V, E = map(int, input().split())
    # 행과 컬럼 수가 V+1이고 모든 값이 0인 2차원 배열
    graph = [[0] * (V+1) for _ in range(V+1)]
    # 입력된 간선엔 1 할당
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1
    # S(출발노드) G(도착노드)
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S,G)}')
