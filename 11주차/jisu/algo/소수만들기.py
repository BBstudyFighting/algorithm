from itertools import combinations
# combinations()는 중복없이 배열의 조합을 리턴

# 소수판별함수
# 1과 자기자신으로만 나눌 수 있으면 True 반환


def prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):
            # 다른수로 나눠지면 False
            if num % n == 0:
                return False
        return True


def solution(nums):
    answer = 0
    # nums의 요소를 3개씩 조합한 리스트 cmb
    cmb = list(combinations(nums, 3))
    for arr in cmb:
        if prime_number(sum(arr)):
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]
solution(nums)
