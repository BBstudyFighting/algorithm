while True: # 또는 while not (a == 0 and b == 0)

    a,b = map(int, input().split())

    if a == 0 and b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")
