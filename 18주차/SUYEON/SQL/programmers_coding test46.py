# 순위
def solution(n, results):
    answer = 0
    # 승패를 저장하기 위해 win과 lose배열
    # 각 배열의 index는 선수번호를 의미하고, 각 배열의 값들은 선수가 이기거나 진 선수들의 번호가 저장됩니다.
    # 초기에 주어진 경기 결과(results)를 사용하여 win과 lose 배열에 이기거나 진 선수들의 번호를 저장합니다. (for i, j in results: 반복문에 해당)
    win = [[]  for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for i,j in results:
        win[i].append(j)
        lose[j].append(i)
    for i in range(1,n+1):
        for w in win[i]:
            if lose[i] :
                for l in lose[i]:
                    if l not in lose[w]:
                        lose[w].append(l)
                    if w not in win[l]:
                        win[l].append(w)

    for w,l in zip(win,lose):
        if len(w)+len(l) == n-1:
            answer+=1
    return answer

# 선수 번호대로 win 배열을 접근하도록 for문을 구성하였습니다. (선수의 번호 변수는 i에 해당함)
# 그리고 i 선수가 이긴 선수를 for문을 이용하여 모두 접근합니다. (변수 w에 해당)
# 1. i 선수가 이긴 선수와 i선수에게 진 선수가 있을 때, 진 선수는 이긴 선수들에 대해 항상 지게 됩니다. 따라서 진 선수의 lose배열에 이긴선수들의 번호를 추가해줍니다. (lose[w].append(l))
# 2. i 선수가 이긴 선수와 i선수에게 진 선수가 있을 때, 이긴 선수는 진 선수들에 대해 항상 이기게 됩니다. 따라서 이긴 선수의 win 배열에 진선수들의 번호를 추가해줍니다. (win[l].append(w)
# 이를 다 거치고 나서 각 선수들의 win과 lose에 저장된 배열의 수의 합이 (전체선수-1)개 이면 전체 선수들에 해당하는 경기 결과가 저장되어 있다는 것을 의미한다. 따라서 이 조건에 만족하는 선수들의 수를 answer에 저장하여 return 한다.