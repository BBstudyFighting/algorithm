def make_tree(idx): 
    if tree[idx]: #값이있으면 값 그대로 반환
        return tree[idx]
    # 값이 없으면 즉 0이면
    a= make_tree(idx*2) if idx*2 <=N else 0
    b= make_tree(idx*2 +1) if idx*2 +1 <=N else 0
    
    return a+b #자식노드를 더해줌

T = int(input())
for tc in range(1,T+1):
    N,M,L = list(map(int,input().split()))
    tree = [0] * (N+1) ####트리생성
    
    ####리프 입력
    for i in range(M):
        idx, val = list(map(int,input().split()))
        tree[idx] = val
    
    print("#{} {}".format(tc, make_tree(L)))