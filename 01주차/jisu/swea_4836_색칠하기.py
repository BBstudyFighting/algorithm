T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]  # 10 x 10 2차원 배열

    cnt = 0  # 보라색될 때마다 하나씩 증가

    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):  # x축 이동하며 Loof
            for j in range(y1, y2+1):  # y축 이동하며 Loof
                if arr[i][j] == 1:
                    cnt += 1  # 좌표값 1이라면 이미 한번 만난 곳이므로 보라색 (cnt +1)
                elif arr[i][j] == 0:
                    arr[i][j] += 1  # 처음만난 좌표에 1 추가

    print(f'#{tc} {cnt}')
