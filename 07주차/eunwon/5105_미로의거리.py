def BFS():
    global answer
    while queue: 
        x,y = queue.pop(0)
        for i in range(4):#x,y 이동방법 4가지
            nx = x+dx[i] 
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:# 범위내에있고, 방문하지않을경우에 
                if not maze[nx][ny] == 1: #0이나 3이면 
                    visited[nx][ny] = True #방문한걸로 바꿈
                    queue.append((nx,ny))
                    Distance[nx][ny] = Distance[x][y] +1
                    if maze[nx][ny] == 3:
                        answer = Distance[nx][ny] - 1
                        break
                        

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    
    dx = [0,0,-1,1]#이동경로
    dy = [1,-1,0,0]
    visited = [[False for _ in range(N)] for _ in range(N)]
    Distance = [[0]*N for _ in range(N)]  ###
    queue = []
    answer = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                queue.append((i,j))
                break
            
    print(queue)
    BFS()

    print('#{} {}'.format(tc, answer))