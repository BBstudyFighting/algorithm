for tc in range(int(input())):
    # 노드 N개, 리프노드 M개, 출력노드 L번
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]  # 루트노드 번호가 1이니 +1

    for _ in range(M):  # 리프노드번호와 값 입력받고 트리에 대입
        idx, value = map(int, input().split())
        tree[idx] = value

    for i in range(N, 0, -1):
        # 마지막 노드부터 역순으로 부모노드 값 대입
        if i // 2 > 0:
            tree[i//2] += tree[i]

    print(f'#{tc+1} {tree[L]}')
