# page는 끝페이지, target은 찾을 페이지

# 이진탐색 함수정의
def binary_search(page, target):
    start = 1     # 시작점
    end = page    # 끝점
    count = 0  # 검색 수행할 때마다 +1

    # 이진탐색 구현하는 while문
    while start <= end:
        mid = int((start+end) / 2)  # 중앙점
        if mid == target:
            # 중앙점과 target 일치 -> count 리턴
            return count
        elif mid < target:  # 중앙점이 타겟보다 작으면
            start = mid  # 시작점을 중앙점으로 바꿈
            count += 1
        elif mid > target:  # 중앙점이 타겟보다 크면
            end = mid  # 끝점을 중앙점으로 바꿈
            count += 1


# 함수실행
T = int(input())
for tc in range(1, T + 1):
    # 책 끝페이지, a가 찾을 페이지, b가 찾을 페이지
    page, a, b = map(int, input().split())

    count_a = binary_search(page, a)
    count_b = binary_search(page, b)

    if count_a > count_b:
        result = 'B'
    elif count_b > count_a:
        result = 'A'
    else:
        result = 0

    print(f'#{tc} {result}')
