T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(range(1, 13))  # 1~12 집합 nums
    cnt = 0
    # 부분집합 경우의 수만큼 반복 (비트연산자 활용)
    for case in range(1 << 12):  # 1 << 12 는 4096 (2의 12승)
        sub_sum = []  # 부분 집합 원소 담을 리스트
        sum_value = 0  # 부분 집합의 값
        for i in range(12):
            if case & (1 << i):  # 아래 참고
                sub_sum.append(nums[i])
                # sub_sum에 nums[i]을 리스트로 추가하고
                sum_value += nums[i]  # sum_value 에도 num[i] 값 추가
        if len(sub_sum) == n and sum_value == k:
            # 부분집합 원소갯수가 n개 이고 부분집합의 합이 k 면 cnt 증가
            cnt += 1

    print(f'#{tc} {cnt}')
