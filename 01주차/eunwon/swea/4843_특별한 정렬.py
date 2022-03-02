T = int(input())
for tc in range(1,T +1 ):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort() 
    ordered_list = []
    for i in range(5): #10/2
        ordered_list.append(numbers.pop(N-1-2*i)) 
        #정렬후 가장 마지막값 = 가장큰값
        ordered_list.append(numbers.pop(0))
        #정렬후 가장 첫번째값 = 가장작은값
    answer =  " ".join(map(str, ordered_list)) 
    #str아닌 값을 join으로 합치기위해 str함수를 map으로 적용시킨 후 join함수로 합쳐줌
    print('#{} {}'.format(tc, answer))