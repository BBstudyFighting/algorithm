# str1 글자 중 str2에 가장 많이 등장한 글자를
# 찾고 몇 번 등장했는지 출력하시오.

# str1 문자를 하나씩 뽑아서 str2와 비교
T = int(input())
for tc in range(1, 1+T):
    str1 = input()
    str2 = input()

    li = []  # 글자마다 반복횟수를 담을 리스트
    for i in str1:
        li.append(str2.count(i))

    print(f'#{tc} {max(li)}')
