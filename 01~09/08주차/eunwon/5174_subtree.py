def sub_tree(idx): 
    global count  # 횟수세기

    for i in range(2): #자식 row 0,1 탐색
        if tree[i][idx]: # 해당되는 곳에 값이 있으면
            count += 1 # 카운트 증가
            nidx = tree[i][idx] # 그값을 인덱스값으로 활용
            sub_tree(nidx) # 다음 세대 확인(반복)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int,input().split()))
    
    # 문제에 주어진것 처럼 row 기준으로 0, 1로 활용
    tree = [[0 for _ in range(E+2)]for _ in range(2)] 
    #노드번호 = E+!=> 인덱스때문에 E+1+1

    for i in range(E): #간선E개에 대해서
        
        idx = temp[2*i]
        number = temp[2*i+1]
        
        if not tree[0][idx]: # 값이없다면
            tree[0][idx] = number #값할당
        
        else: #  이미 있다면 가지 하나 더 만들어줌
            tree[1][idx] = number

    # 시작하면서 자동으로 하나 포함
    count = 1
    # N부터 실행
    sub_tree(N)
    print("#{} {}".format(tc, count))