price, ea, money = map(int, input().split())

if price*ea > money:
    print(price*ea - money)
else:
    print("0")