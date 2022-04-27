def min_heap(node):
    up_node = node//2
    if up_node < 0:  # 루트노드에 도달하면 리턴
        return
    else:
        # 부모노드가 더 크면 위치 바꿔줌
        if tree[up_node] > tree[node]:
            tree[node], tree[up_node] = tree[up_node], tree[node]
            min_heap(up_node)  # 함수에 부모노드 대입해서 반복


for tc in range(1, int(input()) + 1):
    N = int(input())  # 노드갯수
    tree = [0]
    node_num = 1
    for num in map(int, input().split()):
        tree.append(num)
        min_heap(node_num)
        node_num += 1

    sum_value = 0
    while N:  # N(마지막)노드의 조상노드 값들 더함
        N //= 2
        sum_value += tree[N]

    print(f'#{tc} {sum_value}')
