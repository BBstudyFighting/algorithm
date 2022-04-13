def change(node):
    parent = tree[node][0]
    if parent:#루트노드가 아니면
        if tree[parent][3] > tree[node][3]:#규칙이 지켜지지않으면
            tree[parent][3], tree[node][3] = tree[node][3], tree[parent][3]
    else:
        return
    change(parent) #재귀-> 반복

def sum(n):
    global answer
    if not tree[n][0]: ## 루트노드라면 걍 리턴
        return
    answer += tree[tree[n][0]][3] #tree[N][0]:부모노드 전체의 [3] :N의부모노드값
    sum(tree[n][0]) #부모노드넣어서 재귀->반복

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [[0]*4 for _ in range(N+1)] #4=부모인덱스,왼쪽자식,오른쪽자식,내값 #N+1: 노드와 인덱스의 숫자차이떄문에 +1

####이진 트리만들기
    for i in range(1,N+1):
        tree[i][3] = nums[i-1] #nums수열을 일단 차례대로 넣기:[3]노드 자신의 값
        tree[i][0] = i//2 #부모인덱스: i//2 
        if 2*i <= N: #범위내에있을때
            tree[i][1] = 2*i #왼쪽자식인덱스 2*i
            tree[i][2] = 2*i +1 #오른쪽 자식인덱스 2*i +1
            if 2*1 +1 >=N: #오른쪽자식 범위밖으로 나가면 0처리
                tree[i][2] = 0

####이진트리 값을 규칙에 맞게 변경
    for i in range(1,N+1):
        change(i)

##### 부모노드 합구하기
    answer = 0
    sum(N) #마지막 노드:N 의 조상 노드에 저장된 정수의 합

    print("#{} {}".format(tc, answer))