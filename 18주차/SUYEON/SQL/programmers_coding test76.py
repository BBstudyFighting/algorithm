# 중앙값 구하기
def solution(array):
    return sorted(array)[len(array) // 2]

def solution(array):
    array = sorted(array)
    length = len(array)//2
    return array[length]

# 편지
def solution(message):
    return len(message)*2