def chk(y):
    global temp, result 
    
    if temp > result: #3열가기도전에 크면 끝까지 result값그대로 
        return
    
    if y==N:
        if temp < result: #3열갔더니 temp가 최소합 따라서 result로 바꿔줌
            result=temp
            return
    else:
        for x in range(N): #행에대해서 반복
            if not visit[x]:  #방문하지않은 행에대해서
                
                visit[x]=1 #방문설정
                temp += array[y][x] #합해줌
                chk(y+1) #재귀함수
                
                visit[x]=0 #다시돌려주기
                temp -= array[y][x]
T = int(input())
for tc in range(1,T +1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    print(array)
    visit=[0]*N
    
    temp,result=0,999999
    chk(0)
    print(f'#{tc} {result}')