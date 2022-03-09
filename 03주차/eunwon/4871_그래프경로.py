def DFS(start, end): #DFS함수를 만드는데 시작과 끝을 인자로 받는다. 
    stack=[] #빈 스택 생성 
    visited=[False]*(V+1) #경로에 있는지 없는지 확인
    stack.append(start) #start인수를 스택에 추가 
    while stack: #stack이 비어있는 동안 
        now=stack.pop() #stack을 pop으로 꺼내 현재값 지정 
        visited[now]=True #현재값이 방문했다면 
        for i in range(1, V+1): #1부터 V까지의 숫자까지(V는 가장 큰 숫자) 
            if not visited[i] and node[now][i] == 1: #만약 i번째에 방문하지 않고 연결되어있다면 if not visited[i]:visited[i]가false 이고 node[]
                stack.append(i) #경로로 될수 있으므로 stack에 추가해준다. 
    if visited[end]: #만약 끝점을 갔었다면 
        return 1 #1을 반환하고 
    else: 
        return 0 #아니면 0을 반환한다.

# 출처: https://totoma3.tistory.com/129 [토토모의 분석일지]
T = int(input())
for tc in range(1,T+1):
    V, E = list(map(int,input().split()))
    node = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a,b = list(map(int,input().split()))
        node[a][b] = 1 ### not ==(판단->true/false)
    
    S,G = list(map(int,input().split()))
    print("#{} {}".format(tc, DFS(S,G)))
