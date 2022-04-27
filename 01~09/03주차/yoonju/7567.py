plate = list(str(input()))
total = 0

for i in range(len(plate)):
    if i == 0:
        total += 10
    elif plate[i-1] == plate[i]:
        total += 5
    else:
        total += 10

print(total)