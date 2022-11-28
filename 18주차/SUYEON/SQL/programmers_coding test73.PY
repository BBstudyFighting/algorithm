# 2차원으로 만들기
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]

def solution(num_list: list, n: int) -> list:
    return [num_list[x:x+n] for x in range(0, len(num_list), n)]

import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()