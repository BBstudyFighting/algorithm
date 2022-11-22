# 특이한 정렬
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
## answer = sorted(numlist,key = lambda x : (abs(x-n), n-x)) key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다. 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다. 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열되는 것 같다(인덱스가 작은 것이).

# 최빈값 구하기
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

def solution(array: list) -> int:
    dict = {}

    # for 반복문으로 입력 list 순회
    for num in array:
        # 딕셔너리에 현재 값이 할당되있지 않다면 1 할당
        if num not in dict:
            dict[num] = 1
        # 그렇지 않을 시, 증감
        else:
            dict[num] += 1
            
    # 딕셔너리의 벨류값 기준으로 desc 정렬
    result = sorted(dict.items(), key=lambda x: x[-1], reverse=True)
    
    if len(result) <= 1:
        return result[0][0]
    # 최빈값이 여러개면, -1 반환
    return result[0][0] if result[0][-1] != result[1][-1] else -1