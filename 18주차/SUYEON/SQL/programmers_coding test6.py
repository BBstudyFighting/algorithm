# K번째수
def solution(array, commands):
    answer = []
    
    for i in commands:
        ary = array[i[0]-1: i[1]]    # 문제에서 주어진 크기만큼 자르기
        # new_array = array[command[0]:command[1]]  이렇게 짠다면 command[2]:command[5] 이렇게 나오게 됩니다. => 3번째부터 5번째수까지 잘리게됨. n번째부터 자른다고 하면 n-1번째 인덱스부터 잘라주어야합니다.
        ary.sort()    # sort 함수로 정렬
        answer.append(ary[i[2]-1])    # k 번째 값 집어넣기
        
    return answer
###########################################
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
###########################################
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
