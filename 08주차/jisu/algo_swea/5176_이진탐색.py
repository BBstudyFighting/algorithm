# 입력된 tree에 종속되는 sub_tree의 함수 작성
def make_tree(n):
    global count

    # N값이 넘어가지 않아야함
    if n <= N:
        # 왼쪽노드는 현재 인덱스의 2배
        # 예) 6인 경우 1 - 2 - 4 / 3 - 6
        make_tree(n*2)  # 함수 안에 함수(재귀함수) 활용

        # 최하단 노드까지 갔으면 값 넣기
        tree[n] = count
        count += 1  # 다음값을 넣기 위해 count 증가

        # 오른쪽노드는 인덱스 2배 +1
        make_tree(n*2 + 1)


for tc in range(1, int(input()) + 1):
    N = int(input())

    # 트리표시를 위한 리스트
    tree = [0 for i in range(N+1)]
    count = 1
    make_tree(1)  # 함수에 가장 하단 왼쪽노드값인 1 대입

    print(f'#{tc} {tree[1]} {tree[N//2]}')
