# 앞뒤로 추가와 삭제가 가능한 양방향 큐(deque)
from collections import deque

def bfs(start, end):
    # 시작점 설정 및 방문처리
    Q.append(start)
    visited[start] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            # 방문하지 않았다면 
            if not visited[w]:
                # 방문처리하고 거리 설정
                visited[w] = 1 
                distance[w] = distance[v] + 1
                Q.append(w)
                # 도착하면 거리 반환 
                if w == end:
                    return distance[w]
    return 0

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    
    # 그래프 표시할 2차원 행렬
    G = [[] for _ in range(V+1)]
    
    # 방향이 없는 그래프이므 양방향 설정
    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, end = map(int, input().split())
    
    # 방문처리, 거리계산을 위한 리스트 생성
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    
    Q = deque()
    
    print(f'#{tc} {bfs(start,end)}')