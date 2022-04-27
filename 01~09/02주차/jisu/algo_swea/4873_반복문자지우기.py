# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개


# ```python
# 앞뒤로 반복되는 문자열을 지우고 남는 문자열의 갯수를 출력하시오
# 예) ABCCB -> CC 삭제 -> ABB -> BB 삭제 -> A -> 1 출력
# ```

# ### 풀이접근


# ```python
# 문자를 하나씩 꺼내서 스택에 담고,
# 그 다음문자와 스택의 마지막 문자를 비교한 뒤
# 같은 문자면 제거, 아니면 스택에 더해줌
# ```

# 코드

T = int(input())
for tc in range(1, T+1):
    string = list(input())
    stack = []  # 문자열을 하나씩 담을 stack
    for char in string:
        # if stack -> 빈 stack 일 때 False를 반환하여,
        # stack에 문자가 없을 때 else로 보내 char를 더해줌
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{tc} {len(stack)}')

    #  1
    #  ABCCB
