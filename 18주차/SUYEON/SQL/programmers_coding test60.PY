# 숫자 찾기
def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1
    
# 최댓값 만들기 (2)
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 