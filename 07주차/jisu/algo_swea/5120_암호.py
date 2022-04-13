for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # N개의 숫자, M칸 뒤, K회 반복
    array = list(map(int, input().split())) 
    index = M # M칸 씩 이동한 뒤 index

    for _ in range(K):  # 수열갯수만큼 반복
        index %= N # 현재 인덱스를 N으로 나눈 뒤 나머지
        if not index: # index가 0 (index == N)
            array.append(array[-1]+array[0]) # 마지막숫자 + 시작숫자
            index -= 1  # 이 경우엔 index -1 (이래야 리스트 요소 하나 추가된게 반영됨) 
        else: # 평범한 경우
          array.insert(index, array[index-1]+array[index])
        N += 1 # 리스트 요소 하나 추가
        index += M # M칸 뒤로 이동 

    print(f'#{tc}', end=' ')
    print(*array[-10:][::-1])  # 뒤에서부터 역순으로 출력
