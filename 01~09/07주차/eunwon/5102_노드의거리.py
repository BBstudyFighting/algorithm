def BFS(): #가로탐색
    global answer      
    while queue:
        x = queue.pop(0) #시작점뽑기
        for y in range(1,V+1): #모든 y에대해 
            if array[x][y] == 1 and not visited[y]: #간선이연결 & 방문안한노드
                queue.append(y) #큐에 추가
                visited[y] = True #방문함으로 바꿈
                Distance[y] = Distance[x] + 1 #거리 체크
                if y == G:  # 도착지에 도달하면
                    answer = Distance[y] #거리를 답으로 냄
                    break


T = int(input())
for tc in range(1,T+1):
    V,E = list(map(int,input().split())) #노드갯수/ 간선갯수
    array = [[0]*(V+1) for _ in range(V+1) ] # 인덱스와 노드숫자차이때문에 V+1로 생성
    visited = [False  for _ in range(V+1)] #방문 리스트
    Distance = [0 for _ in range(V+1)] #거리 리스트
    queue = []
    answer = 0 #경로없을시 0
    

    #######간선연결 2차원 리스트 만들기
    for i in range(E):
        x,y = list(map(int,input().split())) #노드이어주기
        array[x][y] = 1
        array[y][x] = 1 #방향상관없기때문에 대칭으로 넣어주기
    
    ####### 출발지/도착지 받기
    S,G = list(map(int,input().split()))
    queue.append(S) #출발지입력
    BFS() #가로탐색실행
    print('#{} {}'.format(tc,answer))
