# 입력된 tree에 종속되는 sub_tree의 함수 작성
def sub_tree(idx):
    global count # 서브트리 노드 개수 count
    
    # 노드의 자식노드 좌우검사 (0을 좌, 1을 우로 설정)
    for i in range(2):
        if tree[i][idx]: # 좌 or 우에 값이 있으면
            count += 1 # 서브트리 노드갯수 1 증가 
            # 현재 tree노드값을 대입해 다음 세대확인 
            n = tree[i][idx]
            sub_tree(n)

for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split()) # 간선갯수 E, 서브트리루트노드 N 
    temp = input().split() # 부모-자식 노드 입력받기 
    
    # 좌우에 있는 자식을 표현하기 위한 2차원 리스트
    tree = [[0 for _ in range(E+2)]for _ in range(2)]
    
    for i in range(E): 
        idx = int(temp[2*i]) # tree 부모노드
        number = int(temp[2*i+1]) # tree 자식노드
        # 값이 없으면 좌측에 number 대입 
        if tree[0][idx] == 0:
            tree[0][idx] = number
        # 값이 있으면 우측에 number 대입
        else:
            tree[1][idx] = number
            
    count = 1 # 루트노드도 카운트되니 1부터 시작
    sub_tree(N) # N부터 실행 
        
    print(f'#{tc} {count}')