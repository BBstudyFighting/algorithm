for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 합쳐질 수열 만들기
    array = [float('inf')]  # 양의 무한대 inf (최대값 구할 때 자주 활용)
    cnt = 0  # 수열 더해질때마다 추가될 cnt

    for _ in range(M):  # 수열갯수만큼 반복
        # 개별수열 a
        a = list(map(int, input().split()))
        for i in range(N*cnt+1):
            if a[0] < array[i]:
                array[i:i] = a
                break
        cnt += 1
    print(f'#{tc}', end=' ')
    print(*array[-11:-1][::-1])  # 뒤에서부터 역순으로 출력
