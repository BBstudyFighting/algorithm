T = int(input())
for tc in range(1,T+1):
    N = int(input())
    node = []
    for i in range(N):
        node.append(list(map(int,input(i).split())))
    print(node)