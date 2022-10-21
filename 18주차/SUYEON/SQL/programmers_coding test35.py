# 구명보트
# 인덱스를 start, end 시점으로 투 포인터로 접근
# while문의 조건을 보면 인덱스 같아지는 시점(people의 모든 요소 다 조사됨)을 a<b로 표현한 것도 자주 보는데 난 잘 못 씀ㅠㅠ
# 또 return 값이 결국 len(people) - answer인 것은 전체 한 번은 옮겨야 하는데 가장 가벼운 것과 가장 무거운 것이 묶어서 되는 경우는 2명이 한 보트로 처리되기 때문에 전체에서 그 경우를 빼주려고 한 것 같다.
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
#############################################
# people 리스트를 덱으로 만든 후 내림차순 정렬
# 무거운 사람(왼쪽)과 가벼운 사람(오른쪽)을 인덱스로 매칭
# 합이 보트 무게보다 가벼우면 둘 빼냄
# 보트 무게보다 무거우면 무거운 사람만 빼냄
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer