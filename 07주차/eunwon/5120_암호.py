T = int(input())
for tc in range(1,T+1):
    N,M,K = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    for i in range(1,K+1):
        idx = 0 + M*i
        nums.insert(idx, 0)
        nums[idx] == nums[idx - 1] + nums[idx + 1]
        if len(nums) <= idx:
            nidx = idx - len(nums)
            nums.insert(nidx, 0)
            nums[nidx] == nums[nidx - 1] + nums[nidx + 1]
    answer = nums[-1:-11:-1]
    print("#{}".format(tc), end = ' ')
    print(*answer)
