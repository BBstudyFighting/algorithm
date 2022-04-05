for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))
    for _ in range(M):
        idx, num = map(int, input().split())
        array.insert(idx,num)
    print(f'#{tc} {array[L]}')