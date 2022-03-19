# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg&&#)
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개


# ```python
# - N개의 피자를 굽는 원형화덕이 있다. 1번부터 M번의 피자를 순서대로 틀에 넣을 때,
#   피자마다 치즈 녹는 시간이 달라 꺼내는 순서는 바뀔 수 있다.
#   아래 조건에 따라 피자를 구울 때 마지막에 남아있는 피자 번호는 ?

# - 피자는 1번 위치에서 넣거나 뺄 수 있다.
# - 화덕의 피자는 1번에서 잠시 꺼내 확인하고 다시 1번에 넣을 수 있다
# - M개의 피자에 뿌려진 치즈양이 주어지고, 화덕을 한 바퀴 돌면 반(C//2)이 녹는다.
# - 치즈가 다 녹으면(C==0) 1번 화덕에서 꺼내고, 거기에 남은 피자를 순서대로 넣는다.
# ```

# ### 풀이접근


# ```python
# - 입력된 치즈양(pizza)에 인덱스를 더해 cheese라는 리스트 만듦
# - 이 중 N개(cheese[:N])를 oven에 넣고 remain은 cheese[N:]로 분리
# - oven이 하나 남을 때까지 while문으로 반복
# ```

# 코드


# ```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 각 피자의 최초 치즈 양을 입력해준다
    pizza = list(map(int, input().split()))
    cheese = []
    # 입력된 치즈양에 인덱스 더해준다
    for i in range(M):
        cheese.append([i+1, pizza[i]])
    oven = cheese[:N]  # 화덕엔 N개까지 넣을 수 있음
    remain = cheese[N:]  # 남은 피자

    while len(oven) > 1:  # 하나 남으면 중단
        check = oven.pop(0)  # 맨 앞의 피자를 꺼냄
        check[1] //= 2  # check[0]은 인덱스
        # check[1](남은 치즈양)이 0이면,
        if check[1] == 0:
            if remain:  # 남은 피자가 있다면 넣는다
                oven.append(remain.pop(0))
        else:  # 치즈가 다 안녹았으면 다시 넣는다
            oven.append(check)
    # 화덕에 마지막 남은 피자 출력
    print(f'#{tc} {oven[0][0]}')
# ```

#      1
#      5 10
#      20 4 5 7 3 15 2 1 2 2


#     #1 6


# ### 개념더하기


# ```python
# 양방향 큐(deque)
# - 앞 뒤 양쪽 방향에서 요소를 추가하거나 제거 할 수 있다.
#   (일반 큐는 선입선출방식으로 한쪽에서 추가, 한쪽에서 제거만 가능)
# ```
