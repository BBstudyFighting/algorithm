T = int(input())
for tc in range(1,T+1):
    data = input().split()
    stack = []
    operators = {
        '+': lambda x, y: x + y, 
        '-': lambda x, y: x - y, 
        '*': lambda x, y: x * y, 
        '/': lambda x, y: x // y, 
        }        #기호에 대한 연산자를 만들어둔다.



    # 마침표는 제외하기 위해 N-1까지 반복
    for i in data:  
        if i == '.': #만약 '.'가 나왔을때 
            if len(stack) > 1: #stack에 결과값하나만 있지않은경우
                result = "error" #error를 도출하고
            else:
                result = int(stack.pop()) #stack이 비어있지 않으면 정수로 변환 후 pop한것을 결과


        elif i in operators.keys():
            if len(stack) < 2: #만약 stack이 계산할 수 없는 상황일때 
                result = "error" #error를 도출 
                break 
            else: 
                a = int(stack.pop()) #a는 pop한 정수
                b = int(stack.pop()) #b는 pop한 정수 
                c = operators[i](int(b), int(a)) #연산자의 i번째를 계산
                stack.append(int(c)) #정수로 변환후 stack에 추가 
        else : stack.append(i) 
    
    print("#{} {}".format(t, result))


# 출처: https://totoma3.tistory.com/131 [토토모의 분석일지]
