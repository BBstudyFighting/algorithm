from itertools import permutations

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)
    for permu in permutations(dungeons, len_dungeons):  # 순열로 경우를 만들어줌
        temp_k = k  # k는 그대로 보존하기 위해 temp_k를 k로 초기화 하고 사용
        count = 0  # 던전 수
        for p in permu:
            if temp_k >= p[0]:  # 최소 필요 피로도가 있는지 확인
                temp_k -= p[1]  # 소모 피로도 빼주기
                count += 1  # 던전 수 업데이트
        answer = max(answer, count)  # 최대 던전 탐험 수 업데이트
    return answer

solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer