# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg)  
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개 


# ```python
# N x N 크기의 미로에서 출발(2)지에서 도착(3)지까지 
# 가는 경로가 존재하면 1을 출력하는 프로그램을 작성하시오.
# 입력예시) 0(통로) 1(벽)
# 5
# 13101 -> 맨 아래 2에서 3까지 0으로 이어져 있으므로 1 출력  
# 10101 -> 만약 11101 이라면 막혀있으므로 0 출력
# 10101 
# 10101   
# 10021    
# ```

# ### 풀이접근


# ```python
# 백트레킹 활용 
# - 방문한 노드가 해답이 될 수 없으면 뒤로 돌아감(가지치기)
# 1. 시작점에서 (상하좌우) 중 한 방향을 이동한 후, 
#    갈수 있을 때까지, 같은 방향으로 스택에 push
# 2. 벽에 막혀 이동이 안되면 pop하면서 한칸씩 돌아오다,
#    이동가능 지점에 오면 다시 다른 방향으로 이동 시작 
# ```

### 코드

# 상하좌우 이동 리스트
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 경계 체크


def boundary(y, x):
    if y < 0 or x < 0 or y >= n or x >= n:
        return True  # 경계 벗어남
    return False


T = int(input())
try:
    for tc in range(1, T+1):
        n = int(input())
        map_list = [list(map(int, list(input()))) for _ in range(n)]
        y, x = 0, 0  # 시작좌표
        result = 0  # 통로 연결되면 1로 바뀜
        # 출발점(2) 찾기
        for i in range(n):
            if 2 in map_list[i]:
                x = map_list[i].index(2)
                y = i
                break
        stack = [(y, x)]  # 스택에 시작좌표 넣기
        # 스택이 빌때까지 반복
        while stack:
            y, x = stack.pop()  # 현재 좌표 꺼내서
            map_list[y][x] = 1  # 현재 좌표 방문처리
            # 이동할 4방향 검사
            for _y, _x in move:
                dy = y + _y
                dx = x + _x
                # 경계 벗어나면 다음 길로
                if boundary(dy, dx):
                    continue
                if map_list[dy][dx] == 3:  # 도착하면
                    result = 1
                    break  # 결과 바꾸고 반복문 종료
                # 통로(0)를 만나면 스택에 추가
                elif not map_list[dy][dx]:
                    stack.append((dy, dx))
            else:  # 브레이크 없이 끝나면 다음으로 진행
                continue
            break
        print(f'#{tc} {result}')

except:  # 입력이 잘못되면 error 출력
    print(f'#{tc} error')
