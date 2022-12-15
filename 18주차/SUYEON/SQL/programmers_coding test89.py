# k의 개수
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer


def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        if str(k) in str(num):
            answer += str(num).count(str(k))
    return answer