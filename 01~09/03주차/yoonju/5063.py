T = int(input())

for i in range(1, T+1):
    r,e,c = map(int, input().split())
    
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("does not advertise")