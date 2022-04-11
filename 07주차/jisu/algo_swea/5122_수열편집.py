for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())  # N개의 숫자, M번 편집, 인덱스 L 출력
    array = list(map(int, input().split()))  # 최초 수열
    flag = 1  # array의 요소가 없는 경우 0으로 바뀜

    for _ in range(M):  # M번 편집
        rule = input().split()   # 법칙 입력
        # 법칙적용
        if rule[0] == 'I':
            array.insert(int(rule[1]), int(rule[2]))
        elif rule[0] == 'D':
            if not array:
                flag = 0
                break
            array.pop(int(rule[1]))
        else:
            array[int(rule[1])] = int(rule[2])

    if len(array) > L:  # 평범한 경우
        if flag:  # array에 요소가 있는 경우
            print(f'#{tc} {array[L]}')
        else:  # array에 요소가 없는 경우
            print(f'#{tc} -1')
    else:  # L이 array의 최대 인덱스보다 큰 경우
        print(f'#{tc} -1')
