T = int(input())

for tc in range(1, T+1):
    N= int(input()) #갯수
    e1_list = [] #빨간색이 칠해진 좌표리스트
    e2_list = [] #파란색이 칠해진 좌표리스트

    for nc in range(N):
        nums = list(map(int, input().split())) #좌표인풋숫자화
        a,b,c,d,e = nums # 리스트 추출


    #여기에 문제로직이 들어감
        if e == 1: #빨간색일 때 
            for i in range(a,c+1): #행의 범위
                for j in range(b,d+1): #열의 범위
                    e1_list.append((i,j)) #튜플로 저장
        else:
            for i in range(a,c+1):
                for j in range(b,d+1):
                    e2_list.append((i,j))
    print(e1_list)
    print(e2_list)
    answer = len(list(set(e1_list) & set(e2_list))) # 교집합갯수 set과정에서 중복값사라지면서 합집합이 됨
            
    #최종 출력 예시
    print('#{} {}'.format(tc, answer))