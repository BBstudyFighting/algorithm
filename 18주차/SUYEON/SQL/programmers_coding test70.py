# 문자열 정렬하기 (1)
def solution(my_string: str) -> list:
    return sorted([int(x) for x in my_string if x.isdigit()])

def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

# 가장 큰 수 찾기
def solution(array):
    return [max(array), array.index(max(array))]