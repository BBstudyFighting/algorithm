# 공 던지기
def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1

from collections import deque
def solution(numbers, k):
    array = deque(numbers)
    array.rotate(-(k-1)*2)
    return array[0]

# 종이 자르기
def solution(M, N):
    return (M * N) - 1

def get_cut_cnt_dfs(width, height):
    width, height = min(width, height), max(width, height)

    if width == 1 and height == 1:
        return 0

    return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

def solution(M, N):
    return get_cut_cnt_dfs(M, N)