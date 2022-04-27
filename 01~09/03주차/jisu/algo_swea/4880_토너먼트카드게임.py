# [문제출처 SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg)
# 문제의 저작권은 SW Expert Academy에 있습니다.

# ### 문제소개


# ```python
# - 1번부터 N번까지 N명의 학생이 - 가위(1) 바위(2) 보(3) 카드를 고른 뒤
#   토너먼트로 대결했을 때 최종 승자가 누구인지 찾는 프로그램을 작성하시오.
# - 같은 카드를 고른 경우 번호가 작은 사람이 승자
# ```

# ### 풀이접근


# ```python
# - % 활용해 패턴 도출 (앞카드 - 뒷카드) % 3 == 0(비김), 1(승리), 2(패배)
#   e.g  1-2 -> -1%3 -> 2 (-1은 -3이 되기까지 2가 부족함) -> 패배
# - 그룹을 두 개로 나눠, 승부를 반복시켜 이긴 사람만 남긴다
# - 승부를 반복하다 1명만 남으면 그 학생 번호를 출력한다.
# ```

# ### 코드


# ```python
# 가위바위보 승자 찾는 위너 함수
def winner(a, b):
    ans = (a - b) % 3
    if ans == 1 or ans == 0:
        return True  # a 승리
    return False  # b 승리

# 승자를 다음경기 진출시키는 토너먼트 함수


def tonarment(player):
    # 남은 사람이 1명이 되면
    if len(player) < 2:
        return player[0]  # 우승정보 반환
    a_group, b_group = [], []  # 대결 그룹 리스트
    j = len(player)
    for i in range(j):  # 그룹을 계속 쪼갬
        if i <= (j-1)//2:
            a_group.append(player[i])  # 앞의 절반은 a_match
        else:
            b_group.append(player[i])  # 뒤의 절반은 b_match
    a = tonarment(a_group)
    b = tonarment(b_group)
    # 각 그룹의 첫번째 학생끼리의 경기해서 이긴 사람만 반환됨
    if winner(a[0], b[0]):
        return a
    else:
        return b


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    player = list(map(int, input().split()))
    player = [(i, idx) for idx, i in enumerate(player)]
    # 승자 번호를 추출하기 위한 enumerate (idx 뒤로 보냄)
    result = tonarment(player)
    # result[0] 마지막에 이긴 카드, [1] 승자인덱스
    print(f'#{tc} {result[1]+1}')  # 학생번호는 1부터 시작하니 +1
# ```

#      1
#      7
#      1 3 3 3 1 1 3

# ```python
# player = list(map(int, input().split()))
# player = [(i, idx) for idx, i in enumerate(player)]
# player
# ```

#       1 3 3 3 1 1 3


#     [(1, 0), (3, 1), (3, 2), (3, 3), (1, 4), (1, 5), (3, 6)]
