def RSP(x,y): #1<2<3<1
    rsp_x = [[1,3],[2,1],[3,2]]
    rsp_y = [[1,2],[2,3],[3,1]]
    if card[x] == card[y]:
        return x
    else:
        if [card[x],card[y]] in rsp_x:
            return x
        else:
            return y

def half(start,end):
    if start == end:
        return start
    a = half(start, (start+end)//2)
    b = half((start+end)//2 +1, end)
    return RSP(a,b)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(map(int,(input().split())))
    
    answer = half(0,N-1)+1
    print("# {} {}".format(tc, answer))
