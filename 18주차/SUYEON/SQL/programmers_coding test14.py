# 전력망을 둘로 나누기
# 전선을 입력받아 tree를 만들어준다. 
# 양뱡향이므로 전선으로 연결된 두 개의 노드에 모두 정보를 추가해준다.
# 전선 하나를 끊어서 BFS를 돌리고, 각각의 연결된 노드수(송전탑의 수)를 받아온다.
# 끊을 전선을 BFS에 넘기고 queue에 새로운 노드를 추가할 때, 시작 노드와 추가할 노드가 모두 해당 전선으로 연결된 것이 아니라는 조건을 추가한다.
# 송전탑의 수의 차이를 비교해서 answer을 업데이트한다.
from collections import deque

def bfs(node, tree, visited, wire, cnt):
    queue = deque()
    queue.append([node, tree, visited, wire])
    visited[node] = True

    while queue:
        node, tree, visited, wire = queue.popleft()
        cnt += 1

        for i in tree[node]:
            if not ((node == wire[0] and i == wire[1]) or (node == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, tree, visited, wire])

    return cnt


def solution(n, wires):
    answer = 1e9
    tree = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)

    for wire in wires:
        visited = [False] * (n + 1)
        temp = []
        for i in range(1, n + 1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, wire, 0)
                temp.append(cnt)

        answer = min(answer, abs(temp[0] - temp[1]))

    return answer


##################################################################


uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer