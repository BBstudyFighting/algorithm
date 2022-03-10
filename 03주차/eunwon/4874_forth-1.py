T = int(input())
for tc in range(1,T+1):
    data = list(input().split())
    N = len(data)
    stack = []
    flag = 0

    # 마침표는 제외하기 위해 N-1까지 반복
    for i in range(N-1):  
        
        #숫자인 경우, stack에 append
        if data[i].isdigit():
            stack.append(data[i])

        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if data[i] == "+": result = num1 + num2
                elif data[i] == "-": result = num1 - num2
                elif data[i] == "/": result = num1 / num2
                elif data[i] == "*": result = num1 * num2
                stack.append(result)
            
            except: #에러 발생 예외 처리 예) 숫자 + 연산자 + 연산자
                flag = 333
    #예외처리 조건 (X) + Stack의 길이가 1인 경우(계산이 성공적인경우)
    if flag == 0 and len(stack) == 1:
        print(f'#{tc} {stack[0]}')

    #예외처리 조건 (O) + stack의 길이가 2이상인 경우 ex) 숫자만 입력된 경우
    elif flag == 333 or len(stack)>1:
        print(f'#{tc} error')