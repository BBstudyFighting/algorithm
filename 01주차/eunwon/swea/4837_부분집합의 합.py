T=int(input()) 
for tc in range(1,T+1): 
    N,K=map(int,input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    subset = []
    for i in range(1 << 12): #2의 12승개
        element =[]
        for j in range(12):
            if i & (1 << j):
                element.append(A[j])
        if len(element) == N:
            subset.append(element) #부분집합 형성(전체다계산X, N길이까지만)

    count = 0
    # 내장함수 sum 대신 total로 합을 구해서 원하는 값이 나오면 카운트
    # 내장함수 사용시 위의 반복문에서 종료 가능
    for i in range(len(subset)):
        total = 0
        for j in subset[i]:
            total += j
        if total == K:
            count += 1
    #최종 출력 예시
    print('#{} {}'.format(tc, count))