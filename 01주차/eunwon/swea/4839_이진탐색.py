T = int(input())
for tc in range(1, T+1):
    P,Pa,Pb = map(int,input().split()) # 1<= P, Pa, Pb <=1000
    pages =[1,P] #첫번째 페이지/ 끝페이지
    
    A_cnt = 0 #A가 이겼을때 1로 바뀜
    B_cnt = 0 #B가 이겼을 때 1로 바뀜
    for j in range(10): 
        # 1 400: 1+1
        #n=1 1 200 400 :2^1 +1
        #n=2 1 100 200 300 400 :4+1 2^2+1
        #n=3 1 50 100 150 200 250 300 350 400 :8 +1 2^3+1
        # 2^10 = 1024, P<=1000이므로 n = 10회 반복되면 1~1000까지 모든페이지를 담을수있다
        element =[] #이진 탐색후 페이지 리스트
        for i in range(len(pages)-1):
            pg_i = int((pages[i]+pages[i+1])/2)
            element.append(pg_i) #리스트에 담기
        pages = list(set((pages + element))) #페이지와 엘리먼트를 합해서 중복 제거
        pages.sort() #순서대로 정렬
        if pages.count(Pa) == 1: #Pa값이 있을경우
            A_cnt += 1
        if pages.count(Pb) == 1: #Pb값이 있을경우
            B_cnt += 1
        if A_cnt != 0 or B_cnt != 0: #A나 B가 먼저이겼을 경우 반복중단
            break    
        
    
    if A_cnt > B_cnt:
        answer ="A"
    elif A_cnt < B_cnt: 
        answer = "B"
    else:
        answer = 0
    print('#{} {}'.format(tc,answer))

        




