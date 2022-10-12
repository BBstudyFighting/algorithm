# 올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
    
    return stack==[]




from collections import deque

def solution(s):
    stack = deque()
    for i in s:
        if i == ')' and not stack:  # 스택에 아무것도 없는데 ')'가 있는 경우
            return False
        elif i == ')' and stack[-1] == '(':  # 괄호쌍 없애줌
            stack.pop()
        else:  # i가 '('일 때
            stack.append(i)
    return True if not stack else False