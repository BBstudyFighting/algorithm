n = int(input())
opinion = []

for i in range(n):
    opinion.append(int(input()))


if opinion.count(1) > opinion.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

#########################################

n = int(input())
cute = not_cute = 0

for i in range(n):
    if int(input()) == 1:
        cute += 1
    else:
        not_cute += 1

print("Junhee is cute!" if cute > not_cute else "Junhee is not cute!")
