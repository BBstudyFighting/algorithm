T = int(input())
for tc in range(1,T+1):
    H = (int(input()))/10
    print(H)
    #기본도형모형
    #1번도형(1,2) 2번도형(2,1) 3번도형(2,2)
    #############가로합 = H / 세로합 = 2
    combi = []
    for a in range(31) :#a=1번도형의 갯수 range = 가로길이/1번도형 가로길이 +1
        for b in range(16):#b=2번도형의갯수
            for c in range(16):#3번도형의 갯수
                if a + 2 * b + 2 * c == H : ###가로길이 구하는 방정식
                    combi.append([a,b,c])
    answer = 0
    print(combi)
    #나온값 [a,b,c]를 순서에따른 경우의수 따로 구해야함 어떤게있을까.....