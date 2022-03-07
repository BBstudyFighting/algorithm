# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg)  
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개 


# ```python
# Forth는 스택 연산으로 후위 표기법을 사용하고, '.'으로 숫자를 꺼내 출력한다.
# 형식이 잘못되면 'error'를 출력한다
# 예)
# 10 2 + 3 4 + * . -> 84
# 5 3 * + . -> error
# 1 5 8 10 3 4 + + 3 + * 2 + + + . -> 168
# ```

# ### 풀이접근


# ```python
# 숫자를 만나면 스택에 push한다.
# 연산자를 만나면 필요한만큼의 숫자를 스택에서 pop하고
# 연산결과를 다시 스택에 push함
# ※ 후위표기법 계산시 연산자를 만나면 스택에서 두번 pop하여 계산
#    예) 6 5 2 8 - * 2 / + 
#     1) 2 - 8 = - 6 push 
#     2) 6 5 -6 * 2 / + 
#     3) 5 * -6 = -30 push
#     4) 6 -30 2 / + 
#     5) -30 / 2 = -15 push
#     6) 6 -15 + -> 결과 : -9
# ```

### 코드

# ```python
T = int(input())
for tc in range(1, T+1):
    forth = list(input().split())
    stack = [] # 후위표현식 계산을 위한 스택
    error = False # 에러처리를 위한 변수 설정
    
    # 마지막 . 빼고 for문 넣기 
    for i in range(len(forth)-1):   
        if forth[i].isdigit(): # 숫자라면 스택에 더하고
            stack.append(forth[i])
        # 연산자면 숫자 두개 빼서 계산    
        else: 
            # 에러 처리를 위한 try 문 
            try: 
            # 숫자 2개씩 뽑기
                b = int(stack.pop())
                a = int(stack.pop())
                # 연산자에 따라 다른 계산
                if forth[i] ==  '+':
                    c = a + b
                elif forth[i] ==  '-':
                    c = a - b
                elif forth[i] ==  '*':
                    c = a * b
                elif forth[i] ==  '/':
                # 나머지는 버려야하니까 '//' 연산자 활용
                    c = a // b 
                stack.append(c)
            except: # 숫자도 연산자도 아니면 에러
                error = True
                
    # 에러가 True 이거나 스택에 남은게 하나가 아니면 error 출력
    if error == True or len(stack) != 1:
        print(f'#{tc} error')
    else: # 스택에 마지막 남은 건 후위 연산 결과
        print(f'#{tc} {stack.pop()}')
# ```

#      1
#      1 5 8 10 3 4 + + 3 + * 2 + + + .


    #1 168

