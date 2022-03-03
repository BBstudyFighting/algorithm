t = int(input())
for i in range(t):
    num, str = input().split()
    text = ''
    for i in str:
        text += int(num) * i
    print(text)