# 더 맵게
# 힙은 최소 힙과 최대 힙이 있는데 최소 힙은 루트 노드에 최솟값이 있는 것이고, 최대 힙은 루트 노드에 최대값이 있는 것
# 파이썬의 heapq에서는 최소힙만 지원
from heapq import *

def solution(scoville, K):
    count = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
    return count if scoville[0] >= K else -1