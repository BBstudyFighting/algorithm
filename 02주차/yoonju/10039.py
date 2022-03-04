ts_lst = []

for i in range(5):
    ts = int(input())
    if ts >= 40:
        ts_lst.append(ts)
    else:
        ts = 40
        ts_lst.append(ts)

ts_ave = sum(ts_lst)/len(ts_lst)

print(ts_ave)

        