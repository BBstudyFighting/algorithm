def Melt():
    while len(fire) > 1: #fire리스트길이가 1이 아닌동안 ->1개 남으면 break
        cheese = fire.pop(0)
        if cheese[1]//2 != 0: # 녹은후 0이 아니면
            cheese[1] = cheese[1]//2 #바꿈
            fire.append(cheese) #뒤로 다시 넣어줌
        else:                #녹은게 0이라면
            if remain:       # remain 남은원소가 있다면
                fire.append(remain.pop(0))   #추가
    return fire[0][0] #마지막남은 원소의 enumerate[i+1,p]중 0번째                
    
T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    pizza_list = list(map(int, input().split())) # pizza 리스트
    pizza = [[i+1, p] for i, p in enumerate(pizza_list)]  # 각 피자의 인덱스와 치즈를 같이 저장
    fire = pizza[:N]  # 처음 화덕에 들어갈 수 있는 피자
    remain = pizza[N:]  # 못 들어가고 남는 피자
    
    
    
    print('#{} {}'.format(tc, Melt()))
    
