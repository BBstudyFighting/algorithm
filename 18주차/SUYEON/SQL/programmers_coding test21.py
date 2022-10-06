# 아이템 줍기

# 1. 시작 지점에서부터 U, D, R, L 방향으로 하나씩 이동
# 2. 이동 후 조건에 맞는지 확인
#     - 좌표 범위를 넘어갔으면 continue
#     - 방문 한 적이 있다면 continue
#         - 주어진 직사각형들을 하나씩 순회하며 직사각형 좌표를 받는다
#         - 이동한 좌표가 직사각형 중앙에 있다면 -2
#         - 이동한 좌표가 직사각형 바깥에 있다면 현재 확인하는 직사각형 정보에 -1
#         - 나머지 경우는 직사각형 테두리에 있는 경우므로 1
#     - 만약 직사각형 정보에 -2 가 있다면 이동할 수 없는 좌표이기 때문에 queue에 추가하지 않는다.
#     - 만약 직사각형 정보에 1이 없다면 즉 -1 or -2 인 경우 즉 모든 직사각형 테두리에 있지 않으므로 queue에 추가 X
# 이렇게만 조건을 설정하게 되면 특정 상황에서 문제가 발생하게 된다.
# 이 경우에서 현재 좌표가 (3, 5) 일 경우 위로 갔다고 생각하면 (3, 6)도 조건에 성립한다.
# 실제로는 불가능하지만 (3, 6)이 가능하다고 판단되어서 잘못된 결과값이 나온다.
# 따라서 전체 좌표를 2배 해주게 되면 이런 경우 및 다른 반례도 처리 가능하게 된다.

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    for rec in rectangle:
        rec[0] *=2
        rec[1] *=2
        rec[2] *=2
        rec[3] *=2
    characterX *=2
    characterY *=2
    itemX *= 2
    itemY *= 2
    visited = [[0]*101 for _ in range(101)]
    answer = 202
    # U D R L
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque([(characterX,characterY,0)])
    visited[characterX][characterY] = 1
    checking_rec = [0 for _ in range(len(rectangle))]

    while q:
        x, y, cnt = q.popleft()
        if (x,y) == (itemX,itemY) and answer > cnt:
            answer = cnt
        for move in moves:
            dx, dy = move
            next_x = x + dx
            next_y = y + dy
            if not (1<=next_x<=100 and 1<=next_y<=100):
                # 좌표 범위를 벗어난다면
                continue
            if visited[next_x][next_y] == 1:
                # 방문한 적이 있다면
                continue
            for i,rec in enumerate(rectangle):
                s_x, s_y, e_x, e_y = rec
                # 좌표가 직사각형 바깥으로 나갔다면
                if (next_x < s_x or next_x > e_x) or (next_y < s_y or next_y > e_y):
                    # 일단 여기선 문제가 안되는데, 모두 다 안되면 X
                    checking_rec[i] = -1
                    continue
                # 좌표가 직사각형 중앙에 있다면
                if (s_x < next_x < e_x) and (s_y < next_y < e_y):
                    checking_rec[i] = -2
                    break
                checking_rec[i] = 1
            if -2 in checking_rec or 1 not in checking_rec:
                continue
            visited[next_x][next_y] = 1
            q.append((next_x,next_y,cnt+1))
    return answer//2