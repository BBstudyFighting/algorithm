# 가장 먼 노드
from collections import deque


def solution(n, edge):
    answer = 0
    route = [0]*(n+1) #노드 1부터 각 노드까지의 거리
    edge.sort() #노드 1부터 연결 정보 확인하기 위해 정렬
    queue = deque() 
    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보 저장
    
    for e in edge: # 양방향이므로 
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue.append(1)
    route[1] = 1
    
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g]==0:
                queue.append(g)
                route[g] = route[now]+1
        
    # 1번 노드로부터 가장 멀리 떨어진 노드 개수 계산
    max_edge= max(route)
    for r in route:
        if r == max_edge:
            answer+=1     
            
    return answer
# 1. 먼저 노드 1부터 노드 간 연결 정보를 확인하기 위해 edge를 오름차순 정렬한다.

# 2. edge를 차례대로 보며 리스트 graph에 각 노드마다 연결된 다른 노드 정보를 모두 저장한다. 이 때 양방향 그래프인 것을 유의한다.

# 3. queue(deque())에 현재 노드와 직접 연결되어 있는 노드들을 삽입하는 작업을 반복한다. 
#    - 1번 노드가 기준이므로 먼저 queue에 1을 가장 먼저 삽입한다.

# 4. queue의 가장 앞 원소를 빼고 해당 원소와 연결되어 있는 모든 노드를 접근한다.
#    - 만약 접근한 노드가 아직 연결된 이력이 없다면(route[ ? ] == 0) 현재 원소와 연결되어 있기 때문에 queue에 삽입하고 route값을 현재 원소의 route + 1 해준다.

# 5. queue가 빌 때까지 위 4번 로직을 반복하는데, route란 1번 노드로부터 몇 개의 간선을 통해 연결된 것인지를 표현하는 것이다. 하지만 route의 초기화는 모두 0으로 되어있고 route[1]==0이다.
# 만약 [5,1]이 edge에 있었다면, if route[g] == 0: 구문에서 route[1] 값이 증가하는 일이 발생한다. 따라서 while queue: 반복문을 시작하기 전에 route[1]을 1로 설정하고 이후 노드들의 route 값은 2부터 시작하게 되도록 하였다.
# 노드 1부터 "얼마나 멀리 떨어져 있는가"가 핵심이기 때문에 route의 시작(route[1])을 1로 설정해도 문제가 되지 않는다.

# 6. 정답을 반환하기 위해 route에서 가장 큰 값(노드 1부터 가장 멀리 떨어진 값)을 가지는 노드 갯수를 계산한다.