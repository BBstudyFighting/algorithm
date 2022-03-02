T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int,list(input())))

        #여기에 문제로직이 들어감
    cards_count = [0] * 10  #카드 갯수 리스트 만들기
    for card in nums:
        cards_count[card] += 1

    max_count = max(cards_count)    # 갯수중 최대값구하기
    index = max([i for i, ele in enumerate(cards_count) if ele == max_count]) #최대값 인덱스중 가장큰값구하기

        #최종 출력
    print('#{} {} {}'.format(tc, index, max_count))