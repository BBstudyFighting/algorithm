# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg&&#)
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개


# ```python
# - N개의 숫자로 구성된 수열이 있다.  i.g 1211 2213 3241 4242 5155
# - 맨 앞 숫자를 맨 뒤로 보내기를 M번 했을 때, 수열 맨 앞에 있는 숫자를 출력하시오.
#     i.g 2213 3241 4242 5155 1211
# ```

# 풀이접근


# ```python
# - 첫번째 인덱스를 꺼내 (pop) 가장 앞에 더해준다 (append)
# ```

# 코드


# ```python
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(m):
        nums.append(nums.pop(0))

    print(f'#{tc} {nums[0]}')
# ```

#      1
#      10 23
#      17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

    # 1 2412
