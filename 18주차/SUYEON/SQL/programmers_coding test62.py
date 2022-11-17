# 가까운 수
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer

def solution(array: list, n: int) -> int:
    return array[sorted([[index, abs(n-num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0]]
# 주어진 list를 for 반복문으로 순회하면서 abs 내장함수로 절댓값을 구해 가장 가까운 값을 구한다.
# list에 [index, 가까운 값, 원래 값] 형태로 넣는다.
# sorted 내장함수로 가까운 값 순으로 오름차순 정렬 한 후, 가까운 수가 여러 개일 경우 더 작은 수를 가져와야하므로 원래 값을 두번째 정렬 기준으로 정렬한다.
# 첫번째 인덱스의 값을 가져오면 쉽게 구할 수 있다.
