# 큰 수 만들기
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
# 스택 생성 => 파이썬에서는 리스트 활용 가능
# number를 순회 => for num in number:
# 다음 조건문을 모두 만족할 경우 명령문을 반복
# 조건문
# 1. k > 0
# 2. 스택이 비어있지 않음
# 3. 스택 마지막 값 < num
# 명령문
# 1. 스택을 pop
# k--
# 스택에 num을 push
# k > 0 이상이면 스택에서 k개 삭제 후 join해서 결과 값 반환
#########################################################
# 위 코드에서 중복되는 부분이나 불필요한 부분을 줄이고 최적화된 코드로 작성해보았습니다.
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])
#########################################################
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)