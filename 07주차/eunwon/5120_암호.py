T = int(input())
for tc in range(1,T+1):
    N,M,K = list(map(int,input().split())) 
    #수열길이N, 간격M, 횟수K
    nums = list(map(int,input().split())) #수열받기
    idx = 0 #인덱스 기본값
    for i in range(1,K+1): #K번만큼 반복
        idx += M #idx는 M간격으로 늘어남(횟수가 늘어날수록)
        if idx < N: #인덱스가 N보다 작을때는 강인서트로 더한값삽입
            nums.insert(idx, nums[idx-1]+ nums[idx])
        else: #인덱스가 N보다 클때
            if idx % N: #N으로 나누면 0이아닐때
                idx %= N #나머지를 구함
                nums.insert(idx, nums[idx - 1] + nums[idx])
            else: #N으로 나누어 0일때 맨앞자리에 삽입 따라서 따로 인덱스 번호지정
                nums.insert(idx, nums[-1] + nums[0])
        N += 1 #for문 한번끝날때마다 N+1해주기(하나씩삽입되니까)

    answer = nums[-1:-11:-1]
    print("#{}".format(tc), end = ' ')
    print(*answer)
