# 도둑질
def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대

# 첫 집 부터, 마지막 집까지 하나씩 추가하면서 최대로 가져올 수 있는 값을 구한다.
# 집이 하나 있을 경우, 그 집을 터는게 최대값
# 집이 두 개 있을 경우, 인접한 집을 털지 못하므로 두 집 중 money가 큰 집을 턴다.
# 집이 3 개만 있을 때, 현재 i 집 money + i-2 번째 집 money 혹은 i-1집 money 중 더 큰 값을 가져오면 된다.
# 하지만, 첫 집과 마지막 집이 둘다 포함되는 경우가 생길 수 있기 때문에
# 1) 첫 번째 집을 무조건 털고, 마지막 집은 털지 않는 경우
# 2) 마지막 집을 무조건 털고 첫 번째 집은 털지 않는 경우
# 로 나눠서 생각해야 한다.

########################################
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)
# 초기화에서는 첫 번째 집을 선택했을 경우, 두 번째는 선택하지 않은 경우 그 후 반복문에서는 x와 y 중 더 큰 값에 i 의 값을 더한 후에 x, y 값을 y, z 값으로 초기화 해주는 방식