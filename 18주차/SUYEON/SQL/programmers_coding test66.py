# 문자열 밀기
def solution(A: str, B: str) -> int:
    result = 0

    while result != len(A):
        if A == B:
            return result
        A = A[-1] + A[:-1]
        result += 1

    return -1

solution=lambda a,b:(b*2).find(a)
