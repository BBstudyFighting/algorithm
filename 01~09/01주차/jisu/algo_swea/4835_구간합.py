# T 만큼 반복
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())  # 정수(n) & 구간(m)의 갯수
    nums = list(map(int, input().split()))  # 구간리스트 입력 (nums)

    range_sum = []  # 구간합 리스트
    # n-m+1 만큼 반복하며 구간합 (n-m=0이어도 1회 진행하므로 +1)
    for i in range(n-m+1):
        range_sum.append(sum(nums[i:i+m]))  # i 기준 +m 까지의 구간합

    print(f'#{tc} {max(range_sum)-min(range_sum)}')
