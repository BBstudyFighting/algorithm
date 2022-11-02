# 방의 개수
# 모래 시계 형태 예외를 처리하기 위해서 한 번 이동할 때 두 칸씩 이동하도록 하여, 기존에 노드가 없는 지점에도 노드가 생기도록 한다.
# 방의 생성 여부는 사이클이 생기는 것을 확인해야 함이 맞지만, 유니온-파인드 방법을 고수할 필요는 없었다. 방이 생성되는 경우는 다음과 같다.
# - 방문한 노드가 이미 방문한 적이 있고,
# - 해당 노드로 들어온 경로는 처음 이동한 경우
# 두 번째 조건은 한 경로를 두고 와리가리했을 경우 방이 계속해서 생김을 방지하기 위해 체크한다
import collections


def solution(arrows):
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)

    # visited : 노드 방문 체크
    # visited_dir : 노드 방문 경로 체크 ((A, B)는 A -> B 경로를 의미)
    visited = collections.defaultdict(int)
    visited_dir = collections.defaultdict(int)

    # arrows 따라 노드 좌표를 큐에 추가
    queue = collections.deque([now])
    for i in arrows:
        # 모래 시계 형태 예외를 처리하기 위해 해당 방향으로 2칸씩 추가한다.
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(next)

            now = next

    now = queue.popleft()
    visited[now] = 1

    while queue:
        next = queue.popleft()

        # 이미 방문한 노드(visited[x]==1)인 경우
        if visited[next] == 1:
            # 해당 경로로 처음 들어온 경우인 경우 answer++
            # 처음 들어온 경우에 방이 처음 생성되므로!
            if visited_dir[(now, next)] == 0:
                answer += 1
        # 처음 방문한 노드인 경우 방문 체크를 한다.
        else:
            visited[next] = 1

        # 해당 노드로 들어온 경로를 방문 체크해준다.
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer

#################################################################################
# 오일러 공식 사용
def solution(arrows):
    point=set([(0,0)])
    line=set()
    move=[[0,2],[2,2],[2,0],[2,-2],[0,-2],[-2,-2],[-2,0],[-2,2]]
    pre_point=(0,0)
    for A in arrows:
        next_point=(pre_point[0]+move[A][0],  pre_point[1]+move[A][1] )
        mid_point=(pre_point[0]+move[A][0]//2,  pre_point[1]+move[A][1]//2 )
        point.add(next_point)
        point.add(mid_point)
        line.add((pre_point,mid_point))
        line.add((mid_point,pre_point))
        line.add((mid_point,next_point))
        line.add((next_point,mid_point))
        pre_point=next_point
    answer = len(line)//2-len(point)+1
    return answer if answer>=0 else 0