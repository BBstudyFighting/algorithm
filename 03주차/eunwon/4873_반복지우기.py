T = int(input())
for tc in range(1,T+1):
    alp = input()#############주어진문자열 alphabet
    
    stack = [] ######### alp와 비교하여 반복되지 않는 문자열이 저장될 공간
    for i in range(len(alp)):
        if len(stack) == 0: ######### stack이 비어있는경우
            stack.append(alp[i]) ######일단 stack으로 추가하여 이후부터 비교
        else: ########################### stack이 비어있지않은경우 
            if  alp[i] == stack[-1]: ######alp i번째 문자열과 stack마지막문자: 원래 앞뒤 문자가 같으면 제거
                stack.pop()
            else :
                stack.append(alp[i]) #### 같지않으면 스택에 저장
    print("#{}, {}".format(tc, len(stack)))