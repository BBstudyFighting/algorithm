# 주사위의 개수
def multi(nums: list) -> int:
    result = 0

    for x in nums:
        if not result:
            result = x
            continue
        result *= x

    return result

def solution(box: list, n: int) -> int:
    return multi([x//n for x in box])

if __name__ == '__main__':
    print(solution([1, 1, 1], 1))    # 1
    print(solution([10, 8, 6], 3))   # 12
####################################
def solution(box, n):
    w,h,d = box[0]//n,box[1]//n,box[2]//n 
    return w*d*h
####################################
def solution(box, n):
    answer = 0
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    return a * b * c