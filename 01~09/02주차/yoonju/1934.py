T = int(input())

for tc in range(1, T+1):
    a,b = list(map(int, input().split()))
    
    A,B = a,b
    
    while a != 0:
        b = b % a
        a,b = b,a
    gcd = b
    lcm = A*B//b

    print(lcm)    
