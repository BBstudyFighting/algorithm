# 징검다리
def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    
    rocks.sort() #정렬되어 있지 않은 상태이기 때문에 정렬해야한다.
    
    #이분 탐색
    while start <= end: 
        mid = (start + end) // 2 #중간값을 구한다.
        del_stones = 0 #제거한 돌을 카운트하기 위한 변수
        pre_stone = 0 #기준이되는 돌(시작지점)
        for rock in rocks: #징검다리를 돌면서 
            if rock - pre_stone <  mid: #돌사이의 거리가 가정한 값보다 작으면 제거한다.
                del_stones += 1 
            else: #아니라면 그 돌을 새로운 기준으로 세운다.
                pre_stone = rock
             
            if del_stones > n: #제거된 돌이 문제 조건 보다 크면 for문을 나온다
            	break
                
        if del_stones > n: #제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽으로 줄인다.
            end = mid - 1
        else: #반대라면 큰 쪽으로 줄인다.
            answer = mid
            start = mid + 1
            
    return answer

# 이번 문제에서 기준은 n개의 돌을 징검다리에서 제거했을 때 최소 거리이다. 먼저 범위를 생각해보면 최소값은 징검다리에 돌이 겹쳐있는 경우는 없기 때문에 1이다. 최대 값은 시작지점과 도착지점사이의 거리인 distance이다. 이 값을 기준으로 중간값(mid)가 n개의 돌을 제거했을 때 돌 사이의 거리중 최소값이라고 가정해보자.
# 이 가정하에 돌을 제거했을 때 이 값(mid)보다 작은 거리는 없어야 한다.
# 즉 돌 사이의 거리를 구했을 때 이 mid 값보다 작으면 제거하고 크면 두는 방식의 전략을 사용해야한다.
# 돌 사이의 거리를 모두 재는 것은 무의미하므로 시작지점(0)으로부터 mid값 보다 먼 거리에 있는 돌을 찾기 전까지 돌을 제거하고 찾으면 그 돌을 새로운 기준으로 삼아 다시 돌 사이의 거리를 측정하면 된다.