# 주식가격
# prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]
def solution(prices):
    length = len(prices)
    
    # answer을 max값으로 초기화  
    answer = [ i for i in range (length - 1, -1, -1)]
    
    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
# stack의 초기값에는 0번 인덱스를 넣어준다.
# prices를 순회한다. (1~n-1까지)
# stack이 있을 경우, 현재 순회하는 값이 stack의 top 인덱스에 해당하는 prices의 값보다 작을 경우 아래 과정을 반복한다.
# stack에서 값을 pop한다.
# 위에서 pop한 인덱스의 answer 값을 (작아질 때의 인덱스 - pop한 인덱스)로 변경한다.
# stack에 순회하는 인덱스를 append한다.