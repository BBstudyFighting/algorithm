for tc in range(1, int(input()) + 1):
    # 최초수열갯수 N, 추가숫자갯수 M, 출력할 인덱스 L
    N, M, L = map(int, input().split())
    # 수열만들기
    array = list(map(int, input().split()))
    for _ in range(M):
        idx, num = map(int, input().split())
        # 인덱스와 숫자입력받고, insert로 지정한 위치에 넣기
        array.insert(idx, num)
    print(f'#{tc} {array[L]}')
