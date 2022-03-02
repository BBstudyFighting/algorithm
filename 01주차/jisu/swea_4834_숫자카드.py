
# 테스트케이스
T = int(input())

# T 만큼의 반복
for i in range(1, T+1):
    # 숫자의 갯수와 숫자입력
    n = int(input())
    nums = input()

    # 인덱스가 0~9 까지의 카운트리스트 만듦
    cnt_list = [0]*10

    # 인덱스 성질을 활용하여 cnt_list 값 채움
    for num in nums:
        cnt_list[int(num)] += 1

    # 비교를 위한 변수 설정
    max_idx = 0  # 가장 많이 반복된 숫자값
    max_num = cnt_list[0]  # cnt_list 에서 가장 큰 값

    for j in range(1, len(cnt_list)):
        if cnt_list[j] >= max_num:
            max_num = cnt_list[j]
            max_idx = j

    print(f'#{i} {max_idx} {max_num}')
