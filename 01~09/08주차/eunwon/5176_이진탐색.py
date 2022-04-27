def make_tree(idx):
    global number
    if idx<=N:
        make_tree(2*idx) #왼쪽으로 재귀함수(작은쪽)
        tree[idx] = number
        number += 1
        make_tree(2*idx + 1) #오른쪽으로 재귀함수(큰쪽)

        # 완전이진트리 순서 인덱스 = 1/2(2*idx), 3(2*idx+1)/4,5,-idx=2//6,7 idx = 3
        # 완전이진트리 값 순서 = 쭉왼쪽으로 가다가(재귀) 끝이면 1로 시작 부모노드로 가서 +1/ 그리고 오른쪽노드로 이동 후 왼쪽노드갈게없고(재귀) 오른쪽노드 갈게없으면 +1 


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1) #인덱싱때문에 N+1
    number = 1
    make_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))